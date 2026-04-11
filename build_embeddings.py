from __future__ import annotations

import argparse
import json
import math
import os
import random
import re
from collections import OrderedDict
from pathlib import Path
from typing import Any

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_JOB_FILE_CANDIDATES = (
    BASE_DIR / "data" / "mcf_entrylevel.csv",
)
DEFAULT_COURSE_FILE = BASE_DIR / "data" / "2025-2026_module_clean_with_prereq.csv"
DEFAULT_OUTPUT_DIR = BASE_DIR / "embedding"
DEFAULT_MODEL_NAME = "zeroentropy/zembed-1"
DEFAULT_BATCH_SIZE = 8
JOB_DESCRIPTION_COLUMN = "description"
COURSE_DESCRIPTION_COLUMN = "description"
JOB_ID_COLUMN = "uuid"
COURSE_ID_COLUMN = "moduleCode"
SKILL_SOURCE_COLUMNS = (
    "skills",
    "extracted_skills",
    "extracted_apps_tools",
)
DEFAULT_SPLIT_RATIOS = (0.6, 0.2, 0.2)
DEFAULT_SPLIT_LABELS = ("train", "val", "test")
SKILL_FILE_COLUMN_CANDIDATES = (
    ("parent_skill_title", "parent_skill_description"),
    ("skill_name", "skill_description"),
    ("title", "description"),
    ("name", "description"),
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build local embeddings for jobs, skills, and courses with metadata tags. "
            "Outputs are written as JSONL files for easy ingestion into a vector store."
        )
    )
    parser.add_argument("--jobs-file")
    parser.add_argument("--courses-file", default=str(DEFAULT_COURSE_FILE))
    parser.add_argument("--skills-file")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--model-name", default=DEFAULT_MODEL_NAME)
    parser.add_argument("--device", default="auto")
    parser.add_argument(
        "--torch-dtype",
        choices=("auto", "bfloat16", "float16", "float32"),
        default="auto",
    )
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument(
        "--course-code-prefix",
        help="Only keep course rows whose course code starts with this prefix.",
    )
    parser.add_argument(
        "--split-ratios",
        default="0.6,0.2,0.2",
        help="Comma-separated ratios for train,val,test splits on jobs and courses.",
    )
    parser.add_argument(
        "--split-seed",
        type=int,
        default=42,
        help="Random seed used for deterministic train,val,test assignment.",
    )
    parser.add_argument(
        "--normalize",
        dest="normalize",
        action="store_true",
        default=True,
        help="L2-normalize embeddings before writing them out. Enabled by default.",
    )
    parser.add_argument(
        "--no-normalize",
        dest="normalize",
        action="store_false",
        help="Disable L2-normalization before writing embeddings.",
    )
    parser.add_argument(
        "--skip-jobs",
        action="store_true",
        help="Skip job description embeddings.",
    )
    parser.add_argument(
        "--skip-skills",
        action="store_true",
        help="Skip skill name embeddings.",
    )
    parser.add_argument(
        "--skip-courses",
        action="store_true",
        help="Skip course description embeddings.",
    )
    return parser.parse_args(argv)


def resolve_jobs_file(explicit_path: str | None) -> Path:
    if explicit_path:
        return Path(explicit_path)

    for candidate in DEFAULT_JOB_FILE_CANDIDATES:
        if candidate.exists():
            return candidate

    raise FileNotFoundError(
        "No default jobs file found. Checked: "
        + ", ".join(str(path) for path in DEFAULT_JOB_FILE_CANDIDATES)
    )


def resolve_local_model_path(model_name: str) -> str:
    candidate_path = Path(model_name)
    if candidate_path.exists():
        return str(candidate_path)

    hf_home = Path(os.getenv("HF_HOME", str(Path.home() / ".cache" / "huggingface")))
    cache_root = hf_home / "hub"
    repo_dir = cache_root / f"models--{model_name.replace('/', '--')}"
    if not repo_dir.exists():
        return model_name

    refs_main = repo_dir / "refs" / "main"
    if refs_main.exists():
        revision = refs_main.read_text(encoding="utf-8").strip()
        snapshot_dir = repo_dir / "snapshots" / revision
        if snapshot_dir.exists():
            return str(snapshot_dir)

    snapshots_dir = repo_dir / "snapshots"
    if snapshots_dir.exists():
        snapshots = sorted(path for path in snapshots_dir.iterdir() if path.is_dir())
        if snapshots:
            return str(snapshots[0])

    return model_name


def ensure_file_exists(path: Path, label: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"{label} not found: {path}")


def ensure_columns(df: pd.DataFrame, required_columns: tuple[str, ...], label: str) -> None:
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        raise ValueError(
            f"{label} is missing required column(s): {', '.join(missing)}. "
            f"Available columns: {', '.join(df.columns.astype(str))}"
        )


def normalize_text(value: Any) -> str:
    if pd.isna(value):
        return ""
    text = str(value).strip()
    if not text or text.lower() == "nan":
        return ""
    return re.sub(r"\s+", " ", text)


def normalize_skill_name(value: Any) -> str:
    return normalize_text(value)


def slugify(value: str) -> str:
    lowered = value.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered)
    return slug.strip("-") or "unknown"


def parse_json_list(text: str) -> list[str]:
    try:
        raw = json.loads(text)
    except json.JSONDecodeError:
        return []

    if not isinstance(raw, list):
        return []

    values: list[str] = []
    for item in raw:
        cleaned = normalize_skill_name(item)
        if cleaned:
            values.append(cleaned)
    return values


def parse_pipe_list(text: str) -> list[str]:
    values = []
    for item in text.split("|"):
        cleaned = normalize_skill_name(item)
        if cleaned:
            values.append(cleaned)
    return values


def parse_skill_values(value: Any) -> list[str]:
    text = normalize_text(value)
    if not text:
        return []
    if text.startswith("["):
        return parse_json_list(text)
    if "|" in text:
        return parse_pipe_list(text)
    return [text]


def deduplicate_preserve_order(values: list[str]) -> list[str]:
    return list(OrderedDict.fromkeys(values))


def parse_split_ratios(text: str) -> tuple[float, float, float]:
    parts = [part.strip() for part in text.split(",")]
    if len(parts) != len(DEFAULT_SPLIT_LABELS):
        raise ValueError(
            "--split-ratios must contain exactly three comma-separated values "
            "for train,val,test."
        )

    try:
        ratios = tuple(float(part) for part in parts)
    except ValueError as exc:
        raise ValueError("--split-ratios must contain numeric values.") from exc

    if any(ratio < 0 for ratio in ratios):
        raise ValueError("--split-ratios cannot contain negative values.")

    total = sum(ratios)
    if not math.isclose(total, 1.0, rel_tol=0.0, abs_tol=1e-9):
        raise ValueError("--split-ratios must sum to 1.0.")

    return ratios  # type: ignore[return-value]


def compute_split_counts(total: int, ratios: tuple[float, float, float]) -> list[int]:
    exact_counts = [total * ratio for ratio in ratios]
    counts = [math.floor(value) for value in exact_counts]
    remaining = total - sum(counts)

    fractional_parts = sorted(
        (
            (exact - math.floor(exact), index)
            for index, exact in enumerate(exact_counts)
        ),
        reverse=True,
    )

    for _, index in fractional_parts[:remaining]:
        counts[index] += 1

    return counts


def assign_splits(
    records: list[dict[str, Any]],
    *,
    seed: int,
    ratios: tuple[float, float, float],
) -> list[dict[str, Any]]:
    if not records:
        return records

    shuffled = [dict(record) for record in sorted(records, key=lambda record: record["record_id"])]
    rng = random.Random(seed)
    rng.shuffle(shuffled)

    split_counts = compute_split_counts(len(shuffled), ratios)

    offset = 0
    for split_label, count in zip(DEFAULT_SPLIT_LABELS, split_counts, strict=True):
        for index, record in enumerate(shuffled[offset : offset + count], start=offset):
            shuffled[index] = {"split": split_label, **record}
        offset += count

    return shuffled


def count_records_by_split(records: list[dict[str, Any]]) -> dict[str, int]:
    counts = {label: 0 for label in DEFAULT_SPLIT_LABELS}
    for record in records:
        split_name = record.get("split")
        if split_name in counts:
            counts[split_name] += 1
    return counts


def filter_courses_by_prefix(df: pd.DataFrame, prefix: str | None) -> pd.DataFrame:
    if not prefix:
        return df

    ensure_columns(df, (COURSE_ID_COLUMN,), "courses file")
    mask = df[COURSE_ID_COLUMN].astype(str).str.startswith(prefix, na=False)
    return df.loc[mask].copy()


def resolve_skill_file_columns(df: pd.DataFrame) -> tuple[str, str]:
    for title_column, description_column in SKILL_FILE_COLUMN_CANDIDATES:
        if title_column in df.columns and description_column in df.columns:
            return title_column, description_column

    raise ValueError(
        "skills file is missing a supported title/description column pair. "
        "Expected one of: "
        + "; ".join(
            f"{title_column}+{description_column}"
            for title_column, description_column in SKILL_FILE_COLUMN_CANDIDATES
        )
    )


def build_job_records(df: pd.DataFrame) -> list[dict[str, Any]]:
    ensure_columns(df, (JOB_ID_COLUMN, JOB_DESCRIPTION_COLUMN), "jobs file")
    records: list[dict[str, Any]] = []

    for row in df.itertuples(index=False):
        job_id = normalize_text(getattr(row, JOB_ID_COLUMN))
        description = normalize_text(getattr(row, JOB_DESCRIPTION_COLUMN))
        if not job_id or not description:
            continue

        title = normalize_text(getattr(row, "title", ""))
        records.append(
            {
                "record_id": f"job:{job_id}",
                "entity_type": "job",
                "job_id": job_id,
                "title": title,
                "text": description,
            }
        )

    return records


def build_course_records(df: pd.DataFrame) -> list[dict[str, Any]]:
    ensure_columns(df, (COURSE_ID_COLUMN, COURSE_DESCRIPTION_COLUMN), "courses file")
    records: list[dict[str, Any]] = []

    for row in df.itertuples(index=False):
        course_code = normalize_text(getattr(row, COURSE_ID_COLUMN))
        description = normalize_text(getattr(row, COURSE_DESCRIPTION_COLUMN))
        if not course_code or not description:
            continue

        title = normalize_text(getattr(row, "title", ""))
        records.append(
            {
                "record_id": f"course:{course_code}",
                "entity_type": "course",
                "course_code": course_code,
                "title": title,
                "text": description,
            }
        )

    return records


def collect_skills_from_dataframe(df: pd.DataFrame, source_name: str) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []

    for row in df.itertuples(index=False):
        for column_name in SKILL_SOURCE_COLUMNS:
            if not hasattr(row, column_name):
                continue

            for skill_name in parse_skill_values(getattr(row, column_name)):
                records.append(
                    {
                        "skill_name": skill_name,
                        "source": f"{source_name}.{column_name}",
                    }
                )

    return records


def build_skill_records(job_df: pd.DataFrame, course_df: pd.DataFrame) -> list[dict[str, Any]]:
    raw_skill_records = [
        *collect_skills_from_dataframe(job_df, "jobs"),
        *collect_skills_from_dataframe(course_df, "courses"),
    ]

    grouped: OrderedDict[str, dict[str, Any]] = OrderedDict()
    for record in raw_skill_records:
        key = record["skill_name"].casefold()
        if key not in grouped:
            grouped[key] = {
                "record_id": f"skill:{slugify(record['skill_name'])}",
                "entity_type": "skill",
                "skill_name": record["skill_name"],
                "text": record["skill_name"],
                "sources": [],
            }
        grouped[key]["sources"].append(record["source"])

    for record in grouped.values():
        record["sources"] = deduplicate_preserve_order(record["sources"])

    return list(grouped.values())


def build_skill_records_from_file(df: pd.DataFrame) -> list[dict[str, Any]]:
    title_column, description_column = resolve_skill_file_columns(df)
    records: list[dict[str, Any]] = []

    for row in df.itertuples(index=False):
        skill_name = normalize_skill_name(getattr(row, title_column))
        description = normalize_text(getattr(row, description_column))
        if not skill_name or not description:
            continue

        records.append(
            {
                "record_id": f"skill:{slugify(skill_name)}",
                "entity_type": "skill",
                "skill_name": skill_name,
                "text": description,
                "description": description,
                "source": "skills_file",
            }
        )

    return records


def select_device_and_dtype(device_name: str, dtype_name: str) -> tuple[str, str]:
    try:
        import torch
    except ModuleNotFoundError as exc:
        raise SystemExit(
            "Missing required package: torch. Install a CUDA-enabled PyTorch build first."
        ) from exc

    if device_name == "auto":
        device_name = "cuda" if torch.cuda.is_available() else "cpu"

    if dtype_name != "auto":
        return device_name, dtype_name

    if device_name != "cuda":
        return device_name, "float32"

    if hasattr(torch.cuda, "is_bf16_supported") and torch.cuda.is_bf16_supported():
        return device_name, "bfloat16"
    return device_name, "float16"


def load_embedding_model(model_name: str, device_name: str, dtype_name: str) -> Any:
    try:
        from sentence_transformers import SentenceTransformer
    except ModuleNotFoundError as exc:
        raise SystemExit(
            "Missing required package: sentence-transformers. "
            "Install it with: python -m pip install sentence-transformers accelerate"
        ) from exc

    try:
        import torch
    except ModuleNotFoundError as exc:
        raise SystemExit(
            "Missing required package: torch. Install a CUDA-enabled PyTorch build first."
        ) from exc

    dtype_map = {
        "bfloat16": torch.bfloat16,
        "float16": torch.float16,
        "float32": torch.float32,
    }
    local_files_only = os.getenv("LOCAL_EMBEDDING_LOCAL_FILES_ONLY", "1").strip().lower() not in (
        "0",
        "false",
        "no",
    )
    resolved_model_name = resolve_local_model_path(model_name)
    if local_files_only and resolved_model_name == model_name:
        raise SystemExit(
            f"Local embedding model '{model_name}' was not found in the Hugging Face cache. "
            "Set LOCAL_EMBEDDING_MODEL to a local snapshot path or run the embedding build once "
            "while the model is available."
        )

    return SentenceTransformer(
        resolved_model_name,
        trust_remote_code=True,
        device=device_name,
        local_files_only=local_files_only,
        model_kwargs={"torch_dtype": dtype_map[dtype_name]},
        tokenizer_kwargs={"local_files_only": local_files_only},
        config_kwargs={"local_files_only": local_files_only},
    )


def embed_records(
    records: list[dict[str, Any]],
    model: Any,
    batch_size: int,
    normalize_embeddings: bool,
) -> list[dict[str, Any]]:
    if not records:
        return []

    texts = [record["text"] for record in records]
    vectors = model.encode_document(
        texts,
        batch_size=batch_size,
        convert_to_numpy=True,
        normalize_embeddings=normalize_embeddings,
        show_progress_bar=True,
    )

    output_records: list[dict[str, Any]] = []
    for record, vector in zip(records, vectors, strict=True):
        enriched = dict(record)
        enriched["embedding"] = vector.tolist()
        output_records.append(enriched)
    return output_records


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def build_split_output_paths(output_dir: Path, entity_type: str) -> dict[str, str]:
    return {
        split_label: str(output_dir / "splits" / f"{entity_type}_{split_label}_embeddings.jsonl")
        for split_label in DEFAULT_SPLIT_LABELS
    }


def write_split_jsonl_files(
    output_dir: Path,
    *,
    jobs_records: list[dict[str, Any]],
    courses_records: list[dict[str, Any]],
) -> None:
    for entity_type, records in (("jobs", jobs_records), ("courses", courses_records)):
        for split_label in DEFAULT_SPLIT_LABELS:
            split_records = [
                record for record in records if record.get("split") == split_label
            ]
            write_jsonl(
                output_dir / "splits" / f"{entity_type}_{split_label}_embeddings.jsonl",
                split_records,
            )


def infer_embedding_dimension(records: list[dict[str, Any]]) -> int:
    if not records:
        return 0
    return len(records[0].get("embedding", []))


def build_manifest(
    *,
    model_name: str,
    device_name: str,
    dtype_name: str,
    normalize_embeddings: bool,
    output_dir: Path,
    jobs_file: Path,
    courses_file: Path,
    skills_file: Path | None,
    course_code_prefix: str | None,
    split_ratios: tuple[float, float, float],
    split_seed: int,
    jobs_count: int,
    skills_count: int,
    courses_count: int,
    jobs_split_counts: dict[str, int],
    courses_split_counts: dict[str, int],
    embedding_dimension: int,
) -> dict[str, Any]:
    return {
        "model_name": model_name,
        "device": device_name,
        "torch_dtype": dtype_name,
        "normalize_embeddings": normalize_embeddings,
        "embedding_dimension": embedding_dimension,
        "inputs": {
            "jobs_file": str(jobs_file),
            "courses_file": str(courses_file),
            "skills_file": str(skills_file) if skills_file else None,
        },
        "filters": {
            "course_code_prefix": course_code_prefix,
        },
        "splits": {
            "labels": list(DEFAULT_SPLIT_LABELS),
            "ratios": list(split_ratios),
            "seed": split_seed,
            "jobs": jobs_split_counts,
            "courses": courses_split_counts,
        },
        "outputs": {
            "jobs": str(output_dir / "jobs_embeddings.jsonl"),
            "skills": str(output_dir / "skills_embeddings.jsonl"),
            "courses": str(output_dir / "courses_embeddings.jsonl"),
            "jobs_splits": build_split_output_paths(output_dir, "jobs"),
            "courses_splits": build_split_output_paths(output_dir, "courses"),
        },
        "counts": {
            "jobs": jobs_count,
            "skills": skills_count,
            "courses": courses_count,
        },
    }


def print_summary(manifest: dict[str, Any]) -> None:
    print("Saved embeddings:")
    for entity_type, output_path in manifest["outputs"].items():
        if isinstance(output_path, dict):
            continue
        print(f"  {entity_type}: {output_path}")
    print("Counts:")
    for entity_type, count in manifest["counts"].items():
        print(f"  {entity_type}: {count}")
    print("Splits:")
    for entity_type in ("jobs", "courses"):
        split_counts = manifest["splits"][entity_type]
        rendered = ", ".join(f"{split}={count}" for split, count in split_counts.items())
        print(f"  {entity_type}: {rendered}")
    print(f"Embedding dimension: {manifest['embedding_dimension']}")
    print(f"Device: {manifest['device']}")
    print(f"Torch dtype: {manifest['torch_dtype']}")


def main() -> None:
    args = parse_args()

    jobs_file = resolve_jobs_file(args.jobs_file)
    courses_file = Path(args.courses_file)
    skills_file = Path(args.skills_file) if args.skills_file else None
    output_dir = Path(args.output_dir)
    split_ratios = parse_split_ratios(args.split_ratios)

    ensure_file_exists(jobs_file, "jobs file")
    ensure_file_exists(courses_file, "courses file")
    if skills_file:
        ensure_file_exists(skills_file, "skills file")

    jobs_df = pd.read_csv(jobs_file)
    courses_df = filter_courses_by_prefix(pd.read_csv(courses_file), args.course_code_prefix)
    skills_df = pd.read_csv(skills_file) if skills_file else None

    job_records = [] if args.skip_jobs else assign_splits(
        build_job_records(jobs_df),
        seed=args.split_seed,
        ratios=split_ratios,
    )
    if args.skip_skills:
        skill_records = []
    elif skills_df is not None:
        skill_records = build_skill_records_from_file(skills_df)
    else:
        skill_records = build_skill_records(jobs_df, courses_df)
    course_records = [] if args.skip_courses else assign_splits(
        build_course_records(courses_df),
        seed=args.split_seed,
        ratios=split_ratios,
    )

    if not any((job_records, skill_records, course_records)):
        raise SystemExit("Nothing to embed. Enable at least one entity type.")

    device_name, dtype_name = select_device_and_dtype(args.device, args.torch_dtype)
    print(f"Loading model {args.model_name} on {device_name} with {dtype_name}...")
    model = load_embedding_model(args.model_name, device_name, dtype_name)

    embedded_jobs = embed_records(
        job_records,
        model=model,
        batch_size=args.batch_size,
        normalize_embeddings=args.normalize,
    )
    embedded_skills = embed_records(
        skill_records,
        model=model,
        batch_size=args.batch_size,
        normalize_embeddings=args.normalize,
    )
    embedded_courses = embed_records(
        course_records,
        model=model,
        batch_size=args.batch_size,
        normalize_embeddings=args.normalize,
    )

    write_jsonl(output_dir / "jobs_embeddings.jsonl", embedded_jobs)
    write_jsonl(output_dir / "skills_embeddings.jsonl", embedded_skills)
    write_jsonl(output_dir / "courses_embeddings.jsonl", embedded_courses)
    write_split_jsonl_files(
        output_dir,
        jobs_records=embedded_jobs,
        courses_records=embedded_courses,
    )

    manifest = build_manifest(
        model_name=args.model_name,
        device_name=device_name,
        dtype_name=dtype_name,
        normalize_embeddings=args.normalize,
        output_dir=output_dir,
        jobs_file=jobs_file,
        courses_file=courses_file,
        skills_file=skills_file,
        course_code_prefix=args.course_code_prefix,
        split_ratios=split_ratios,
        split_seed=args.split_seed,
        jobs_count=len(embedded_jobs),
        skills_count=len(embedded_skills),
        courses_count=len(embedded_courses),
        jobs_split_counts=count_records_by_split(embedded_jobs),
        courses_split_counts=count_records_by_split(embedded_courses),
        embedding_dimension=infer_embedding_dimension(
            embedded_jobs or embedded_skills or embedded_courses
        ),
    )
    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print_summary(manifest)
    print(f"Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
