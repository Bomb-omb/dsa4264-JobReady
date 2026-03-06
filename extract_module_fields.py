from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
INPUT_PATH = BASE_DIR / "data" / "raw" / "nusmods" / "2025-2026_moduleInfo.json"
OUTPUT_PATH = BASE_DIR / "data" / "2025-2026_moduleInfo_clean.json"
FIELDS = ("moduleCode", "title", "description")


def main() -> None:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_PATH}")

    modules = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    filtered_modules = [{field: module.get(field) for field in FIELDS} for module in modules]

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(filtered_modules, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Saved {len(filtered_modules)} records to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
