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

## Using `train_ovr_logreg.py`

`train_ovr_logreg.py` trains one logistic regression classifier per skill on the accounting
job-description embeddings and ACC course embeddings in `embedding/acc`, then evaluates the
test split with top-k predictions.

Default inputs:

- jobs file: `data/acc/audit_tax_accounting_jobs.csv`
- jobs embeddings: `embedding/acc/acc_jobs_embeddings.jsonl`
- courses file: `data/2025-2026_module_clean_with_prereq_skillsfuture.csv`
- courses embeddings: `embedding/acc/acc_courses_embeddings.jsonl`
- label column: `extracted_skills`
- train split: `train`
- test split: `test`
- output folder: `embedding/acc/logreg_topk`

Example:

```powershell
python train_ovr_logreg.py --entity both --top-k 5
```

Outputs:

- `embedding/acc/logreg_topk/jobs/metrics_top_5.json`
- `embedding/acc/logreg_topk/jobs/predictions_top_5.csv`
- `embedding/acc/logreg_topk/courses/metrics_top_5.json`
- `embedding/acc/logreg_topk/courses/predictions_top_5.csv`
- `trained_skills.csv` inside each entity folder with one row per classifier

Useful flags:

- `--entity jobs` to run only accounting jobs
- `--entity courses` to run only ACC courses
- `--top-k 7` to change how many skills are returned at inference time
- `--min-positive-train 3` to require more positive examples before fitting a skill classifier
- `--jobs-embeddings-file path\to\jobs_embeddings.jsonl` to override the jobs embedding file
- `--courses-embeddings-file path\to\courses_embeddings.jsonl` to override the ACC courses embedding file

## Using `streamlit_app.py`

`streamlit_app.py` is the chatbot website for this project. It is designed as a light, school-oriented
career assistant that helps students ask in plain English about job postings, university modules, and
the links between them.

What it does:

- matches `course -> jobs`
- matches `job -> courses`
- supports free-text search over the job and course data
- uses local sentence embeddings for query and document representation
- uses the notebook-style OVR threshold model, tuned on the validation split, as the main ranking signal
- sends only the final structured context to OpenAI for answer generation using `OPENAI_API_KEY`
- shows ranked evidence cards so the answer stays grounded in the data
- supports both the ACC slice and a broader full-data mode from the sidebar

Retrieval behavior:

- the app loads the accounting job data from `data/acc/audit_tax_accounting_jobs.csv`
- the app loads module data from `data/2025-2026_module_clean_with_prereq_skillsfuture.csv`
- the app loads the precomputed local embeddings from `embedding/acc/acc_jobs_embeddings.jsonl`
  and `embedding/acc/acc_courses_embeddings.jsonl`
- the app runs a local sentence-transformer model for the user query only
- the query embedding is scored by the local OVR-threshold classifiers to predict relevant skills
- those predictions are combined with the local embeddings to rank jobs and modules
- the chat explanation layer uses the OpenAI Responses API with a configurable chat model

Full mode:

- switch the sidebar `Dataset mode` to `Full`
- jobs come from `data/mcf_entrylevel.csv` and `embedding/jobs_embeddings.jsonl`
- courses come from `data/2025-2026_moduleInfo_clean.csv` and `embedding/courses_embeddings.jsonl`
- the local OVR model is trained on the labeled rows that are available in the loaded data
- this gives you a broader job pool while keeping the course side searchable with the broader embedding corpus

Set up `.env` in the project root:

```dotenv
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-5.4-mini
LOCAL_EMBEDDING_MODEL=zeroentropy/zembed-1
LOCAL_EMBEDDING_DEVICE=cpu
LOCAL_EMBEDDING_DTYPE=float32
```

Run it from the project root:

```powershell
streamlit run streamlit_app.py
```

Example prompts:

- `What jobs fit ACC3706?`
- `Which modules help with audit roles?`
- `Show me courses related to governance and risk`
- `Which job posting is closest to financial reporting work?`

Notes:

- the sidebar includes a cache refresh button if you update the CSV files or embeddings
- the chatbot keeps conversation history inside the page session
- the model choice can be changed in the sidebar if your account uses a different allowed model
- if no API key is configured, the app still performs local ranking and shows the best matches
- if the local embedding stack is missing, the app will show a startup error instead of crashing

Troubleshooting:

- if you see `TypeError: Client.__init__() got an unexpected keyword argument 'proxies'`,
  reinstall dependencies so `httpx` is pinned below `0.28`:

```powershell
python -m pip install "httpx<0.28" --upgrade --force-reinstall
```
