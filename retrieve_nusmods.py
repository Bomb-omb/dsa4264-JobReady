import json
from pathlib import Path

import requests

BASE_DIR = Path(__file__).resolve().parent
ACADEMIC_YEAR = "2025-2026"
OUTPUT_PATH = BASE_DIR / "data" / "raw" / "nusmods" / f"{ACADEMIC_YEAR}_moduleInfo.json"


def fetch_module_info(acad_year: str) -> list[dict]:
    url = f"https://api.nusmods.com/v2/{acad_year}/moduleInfo.json"
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    return response.json()


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    module_info = fetch_module_info(ACADEMIC_YEAR)
    OUTPUT_PATH.write_text(json.dumps(module_info, indent=4), encoding="utf-8")

    print(f"Saved {ACADEMIC_YEAR}_moduleInfo.json to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
