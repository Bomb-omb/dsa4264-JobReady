import argparse
import csv
import platform
import shutil
import time
from pathlib import Path

import pandas as pd

try:
    import pyautogui
except ModuleNotFoundError:
    pyautogui = None

try:
    import pyperclip
except ModuleNotFoundError:
    pyperclip = None


DEFAULT_INPUT_FILE = "data/2025-2026_module_clean_with_prereq.csv"
DEFAULT_ID_COLUMN = "moduleCode"
DEFAULT_TEXT_COLUMN = "description"
DEFAULT_OUTPUT_COLUMN = "extracted_skills"
DEFAULT_APPS_TOOLS_COLUMN = "extracted_apps_tools"
DEFAULT_STATUS_COLUMN = "done"
DOWNLOAD_DIR = Path.home() / "Downloads"

# Approximate positions based on the current Edge layout in your screenshots.
TEXTBOX_POS = (650, 620)
SKILLS_TAB_POS = (1045, 444)
APPS_TOOLS_TAB_POS = (1188, 444)
DOWNLOAD_BTN_POS = (1010, 510)
RESET_BTN_POS = (665, 960)

WAIT_AFTER_PASTE = 2
WAIT_AFTER_RESET = 2
WAIT_AFTER_TAB_SWITCH = 0.5
WAIT_FOR_RESULTS = 5
DOWNLOAD_TIMEOUT = 5

SKILLS_SECTION_HEADER = "extracted_skills"
APPS_TOOLS_SECTION_HEADER = "extracted_apps_and_tools"

SYSTEM = platform.system()
CMD_KEY = "command" if SYSTEM == "Darwin" else "ctrl"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Automate SkillsFuture extraction from a CSV of course descriptions."
    )
    parser.add_argument("--input-file", default=DEFAULT_INPUT_FILE)
    parser.add_argument("--output-file")
    parser.add_argument("--id-column", default=DEFAULT_ID_COLUMN)
    parser.add_argument("--text-column", default=DEFAULT_TEXT_COLUMN)
    parser.add_argument("--output-column", default=DEFAULT_OUTPUT_COLUMN)
    parser.add_argument("--apps-tools-column", default=DEFAULT_APPS_TOOLS_COLUMN)
    parser.add_argument("--status-column", default=DEFAULT_STATUS_COLUMN)
    parser.add_argument("--row-index", type=int)
    parser.add_argument("--row-count", type=int)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args(argv)


def require_runtime_dependencies() -> None:
    missing = []
    if pyautogui is None:
        missing.append("pyautogui")
    if pyperclip is None:
        missing.append("pyperclip")

    if missing:
        install_list = " ".join(missing)
        raise SystemExit(
            "Missing required packages: "
            + ", ".join(missing)
            + ". Install them with: python -m pip install "
            + install_list
        )

    pyautogui.FAILSAFE = True


def validate_input_path(input_path: Path) -> None:
    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")


def validate_args(args: argparse.Namespace) -> None:
    if args.row_index is not None and args.row_count is not None:
        raise SystemExit("--row-index cannot be used with --row-count.")
    if args.row_index is None and args.row_count is None:
        raise SystemExit("--row-count is required unless --row-index is used.")
    if args.row_count is not None and args.row_count <= 0:
        raise SystemExit("--row-count must be a positive integer.")


def ensure_output_columns(df: pd.DataFrame, args: argparse.Namespace) -> pd.DataFrame:
    prepared = df.copy()
    for column_name in (
        args.output_column,
        args.apps_tools_column,
        args.status_column,
    ):
        if column_name not in prepared.columns:
            prepared[column_name] = ""
    return prepared


def validate_columns(df: pd.DataFrame, args: argparse.Namespace) -> None:
    required_columns = [
        args.id_column,
        args.text_column,
        args.output_column,
        args.apps_tools_column,
        args.status_column,
    ]
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        raise SystemExit(
            "Missing required column(s): "
            + ", ".join(missing)
            + ". Available columns: "
            + ", ".join(df.columns.astype(str))
        )


def normalize_output_value(value: object) -> str:
    if pd.isna(value):
        return ""
    text = str(value)
    return "" if text.lower() == "nan" else text


def normalize_status_value(value: object) -> str:
    if pd.isna(value):
        return "pending"
    text = str(value).strip()
    return text or "pending"


def normalize_dataframe(df: pd.DataFrame, args: argparse.Namespace) -> pd.DataFrame:
    normalized = df.copy()
    normalized[args.output_column] = normalized[args.output_column].map(normalize_output_value)
    normalized[args.apps_tools_column] = normalized[args.apps_tools_column].map(
        normalize_output_value
    )
    normalized[args.status_column] = normalized[args.status_column].map(normalize_status_value)
    return normalized


def build_output_path(
    input_path: Path,
    output_file: str | None,
) -> Path:
    if output_file:
        return Path(output_file)
    return input_path


def resolve_load_and_output_paths(
    input_path: Path,
    args: argparse.Namespace,
) -> tuple[Path, Path]:
    output_path = build_output_path(input_path, args.output_file)
    load_path = output_path if output_path.exists() else input_path
    return load_path, output_path


def build_backup_path(input_path: Path) -> Path:
    return input_path.with_name(f"{input_path.stem}.backup{input_path.suffix}")


def ensure_backup(input_path: Path) -> None:
    backup_path = build_backup_path(input_path)
    if backup_path.exists():
        return

    shutil.copy2(input_path, backup_path)
    print(f"Created backup: {backup_path}")


def save_dataframe(
    df: pd.DataFrame,
    input_path: Path,
    output_path: Path,
) -> None:
    if output_path == input_path:
        ensure_backup(input_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def format_identifier(value: object) -> str:
    if pd.isna(value):
        return "<missing>"
    return str(value)


def get_result_columns(args: argparse.Namespace) -> list[str]:
    return [args.output_column, args.apps_tools_column, args.status_column]


def build_unique_rows_dataframe(
    df: pd.DataFrame,
    args: argparse.Namespace,
) -> pd.DataFrame:
    return df[
        [
            args.id_column,
            args.text_column,
            args.output_column,
            args.apps_tools_column,
            args.status_column,
        ]
    ].drop_duplicates(subset=[args.text_column], keep="first").copy()


def find_first_pending_row(
    df: pd.DataFrame,
    status_column: str,
) -> int | None:
    normalized_statuses = df[status_column].map(normalize_status_value)
    for position, value in enumerate(normalized_statuses.tolist()):
        if value == "pending":
            return position
    return None


def resolve_batch_row_window(
    df: pd.DataFrame,
    args: argparse.Namespace,
) -> tuple[int | None, int | None]:
    if args.row_count is None:
        raise ValueError("row_count must be provided for batch processing.")

    start_row = find_first_pending_row(df, args.status_column)
    if start_row is None:
        return None, None
    end_row = min(start_row + args.row_count, len(df))
    return start_row, end_row


def print_resolved_config(
    args: argparse.Namespace,
    input_path: Path,
    load_path: Path,
    output_path: Path,
    df: pd.DataFrame,
    resolved_start_row: int | None = None,
) -> None:
    unique_count = df[args.text_column].nunique(dropna=False)
    if args.row_index is not None:
        row_mode = args.row_index
    else:
        row_mode = "batch"
    write_mode = "in-place" if output_path == input_path else "output-file"

    print(f"Running on: {SYSTEM}")
    print("Resolved config:")
    print(f"  input_file: {input_path}")
    print(f"  load_file: {load_path}")
    print(f"  output_file: {output_path}")
    print(f"  id_column: {args.id_column}")
    print(f"  text_column: {args.text_column}")
    print(f"  output_column: {args.output_column}")
    print(f"  apps_tools_column: {args.apps_tools_column}")
    print(f"  status_column: {args.status_column}")
    print(f"  row_index: {row_mode}")
    print(f"  write_mode: {write_mode}")
    if args.row_index is None:
        print(f"  working_file: {output_path}")
        print(f"  resolved_start_row: {resolved_start_row}")
        print(f"  row_count: {args.row_count}")
    print(f"  total_rows: {len(df)}")
    print(f"  unique_text_rows: {unique_count}")
    if output_path == input_path:
        print(f"  backup_path: {build_backup_path(input_path)}")


def get_latest_csv(after_time: float) -> Path | None:
    files = list(DOWNLOAD_DIR.glob("*.csv"))
    if not files:
        return None

    newest = max(files, key=lambda path: path.stat().st_mtime)
    if newest.stat().st_mtime > after_time:
        return newest
    return None


def wait_for_download(after_time: float, timeout: int = DOWNLOAD_TIMEOUT) -> Path | None:
    start = time.time()
    while time.time() - start < timeout:
        file_path = get_latest_csv(after_time)
        if file_path is not None:
            time.sleep(1.0)
            return file_path
        time.sleep(0.5)
    return None


def extract_section_from_csv(file_path: Path, section_header: str) -> str:
    values = []
    found_section = False

    with file_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle, skipinitialspace=True)

        for row in reader:
            for cell in row:
                cleaned = str(cell).strip()
                if not cleaned:
                    continue

                if not found_section:
                    if cleaned == section_header:
                        found_section = True
                    continue

                value = cleaned.split("; Tags:")[0].strip()
                if value:
                    values.append(value)

    if not found_section:
        raise RuntimeError(f"Section '{section_header}' not found in downloaded CSV.")

    deduplicated_values = list(dict.fromkeys(values))
    return " | ".join(deduplicated_values)


def paste_text(text: str) -> None:
    pyautogui.click(TEXTBOX_POS, clicks=3)
    time.sleep(0.5)

    pyautogui.hotkey(CMD_KEY, "a")
    time.sleep(0.3)

    pyautogui.press("backspace")
    time.sleep(0.3)

    pyperclip.copy(text)
    pyautogui.hotkey(CMD_KEY, "v")
    time.sleep(WAIT_AFTER_PASTE)

    pyautogui.click(RESET_BTN_POS)
    time.sleep(0.5)


def click_result_tab(tab_pos: tuple[int, int], tab_name: str) -> None:
    print(f"  Opening {tab_name} tab")
    pyautogui.click(tab_pos)
    time.sleep(WAIT_AFTER_TAB_SWITCH)


def click_download_and_read(
    section_header: str,
    tab_name: str,
    allow_empty: bool,
) -> str:
    download_start = time.time()
    pyautogui.click(DOWNLOAD_BTN_POS)

    downloaded_file = wait_for_download(download_start, timeout=DOWNLOAD_TIMEOUT)
    if downloaded_file is None:
        raise RuntimeError(f"{tab_name} download failed.")

    try:
        section_value = extract_section_from_csv(downloaded_file, section_header)
    finally:
        if downloaded_file.exists():
            downloaded_file.unlink()

    if not section_value and not allow_empty:
        raise RuntimeError(f"No {tab_name.lower()} extracted or download failed.")

    return section_value


def reset_page() -> None:
    pyautogui.click(RESET_BTN_POS)
    time.sleep(WAIT_AFTER_RESET)


def apply_partial_results(
    target_df: pd.DataFrame,
    row_label: object,
    partial_results: dict[str, str],
) -> None:
    for column_name, value in partial_results.items():
        target_df.at[row_label, column_name] = value


def run_extraction_for_text(
    identifier: str,
    text: str,
    args: argparse.Namespace,
) -> tuple[bool, dict[str, str], str]:
    if not text.strip():
        return False, {}, "Text to extract is empty."

    print(f"Processing {identifier}")

    partial_results: dict[str, str] = {}
    try:
        paste_text(text)
        time.sleep(WAIT_FOR_RESULTS)

        click_result_tab(SKILLS_TAB_POS, "Skills")
        partial_results[args.output_column] = click_download_and_read(
            section_header=SKILLS_SECTION_HEADER,
            tab_name="Skills",
            allow_empty=False,
        )

        click_result_tab(APPS_TOOLS_TAB_POS, "Apps & Tools")
        partial_results[args.apps_tools_column] = click_download_and_read(
            section_header=APPS_TOOLS_SECTION_HEADER,
            tab_name="Apps & Tools",
            allow_empty=True,
        )

        print(f"  Skills: {partial_results[args.output_column]}")
        print(f"  Apps & Tools: {partial_results[args.apps_tools_column]}")
        reset_page()
        return True, partial_results, ""

    except Exception as exc:
        error_message = str(exc)
        print(f"  Error: {error_message}")

        try:
            reset_page()
        except Exception:
            pass

        time.sleep(1.5)
        print(f"  Failed: {error_message}")
        return False, partial_results, error_message


def apply_unique_results_to_full_dataframe(
    full_df: pd.DataFrame,
    unique_df: pd.DataFrame,
    args: argparse.Namespace,
) -> pd.DataFrame:
    mapped = unique_df[
        [args.text_column, args.output_column, args.apps_tools_column, args.status_column]
    ].drop_duplicates(
        subset=[args.text_column],
        keep="last",
    )
    result_map = mapped.set_index(args.text_column)

    updated = full_df.copy()
    updated[args.output_column] = updated[args.text_column].map(result_map[args.output_column])
    updated[args.apps_tools_column] = updated[args.text_column].map(
        result_map[args.apps_tools_column]
    )
    updated[args.status_column] = updated[args.text_column].map(result_map[args.status_column])
    return updated


def apply_unique_results_to_row_subset(
    full_df: pd.DataFrame,
    row_labels: pd.Index,
    unique_df: pd.DataFrame,
    args: argparse.Namespace,
) -> None:
    updated_subset = apply_unique_results_to_full_dataframe(
        full_df.loc[row_labels].copy(),
        unique_df,
        args,
    )
    result_columns = get_result_columns(args)
    full_df.loc[row_labels, result_columns] = updated_subset[result_columns]


def process_single_row(
    df: pd.DataFrame,
    args: argparse.Namespace,
    input_path: Path,
    output_path: Path,
) -> None:
    if args.row_index is None:
        raise ValueError("row_index must be provided for single-row processing.")
    if args.row_index < 0 or args.row_index >= len(df):
        raise SystemExit(f"row-index is out of range: {args.row_index}")

    row_label = df.index[args.row_index]
    identifier = format_identifier(df.at[row_label, args.id_column])
    text = str(df.at[row_label, args.text_column])
    current_status = str(df.at[row_label, args.status_column]).strip().lower()

    print(f"Processing physical row index {args.row_index}")

    if current_status == "success" and not args.force:
        print("Row already marked success. Use --force to rerun it.")
        return

    success, partial_results, error_message = run_extraction_for_text(
        identifier=identifier,
        text=text,
        args=args,
    )

    apply_partial_results(df, row_label, partial_results)
    if success:
        df.at[row_label, args.status_column] = "success"
    else:
        df.at[row_label, args.status_column] = f"error: {error_message}"

    save_dataframe(df, input_path, output_path)
    print(f"Saved output to: {output_path}")


def process_batch_rows(
    df: pd.DataFrame,
    args: argparse.Namespace,
    input_path: Path,
    output_path: Path,
    start_row: int,
    end_row: int,
) -> None:
    batch_df = df.iloc[start_row:end_row].copy()
    unique_df = build_unique_rows_dataframe(batch_df, args)

    print(f"Processing physical rows {start_row} to {end_row - 1}")
    print(f"Unique descriptions to process in batch: {len(unique_df)}")

    for position, (row_label, row) in enumerate(unique_df.iterrows(), start=1):
        current_status = str(row[args.status_column]).strip().lower()
        if current_status == "success" and not args.force:
            continue

        identifier = format_identifier(row[args.id_column])
        text = str(row[args.text_column])

        print(f"Processing batch unique row {position}/{len(unique_df)}")
        success, partial_results, error_message = run_extraction_for_text(
            identifier=identifier,
            text=text,
            args=args,
        )

        apply_partial_results(unique_df, row_label, partial_results)
        if success:
            unique_df.at[row_label, args.status_column] = "success"
        else:
            unique_df.at[row_label, args.status_column] = f"error: {error_message}"

        apply_unique_results_to_row_subset(df, batch_df.index, unique_df, args)
        save_dataframe(df, input_path, output_path)

    print(f"Saved output to: {output_path}")


def main() -> None:
    args = parse_args()
    validate_args(args)

    input_path = Path(args.input_file)
    load_path, output_path = resolve_load_and_output_paths(input_path, args)

    validate_input_path(load_path)

    df = pd.read_csv(load_path)
    df = ensure_output_columns(df, args)
    validate_columns(df, args)
    df = normalize_dataframe(df, args)

    resolved_start_row = None
    if args.row_index is None:
        resolved_start_row, _ = resolve_batch_row_window(df, args)

    print_resolved_config(args, input_path, load_path, output_path, df, resolved_start_row)
    if args.row_index is None and resolved_start_row is None:
        print("No pending rows found. Nothing to do.")
        return

    require_runtime_dependencies()

    print("Starting in 3 seconds. Keep the browser fixed and do not touch the mouse or keyboard.")
    time.sleep(3)

    if args.row_index is not None:
        process_single_row(df, args, input_path, output_path)
    else:
        start_row, end_row = resolve_batch_row_window(df, args)
        if start_row is None or end_row is None:
            print("No pending rows found. Nothing to do.")
            return
        process_batch_rows(df, args, input_path, output_path, start_row, end_row)


if __name__ == "__main__":
    main()
