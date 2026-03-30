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
It reads module descriptions from `data/2025-2026_module_clean_with_prereq.csv` and, by default,
updates that same file in place while resuming from the first pending row.

### Default input and output

- input file: `data/2025-2026_module_clean_with_prereq.csv`
- id column: `moduleCode`
- text column: `description`
- output column: `extracted_skills`
- apps/tools column: `extracted_apps_tools`
- status column: `done`
- default write mode: in place on the input CSV
- optional output file: set with `--output-file`

If the output columns do not exist in the input file, the script creates them automatically before saving.

### Test on the first course row

Use this first before running a batch:

```powershell
python extract_skillsfuture_course.py --row-index 0 --force
```

Expected result:

- `data/2025-2026_module_clean_with_prereq.csv` is updated in place by default
- it contains all original module columns plus `extracted_skills`, `extracted_apps_tools`, and `done`
- row `0` is updated in the working CSV
- `done` becomes `success` only if both tab downloads succeed

### Run the next pending batch

Use this to continue from the first row whose `done` value is `pending` and update only a bounded
number of physical rows:

```powershell
python extract_skillsfuture_course.py --row-count 10 --output-file data\2025-2026_module_clean_with_prereq_skillsfuture.csv
```

Behavior:

- the input CSV is both the load file and the working file by default
- processing starts at the first physical row whose normalized `done` value is exactly `pending`
- the script runs for the requested number of physical rows from that starting point
- duplicate descriptions are deduplicated only inside that selected row window
- rows already marked `success` inside that batch are skipped unless `--force` is used
- earlier rows marked `error: ...` are left untouched when finding the resume point

If there are no pending rows left, the script exits cleanly without writing anything.

If you want to keep the source CSV untouched, use a separate working file explicitly:

```powershell
python extract_skillsfuture_course.py --row-count 10 --output-file data/custom_skillsfuture.csv
```

When `--output-file` is provided:

- if the output file already exists, the script loads it first and continues from its first pending row
- if it does not exist, the script bootstraps from the input CSV and writes to the specified output file
- the source CSV remains unchanged

In default in-place mode, the script creates a one-time backup at
`data/2025-2026_module_clean_with_prereq.backup.csv`.
