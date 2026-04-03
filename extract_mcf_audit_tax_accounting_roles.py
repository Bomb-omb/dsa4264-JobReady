from __future__ import annotations

import argparse
import re
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT_PATH = BASE_DIR / "data" / "mcf_entrylevel.csv"
DEFAULT_OUTPUT_PATH = BASE_DIR / "data" / "acc" / "audit_tax_accounting_jobs.csv"
ACCOUNTING_CATEGORY = "accounting / auditing / taxation"

DIRECT_TITLE_PATTERNS = (
    re.compile(r"\baudit(?:or|ing)?\b", re.IGNORECASE),
    re.compile(r"\btax(?:ation)?\b", re.IGNORECASE),
    re.compile(r"\baccount(?:ant|ancy|ing)\b", re.IGNORECASE),
    re.compile(r"\baccounts\b", re.IGNORECASE),
    re.compile(r"\bbookkeep(?:er|ing)?\b", re.IGNORECASE),
)
WEAK_TITLE_PATTERNS = (
    re.compile(r"\baccount (?:assistant|associate|executive|officer)\b", re.IGNORECASE),
)
SPECIAL_TITLE_PATTERN = re.compile(r"\bassurance\b", re.IGNORECASE)
STRONG_DESCRIPTION_PATTERNS = (
    re.compile(r"\baccounts? payable\b", re.IGNORECASE),
    re.compile(r"\baccounts? receivable\b", re.IGNORECASE),
    re.compile(r"\bfull set of accounts?\b", re.IGNORECASE),
    re.compile(r"\bgeneral ledger\b", re.IGNORECASE),
    re.compile(r"\bbank reconciliation(?:s)?\b", re.IGNORECASE),
    re.compile(r"\bmonth[- ]end (?:closing|close)\b", re.IGNORECASE),
    re.compile(r"\byear[- ]end (?:closing|close)\b", re.IGNORECASE),
    re.compile(r"\bfinancial statements?\b", re.IGNORECASE),
    re.compile(r"\bbookkeep(?:er|ing)?\b", re.IGNORECASE),
    re.compile(r"\bgst\b", re.IGNORECASE),
    re.compile(r"\biras\b", re.IGNORECASE),
    re.compile(r"\btax (?:filing|compliance|return|returns)\b", re.IGNORECASE),
    re.compile(r"\bstatutory (?:and regulatory )?audit\b", re.IGNORECASE),
    re.compile(r"\baudit (?:engagements?|assignments?|support|schedules?|processes?)\b", re.IGNORECASE),
    re.compile(r"\baccount reconciliations?\b", re.IGNORECASE),
    re.compile(r"\bclose the books\b", re.IGNORECASE),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract audit, tax, and accounting-focused roles from an MCF CSV.",
    )
    parser.add_argument(
        "--input-file",
        default=str(DEFAULT_INPUT_PATH),
        help="Path to the source MCF CSV.",
    )
    parser.add_argument(
        "--output-file",
        default=str(DEFAULT_OUTPUT_PATH),
        help="Path to write the filtered CSV.",
    )
    return parser.parse_args()


def normalize_text(value: object) -> str:
    if value is None or pd.isna(value):
        return ""
    return str(value).strip().lower()


def count_pattern_matches(text: str, patterns: tuple[re.Pattern[str], ...]) -> int:
    return sum(1 for pattern in patterns if pattern.search(text))


def is_audit_tax_accounting_role(row: pd.Series) -> bool:
    title = normalize_text(row.get("title", ""))
    description = normalize_text(row.get("description", ""))
    categories = normalize_text(row.get("categories", ""))

    category_signal = ACCOUNTING_CATEGORY in categories
    description_match_count = count_pattern_matches(description, STRONG_DESCRIPTION_PATTERNS)

    if any(pattern.search(title) for pattern in DIRECT_TITLE_PATTERNS):
        return True

    if SPECIAL_TITLE_PATTERN.search(title) and (category_signal or description_match_count >= 1):
        return True

    if any(pattern.search(title) for pattern in WEAK_TITLE_PATTERNS):
        return category_signal or description_match_count >= 1

    return category_signal and description_match_count >= 2


def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    matching_rows = df.apply(is_audit_tax_accounting_role, axis=1)
    return df.loc[matching_rows].copy()


def filter_csv(input_path: Path, output_path: Path) -> pd.DataFrame:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    filtered_df = filter_dataframe(df)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    filtered_df.to_csv(output_path, index=False)

    print(f"Loaded {len(df)} rows from {input_path}")
    print(f"Matched {len(filtered_df)} audit/tax/accounting rows")
    print(f"Saved filtered roles to {output_path}")

    return filtered_df


def main() -> None:
    args = parse_args()
    filter_csv(
        input_path=Path(args.input_file),
        output_path=Path(args.output_file),
    )


if __name__ == "__main__":
    main()
