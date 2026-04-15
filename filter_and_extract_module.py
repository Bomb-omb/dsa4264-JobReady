import csv
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_PATH = BASE_DIR / "data" / "raw" / "nusmods" / "2025-2026_moduleInfo.json"
OUTPUT_PATH = BASE_DIR / "data" / "2025-2026_moduleInfo_clean.csv"
FIELDS = ("moduleCode", "title", "description")
EXCLUDED_FACULTIES = {
    "Dentistry",
    "Cont and Lifelong Education",
    "YST Conservatory of Music",
    "Yale-NUS College",
    "Law",
    "Yong Loo Lin Sch of Medicine",
    "Duke-NUS Medical School",
}
EXCLUDED_DEPARTMENTS = {
    "Architecture",
    "Yale-NUS College",
    "FoL Dean's Office",
    "YSTCM Dean's Office",
    "SCALE Dean's Office",
    "Division of Graduate Dental Studies",
    "NUS Medicine Dean's Office",
    "Division of Graduate Medical Studies",
    "Medicine",
    "Duke-NUS Medical School",
    "Duke-NUS Dean's Office",
    "PharmacyandPharmaceuticalScience",
    "Pharmacology",
}
MIN_DESCRIPTION_WORDS = 20

#Remove general education pillar
EXCLUDED_MODULE_CODE_PATTERN = re.compile(r"^(HS|GE[A-Za-z])")

#remove internship modules because we don't know what students learn during intern
EXCLUDED_INTERNSHIP_PATTERN = re.compile(r"\binternships?\b", re.IGNORECASE)
WORD_PATTERN = re.compile(r"\b[\w'-]+\b")


def extract_module_number(module_code: str) -> int | None:
    match = re.search(r"(\d+)", module_code)
    return int(match.group(1)) if match else None


def count_words(text: str) -> int:
    return len(WORD_PATTERN.findall(text))


def should_keep_module(module: dict) -> bool:
    module_code = module.get("moduleCode", "")
    if EXCLUDED_MODULE_CODE_PATTERN.match(module_code):
        return False

    title = (module.get("title") or "").strip()
    description = (module.get("description") or "").strip()
    if EXCLUDED_INTERNSHIP_PATTERN.search(title):
        return False
    if EXCLUDED_INTERNSHIP_PATTERN.search(description):
        return False

    # these are exchange courses so dont have description so remove
    if description.lower() == "not available":
        return False
    if "exchange course" in description.lower():
        return False
    
    ## This remove courses that have description with <20 words
    ## the description is too short for reader to understand what they are teaching, so remove
    if count_words(description) < MIN_DESCRIPTION_WORDS:
        return False

    module_number = extract_module_number(module_code)
    # remove module that is 5k or above
    if module_number is not None and module_number >= 5000:
        return False

    if module.get("faculty") in EXCLUDED_FACULTIES:
        return False

    if module.get("department") in EXCLUDED_DEPARTMENTS:
        return False

    return True


def main() -> None:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_PATH}")

    modules = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    filtered_modules = [
        {field: module.get(field) for field in FIELDS}
        for module in modules
        if should_keep_module(module)
    ]

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(filtered_modules)

    print(f"Saved {len(filtered_modules)} records to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
