# Project Plan: Course-Job Alignment Pipeline

## 1. Project Goal

The end goal of this project is not just to find similar words between courses and jobs. The goal is to build a pipeline that can:

- understand what a course teaches
- understand what a job requires
- measure how well courses and jobs align with each other
- explain that relevance in terms of matched and missing skills

The desired user-facing outcome is:

Given a course, the system should be able to answer:

- which jobs are most relevant to this course
- how many jobs pass a relevance threshold
- which skills taught by the course match each job
- which important job skills are missing from the course

Given a job, the system should also be able to answer:

- which courses best prepare a student for this job
- how many courses meaningfully align with this job
- which required job skills are covered by each course
- which required job skills are still missing

Later, this can be wrapped in a chatbot so a user can ask questions naturally, but the core logic should first be built as a retrieval and scoring pipeline.

## 2. Recommended Modeling Approach

The recommended setup is to use two different signals.

### 2.1 Primary semantic signal

Use embeddings for:

- course descriptions
- job descriptions

This is the main semantic layer. Descriptions contain much richer context than skill keywords alone. They capture domain, task type, depth, and framing, which makes them the best first representation for course-job alignment.

### 2.2 Secondary structured signal

Use extracted skills as metadata for:

- course skills
- job skills

These should be stored and compared directly, but they should not be the main representation at the start. Skills are very useful for interpretability, overlap analysis, reranking, and later model features, but on their own they are usually too sparse and noisy to represent the whole course-job relationship.

### 2.3 Relevance score

The first version of relevance should be a combined score, not a single metric. A good initial design is:

- description embedding similarity
- skill overlap count
- weighted skill overlap
- optional prerequisite, domain, or category alignment later

This makes the system both useful and explainable in both directions.

## 3. What Existing Files Already Do

The current repository already contains useful pieces of the pipeline.

### 3.1 Course data preparation

[`filter_and_extract_module.py`](./filter_and_extract_module.py)

- Reads raw NUSMods module JSON.
- Filters out modules that are not relevant for the analysis.
- Keeps the main fields needed for downstream work: `moduleCode`, `title`, and `description`.
- Writes the cleaned module CSV to `data/2025-2026_moduleInfo_clean.csv`.

[`extract_prereq_courses.py`](./extract_prereq_courses.py)

- Reads the cleaned course CSV.
- Fetches prerequisite trees from the NUSMods API.
- Extracts prerequisite course codes and appends them.
- Writes the enriched course file to `data/2025-2026_module_clean_with_prereq.csv`.

### 3.2 Job and course skill extraction

[`extract_skillsfuture_course.py`](./extract_skillsfuture_course.py)

- Reads course descriptions.
- Automates the SkillsFuture extraction website.
- Writes `extracted_skills`, `extracted_apps_tools`, and `done` columns.
- By default writes to a derived course CSV, preserving the original source file.

[`extract_skillsfuture(jd).py`](./extract_skillsfuture(jd).py)

- Reads job descriptions from a job CSV.
- Automates the same SkillsFuture extraction process for job descriptions.
- Writes extracted skill columns back to the job CSV or a derived copy depending on run mode.

### 3.3 Embedding generation

[`build_embeddings.py`](./build_embeddings.py)

- Reads jobs and courses CSVs.
- Builds three record sets: jobs, courses, and skills.
- Embeds the `description` text for jobs and courses.
- Also embeds skill names when skill columns are present.
- Writes JSONL embedding outputs and a manifest under `embedding/`.

This script is useful, but it currently mixes two concerns:

- the main semantic embeddings we want to rely on
- skill embeddings, which are probably optional for the first version

For the next phase, the project should treat job/course description embeddings as the main output, while skill columns remain structured evidence.

## 4. Current Data Files Relevant To The Next Phase

These are the key files that matter for the next stage.

### 4.1 Current course-side files

- `data/2025-2026_moduleInfo_clean.csv`
  - clean course base file
- `data/2025-2026_module_clean_with_prereq.csv`
  - course file enriched with prerequisite course codes
- `data/2025-2026_module_clean_with_prereq_skillsfuture.csv`
  - expected enriched course file after SkillsFuture extraction

### 4.2 Current job-side files

- `data/mcf_entrylevel.csv`
  - most likely main job file for the embedding stage
- `data/jd2.csv` and related `jd*.csv`
  - earlier or intermediate job extraction files
- `data/mcf_clean_data.csv`
  - likely earlier cleaned job dataset

Before building the retrieval pipeline, the team should confirm one canonical job input file and one canonical course input file so downstream scripts do not depend on multiple inconsistent CSV variants.

### 4.3 Current embedding outputs

- `embedding/jobs_embeddings.jsonl`
- `embedding/courses_embeddings.jsonl`
- `embedding/skills_embeddings.jsonl`
- `embedding/manifest.json`

The first two are the most important for the next phase.

## 5. Recommended Canonical Data Flow

The pipeline should be treated as a sequence of clear stages.

### Stage 1: Prepare course data

1. Run `filter_and_extract_module.py`
2. Run `extract_prereq_courses.py`
3. Run `extract_skillsfuture_course.py`

Expected course output for later stages:

- `moduleCode`
- `title`
- `description`
- `prereqCourseCodes`
- `extracted_skills`
- `extracted_apps_tools`
- `done`

### Stage 2: Prepare job data

1. Select the canonical jobs CSV
2. Ensure it has at least:
   - `uuid`
   - `title`
   - `description`
3. Run `extract_skillsfuture(jd).py` on that canonical file

Expected job output for later stages:

- `uuid`
- `title`
- `description`
- `extracted_skills`
- `extracted_apps_tools`
- `done`

### Stage 3: Build semantic embeddings

Use embeddings for:

- course descriptions
- job descriptions

Do not make skill embeddings the main dependency of the pipeline yet.

### Stage 4: Build alignment scoring

For each course-job pair:

1. Compare the course embedding with all job embeddings
2. Rank jobs by semantic similarity for the course-centric view
3. Rank courses by semantic similarity for the job-centric view
4. Compare course skills with each paired job’s skills
5. Produce a combined alignment score
6. Save interpretable output tables

### Stage 5: Build user-facing outputs

For each course, generate:

- top relevant jobs
- number of jobs above threshold
- matched skills per job
- missing skills per job
- summary metrics for analytics

For each job, also generate:

- top relevant courses
- number of courses above threshold
- matched skills per course
- missing skills per course
- summary metrics for analytics

### Stage 6: Add chatbot layer

Once the scoring layer is stable, the chatbot can sit on top of it and explain the results in natural language.

## 6. Minimal New Files To Create

To keep the project clean, the next stage should add only a few focused files instead of many scripts with overlapping responsibility.

### 6.1 `prepare_analysis_data.py`

Purpose:

- read the canonical enriched course CSV and canonical enriched job CSV
- standardize columns
- clean text fields
- parse skill columns into normalized Python lists
- optionally drop rows with missing descriptions
- write clean analysis-ready CSV or parquet files

Why this is needed:

Right now data preparation is spread across extraction scripts. This file should define the exact datasets used by the relevance pipeline so later stages work from one clean source of truth.

Suggested outputs:

- `data/processed/courses_analysis.csv`
- `data/processed/jobs_analysis.csv`

### 6.2 `build_description_embeddings.py`

Purpose:

- build embeddings only for course descriptions and job descriptions
- remove the ambiguity around whether to embed skills
- write only the semantic embedding outputs used by the retrieval layer

Why this is needed:

`build_embeddings.py` currently embeds jobs, courses, and skills together. For the first real relevance pipeline, it is cleaner to separate semantic description embeddings from optional skill experiments.

Suggested outputs:

- `embedding/jobs_description_embeddings.jsonl`
- `embedding/courses_description_embeddings.jsonl`
- `embedding/manifest_descriptions.json`

Optional note:

This can be implemented either as a new script or by refactoring `build_embeddings.py` into clearer modes. If the team prefers minimal file count, updating `build_embeddings.py` with a `--descriptions-only` mode is also acceptable.

### 6.3 `score_course_job_relevance.py`

Purpose:

- load course and job description embeddings
- compute pairwise or top-k cosine similarity
- parse job and course skills
- compute skill overlap metrics
- combine signals into an initial alignment score
- save ranked course-job matches that can be viewed from either direction

Why this is needed:

This is the core analytics script. It turns embeddings and extracted skills into an interpretable alignment table.

Suggested outputs:

- `results/course_job_matches.csv`
- `results/course_summary.csv`
- `results/job_summary.csv`

Expected columns for `course_job_matches.csv`:

- `course_code`
- `course_title`
- `job_id`
- `job_title`
- `description_similarity`
- `matched_skills_count`
- `job_skills_count`
- `course_skills_count`
- `matched_skills`
- `missing_job_skills`
- `relevance_score`
- `rank_within_course`

Expected columns for `course_summary.csv`:

- `course_code`
- `course_title`
- `relevant_job_count`
- `avg_relevance_score`
- `top_job_titles`
- `top_matched_skills`
- `top_missing_skills`

Expected columns for `job_summary.csv`:

- `job_id`
- `job_title`
- `relevant_course_count`
- `avg_relevance_score`
- `top_course_codes`
- `top_course_titles`
- `top_matched_skills`
- `top_missing_skills`

### 6.4 `app.py` or `streamlit_app.py`

Purpose:

- provide a simple interface for selecting a course or a job
- show top matching jobs for a course
- show top matching courses for a job
- show matched and missing skills in both directions
- later support chatbot-style natural-language explanation

Why this is needed:

This should come after the scoring logic works. It is the presentation layer, not the modeling layer.

Use only one app entry point to keep the project tidy.

## 7. Suggested Folder Structure

Keep the structure small and explicit.

Suggested additions:

```text
data/
  processed/
    courses_analysis.csv
    jobs_analysis.csv

embedding/
  jobs_description_embeddings.jsonl
  courses_description_embeddings.jsonl
  manifest_descriptions.json

results/
  course_job_matches.csv
  course_summary.csv
  job_summary.csv

prepare_analysis_data.py
build_description_embeddings.py
score_course_job_relevance.py
streamlit_app.py
```

If the team wants even fewer files, `build_description_embeddings.py` can be replaced by a cleaner version of the existing `build_embeddings.py`.

## 8. Detailed Execution Plan

### Phase 1: Lock the source-of-truth datasets

Objective:

Choose exactly one course CSV and one job CSV for downstream analytics.

Work to do:

- confirm the canonical course file after SkillsFuture extraction
- confirm the canonical job file after SkillsFuture extraction
- document those filenames in `README.md`
- stop downstream scripts from switching between multiple job CSV variants

Why this matters:

If the source files change between runs, any relevance analysis becomes hard to reproduce.

### Phase 2: Build analysis-ready datasets

Objective:

Create clean tables specifically for matching and scoring.

Work to do:

- create `prepare_analysis_data.py`
- normalize description text
- normalize skill strings into clean deduplicated lists
- preserve identifiers such as `moduleCode` and `uuid`
- preserve titles for reporting
- preserve prerequisite columns for future experiments
- write processed analysis tables

Success criteria:

- both processed files have consistent schemas
- rows with usable descriptions are ready for embedding
- skill columns are normalized enough for overlap comparison

### Phase 3: Build semantic description embeddings

Objective:

Generate only the embeddings needed for course-job retrieval in both directions.

Work to do:

- create `build_description_embeddings.py` or refactor `build_embeddings.py`
- embed `description` for courses
- embed `description` for jobs
- save embeddings with identifiers and metadata
- write a manifest describing model, files, and counts

Success criteria:

- every valid course has a description embedding
- every valid job has a description embedding
- outputs are stable and reproducible

### Phase 4: Implement the first alignment score

Objective:

Turn embeddings and skill metadata into ranked course-job matches that support both course-centric and job-centric queries.

Work to do:

- create `score_course_job_relevance.py`
- compute cosine similarity between each course and all jobs
- keep top-k jobs per course
- derive top-k courses per job from the same match table
- compare normalized course skill list against normalized job skill list
- compute:
  - raw overlap count
  - overlap ratio
  - missing job skills
  - optional weighted overlap later
- combine semantic similarity and skill overlap into a first alignment score

Recommended first formula:

`relevance_score = 0.7 * description_similarity + 0.3 * skill_overlap_ratio`

This does not need to be the final formula. It is a practical first baseline that balances meaning and explainability.

Success criteria:

- every course has a ranked list of jobs
- every job has a ranked list of courses
- each match includes both a semantic score and skill evidence
- outputs are usable for manual inspection

### Phase 5: Define thresholding and reporting

Objective:

Answer the business question in a way that is interpretable from both directions.

Work to do:

- choose a relevance threshold for counting jobs as relevant
- choose a relevance threshold for counting courses as relevant to a job
- generate per-course summary outputs
- generate per-job summary outputs
- inspect edge cases manually
- compare obviously related and obviously unrelated course-job pairs

Possible thresholding approach:

- start with a top-k inspection workflow
- manually review the top 10 to 20 jobs for a sample of courses
- set an initial threshold based on the distribution of relevance scores
- revise after seeing real examples

Why this matters:

The threshold should not be arbitrary. It should come from inspecting actual matches.

### Phase 6: Evaluate and refine

Objective:

Check whether the pipeline is producing sensible results before adding an LLM layer.

Work to do:

- sample a set of courses from different disciplines
- inspect top job matches
- inspect matched and missing skills
- identify false positives and false negatives
- tune the weighting between semantic similarity and skill overlap
- decide whether prerequisite alignment should be introduced

Optional later work:

- add job clustering
- add course category labels
- add job family labels
- train a supervised relevance model once labels exist

### Phase 7: Add the chatbot layer

Objective:

Expose the pipeline through a user-friendly interface.

Work to do:

- create `streamlit_app.py` or `app.py`
- let the user select a course or paste a course description
- let the user select a job or paste a job description
- retrieve top relevant jobs from the scored results for course queries
- retrieve top relevant courses from the scored results for job queries
- display matched skills and missing skills
- optionally call an LLM to explain the results in plain language

Important design principle:

The LLM should explain retrieved evidence, not invent relevance from scratch.

The LLM input should include:

- course title and description
- job title and description
- top matched jobs
- top matched courses
- relevance scores
- matched skills
- missing skills

The LLM output should focus on:

- how relevant the course is to the job market
- how well a job is covered by available courses
- which job families align most strongly
- which courses best prepare a user for a chosen job
- which skills are covered well
- which skills may still be missing

## 9. What Not To Do Yet

To keep the project focused, avoid these for now:

- do not make standalone skill embeddings the main relevance engine
- do not train a classifier before the baseline retrieval pipeline exists
- do not introduce a chatbot before the scoring outputs are trustworthy
- do not maintain multiple overlapping scripts that all partially prepare the same downstream data

## 10. Immediate Next Actions

The next concrete steps should be:

1. Confirm the canonical enriched jobs CSV and canonical enriched courses CSV.
2. Create `prepare_analysis_data.py` to produce clean processed analysis tables.
3. Create or refactor the embedding script so it only builds description embeddings for the main pipeline.
4. Create `score_course_job_relevance.py` for ranking, overlap analysis, and both course-centric and job-centric summary outputs.
5. Inspect the first batch of results manually before adding any chatbot layer.

## 11. Summary

The project should move forward with this logic:

- use course descriptions and job descriptions as the main semantic representation
- use extracted skills as structured evidence and overlap features
- define course-job alignment as a combined score
- build a clean retrieval and scoring pipeline first
- add a chatbot only after the analytics layer is reliable

This approach is the most practical starting point because it supports both `course -> job` and `job -> course` use cases, while staying explainable enough for later modeling and chatbot work.
