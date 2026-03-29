import argparse
import csv
import platform
import shutil
import time
from pathlib import Path

import pandas as pd

try:
    import keyboard
except ModuleNotFoundError:
    keyboard = None

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
MAX_RETRIES = 1
ERROR_REFRESH_THRESHOLD = 5
TIME_FOR_REFRESH = 2

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
    parser.add_argument("--in-place", action="store_true")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args(argv)


def require_runtime_dependencies() -> None:
    missing = []
    if keyboard is None:
        missing.append("keyboard")
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


def build_default_output_path(input_path: Path) -> Path:
    return input_path.with_name(f"{input_path.stem}_skillsfuture{input_path.suffix}")


def build_output_path(
    input_path: Path,
    output_file: str | None,
    in_place: bool,
) -> Path:
    if in_place:
        return input_path
    if output_file:
        return Path(output_file)
    return build_default_output_path(input_path)


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
    in_place: bool,
) -> None:
    if in_place:
        ensure_backup(input_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def format_identifier(value: object) -> str:
    if pd.isna(value):
        return "<missing>"
    return str(value)


def print_resolved_config(
    args: argparse.Namespace,
    input_path: Path,
    output_path: Path,
    df: pd.DataFrame,
) -> None:
    unique_count = df[args.text_column].nunique(dropna=False)
    row_mode = args.row_index if args.row_index is not None else "all"
    write_mode = "in-place" if args.in_place else "copy"

    print(f"Running on: {SYSTEM}")
    print("Resolved config:")
    print(f"  input_file: {input_path}")
    print(f"  output_file: {output_path}")
    print(f"  id_column: {args.id_column}")
    print(f"  text_column: {args.text_column}")
    print(f"  output_column: {args.output_column}")
    print(f"  apps_tools_column: {args.apps_tools_column}")
    print(f"  status_column: {args.status_column}")
    print(f"  row_index: {row_mode}")
    print(f"  write_mode: {write_mode}")
    print(f"  total_rows: {len(df)}")
    print(f"  unique_text_rows: {unique_count}")
    if args.in_place:
        print(f"  backup_path: {build_backup_path(input_path)}")


def manual_pause() -> None:
    print("\nPaused. Refresh the website now.")
    print("Press 'r' to resume.")

    keyboard.wait("r")

    print("Resuming.\n")
    time.sleep(1)


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


def refresh_website() -> None:
    print("\nAuto-refreshing website...")

    if SYSTEM in {"Darwin", "Windows"}:
        pyautogui.hotkey(CMD_KEY, "r")
    else:
        print(f"Unsupported OS for auto-refresh: {SYSTEM}")
        return

    time.sleep(TIME_FOR_REFRESH)
    print(f"Website refreshed on {SYSTEM}.")


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
    error_count: int,
) -> tuple[bool, dict[str, str], str, int]:
    if not text.strip():
        return False, {}, "Text to extract is empty.", error_count

    print(f"Processing {identifier}")

    last_error = ""
    partial_results: dict[str, str] = {}

    for attempt in range(1, MAX_RETRIES + 1):
        attempt_results: dict[str, str] = {}
        try:
            print(f"  Attempt {attempt}/{MAX_RETRIES}")

            paste_text(text)
            time.sleep(WAIT_FOR_RESULTS)

            click_result_tab(SKILLS_TAB_POS, "Skills")
            attempt_results[args.output_column] = click_download_and_read(
                section_header=SKILLS_SECTION_HEADER,
                tab_name="Skills",
                allow_empty=False,
            )

            click_result_tab(APPS_TOOLS_TAB_POS, "Apps & Tools")
            attempt_results[args.apps_tools_column] = click_download_and_read(
                section_header=APPS_TOOLS_SECTION_HEADER,
                tab_name="Apps & Tools",
                allow_empty=True,
            )

            print(f"  Skills: {attempt_results[args.output_column]}")
            print(f"  Apps & Tools: {attempt_results[args.apps_tools_column]}")
            reset_page()
            return True, attempt_results, "", 0

        except Exception as exc:
            partial_results.update(attempt_results)
            last_error = str(exc)
            error_count += 1

            print(f"  Error: {last_error}")
            print(f"  Current error count: {error_count}")

            if error_count >= ERROR_REFRESH_THRESHOLD:
                print("Too many errors. Refreshing website.")
                refresh_website()
                error_count = 0
                try:
                    reset_page()
                except Exception:
                    pass

            try:
                reset_page()
            except Exception:
                pass

            time.sleep(1.5)

    print(f"  Failed after retries: {last_error}")
    return False, partial_results, last_error, error_count


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

    error_count = 0
    success, partial_results, error_message, _ = run_extraction_for_text(
        identifier=identifier,
        text=text,
        args=args,
        error_count=error_count,
    )

    apply_partial_results(df, row_label, partial_results)
    if success:
        df.at[row_label, args.status_column] = "success"
    else:
        df.at[row_label, args.status_column] = f"error: {error_message}"

    save_dataframe(df, input_path, output_path, args.in_place)
    print(f"Saved output to: {output_path}")


def process_all_unique_rows(
    df: pd.DataFrame,
    args: argparse.Namespace,
    input_path: Path,
    output_path: Path,
) -> None:
    unique_df = df[
        [
            args.id_column,
            args.text_column,
            args.output_column,
            args.apps_tools_column,
            args.status_column,
        ]
    ].drop_duplicates(subset=[args.text_column], keep="first").copy()

    print(f"Unique descriptions to process: {len(unique_df)}")
    error_count = 0

    for position, (row_label, row) in enumerate(unique_df.iterrows(), start=1):
        current_status = str(row[args.status_column]).strip().lower()
        if current_status == "success" and not args.force:
            continue

        identifier = format_identifier(row[args.id_column])
        text = str(row[args.text_column])

        print(f"Processing unique row {position}/{len(unique_df)}")
        success, partial_results, error_message, error_count = run_extraction_for_text(
            identifier=identifier,
            text=text,
            args=args,
            error_count=error_count,
        )

        apply_partial_results(unique_df, row_label, partial_results)
        if success:
            unique_df.at[row_label, args.status_column] = "success"
        else:
            unique_df.at[row_label, args.status_column] = f"error: {error_message}"

        updated_full_df = apply_unique_results_to_full_dataframe(df, unique_df, args)
        df.loc[:, args.output_column] = updated_full_df[args.output_column]
        df.loc[:, args.apps_tools_column] = updated_full_df[args.apps_tools_column]
        df.loc[:, args.status_column] = updated_full_df[args.status_column]

        save_dataframe(df, input_path, output_path, args.in_place)

    print(f"Saved output to: {output_path}")


def main() -> None:
    args = parse_args()

    input_path = Path(args.input_file)
    output_path = build_output_path(input_path, args.output_file, args.in_place)

    validate_input_path(input_path)

    df = pd.read_csv(input_path)
    df = ensure_output_columns(df, args)
    validate_columns(df, args)
    df = normalize_dataframe(df, args)

    print_resolved_config(args, input_path, output_path, df)
    require_runtime_dependencies()

    print("Starting in 3 seconds. Keep the browser fixed and do not touch the mouse or keyboard.")
    time.sleep(3)

    if args.row_index is not None:
        process_single_row(df, args, input_path, output_path)
    else:
        process_all_unique_rows(df, args, input_path, output_path)


if __name__ == "__main__":
    main()
