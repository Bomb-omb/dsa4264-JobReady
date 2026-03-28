# dsa4264-JobReady

## Using `extract_skillsfuture.py`

`extract_skillsfuture.py` automates the SkillsFuture Skills Extraction & Comparison Tool with `pyautogui`.
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
3. Keep the browser window in the same layout used to set the coordinates in `extract_skillsfuture.py`.
4. Make sure downloads go to your normal `Downloads` folder.
5. Do not place the mouse in any screen corner, because `pyautogui` fail-safe is enabled.

The current screen positions are stored in:

- `TEXTBOX_POS`
- `SKILLS_TAB_POS`
- `APPS_TOOLS_TAB_POS`
- `DOWNLOAD_BTN_POS`
- `RESET_BTN_POS`

If the website layout changes or the clicks miss the controls, update those coordinates in `extract_skillsfuture.py`.

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
