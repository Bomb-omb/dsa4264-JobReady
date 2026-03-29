# dsa4264-JobReady

## Using `extract_skillsfuture(jd).py`

`extract_skillsfuture(jd).py` automates the SkillsFuture Skills Extraction & Comparison Tool with `pyautogui`.
It reads job descriptions from a CSV, pastes them into the website, downloads both result tabs, and writes the extracted values back into the CSV.

### What it updates

For `data/jd2.csv`, the script uses:

- `description` as the input text
- `extracted_skills` for the Skills tab output
- `extracted_apps_tools` for the Apps & Tools tab output
- `done` for the shared status

When running in place, it also creates a one-time backup at `data/jd2.backup.csv`.

### Install dependencies

From the project root:

```powershell
python -m pip install pandas pyautogui pyperclip keyboard
```

### Prepare the browser

Before running the script:

1. Open Microsoft Edge.
2. Open the SkillsFuture Skills Extraction & Comparison Tool.
3. Keep the browser window in the same layout used to set the coordinates in `extract_skillsfuture(jd).py`.
4. Make sure downloads go to your normal `Downloads` folder.
5. Do not place the mouse in any screen corner, because `pyautogui` fail-safe is enabled.

The current screen positions are stored in:

- `TEXTBOX_POS`
- `SKILLS_TAB_POS`
- `APPS_TOOLS_TAB_POS`
- `DOWNLOAD_BTN_POS`
- `RESET_BTN_POS`

If the website layout changes or the clicks miss the controls, update those coordinates in `extract_skillsfuture(jd).py`.

### Test on the first row of `jd2.csv`

Use this first before a full run:

```powershell
python extract_skillsfuture.py --input-file data/jd2.csv --id-column uuid --text-column description --output-column extracted_skills --status-column done --row-index 0 --in-place --force
```

Expected result:

- row `0` in `data/jd2.csv` is updated
- `extracted_skills` contains the Skills tab output
- `extracted_apps_tools` contains the Apps & Tools tab output
- `done` becomes `success` only if both tab downloads succeed

### Run the full `jd2.csv`

```powershell
python extract_skillsfuture.py --input-file data/jd2.csv --id-column uuid --text-column description --output-column extracted_skills --status-column done --in-place
```

Behavior:

- duplicate descriptions are processed once and mapped back to matching rows
- rows already marked `success` are skipped unless `--force` is used
- partial results are preserved if one tab succeeds and the other fails
- `done` is written as `error: ...` if the row does not complete successfully

### Notes

- The script removes `; Tags: ...` suffixes from downloaded values before saving them.
- `Apps & Tools` is treated as a valid empty result if the CSV downloads correctly but contains no items.
- If you want to inspect the available flags:

```powershell
python extract_skillsfuture.py --help
```

## Using `extract_skillsfuture_course.py`

`extract_skillsfuture_course.py` automates the same SkillsFuture workflow for NUS course descriptions.
It reads module descriptions from `data/2025-2026_module_clean_with_prereq.csv` and writes results to a
derived CSV by default so the source file stays untouched.

### Default input and output

- input file: `data/2025-2026_module_clean_with_prereq.csv`
- id column: `moduleCode`
- text column: `description`
- output column: `extracted_skills`
- apps/tools column: `extracted_apps_tools`
- status column: `done`
- default output file: `data/2025-2026_module_clean_with_prereq_skillsfuture.csv`

If the output columns do not exist in the input file, the script creates them automatically in the output.

### Test on the first course row

Use this first before a full run:

```powershell
python extract_skillsfuture_course.py --row-index 0 --force
```

Expected result:

- `data/2025-2026_module_clean_with_prereq_skillsfuture.csv` is created
- it contains all original module columns plus `extracted_skills`, `extracted_apps_tools`, and `done`
- row `0` is updated in the derived CSV
- `done` becomes `success` only if both tab downloads succeed

### Run the full course file

```powershell
python extract_skillsfuture_course.py
```

Behavior:

- duplicate descriptions are processed once and mapped back to matching rows
- rows already marked `success` are skipped unless `--force` is used
- partial results are preserved if one tab succeeds and the other fails
- the source CSV remains unchanged by default

### Resume from a course code for a fixed number of rows

Use this to continue from a specific module code and update only a bounded batch of physical rows:

```powershell
python extract_skillsfuture_course.py --start-course-code CS1010 --row-count 10
```

Behavior:

- the working file becomes `data/2025-2026_module_clean_with_prereq_skillsfuture.csv`
- if that file already exists, the script loads it first so previous extracted values and `done` statuses are preserved
- if that file does not exist, the script bootstraps from `data/2025-2026_module_clean_with_prereq.csv` and creates the derived output on save
- processing starts at the first exact `moduleCode` match and runs for the requested number of physical rows
- duplicate descriptions are deduplicated only inside that selected row window

If you need a different derived output target for batch mode, you can override it explicitly:

```powershell
python extract_skillsfuture_course.py --start-course-code CS1010 --row-count 10 --output-file data/custom_skillsfuture.csv
```

### Optional in-place run

If you explicitly want to update the source CSV instead of writing the derived output file:

```powershell
python extract_skillsfuture_course.py --in-place
```

This creates a one-time backup at `data/2025-2026_module_clean_with_prereq.backup.csv`.
`--in-place` cannot be combined with `--start-course-code`.
