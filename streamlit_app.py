from __future__ import annotations

import html
import json
import os
import re
import hashlib
import pickle
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import streamlit as st
from build_embeddings import load_embedding_model
from dotenv import load_dotenv
from openai import OpenAI
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from train_ovr_logreg import (
    combine_rows as ovr_combine_rows,
    evaluate_with_threshold,
    find_best_global_threshold,
    fit_label_binarizer,
    fit_models,
    load_embedding_rows as ovr_load_embedding_rows,
    parse_skill_values as ovr_parse_skill_values,
    predict_probabilities,
    select_split_rows,
)


BASE_DIR = Path(__file__).resolve().parent
JOB_FILE = BASE_DIR / "data" / "acc" / "audit_tax_accounting_jobs.csv"
COURSE_FILE = BASE_DIR / "data" / "2025-2026_module_clean_with_prereq_skillsfuture.csv"
JOB_EMBEDDINGS_FILE = BASE_DIR / "embedding" / "acc" / "acc_jobs_embeddings.jsonl"
COURSE_EMBEDDINGS_FILE = BASE_DIR / "embedding" / "acc" / "acc_courses_embeddings.jsonl"

OPENAI_EMBEDDING_MODEL = "text-embedding-3-small"
DEFAULT_CHAT_MODEL = "gpt-5.4-mini"
CHAT_MODEL_FALLBACKS = (DEFAULT_CHAT_MODEL, "gpt-5.2-mini", "gpt-4.1-mini")
MAX_CONTEXT_ITEMS = 4
MAX_SNIPPET_CHARS = 360
MAX_HISTORY_TURNS = 6
LOCAL_EMBEDDING_MODEL = os.getenv("LOCAL_EMBEDDING_MODEL", "zeroentropy/zembed-1")
LOCAL_EMBEDDING_DEVICE = os.getenv("LOCAL_EMBEDDING_DEVICE", "cpu")
LOCAL_EMBEDDING_DTYPE = os.getenv("LOCAL_EMBEDDING_DTYPE", "float32")
OVR_MIN_POSITIVE_TRAIN = int(os.getenv("OVR_MIN_POSITIVE_TRAIN", "2"))
OVR_MIN_POSITIVE_TRAIN_FULL = int(os.getenv("OVR_MIN_POSITIVE_TRAIN_FULL", "15"))
OVR_MAX_ITER = int(os.getenv("OVR_MAX_ITER", "1000"))
OVR_RANDOM_STATE = int(os.getenv("OVR_RANDOM_STATE", "42"))
MIN_DISPLAY_MATCH_SCORE = float(os.getenv("MIN_DISPLAY_MATCH_SCORE", "0.65"))
MIN_DISPLAY_MATCH_SKILLS = int(os.getenv("MIN_DISPLAY_MATCH_SKILLS", "2"))
RUNTIME_MODEL_CACHE_DIR = BASE_DIR / "embedding" / "runtime_cache"

load_dotenv()


@dataclass(frozen=True)
class KnowledgeItem:
    kind: str
    item_id: str
    title: str
    subtitle: str
    description: str
    search_text: str
    payload: dict[str, Any]


@dataclass(frozen=True)
class MatchResult:
    item: KnowledgeItem
    score: float
    semantic_score: float
    lexical_score: float
    highlight_terms: list[str]


@dataclass(frozen=True)
class KnowledgeBase:
    jobs: list[KnowledgeItem]
    courses: list[KnowledgeItem]
    job_embeddings: np.ndarray | None
    course_embeddings: np.ndarray | None
    vectorizer: TfidfVectorizer | None
    job_tfidf: Any
    course_tfidf: Any
    retrieval_mode: str
    status_message: str


@dataclass(frozen=True)
class IndexedItem:
    source: str
    item_id: str
    title: str
    description: str
    skills: list[str]
    embedding: np.ndarray
    split: str


@dataclass(frozen=True)
class OVRRuntime:
    class_names: list[str]
    models: list[LogisticRegression]
    threshold: float
    metrics: dict[str, float]


@dataclass(frozen=True)
class AppRuntime:
    encoder: Any
    skill_model: OVRRuntime
    items: list[IndexedItem]
    status_message: str


def skill_model_cache_path(mode_label: str, min_positive_train: int) -> Path:
    safe_mode = re.sub(r"[^A-Za-z0-9_.-]+", "_", mode_label).lower()
    return RUNTIME_MODEL_CACHE_DIR / f"{safe_mode}_skill_model_min{min_positive_train}.pkl"


def load_cached_skill_model(cache_path: Path) -> OVRRuntime | None:
    if not cache_path.exists():
        return None

    try:
        with cache_path.open("rb") as handle:
            cached = pickle.load(handle)
    except Exception:
        return None

    if isinstance(cached, OVRRuntime):
        return cached
    return None


def save_cached_skill_model(cache_path: Path, skill_model: OVRRuntime) -> None:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    with cache_path.open("wb") as handle:
        pickle.dump(skill_model, handle, protocol=pickle.HIGHEST_PROTOCOL)


@dataclass(frozen=True)
class SourceSpec:
    data_file: Path
    embeddings_file: Path
    id_column: str
    title_columns: tuple[str, ...]
    description_columns: tuple[str, ...]
    skill_columns: tuple[str, ...]


@dataclass(frozen=True)
class DatasetMode:
    label: str
    jobs: SourceSpec
    courses: SourceSpec
    notes: str


ACC_MODE = DatasetMode(
    label="ACC",
    jobs=SourceSpec(
        data_file=BASE_DIR / "data" / "acc" / "audit_tax_accounting_jobs.csv",
        embeddings_file=BASE_DIR / "embedding" / "acc" / "acc_jobs_embeddings.jsonl",
        id_column="uuid",
        title_columns=("title", "raw_title"),
        description_columns=("description", "raw_description"),
        skill_columns=("extracted_skills",),
    ),
    courses=SourceSpec(
        data_file=BASE_DIR / "data" / "2025-2026_module_clean_with_prereq_skillsfuture.csv",
        embeddings_file=BASE_DIR / "embedding" / "acc" / "acc_courses_embeddings.jsonl",
        id_column="moduleCode",
        title_columns=("title", "moduleTitle"),
        description_columns=("description", "moduleDescription"),
        skill_columns=("extracted_skills",),
    ),
    notes="Focused accounting, audit, and tax slice.",
)

FULL_MODE = DatasetMode(
    label="Full",
    jobs=SourceSpec(
        data_file=BASE_DIR / "data" / "mcf_entrylevel.csv",
        embeddings_file=BASE_DIR / "embedding" / "jobs_embeddings.jsonl",
        id_column="uuid",
        title_columns=("title", "raw_title"),
        description_columns=("description", "raw_description"),
        skill_columns=("extracted_skills",),
    ),
    courses=SourceSpec(
        data_file=BASE_DIR / "data" / "2025-2026_moduleInfo_clean.csv",
        embeddings_file=BASE_DIR / "embedding" / "courses_embeddings.jsonl",
        id_column="moduleCode",
        title_columns=("title", "moduleTitle"),
        description_columns=("description", "moduleDescription"),
        skill_columns=(),
    ),
    notes="Broader jobs and broad module embeddings.",
)

DATASET_MODES = {
    ACC_MODE.label: ACC_MODE,
    FULL_MODE.label: FULL_MODE,
}


def clean_text(value: Any) -> str:
    if pd.isna(value):
        return ""
    text = html.unescape(str(value)).strip()
    if not text or text.lower() == "nan":
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def truncate(text: str, limit: int = MAX_SNIPPET_CHARS) -> str:
    text = clean_text(text)
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def tokenize(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9]+", text.lower())


def unique_preserve_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            ordered.append(value)
    return ordered


def parse_skill_value(value: Any) -> str:
    text = clean_text(value)
    if not text or text.lower() == "na":
        return ""
    return text


def build_job_item(row: dict[str, Any]) -> KnowledgeItem:
    job_id = clean_text(row.get("uuid") or row.get("job_id") or row.get("record_id") or row.get("id"))
    title = clean_text(row.get("title") or row.get("raw_title") or row.get("position") or "Untitled job")
    description = clean_text(row.get("description") or row.get("raw_description") or row.get("job_description"))
    skills = parse_skill_value(row.get("extracted_skills"))
    tools = parse_skill_value(row.get("extracted_apps_tools"))
    minimum_experience = clean_text(row.get("minimumYearsExperience"))
    categories = clean_text(row.get("categories"))
    employment = clean_text(row.get("employmentTypes"))
    level = clean_text(row.get("positionLevels"))

    subtitle_parts = [part for part in [job_id, minimum_experience and f"Experience: {minimum_experience}", categories] if part]
    subtitle = " | ".join(subtitle_parts) if subtitle_parts else "Job posting"

    search_parts = [title, description, skills, tools, categories, employment, level]
    search_text = "\n".join(part for part in search_parts if part)

    payload = {
        "job_id": job_id,
        "minimum_experience": minimum_experience,
        "categories": categories,
        "employment": employment,
        "level": level,
        "skills": skills,
        "tools": tools,
    }

    return KnowledgeItem(
        kind="job",
        item_id=job_id or title,
        title=title,
        subtitle=subtitle,
        description=description,
        search_text=search_text,
        payload=payload,
    )


def build_course_item(row: dict[str, Any]) -> KnowledgeItem:
    course_code = clean_text(row.get("moduleCode") or row.get("course_code") or row.get("code"))
    title = clean_text(row.get("title") or row.get("moduleTitle") or "Untitled module")
    description = clean_text(row.get("description") or row.get("moduleDescription"))
    prereq = clean_text(row.get("prereqCourseCodes") or row.get("prerequisites"))

    subtitle_parts = [part for part in [course_code, prereq and f"Prereq: {prereq}"] if part]
    subtitle = " | ".join(subtitle_parts) if subtitle_parts else "Course module"

    search_parts = [course_code, title, description, prereq]
    search_text = "\n".join(part for part in search_parts if part)

    payload = {
        "course_code": course_code,
        "prereq": prereq,
    }

    return KnowledgeItem(
        kind="course",
        item_id=course_code or title,
        title=title,
        subtitle=subtitle,
        description=description,
        search_text=search_text,
        payload=payload,
    )


def load_api_key() -> str:
    return (os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY".lower()) or "").strip()


def build_openai_client() -> OpenAI | None:
    api_key = load_api_key()
    if not api_key:
        return None

    base_url = (
        os.getenv("OPENAI_BASE_URL")
        or os.getenv("OPENAI_API_BASE")
        or os.getenv("OPENAI_BASE_URL".lower())
        or None
    )

    if base_url:
        return OpenAI(api_key=api_key, base_url=base_url)
    return OpenAI(api_key=api_key)


def embed_texts(client: OpenAI, texts: list[str]) -> np.ndarray:
    vectors: list[np.ndarray] = []
    batch_size = 64
    for start in range(0, len(texts), batch_size):
        batch = texts[start : start + batch_size]
        response = client.embeddings.create(model=OPENAI_EMBEDDING_MODEL, input=batch)
        vectors.extend(np.asarray(item.embedding, dtype=np.float32) for item in response.data)

    if not vectors:
        return np.zeros((0, 0), dtype=np.float32)

    matrix = np.vstack(vectors)
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return matrix / norms


def fit_tfidf(corpus: list[str]) -> tuple[TfidfVectorizer, Any]:
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), max_features=20000)
    matrix = vectorizer.fit_transform(corpus)
    return vectorizer, matrix


def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


@st.cache_resource(show_spinner=False)
def load_knowledge_base(
    openai_available: bool,
    jobs_mtime: float,
    courses_mtime: float,
) -> KnowledgeBase:
    _ = jobs_mtime, courses_mtime
    jobs_df = load_csv(JOB_FILE)
    courses_df = load_csv(COURSE_FILE)

    job_items = [
        build_job_item(row)
        for row in jobs_df.to_dict(orient="records")
        if clean_text(row.get("title") or row.get("raw_title") or row.get("description"))
    ]
    course_items = [
        build_course_item(row)
        for row in courses_df.to_dict(orient="records")
        if clean_text(row.get("moduleCode") or row.get("title") or row.get("description"))
    ]

    all_texts = [item.search_text for item in job_items + course_items]
    vectorizer, tfidf_matrix = fit_tfidf(all_texts)
    job_tfidf = tfidf_matrix[: len(job_items)]
    course_tfidf = tfidf_matrix[len(job_items) :]

    status_lines = [
        f"Loaded {len(job_items)} job postings and {len(course_items)} course modules.",
        "Retrieval fallback: TF-IDF",
    ]

    job_embeddings = None
    course_embeddings = None

    if openai_available:
        client = build_openai_client()
        if client is not None:
            try:
                job_embeddings = embed_texts(client, [item.search_text for item in job_items])
                course_embeddings = embed_texts(client, [item.search_text for item in course_items])
                status_lines.append(f"Semantic retrieval: {OPENAI_EMBEDDING_MODEL}")
            except Exception as exc:
                job_embeddings = None
                course_embeddings = None
                status_lines.append(f"OpenAI embeddings unavailable, using TF-IDF fallback ({exc.__class__.__name__}).")
        else:
            status_lines.append("OpenAI API key not detected, using TF-IDF fallback.")
    else:
        status_lines.append("OpenAI API key not detected, using TF-IDF fallback.")

    retrieval_mode = "openai" if job_embeddings is not None and course_embeddings is not None else "tfidf"
    if retrieval_mode == "tfidf" and "OpenAI embeddings unavailable" not in " ".join(status_lines):
        status_lines.append("Semantic retrieval disabled for this session.")

    return KnowledgeBase(
        jobs=job_items,
        courses=course_items,
        job_embeddings=job_embeddings,
        course_embeddings=course_embeddings,
        vectorizer=vectorizer,
        job_tfidf=job_tfidf,
        course_tfidf=course_tfidf,
        retrieval_mode=retrieval_mode,
        status_message=" ".join(status_lines),
    )


def score_boost(query: str, item: KnowledgeItem) -> float:
    query_lower = query.lower()
    title_lower = item.title.lower()
    text_lower = item.search_text.lower()
    boost = 0.0

    if title_lower and title_lower in query_lower:
        boost += 0.22

    query_codes = re.findall(r"[A-Z]{2,}\d{3,4}[A-Z]?", query.upper())
    for code in query_codes:
        if code.lower() in title_lower or code.lower() in text_lower or code.lower() in item.item_id.lower():
            boost += 0.16

    query_tokens = {token for token in tokenize(query) if len(token) > 2}
    item_tokens = set(tokenize(item.search_text))
    overlap = len(query_tokens & item_tokens)
    boost += min(overlap, 8) * 0.015

    return min(boost, 0.4)


def rank_items(
    query: str,
    items: list[KnowledgeItem],
    *,
    embeddings: np.ndarray | None,
    tfidf_matrix: Any,
    vectorizer: TfidfVectorizer | None,
    top_k: int,
) -> list[MatchResult]:
    if not items:
        return []

    lexical_scores = np.zeros(len(items), dtype=np.float32)
    if vectorizer is not None and tfidf_matrix is not None:
        query_vector = vectorizer.transform([query])
        lexical_scores = cosine_similarity(query_vector, tfidf_matrix).ravel().astype(np.float32)

    semantic_scores = np.zeros(len(items), dtype=np.float32)
    if embeddings is not None and embeddings.size:
        client = build_openai_client()
        if client is not None:
            try:
                query_embedding = embed_texts(client, [query])[0]
                semantic_scores = (embeddings @ query_embedding).astype(np.float32)
            except Exception:
                semantic_scores = np.zeros(len(items), dtype=np.float32)

    final_scores = 0.7 * semantic_scores + 0.3 * lexical_scores
    final_scores += np.asarray([score_boost(query, item) for item in items], dtype=np.float32)

    order = np.argsort(final_scores)[::-1][:top_k]
    query_terms = {token for token in tokenize(query) if len(token) > 2}

    results: list[MatchResult] = []
    for index in order:
        item = items[int(index)]
        item_terms = set(tokenize(item.search_text))
        highlights = unique_preserve_order(
            [token for token in tokenize(query) if token in item_terms and len(token) > 2]
        )
        if not highlights:
            highlights = sorted(query_terms & item_terms)[:4]
        results.append(
            MatchResult(
                item=item,
                score=float(final_scores[index]),
                semantic_score=float(semantic_scores[index]),
                lexical_score=float(lexical_scores[index]),
                highlight_terms=highlights[:5],
            )
        )

    return results


def choose_mode(query: str, override: str) -> str:
    if override != "Auto":
        return override

    query_lower = query.lower()
    has_module_code = bool(re.search(r"\b[A-Z]{2,}\d{3,4}[A-Z]?\b", query.upper()))
    course_to_jobs_signals = (
        "what jobs fit",
        "what jobs can",
        "jobs for",
        "jobs related to",
        "job roles related to",
        "what job roles are related to",
        "what job roles fit",
        "job paths from",
        "career from",
        "what can i do with",
        "which jobs match",
        "what jobs are related to",
        "jobs are related to",
        "roles related to",
    )
    job_to_courses_signals = (
        "what modules",
        "which modules",
        "modules for",
        "what courses",
        "which courses",
        "study for",
        "modules help with",
        "courses help with",
        "what should i take",
        "study pathway",
    )

    if any(signal in query_lower for signal in course_to_jobs_signals):
        return "Course to jobs"
    if any(signal in query_lower for signal in job_to_courses_signals):
        return "Job to courses"

    if has_module_code and any(token in query_lower for token in ("job", "role", "career", "posting", "vacancy", "hiring")):
        return "Course to jobs"
    if has_module_code:
        return "Course to jobs"

    if any(token in query_lower for token in ("course", "module", "study", "curriculum", "class")) and "job" not in query_lower:
        return "Course to jobs"
    if any(token in query_lower for token in ("job", "role", "career", "posting", "vacancy", "hiring")) and "course" not in query_lower:
        return "Job to courses"
    return "General"


def format_match_block(matches: list[MatchResult]) -> str:
    if not matches:
        return "No strong matches were found."

    lines = []
    for idx, match in enumerate(matches, start=1):
        item = match.item
        highlights = ", ".join(match.highlight_terms) if match.highlight_terms else "semantic fit"
        description = truncate(item.description, 220)
        lines.append(
            f"{idx}. {item.title} [{item.subtitle}]"
            f"\n   score={match.score:.3f} | semantic={match.semantic_score:.3f} | lexical={match.lexical_score:.3f}"
            f"\n   evidence: {highlights}"
            f"\n   summary: {description}"
        )
    return "\n".join(lines)


def extract_response_text(response: Any) -> str:
    output_text = getattr(response, "output_text", None)
    if output_text:
        return str(output_text).strip()

    parts: list[str] = []
    for item in getattr(response, "output", []):
        if getattr(item, "type", "") != "message":
            continue
        for content in getattr(item, "content", []):
            if getattr(content, "type", "") == "output_text":
                parts.append(str(getattr(content, "text", "")).strip())
    return "\n".join(part for part in parts if part).strip()


SYSTEM_PROMPT = (
    "You are a friendly university career and study advisor for an accounting and business student audience. "
    "You help users connect job postings to relevant university modules and connect modules to likely job paths. "
    "Use only the provided evidence and never invent course codes, job titles, or requirements that are not in the context. "
    "When the evidence is ambiguous, say so clearly and recommend a next step. "
    "Write in a practical, encouraging tone. "
    "Write a very short summary only, in 1 to 3 sentences. "
    "Do not list recommendations as bullets and do not repeat the evidence table; the app will show the ranked recommendations below. "
    "Always include a direct answer and one brief next-step suggestion. "
    "Keep the response concise."
)


def build_chat_prompt(
    *,
    query: str,
    mode: str,
    history: list[dict[str, str]],
    job_matches: list[MatchResult],
    course_matches: list[MatchResult],
) -> str:
    history_lines = []
    for turn in history[-MAX_HISTORY_TURNS:]:
        role = turn["role"].capitalize()
        text = turn["content"].strip()
        if text:
            history_lines.append(f"{role}: {text}")

    history_block = "\n".join(history_lines) if history_lines else "No prior conversation."

    job_block = format_match_block(job_matches)
    course_block = format_match_block(course_matches)

    return (
        f"Mode: {mode}\n\n"
        f"Conversation history:\n{history_block}\n\n"
        f"Current user question:\n{query}\n\n"
        f"Top job matches:\n{job_block}\n\n"
        f"Top course matches:\n{course_block}\n\n"
        "Draft a short natural-language summary. "
        "If the mode is Job to courses, summarize the strongest module fit and why. "
        "If the mode is Course to jobs, summarize the strongest job fit and why. "
        "If the mode is General, summarize both the strongest job and module fit. "
        "Do not use bullet lists."
    )


def generate_answer(client: OpenAI | None, model: str, prompt: str) -> tuple[str, str | None, str | None]:
    if client is None:
        return "", None, "OpenAI client unavailable."

    errors: list[str] = []
    for candidate_model in unique_preserve_order([model, *CHAT_MODEL_FALLBACKS]):
        try:
            response = client.responses.create(
                model=candidate_model,
                instructions=SYSTEM_PROMPT,
                input=prompt,
            )
            text = extract_response_text(response)
            if text.strip():
                return text.strip(), candidate_model, None
            errors.append(f"{candidate_model}: empty response")
        except Exception as exc:
            errors.append(f"{candidate_model}: {exc.__class__.__name__}")

    return "", None, "; ".join(errors) if errors else "Unknown model error."


def first_nonempty(record: dict[str, Any], columns: tuple[str, ...]) -> str:
    for column in columns:
        value = clean_text(record.get(column))
        if value:
            return value
    return ""


def load_source_rows(entity: str, mode: DatasetMode) -> dict[str, dict[str, Any]]:
    spec = mode.jobs if entity == "jobs" else mode.courses if entity == "courses" else None
    if spec is None:
        raise ValueError(f"Unknown entity: {entity}")

    df = pd.read_csv(spec.data_file, dtype=str, keep_default_na=False)
    missing = []
    if spec.id_column not in df.columns:
        missing.append(spec.id_column)
    if not any(column in df.columns for column in spec.title_columns):
        missing.append(f"one of {', '.join(spec.title_columns)}")
    if not any(column in df.columns for column in spec.description_columns):
        missing.append(f"one of {', '.join(spec.description_columns)}")
    if missing:
        raise ValueError(
            f"{entity} data file is missing required column(s): {', '.join(missing)}. "
            f"Available columns: {', '.join(df.columns.astype(str))}"
        )

    rows: dict[str, dict[str, Any]] = {}
    for record in df.to_dict(orient="records"):
        record_id = clean_text(record.get(spec.id_column))
        if not record_id:
            continue
        title = first_nonempty(record, spec.title_columns)
        description = first_nonempty(record, spec.description_columns)
        skills_text = first_nonempty(record, spec.skill_columns) if spec.skill_columns else ""
        rows[record_id] = {
            "record_id": record_id,
            "title": title,
            "description": description,
            "skills": ovr_parse_skill_values(skills_text) if skills_text else [],
        }
    return rows


def load_embedding_rows(entity: str, embeddings_file: Path) -> list[dict[str, Any]]:
    id_key = "job_id" if entity == "jobs" else "course_code" if entity == "courses" else None
    if id_key is None:
        raise ValueError(f"Unknown entity: {entity}")

    rows: list[dict[str, Any]] = []
    with embeddings_file.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            record = json.loads(stripped)
            record_id = clean_text(record.get(id_key) or record.get("record_id"))
            embedding = record.get("embedding")
            split = clean_text(record.get("split"))
            if not split:
                digest = hashlib.sha1(record_id.encode("utf-8")).digest()[0] / 255.0
                if digest < 0.6:
                    split = "train"
                elif digest < 0.8:
                    split = "val"
                else:
                    split = "test"
            if not record_id or not isinstance(embedding, list):
                raise ValueError(
                    f"{entity} embedding record on line {line_number} is missing a valid "
                    f"{id_key}, split, or embedding."
                )
            rows.append(
                {
                    "record_id": record_id,
                    "title": clean_text(record.get("title")),
                    "split": split,
                    "embedding": np.asarray(embedding, dtype=np.float32),
                }
            )
    return rows


def combine_indexed_items(entity: str, mode: DatasetMode) -> list[IndexedItem]:
    source_rows = load_source_rows(entity, mode)
    spec = mode.jobs if entity == "jobs" else mode.courses if entity == "courses" else None
    if spec is None:
        raise ValueError(f"Unknown entity: {entity}")
    embedding_file = spec.embeddings_file
    embedding_rows = load_embedding_rows(entity, embedding_file)
    items: list[IndexedItem] = []
    missing: list[str] = []

    for emb_row in embedding_rows:
        source_row = source_rows.get(emb_row["record_id"])
        if source_row is None:
            missing.append(emb_row["record_id"])
            continue
        items.append(
            IndexedItem(
                source=entity,
                item_id=emb_row["record_id"],
                title=source_row["title"] or emb_row["title"],
                description=source_row["description"],
                skills=source_row["skills"],
                embedding=np.asarray(emb_row["embedding"], dtype=np.float32),
                split=str(emb_row["split"]),
            )
        )

    if missing:
        preview = ", ".join(sorted(set(missing))[:5])
        raise ValueError(f"Some {entity} embedding rows could not be matched to the source CSV. Examples: {preview}")

    return items


def item_to_row(item: IndexedItem) -> dict[str, Any]:
    return {
        "record_id": item.item_id,
        "title": item.title,
        "skills": item.skills,
        "embedding": item.embedding,
    }


def split_indexed_items(items: list[IndexedItem], split_name: str) -> list[IndexedItem]:
    return [item for item in items if item.split == split_name and item.skills]


def fit_local_skill_model(
    items: list[IndexedItem],
    *,
    min_positive_train: int = OVR_MIN_POSITIVE_TRAIN,
) -> OVRRuntime:
    train_items = split_indexed_items(items, "train")
    if not train_items:
        raise ValueError("No train split rows were found for the local OVR model.")

    val_items = split_indexed_items(items, "val")
    if not val_items:
        raise ValueError("No validation split rows were found for the local OVR model.")

    train_rows = [item_to_row(item) for item in train_items]
    val_rows = [item_to_row(item) for item in val_items]
    (
        binarizer,
        y_train,
        y_val,
        _train_counts,
        _val_counts,
        dropped_classes,
        ignored_val_only_skills,
    ) = fit_label_binarizer(
        train_rows,
        val_rows,
        min_positive_train=min_positive_train,
    )

    class_names = list(binarizer.classes_)
    x_train = np.vstack([item.embedding for item in train_items])
    models, _model_summaries = fit_models(
        x_train,
        y_train,
        class_names,
        max_iter=OVR_MAX_ITER,
        random_state=OVR_RANDOM_STATE,
    )

    probabilities = predict_probabilities(models, np.vstack([item.embedding for item in val_items]))
    threshold, threshold_metrics = find_best_global_threshold(probabilities, y_val)

    metrics = {
        **threshold_metrics,
        "global_threshold": float(threshold),
        "train_rows": float(len(train_items)),
        "validation_rows": float(len(val_items)),
        "trained_skills": float(len(class_names)),
        "min_positive_train": float(min_positive_train),
        "dropped_train_only_skills": float(len(dropped_classes)),
        "ignored_validation_only_skills": float(len(ignored_val_only_skills)),
    }

    return OVRRuntime(
        class_names=class_names,
        models=models,
        threshold=float(threshold),
        metrics=metrics,
    )


@st.cache_resource(show_spinner=False)
def load_local_encoder() -> Any:
    return load_embedding_model(
        LOCAL_EMBEDDING_MODEL,
        LOCAL_EMBEDDING_DEVICE,
        LOCAL_EMBEDDING_DTYPE,
    )


@st.cache_resource(show_spinner=False)
def load_runtime_assets(mode_label: str) -> AppRuntime:
    mode = DATASET_MODES[mode_label]
    encoder = load_local_encoder()
    job_items = combine_indexed_items("jobs", mode)
    course_items = combine_indexed_items("courses", mode)
    all_items = job_items + course_items
    min_positive_train = OVR_MIN_POSITIVE_TRAIN
    if len(job_items) > 1000:
        min_positive_train = max(min_positive_train, OVR_MIN_POSITIVE_TRAIN_FULL)

    cache_path = skill_model_cache_path(mode_label, min_positive_train)
    skill_model = load_cached_skill_model(cache_path)
    if skill_model is None:
        skill_model = fit_local_skill_model(all_items, min_positive_train=min_positive_train)
        save_cached_skill_model(cache_path, skill_model)

    status_message = (
        f"Dataset mode: {mode.label}. "
        f"Loaded {len(job_items)} jobs and {len(course_items)} courses. "
        f"Trained {len(skill_model.class_names)} local skill classifiers from "
        f"{skill_model.metrics['train_rows']:.0f} train rows and tuned the threshold on "
        f"{skill_model.metrics['validation_rows']:.0f} validation rows. "
        f"Minimum positives per skill: {int(skill_model.metrics['min_positive_train'])}. "
        f"Embedding model: {LOCAL_EMBEDDING_MODEL}."
    )
    return AppRuntime(
        encoder=encoder,
        skill_model=skill_model,
        items=all_items,
        status_message=status_message,
    )


def encode_texts(encoder: Any, texts: list[str]) -> np.ndarray:
    if not texts:
        return np.zeros((0, 0), dtype=np.float32)

    encode_kwargs = {
        "batch_size": 8,
        "convert_to_numpy": True,
        "normalize_embeddings": True,
        "show_progress_bar": False,
    }

    if hasattr(encoder, "encode_document"):
        vectors = encoder.encode_document(texts, **encode_kwargs)
    else:
        vectors = encoder.encode(texts, **encode_kwargs)

    vectors = np.asarray(vectors, dtype=np.float32)
    if vectors.ndim == 1:
        vectors = vectors[np.newaxis, :]
    return vectors


def predict_query_skills(
    runtime: AppRuntime,
    query_embedding: np.ndarray,
    top_k: int = 10,
) -> tuple[dict[str, float], list[str]]:
    probabilities = predict_probabilities(runtime.skill_model.models, query_embedding[np.newaxis, :])[0]
    skill_scores = {
        skill: float(probability)
        for skill, probability in zip(runtime.skill_model.class_names, probabilities, strict=True)
    }
    ordered = sorted(skill_scores.items(), key=lambda item: item[1], reverse=True)
    predicted = [skill for skill, score in ordered if score >= runtime.skill_model.threshold]
    if not predicted:
        predicted = [skill for skill, _score in ordered[:top_k]]
    return skill_scores, predicted[:top_k]


def score_item(
    item: IndexedItem,
    query_embedding: np.ndarray,
    skill_scores: dict[str, float],
    predicted_skills: list[str],
) -> tuple[float, float, float, float, list[str]]:
    cosine = float(np.dot(query_embedding, item.embedding))
    cosine_score = max(0.0, min(1.0, (cosine + 1.0) / 2.0))

    matched_scores = [skill_scores.get(skill, 0.0) for skill in item.skills if skill in skill_scores]
    matched_predicted = [skill for skill in predicted_skills if skill in item.skills]

    if matched_scores:
        skill_affinity = float(np.mean(matched_scores))
        coverage = len(matched_predicted) / max(len(item.skills), 1)
    else:
        skill_affinity = 0.0
        coverage = 0.0

    overlap_bonus = len(matched_predicted) / max(len(predicted_skills), 1)
    score = (0.52 * cosine_score) + (0.38 * skill_affinity) + (0.10 * overlap_bonus)
    return score, cosine_score, skill_affinity, overlap_bonus, matched_predicted[:5]


def rank_items(
    runtime: AppRuntime,
    query_embedding: np.ndarray,
    skill_scores: dict[str, float],
    predicted_skills: list[str],
    *,
    entity: str | None = None,
    top_k: int = 4,
) -> list[dict[str, Any]]:
    candidates = runtime.items if entity is None else [item for item in runtime.items if item.source == entity]
    scored: list[dict[str, Any]] = []

    for item in candidates:
        score, cosine_score, skill_affinity, overlap_bonus, matched_skills = score_item(
            item,
            query_embedding,
            skill_scores,
            predicted_skills,
        )
        scored.append(
            {
                "item": item,
                "score": score,
                "cosine_score": cosine_score,
                "skill_affinity": skill_affinity,
                "overlap_bonus": overlap_bonus,
                "matched_skills": matched_skills,
            }
        )

    scored.sort(key=lambda record: record["score"], reverse=True)
    return scored[:top_k]


def build_response_context(
    query: str,
    mode: str,
    predicted_skills: list[str],
    primary_matches: list[dict[str, Any]],
    secondary_matches: list[dict[str, Any]],
) -> str:
    def format_matches(matches: list[dict[str, Any]]) -> str:
        if not matches:
            return "No strong matches."
        lines: list[str] = []
        for index, record in enumerate(matches, start=1):
            item: IndexedItem = record["item"]
            matched_skills = ", ".join(record["matched_skills"]) if record["matched_skills"] else "skill overlap"
            description = truncate(item.description, 220)
            lines.append(
                f"{index}. {item.title} [{item.source}]"
                f"\n   score={record['score']:.3f} | cosine={record['cosine_score']:.3f} | skill={record['skill_affinity']:.3f}"
                f"\n   matched skills: {matched_skills}"
                f"\n   summary: {description}"
            )
        return "\n".join(lines)

    skill_line = ", ".join(predicted_skills) if predicted_skills else "none"
    return (
        f"Mode: {mode}\n\n"
        f"User question:\n{query}\n\n"
        f"Predicted skills from local OVR model:\n{skill_line}\n\n"
        f"Primary matches:\n{format_matches(primary_matches)}\n\n"
        f"Secondary matches:\n{format_matches(secondary_matches)}\n\n"
        "Write a concise student-friendly answer. "
        "Use the predicted skills and the ranked matches to explain why the options fit. "
        "If the evidence is weak, say that clearly and suggest a better follow-up query."
    )


def ensure_session_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "selected_prompt" not in st.session_state:
        st.session_state.selected_prompt = ""


def reset_chat() -> None:
    st.session_state.messages = []
    st.session_state.selected_prompt = ""


def render_chat_home() -> None:
    st.markdown(
        """
        <div class="hero hero-center">
            <div class="eyebrow">Study and career assistant</div>
            <h1>Ready when you are.</h1>
            <p>
                Ask about jobs, modules, or study pathways.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_success_criteria()


def render_chat_history_sidebar() -> None:
    user_prompts = [
        message["content"].strip()
        for message in st.session_state.messages
        if message["role"] == "user" and message["content"].strip()
    ]

    st.markdown("### New chat")
    if st.button("Start fresh", use_container_width=True):
        reset_chat()
        st.rerun()

    st.markdown("### History")
    if not user_prompts:
        st.caption("No previous prompts yet.")
        return

    for index, prompt in enumerate(reversed(user_prompts[-8:])):
        label = truncate(prompt, 48)
        if st.button(label, key=f"history_prompt_{index}", use_container_width=True):
            st.session_state.selected_prompt = prompt
            st.rerun()


def keep_strong_matches(matches: list[dict[str, Any]]) -> list[dict[str, Any]]:
    strong_matches = [
        match
        for match in matches
        if match["score"] >= MIN_DISPLAY_MATCH_SCORE or len(match["matched_skills"]) >= MIN_DISPLAY_MATCH_SKILLS
    ]
    return strong_matches or matches[:1]


def render_match_card(match: MatchResult, accent: str) -> None:
    item = match.item
    highlight_text = ", ".join(match.highlight_terms) if match.highlight_terms else "semantic fit"
    score_pct = max(0.0, min(match.score, 1.0)) * 100
    summary = truncate(item.description, 260) or "No description available."

    st.markdown(
        f"""
        <div class="match-card">
            <div class="match-card-top">
                <div>
                    <div class="match-kicker">{accent}</div>
                    <div class="match-title">{item.title}</div>
                </div>
                <div class="score-pill">{score_pct:.0f}%</div>
            </div>
            <div class="match-subtitle">{item.subtitle}</div>
            <div class="match-body">{summary}</div>
            <div class="match-foot">Key overlap: {highlight_text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def style_app() -> None:
    st.markdown(
        """
        <style>
        :root {
            --bg: #f7f3eb;
            --panel: #ffffff;
            --panel-soft: #eef6f0;
            --ink: #1d2a23;
            --muted: #5f6f66;
            --accent: #4f8a74;
            --accent-2: #c9e7d8;
            --accent-3: #f0f7f2;
            --border: rgba(29, 42, 35, 0.10);
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(79, 138, 116, 0.14), transparent 32%),
                radial-gradient(circle at top right, rgba(201, 231, 216, 0.35), transparent 28%),
                linear-gradient(180deg, #fdfbf7 0%, #f6f3eb 100%);
            color: var(--ink);
        }

        .hero {
            background: linear-gradient(135deg, rgba(255,255,255,0.92), rgba(240,247,242,0.95));
            border: 1px solid var(--border);
            border-radius: 28px;
            padding: 1.7rem 1.8rem;
            box-shadow: 0 18px 50px rgba(28, 41, 35, 0.08);
            margin-bottom: 1rem;
        }

        .eyebrow {
            display: inline-block;
            font-size: 0.78rem;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            color: var(--accent);
            font-weight: 700;
            margin-bottom: 0.6rem;
        }

        .hero h1 {
            color: var(--ink);
            margin: 0;
            font-size: 2.4rem;
            line-height: 1.1;
        }

        .hero p {
            color: var(--muted);
            margin-top: 0.8rem;
            margin-bottom: 0;
            max-width: 62rem;
        }

        .hero-center {
            text-align: center;
        }

        .hero-center p {
            margin-left: auto;
            margin-right: auto;
        }

        .metric-wrap {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 0.85rem;
            margin: 1rem 0 1.3rem 0;
        }

        .metric-card, .match-card, .section-card {
            background: rgba(255,255,255,0.96);
            border: 1px solid var(--border);
            border-radius: 22px;
            box-shadow: 0 14px 40px rgba(28, 41, 35, 0.07);
        }

        .metric-card {
            padding: 1rem 1rem 0.95rem 1rem;
        }

        .metric-label {
            color: var(--muted);
            font-size: 0.85rem;
            margin-bottom: 0.35rem;
        }

        .metric-value {
            font-size: 1.55rem;
            font-weight: 800;
            color: var(--ink);
        }

        .metric-note {
            color: var(--muted);
            font-size: 0.82rem;
            margin-top: 0.2rem;
        }

        .section-card {
            padding: 1rem 1rem 1.1rem 1rem;
            margin-bottom: 1rem;
        }

        .match-card {
            padding: 1rem;
            margin-bottom: 0.85rem;
        }

        .match-card-top {
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            align-items: flex-start;
        }

        .match-kicker {
            color: var(--accent);
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 0.15rem;
        }

        .match-title {
            font-size: 1.08rem;
            font-weight: 750;
            color: var(--ink);
        }

        .match-subtitle {
            color: var(--muted);
            font-size: 0.88rem;
            margin-top: 0.45rem;
            margin-bottom: 0.4rem;
        }

        .match-body {
            color: var(--ink);
            font-size: 0.94rem;
            line-height: 1.55;
        }

        .match-foot {
            color: var(--muted);
            font-size: 0.82rem;
            margin-top: 0.45rem;
        }

        .score-pill {
            background: var(--accent-3);
            color: var(--accent);
            font-weight: 800;
            border-radius: 999px;
            padding: 0.3rem 0.7rem;
            white-space: nowrap;
        }

        .status-banner {
            background: rgba(79, 138, 116, 0.08);
            border: 1px solid rgba(79, 138, 116, 0.18);
            color: var(--ink);
            padding: 0.75rem 0.95rem;
            border-radius: 16px;
            margin: 0.75rem 0 1rem 0;
        }

        .stTextInput input, .stTextArea textarea {
            border-radius: 16px !important;
        }

        .stButton button {
            border-radius: 999px;
            border: 1px solid rgba(79, 138, 116, 0.26);
            background: linear-gradient(135deg, #ffffff, #edf7f1);
            color: var(--ink);
        }

        .stButton button:hover {
            border-color: rgba(79, 138, 116, 0.55);
            color: var(--accent);
        }

        .success-list li {
            margin-bottom: 0.35rem;
        }

        @media (max-width: 980px) {
            .metric-wrap {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
            .hero h1 {
                font-size: 2rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_metrics(kb: KnowledgeBase, query_mode: str) -> None:
    metrics = [
        ("Indexed jobs", str(len(kb.jobs)), "Accounting job ads loaded"),
        ("Indexed modules", str(len(kb.courses)), "School modules loaded"),
        ("Retrieval mode", kb.retrieval_mode.upper(), "OpenAI embeddings or TF-IDF"),
        ("Query mode", query_mode, "Auto-detected from your question"),
    ]
    st.markdown("<div class='metric-wrap'>", unsafe_allow_html=True)
    for label, value, note in metrics:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-note">{note}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)


def render_success_criteria() -> None:
    st.markdown(
        """
        <div class="section-card">
            <h3 style="margin-top:0;">How this app maps to the project goal</h3>
            <ul class="success-list">
                <li>Natural-language question answering for jobs, modules, and study pathways.</li>
                <li>Relevant course-to-job and job-to-course mapping with evidence from the data.</li>
                <li>Live reload of the source CSV files when you refresh the app cache.</li>
                <li>Transparent confidence cues through ranked matches and highlighted overlap terms.</li>
                <li>Reduced manual screening work by surfacing the strongest matches first.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_runtime_metrics(runtime: AppRuntime, query_mode: str) -> None:
    job_count = sum(1 for item in runtime.items if item.source == "jobs")
    course_count = sum(1 for item in runtime.items if item.source == "courses")
    metrics = [
        ("Indexed jobs", str(job_count), "Local job embeddings loaded"),
        ("Indexed modules", str(course_count), "Local course embeddings loaded"),
        ("Skill classes", str(len(runtime.skill_model.class_names)), "OVR classifiers trained"),
        ("Threshold", f"{runtime.skill_model.threshold:.3f}", "Validation-tuned global boundary"),
    ]
    st.markdown("<div class='metric-wrap'>", unsafe_allow_html=True)
    for label, value, note in metrics:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-note">{note}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)


def render_indexed_match_card(match: dict[str, Any], accent: str) -> None:
    item: IndexedItem = match["item"]
    highlight_text = ", ".join(match["matched_skills"]) if match["matched_skills"] else "skill overlap"
    score_pct = max(0.0, min(float(match["score"]), 1.0)) * 100
    summary = truncate(item.description, 260) or "No description available."

    st.markdown(
        f"""
        <div class="match-card">
            <div class="match-card-top">
                <div>
                    <div class="match-kicker">{accent}</div>
                    <div class="match-title">{item.title}</div>
                </div>
                <div class="score-pill">{score_pct:.0f}%</div>
            </div>
            <div class="match-subtitle">{item.source} | {item.item_id}</div>
            <div class="match-body">{summary}</div>
            <div class="match-foot">Key overlap: {highlight_text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    st.set_page_config(
        page_title="Campus Career Compass",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    style_app()
    ensure_session_state()

    with st.sidebar:
        st.markdown("## Controls")
        search_mode = st.selectbox("Search mode", ["Auto", "Course to jobs", "Job to courses", "General"], index=0)
        top_k = st.slider("Matches to show", min_value=2, max_value=8, value=4)
        default_model = os.getenv("OPENAI_MODEL", DEFAULT_CHAT_MODEL).strip() or DEFAULT_CHAT_MODEL
        model_options = list(unique_preserve_order([default_model, DEFAULT_CHAT_MODEL, *CHAT_MODEL_FALLBACKS]))
        model_name = st.selectbox("Chat model", model_options, index=0)
        st.caption("OpenAI API key: `OPENAI_API_KEY`")

        if st.button("Refresh data cache"):
            st.cache_data.clear()
            st.cache_resource.clear()
            st.rerun()

        if st.button("Clear chat"):
            reset_chat()
            st.rerun()

        st.markdown(
            """
            <div class="status-banner">
                Tip: ask with a course code, a job title, or a plain-English question like
                "What jobs fit ACC3706?" or "Which modules help with audit roles?"
            </div>
            """,
            unsafe_allow_html=True,
        )

    jobs_stamp = JOB_FILE.stat().st_mtime if JOB_FILE.exists() else 0.0
    courses_stamp = COURSE_FILE.stat().st_mtime if COURSE_FILE.exists() else 0.0
    kb = load_knowledge_base(bool(load_api_key()), jobs_stamp, courses_stamp)
    client = build_openai_client()

    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">Study and career assistant</div>
            <h1>Campus Career Compass</h1>
            <p>
                A light, school-friendly chatbot for exploring accounting jobs, university modules, and
                the connections between them. It ranks the best matches, explains why they fit, and keeps
                the browsing flow simple for students.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_metrics(kb, search_mode)
    render_success_criteria()

    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("### Try a quick prompt")
    prompt_cols = st.columns(4)
    example_prompts = [
        "What jobs fit ACC3706?",
        "Which modules help with audit roles?",
        "Show me courses related to governance and risk",
        "Which job posting is closest to financial reporting work?",
    ]
    for col, example in zip(prompt_cols, example_prompts, strict=False):
        with col:
            if st.button(example):
                st.session_state.selected_prompt = example
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.selected_prompt:
        prompt_to_run = st.session_state.selected_prompt
        st.session_state.selected_prompt = ""
    else:
        prompt_to_run = st.chat_input("Ask about jobs, modules, or study pathways")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt_to_run:
        st.session_state.messages.append({"role": "user", "content": prompt_to_run})
        with st.chat_message("user"):
            st.markdown(prompt_to_run)

        mode = choose_mode(prompt_to_run, search_mode)
        job_matches = rank_items(
            prompt_to_run,
            kb.jobs,
            embeddings=kb.job_embeddings,
            tfidf_matrix=kb.job_tfidf,
            vectorizer=kb.vectorizer,
            top_k=top_k,
        )
        course_matches = rank_items(
            prompt_to_run,
            kb.courses,
            embeddings=kb.course_embeddings,
            tfidf_matrix=kb.course_tfidf,
            vectorizer=kb.vectorizer,
            top_k=top_k,
        )

        if mode == "Course to jobs":
            explanation_context = build_chat_prompt(
                query=prompt_to_run,
                mode=mode,
                history=st.session_state.messages,
                job_matches=job_matches[:MAX_CONTEXT_ITEMS],
                course_matches=course_matches[: min(2, len(course_matches))],
            )
        elif mode == "Job to courses":
            explanation_context = build_chat_prompt(
                query=prompt_to_run,
                mode=mode,
                history=st.session_state.messages,
                job_matches=job_matches[: min(2, len(job_matches))],
                course_matches=course_matches[:MAX_CONTEXT_ITEMS],
            )
        else:
            explanation_context = build_chat_prompt(
                query=prompt_to_run,
                mode=mode,
                history=st.session_state.messages,
                job_matches=job_matches[:MAX_CONTEXT_ITEMS],
                course_matches=course_matches[:MAX_CONTEXT_ITEMS],
            )

        with st.chat_message("assistant"):
            with st.spinner("Searching the dataset and drafting an answer..."):
                answer_text, used_model, error_text = generate_answer(client, model_name, explanation_context)

            if answer_text:
                st.markdown(answer_text)
                if used_model:
                    st.caption(f"Response model: {used_model}")
            else:
                st.caption("Recommendations are shown below.")

        if mode == "Course to jobs":
            primary_matches = job_matches
            primary_label = "Recommended jobs"
            secondary_matches = course_matches
            secondary_label = "Supporting modules"
        elif mode == "Job to courses":
            primary_matches = course_matches
            primary_label = "Recommended modules"
            secondary_matches = job_matches
            secondary_label = "Matching jobs"
        else:
            primary_matches = job_matches
            primary_label = "Job matches"
            secondary_matches = course_matches
            secondary_label = "Course matches"

        left, right = st.columns(2)
        with left:
            st.markdown(f"#### {primary_label}")
            for match in primary_matches[:top_k]:
                render_match_card(match, "Primary match")
        with right:
            st.markdown(f"#### {secondary_label}")
            for match in secondary_matches[:top_k]:
                render_match_card(match, "Supporting match")

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer_text
                if answer_text
                else "I found matches, but the model response was unavailable. Check the ranked evidence cards below.",
            }
        )


def run_app() -> None:
    st.set_page_config(
        page_title="Campus Career Compass",
        page_icon="book",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    style_app()
    ensure_session_state()
    dataset_mode = "ACC"
    search_mode = "Auto"
    top_k = 4
    default_model = os.getenv("OPENAI_MODEL", DEFAULT_CHAT_MODEL).strip() or DEFAULT_CHAT_MODEL
    model_name = default_model

    with st.sidebar:
        render_chat_history_sidebar()

    try:
        runtime = load_runtime_assets(dataset_mode)
    except SystemExit as exc:
        st.error(str(exc))
        st.stop()
    except Exception as exc:
        st.error(
            "The local embedding or OVR pipeline could not start. "
            f"{exc.__class__.__name__}: {exc}"
        )
        st.stop()
    client = build_openai_client()

    _left, center_col, _right = st.columns([1, 3.2, 1])
    with center_col:
        if not any(message["role"] == "user" for message in st.session_state.messages):
            render_chat_home()

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if st.session_state.selected_prompt:
            prompt_to_run = st.session_state.selected_prompt
            st.session_state.selected_prompt = ""
        else:
            prompt_to_run = st.chat_input("Ask about jobs, modules, or study pathways")

        if prompt_to_run:
            st.session_state.messages.append({"role": "user", "content": prompt_to_run})
            with st.chat_message("user"):
                st.markdown(prompt_to_run)

            mode = choose_mode(prompt_to_run, search_mode)
            query_embedding = encode_texts(runtime.encoder, [prompt_to_run])[0]
            skill_scores, predicted_skills = predict_query_skills(runtime, query_embedding, top_k=10)
            job_matches = rank_items(
                runtime,
                query_embedding,
                skill_scores,
                predicted_skills,
                entity="jobs",
                top_k=top_k,
            )
            course_matches = rank_items(
                runtime,
                query_embedding,
                skill_scores,
                predicted_skills,
                entity="courses",
                top_k=top_k,
            )
            job_matches = keep_strong_matches(job_matches)
            course_matches = keep_strong_matches(course_matches)

            if mode == "Course to jobs":
                primary_matches = job_matches
                primary_label = "Recommended jobs"
                secondary_matches = []
                secondary_label = ""
            elif mode == "Job to courses":
                primary_matches = course_matches
                primary_label = "Recommended modules"
                secondary_matches = []
                secondary_label = ""
            else:
                primary_matches = job_matches
                secondary_matches = course_matches
                primary_label = "Job matches"
                secondary_label = "Course matches"

            explanation_context = build_response_context(
                prompt_to_run,
                mode,
                predicted_skills,
                primary_matches[:MAX_CONTEXT_ITEMS],
                secondary_matches[:MAX_CONTEXT_ITEMS],
            )

            with st.chat_message("assistant"):
                with st.spinner("Searching the dataset and drafting an answer..."):
                    answer_text, used_model, error_text = generate_answer(client, model_name, explanation_context)

                if answer_text:
                    st.markdown(answer_text)
                    if used_model:
                        st.caption(f"Response model: {used_model}")
                else:
                    st.caption("Ranked recommendations are shown below.")

            if predicted_skills:
                st.markdown(
                    "**Top predicted skills:** "
                    + ", ".join(predicted_skills[:MAX_CONTEXT_ITEMS])
                )

            if mode == "General":
                left, right = st.columns(2)
                with left:
                    st.markdown(f"#### {primary_label}")
                    for match in primary_matches[:top_k]:
                        render_indexed_match_card(match, "Primary match")
                with right:
                    st.markdown(f"#### {secondary_label}")
                    for match in secondary_matches[:top_k]:
                        render_indexed_match_card(match, "Supporting match")
            else:
                st.markdown(f"#### {primary_label}")
                for match in primary_matches[:top_k]:
                    render_indexed_match_card(match, "Primary match")

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer_text
                    if answer_text
                    else "I found matches, but the model response was unavailable. Check the ranked evidence cards below.",
                }
            )


if __name__ == "__main__":
    run_app()
