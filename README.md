# dsa4264-JobReady

The technical report is [here](https://bomb-omb.github.io/dsa4264-JobReady/)

## Embedding and Data Folder Note

This project references a `data/` folder throughout the scripts and notebooks, but that folder has been  removed to satisfy submission requirements. This note is here so readers are not confused when they see paths under `data/` in the code.

This project also uses an `embedding/` folder to store vector embeddings of jobs, courses&skills description. The folder has been removed to satisfy submission requirements. This note is here so readers are not confused when they see paths under `embedding/` in the code.

The main files and subfolders the code expects are:

### Raw data
- `data/raw/nusmods/`: raw NUSMods JSON exports used to build the module datasets
- `data/raw/mcf_data/`: raw MyCareersFuture job-posting JSON files
- `data/raw/jobsandskills-skillsfuture-unique-skills-list.xlsx`: raw SkillsFuture unique-skills source file
- `data/raw/jobsandskills-skillsfuture-tsc-to-unique-skills-mapping.xlsx`: raw SkillsFuture sector mapping file

### Module data
- `data/2025-2026_moduleInfo_clean.csv`: broader cleaned module dataset
- `data/2025-2026_module_clean_with_prereq.csv`: cleaned NUS module dataset before SkillsFuture extraction
- `data/2025-2026_module_clean_with_prereq_skillsfuture.csv`: module dataset after SkillsFuture skill extraction

These three files are part of a derivation chain:
`data/2025-2026_module_clean_with_prereq.csv` -> `data/2025-2026_moduleInfo_clean.csv` -> `data/2025-2026_module_clean_with_prereq_skillsfuture.csv`
How each file is derived is explained in later sections of this README.

### Jobs Data
- `data/mcf_clean_data.csv`: intermediate cleaned MyCareersFuture job dataset
- `data/mcf_entrylevel.csv`: filtered entry-level jobs dataset derived from `data/mcf_clean_data.csv` and added skills from SkillsFuture

### Cleaned Skills Taxonomy
- `data/skills_taxo.csv`: SkillsFuture skills taxonomy 

### Accountancy dataset
- `data/acc/audit_tax_accounting_jobs.csv`: accounting-focused jobs dataset 
- `data/acc/acc_courses.csv`: accounting-focused course subset 
- `data/acc/skills_taxo_acc.csv`: accounting-only filtered skills taxonomy

## How was the course data derived?

`retrieve_nusmods.py` downloads the raw NUSMods module catalogue for academic year `2025-2026` from the public NUSMods API and saves it to `data/raw/nusmods/2025-2026_moduleInfo.json`. This is the first data-ingestion step for the NUS course pipeline.

`filter_and_extract_module.py` cleans and filters the raw NUSMods module export into a smaller course dataset containing only `moduleCode`, `title`, and `description`. It removes general education modules, internship modules, exchange-style records, selected faculties and departments, and modules at the 5000 level or above, then writes the result to `data/2025-2026_moduleInfo_clean.csv`.

`extract_prereq_courses.py` enriches the cleaned NUS module dataset with prerequisite course codes by querying the per-module NUSMods API. It fetches prerequisite trees then outputs `data/2025-2026_module_clean_with_prereq.csv`.

`extract_skillsfuture_course.py` automates the SkillsFuture skills extraction for courses in `data/2025-2026_module_clean_with_prereq.csv` to produce `data/2025-2026_module_clean_with_prereq_skillsfuture.csv`. The instructions to run it can be found under [Using extract_skillsfuture_course.py](#using-extract_skillsfuture_coursepy)

## `check_extraction_(courses).ipynb`

`check_extraction_(courses).ipynb` is a QA and cleanup notebook for the course extraction output in `data/2025-2026_module_clean_with_prereq_skillsfuture.csv`. It validates `extracted_skills` against the SkillsFuture taxonomy in `data/skills_taxo.csv`, identifies unmatched skill names, replaces partial/truncated matches with the correct taxonomy labels where possible, removes invalid leftovers, and confirms that no unmatched skills remain after cleaning. 

The notebook also audits courses with missing `extracted_skills` and `extracted_apps_tools`, checks the `done` status column to diagnose extraction failures, resets rows affected by a known extraction bug back to `pending` for reruns, and samples the remaining blank rows to estimate residual extraction error. 

In addition, it contains manual review and removal of some skills that were falsely included by the SkillsFuture tools based on the description. 
 
Lastly, records that courses with descriptions under 20 words or marked `Not Applicable` were removed outside the notebook because they are below the minimum description length recommended for SkillsFuture extraction.

## How was the jobs data derived?
### `extract_mcf_fields.py`

`extract_mcf_fields.py` converts raw MyCareersFuture JSON job-posting files from `data/raw/mcf_data/` into a cleaned tabular dataset at `data/mcf_clean_data.csv`. The script cleans HTML and encoding issues, standardizes text fields, and extracts minimum years of experience.

`extract_skillsfuture(jd).py` automates the SkillsFuture skills extractions for the jobs in `data/mcf_entrylevel.csv` and edited the csv in-place. The instructions to run it can be found under [Using extract_skillsfuture(jd).py](#using-extract_skillsfuturejdpy)

### `mcf_entrylevel.ipynb`

`mcf_entrylevel.ipynb` prepares the entry-level subset of the MCF job postings dataset for downstream analysis. It starts from `data/mcf_clean_data.csv` with 22,719 cleaned postings, filters for roles that mention bachelor-level education keywords and are either fresh/junior roles or require fewer than 4 years of experience, and produces an initial set of 1,589 candidate jobs into `data/mcf_clean_data.csv`. 

The notebook then reviews missing extracted skills and tools in `data/mcf_entrylevel.csv`, applies a few manual fixes, removes two unsuitable records, cleans leftover emoji noise from titles and descriptions, and saves the final output to `data/mcf_entrylevel.csv` with 1,587 entry-level postings. 

To improve consistency, it also builds a SkillsFuture-based skill taxonomy file (`data/skills_taxo.csv`) and normalizes the extracted skills against that taxonomy, including fixing cases where multi-word skills were incorrectly split by delimiters. After the final cleanup, the skill labels align with the taxonomy.

After review some courses and jobs using the 2 notebooks mentioned above, the group realised that there is too many courses and jobs to clean up so we decided to focus only on the accountancy related jobs & courses.

## Accountancy subset

`extract_mcf_audit_tax_accounting_roles.py` filters `data/mcf_entrylevel.csv` to keep only audit, tax, and accounting-related roles. It uses rule-based keyword matching on job titles, job categories, and job descriptions, then saves the accounting-focused subset to `data/acc/audit_tax_accounting_jobs.csv`.

`filter_acc_skills.py` creates an accounting-focused SkillsFuture taxonomy by filtering the broader skills taxonomy using the SkillsFuture sector mapping file. It keeps skills associated with the `Accountancy` and `Financial Services` sectors and saves the result to `data/acc/skills_taxo_acc.csv`.

## Embeddings

`build_embeddings.py` builds the embedding files used by the model notebooks and the Streamlit app. It reads the cleaned job, course, and skill datasets, generates local sentence embeddings, assigns train/validation/test splits, and writes the JSONL outputs under `embedding/`.

## `Model` folder

### Cosine Similarity Threshold Model

`model/cosine_sim_thres.ipynb` is the exploratory notebook used to develop and compare these thresholding approaches. It starts with a jobs-only version of the cosine-similarity model, documents the threshold-selection logic step by step, and compares the performance of global-threshold, common-skill, and greedy threshold tuning. It then extends the setup to a combined jobs-plus-courses dataset, shows that using a single shared thresholding scheme across both entity types reduces performance, and introduces a two-part model that learns separate thresholds for jobs and courses. The notebook also tests different numbers of greedy optimization rounds and evaluates all learned thresholding strategies on a validation split. In the recorded notebook run, the two-part greedy model with 2 greedy rounds gave the best overall validation performance among the tested variants.

`model/cosine_sim_two_part.py` implements the cosine-similarity skill prediction pipeline. It loads job/course labels and embeddings, computes similarity between entities and skill embeddings, and compares several thresholding strategies: a global threshold, skill-specific thresholds for common skills, greedy per-skill tuning for better micro-F1, and a two-part version with separate thresholds for jobs and courses. It also provides evaluation utilities that output metrics, learned thresholds, and predicted skills.

### Cosine Similarity Top K Model



### One-vs-Rest (OvR) Threshold Model

`model/ovr_logreg_thres.ipynb` is the exploratory notebook used to develop and compare the one-vs-rest logistic regression threshold model. It builds the project-required jobs-plus-courses dataset, trains one logistic regression classifier per skill, and compares a single global probability threshold against skill-specific thresholds tuned on the validation split. The notebook then selects the final configuration using validation performance, reports the locked held-out test metrics, and uses the selected model to build the skills gap table that links predicted job demand to curriculum coverage. In the recorded notebook run, the `jobs_plus_courses + global` threshold configuration gave the best overall validation performance among the tested variants.

### One-vs-Rest (OvR) Top K Model



## Using `extract_skillsfuture(jd).py`

`extract_skillsfuture(jd).py` automates the SkillsFuture Skills Extraction & Comparison Tool with `pyautogui`.
It reads job descriptions from a CSV, pastes them into the website, downloads both result tabs, and writes the extracted values back into the CSV.

### Default target

By default, the script reads and updates the MyCareersFuture entry-level jobs file:

- input file: `data/mcf_entrylevel.csv`
- id column: `uuid`
- text column: `description`
- output column: `extracted_skills`
- apps/tools column: `extracted_apps_tools`
- status column: `done`

Before the first overwrite, it creates a one-time backup at `data/mcf_entrylevel.backup.csv`.

### What it updates

For `data/mcf_entrylevel.csv`, the script uses:

- `description` as the input text
- `extracted_skills` for the Skills tab output
- `extracted_apps_tools` for the Apps & Tools tab output
- `done` for the shared status

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

### Test on the first row of `mcf_entrylevel.csv`

Use this first before a full run:

```powershell
python "extract_skillsfuture(jd).py" --row-index 0 --force
```

Expected result:

- row `0` in `data/mcf_entrylevel.csv` is updated
- `extracted_skills` contains the Skills tab output
- `extracted_apps_tools` contains the Apps & Tools tab output
- `done` becomes `success` only if both tab downloads succeed

### Run the full `mcf_entrylevel.csv`

```powershell
python "extract_skillsfuture(jd).py"
```

Behavior:

- the script always updates the input CSV in place, including custom files passed with `--input-file`
- duplicate descriptions are processed once and mapped back to matching rows
- rows already marked `success` are skipped unless `--force` is used
- partial results are preserved if one tab succeeds and the other fails
- `done` is written as `error: ...` if the row does not complete successfully

If you want to run the same workflow on a different CSV, override the defaults explicitly:

```powershell
python "extract_skillsfuture(jd).py" --input-file data/custom_jobs.csv --id-column uuid --text-column description
```

### Notes

- The script removes `; Tags: ...` suffixes from downloaded values before saving them.
- `Apps & Tools` is treated as a valid empty result if the CSV downloads correctly but contains no items.
- PowerShell examples quote the script name because the filename contains parentheses.
- If you want to inspect the available flags:

```powershell
python "extract_skillsfuture(jd).py" --help
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

Use this to continue from the first row whose `done` value is `pending` and update only a bounded number of physical rows:

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
