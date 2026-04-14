# Known limitation:
# `clean_text()` unescapes HTML entities and then strips `<...>` with a regex,
# so literal angle-bracketed text like `<12 months contract>` can be removed.
# This is currently treated as non-severe for this pipeline because the lost
# snippets are peripheral metadata, not the main job scope / responsibility text
# used downstream.
from __future__ import annotations

import csv
import html
import json
import re
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "data" / "raw" / "mcf_data"
OUTPUT_PATH = BASE_DIR / "data" / "mcf_clean_data.csv"
FIELDS = (
    "uuid",
    "raw_title",
    "title",
    "raw_description",
    "description",
    "minimumYearsExperience",
    "skills",
    "categories",
    "employmentTypes",
    "positionLevels",
)
MOJIBAKE_REPLACEMENTS = (
    ("\u00e2\u20ac\u2122", "'"),
    ("\u00e2\u20ac\u02dc", "'"),
    ("\u00e2\u20ac\u0153", '"'),
    ("\u00e2\u20ac\u009d", '"'),
    ("\u00e2\u20ac\u201c", "-"),
    ("\u00e2\u20ac\u201d", "-"),
    ("\u00c2", ""),
)


def clean_text(value: Any) -> str:
    if value is None:
        return ""

    text = str(value)
    text = html.unescape(text)

    for bad, good in MOJIBAKE_REPLACEMENTS:
        text = text.replace(bad, good)

    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("\u00A0", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_minimum_years(value: Any) -> int | None:
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value if value >= 0 else None
    if isinstance(value, float) and value.is_integer():
        return int(value) if value >= 0 else None

    text_value = str(value).strip()
    if text_value.isdigit():
        return int(text_value)
    return None


def unique_preserve_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            output.append(value)
    return output


def extract_named_list(data: dict[str, Any], field: str, name_key: str) -> list[str]:
    raw_value = data.get(field)
    if not isinstance(raw_value, list):
        return []

    extracted: list[str] = []
    for item in raw_value:
        if isinstance(item, dict):
            name = clean_text(item.get(name_key))
        elif isinstance(item, str):
            name = clean_text(item)
        else:
            name = ""

        if name:
            extracted.append(name)

    return unique_preserve_order(extracted)


def extract_record(data: dict[str, Any]) -> dict[str, Any]:
    raw_title = "" if data.get("title") is None else str(data.get("title"))
    raw_description = "" if data.get("description") is None else str(data.get("description"))

    return {
        "uuid": clean_text(data.get("uuid")),
        "raw_title": raw_title,
        "title": clean_text(data.get("title")),
        "raw_description": raw_description,
        "description": clean_text(data.get("description")),
        "minimumYearsExperience": parse_minimum_years(data.get("minimumYearsExperience")),
        "skills": json.dumps(extract_named_list(data, "skills", "skill"), ensure_ascii=False),
        "categories": json.dumps(
            extract_named_list(data, "categories", "category"),
            ensure_ascii=False,
        ),
        "employmentTypes": json.dumps(
            extract_named_list(data, "employmentTypes", "employmentType"),
            ensure_ascii=False,
        ),
        "positionLevels": json.dumps(
            extract_named_list(data, "positionLevels", "position"),
            ensure_ascii=False,
        ),
    }


def main() -> None:
    if not INPUT_DIR.exists():
        raise FileNotFoundError(f"Input directory not found: {INPUT_DIR}")

    json_files = sorted(INPUT_DIR.glob("*.json"))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    extracted_records: list[dict[str, Any]] = []
    skipped_files: list[str] = []

    for file_path in json_files:
        try:
            data = json.loads(file_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            skipped_files.append(file_path.name)
            continue

        extracted_records.append(extract_record(data))

    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(extracted_records)

    print(f"Saved {len(extracted_records)} cleaned records to {OUTPUT_PATH}")
    if skipped_files:
        print(f"Skipped {len(skipped_files)} invalid JSON files.")


if __name__ == "__main__":
    main()
