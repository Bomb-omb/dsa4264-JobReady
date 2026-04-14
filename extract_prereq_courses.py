#
# Known limitation: if the NUSMods API returns a malformed/truncated JSON payload
# while still succeeding at the HTTP layer, `json.load(response)` can raise
# `json.JSONDecodeError` and abort the batch because that case is not retried explicitly . 
# we assume the # API behaved as expected and returned valid JSON responses, so this failure path
# was not triggered and did not affect the generated prerequisite output.
# the prerequisite extracted was not used for downward analysis anyways
#
import argparse
import csv
import json
import socket
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
INPUT_PATH = BASE_DIR / "data" / "2025-2026_moduleInfo_clean.csv"
OUTPUT_PATH = BASE_DIR / "data" / "2025-2026_module_clean_with_prereq.csv"
ACAD_YEAR = "2025-2026"
USER_AGENT = "dsa4264-jobready/1.0"
DEFAULT_TIMEOUT = 30
DEFAULT_RETRIES = 3
DEFAULT_WORKERS = 8
MISSING_VALUE = "NA"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch NUSMods prereq trees and extract prerequisite course codes."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=INPUT_PATH,
        help=f"Input CSV path. Defaults to {INPUT_PATH}.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=OUTPUT_PATH,
        help=f"Output CSV path. Defaults to {OUTPUT_PATH}.",
    )
    parser.add_argument(
        "--acad-year",
        default=ACAD_YEAR,
        help=f"Academic year to query. Defaults to {ACAD_YEAR}.",
    )
    parser.add_argument(
        "--codes",
        nargs="*",
        help="Optional explicit module code subset to fetch.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"Per-request timeout in seconds. Defaults to {DEFAULT_TIMEOUT}.",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=DEFAULT_RETRIES,
        help=f"Retries per module on fetch failure. Defaults to {DEFAULT_RETRIES}.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=DEFAULT_WORKERS,
        help=f"Number of concurrent fetch workers. Defaults to {DEFAULT_WORKERS}.",
    )
    return parser.parse_args()


def load_rows(input_path: Path) -> list[dict[str, str]]:
    with input_path.open("r", newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def build_prefix_matches(rows: list[dict[str, str]]) -> tuple[list[str], dict[str, list[str]]]:
    module_codes = [row["moduleCode"] for row in rows]
    return module_codes, {}


def iter_tree_tokens(tree: Any) -> list[str]:
    if tree is None:
        return []
    if isinstance(tree, str):
        return [tree]
    if isinstance(tree, list):
        tokens: list[str] = []
        for item in tree:
            tokens.extend(iter_tree_tokens(item))
        return tokens
    if isinstance(tree, dict):
        tokens: list[str] = []
        for value in tree.values():
            tokens.extend(iter_tree_tokens(value))
        return tokens
    return []


def clean_token(token: str) -> str:
    return token.strip().split(":", 1)[0].strip()


def expand_token(
    token: str,
    all_module_codes: list[str],
    prefix_cache: dict[str, list[str]],
) -> list[str]:
    cleaned = clean_token(token)
    if not cleaned:
        return []

    if cleaned.endswith("%"):
        prefix = cleaned[:-1]
        if prefix not in prefix_cache:
            prefix_cache[prefix] = [code for code in all_module_codes if code.startswith(prefix)]
        return prefix_cache[prefix]

    return [cleaned]


def unique_in_order(values: list[str]) -> list[str]:
    return list(dict.fromkeys(values))


def serialize_codes(codes: list[str]) -> str:
    return json.dumps(codes, ensure_ascii=False)


def fetch_module(acad_year: str, module_code: str, timeout: int) -> dict[str, Any]:
    url = f"https://api.nusmods.com/v2/{acad_year}/modules/{module_code}.json"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


def fetch_with_retries(
    acad_year: str,
    module_code: str,
    timeout: int,
    retries: int,
) -> tuple[dict[str, Any] | None, str]:
    last_error = ""
    for attempt in range(1, retries + 1):
        try:
            return fetch_module(acad_year, module_code, timeout), ""
        except urllib.error.HTTPError as error:
            last_error = f"HTTP {error.code}"
            # 4xx errors are unlikely to recover on retry.
            if 400 <= error.code < 500:
                break
        except (urllib.error.URLError, TimeoutError, socket.timeout) as error:
            reason = getattr(error, "reason", error)
            last_error = str(reason)

        if attempt < retries:
            time.sleep(min(2 ** (attempt - 1), 4))

    return None, last_error or "Unknown fetch error"


def extract_prereq_codes(
    tree: Any,
    all_module_codes: list[str],
    prefix_cache: dict[str, list[str]],
) -> list[str]:
    expanded_codes: list[str] = []
    for token in iter_tree_tokens(tree):
        expanded_codes.extend(expand_token(token, all_module_codes, prefix_cache))
    return unique_in_order(expanded_codes)


def build_output_row(
    row: dict[str, str],
    payload: dict[str, Any] | None,
    error: str,
    all_module_codes: list[str],
    prefix_cache: dict[str, list[str]],
) -> dict[str, str]:
    output_row = dict(row)
    if payload is None:
        output_row["prereqCourseCodes"] = MISSING_VALUE
        output_row["fetchError"] = error
        return output_row

    codes = extract_prereq_codes(payload.get("prereqTree"), all_module_codes, prefix_cache)
    output_row["prereqCourseCodes"] = serialize_codes(codes) if codes else MISSING_VALUE
    output_row["fetchError"] = ""
    return output_row


def main() -> None:
    args = parse_args()
    rows = load_rows(args.input)
    if not rows:
        raise ValueError(f"No rows found in input CSV: {args.input}")

    all_module_codes, prefix_cache = build_prefix_matches(rows)
    selected_codes = set(args.codes) if args.codes else None
    rows_to_process = [row for row in rows if selected_codes is None or row["moduleCode"] in selected_codes]
    if not rows_to_process:
        raise ValueError("No matching module codes found to process.")

    results_by_code: dict[str, tuple[dict[str, Any] | None, str]] = {}

    with ThreadPoolExecutor(max_workers=max(args.workers, 1)) as executor:
        future_by_code = {
            executor.submit(
                fetch_with_retries,
                args.acad_year,
                row["moduleCode"],
                args.timeout,
                args.retries,
            ): row["moduleCode"]
            for row in rows_to_process
        }
        completed = 0
        for future in future_by_code:
            module_code = future_by_code[future]
            results_by_code[module_code] = future.result()
            completed += 1
            if completed % 100 == 0 or completed == len(rows_to_process):
                print(f"Fetched {completed}/{len(rows_to_process)} modules")

    output_rows = [
        build_output_row(
            row,
            results_by_code[row["moduleCode"]][0],
            results_by_code[row["moduleCode"]][1],
            all_module_codes,
            prefix_cache,
        )
        for row in rows_to_process
    ]

    has_fetch_errors = any(row["fetchError"] for row in output_rows)
    fieldnames = list(rows[0].keys()) + ["prereqCourseCodes"]
    if has_fetch_errors:
        fieldnames.append("fetchError")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Saved {len(output_rows)} records to {args.output}")


if __name__ == "__main__":
    main()
