import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_PATH = BASE_DIR / "data" / "raw" / "nusmods" / "2025-2026_moduleInfo.json"
OUTPUT_PATH = BASE_DIR / "data" / "2025-2026_moduleInfo_clean.csv"
FIELDS = ("moduleCode", "title", "description")


def main() -> None:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_PATH}")

    modules = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    filtered_modules = [{field: module.get(field) for field in FIELDS} for module in modules]

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(filtered_modules)

    print(f"Saved {len(filtered_modules)} records to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
