from __future__ import annotations

import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "data" / "raw" / "mcf_data"
OUTPUT_DIR = BASE_DIR / "data" / "raw" / "mcf_clean_data"
FIELDS = (
    "title",
    "description",
    "minimumYearsExperience",
    "skills",
    "categories",
    "employmentTypes",
    "positionLevels",
)


def extract_list_field(data: dict[str, Any], field: str) -> list[Any]:
    value = data.get(field)
    return value if isinstance(value, list) else []


def extract_record(data: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": data.get("title"),
        "description": data.get("description"),
        "minimumYearsExperience": data.get("minimumYearsExperience"),
        "skills": extract_list_field(data, "skills"),
        "categories": extract_list_field(data, "categories"),
        "employmentTypes": extract_list_field(data, "employmentTypes"),
        "positionLevels": extract_list_field(data, "positionLevels"),
    }


def main() -> None:
    if not INPUT_DIR.exists():
        raise FileNotFoundError(f"Input directory not found: {INPUT_DIR}")

    json_files = sorted(INPUT_DIR.glob("*.json"))
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for file_path in json_files:
        data = json.loads(file_path.read_text(encoding="utf-8"))
        cleaned_data = extract_record(data)
        output_path = OUTPUT_DIR / file_path.name
        output_path.write_text(
            json.dumps(cleaned_data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    print(f"Saved {len(json_files)} cleaned records to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
