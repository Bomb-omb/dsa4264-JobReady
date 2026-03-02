from pathlib import Path
import json

INPUT_PATH = Path("data/raw/nusmods/2025-2026_moduleInfo.json")
OUTPUT_PATH = Path("data/2025-2026_moduleInfo_clean.json")
FIELDS = ("moduleCode", "title", "description")


def main() -> None:
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
