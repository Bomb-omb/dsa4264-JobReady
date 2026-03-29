from __future__ import annotations

import argparse
import json
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


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build local embeddings for jobs, skills, and courses with metadata tags. "
            "Outputs are written as JSONL files for easy ingestion into a vector store."
        )
    )
    parser.add_argument("--jobs-file")
    parser.add_argument("--courses-file", default=str(DEFAULT_COURSE_FILE))
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

    return SentenceTransformer(
        model_name,
        trust_remote_code=True,
        device=device_name,
        model_kwargs={"torch_dtype": dtype_map[dtype_name]},
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
    jobs_count: int,
    skills_count: int,
    courses_count: int,
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
        },
        "outputs": {
            "jobs": str(output_dir / "jobs_embeddings.jsonl"),
            "skills": str(output_dir / "skills_embeddings.jsonl"),
            "courses": str(output_dir / "courses_embeddings.jsonl"),
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
        print(f"  {entity_type}: {output_path}")
    print("Counts:")
    for entity_type, count in manifest["counts"].items():
        print(f"  {entity_type}: {count}")
    print(f"Embedding dimension: {manifest['embedding_dimension']}")
    print(f"Device: {manifest['device']}")
    print(f"Torch dtype: {manifest['torch_dtype']}")


def main() -> None:
    args = parse_args()

    jobs_file = resolve_jobs_file(args.jobs_file)
    courses_file = Path(args.courses_file)
    output_dir = Path(args.output_dir)

    ensure_file_exists(jobs_file, "jobs file")
    ensure_file_exists(courses_file, "courses file")

    jobs_df = pd.read_csv(jobs_file)
    courses_df = pd.read_csv(courses_file)

    job_records = [] if args.skip_jobs else build_job_records(jobs_df)
    skill_records = [] if args.skip_skills else build_skill_records(jobs_df, courses_df)
    course_records = [] if args.skip_courses else build_course_records(courses_df)

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

    manifest = build_manifest(
        model_name=args.model_name,
        device_name=device_name,
        dtype_name=dtype_name,
        normalize_embeddings=args.normalize,
        output_dir=output_dir,
        jobs_file=jobs_file,
        courses_file=courses_file,
        jobs_count=len(embedded_jobs),
        skills_count=len(embedded_skills),
        courses_count=len(embedded_courses),
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
