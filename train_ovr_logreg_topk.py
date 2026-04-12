from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_fscore_support
from sklearn.preprocessing import MultiLabelBinarizer


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = BASE_DIR / "embedding" / "acc" / "logreg_topk_val"
EPS = 1e-12

ENTITY_CONFIGS: dict[str, dict[str, Any]] = {
    "jobs": {
        "label": "jobs",
        "default_data_file": BASE_DIR / "data" / "acc" / "audit_tax_accounting_jobs.csv",
        "default_embeddings_candidates": (
            BASE_DIR / "embedding" / "acc" / "acc_jobs_embeddings.jsonl",
            BASE_DIR / "embedding" / "acc" / "jobs_embeddings.jsonl",
        ),
        "default_skills_embeddings_candidates": (
            BASE_DIR / "embedding" / "acc" / "acc_skills_embeddings.jsonl",
            BASE_DIR / "embedding" / "acc" / "skills_embeddings.jsonl",
        ),
        "data_id_column": "uuid",
        "title_column": "title",
        "skills_column": "extracted_skills",
        "embedding_id_key": "job_id",
    },
    "courses": {
        "label": "courses",
        "default_data_file": BASE_DIR / "data" / "2025-2026_module_clean_with_prereq_skillsfuture.csv",
        "default_embeddings_candidates": (
            BASE_DIR / "embedding" / "acc" / "acc_courses_embeddings.jsonl",
            BASE_DIR / "embedding" / "acc" / "courses_embeddings.jsonl",
        ),
        "default_skills_embeddings_candidates": (
            BASE_DIR / "embedding" / "acc" / "acc_skills_embeddings.jsonl",
            BASE_DIR / "embedding" / "acc" / "skills_embeddings.jsonl",
        ),
        "data_id_column": "moduleCode",
        "title_column": "title",
        "skills_column": "extracted_skills",
        "embedding_id_key": "course_code",
    },
}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Train one-vs-rest logistic regression models, select a global top-k on the "
            "validation split, and evaluate final multilabel predictions on the test split."
        )
    )
    parser.add_argument(
        "--entity",
        choices=("jobs", "courses", "both"),
        default="both",
        help="Which dataset to evaluate. Defaults to both jobs and ACC courses.",
    )
    parser.add_argument("--jobs-file", default=str(ENTITY_CONFIGS["jobs"]["default_data_file"]))
    parser.add_argument("--jobs-embeddings-file")
    parser.add_argument("--courses-file", default=str(ENTITY_CONFIGS["courses"]["default_data_file"]))
    parser.add_argument("--courses-embeddings-file")
    parser.add_argument("--skills-embeddings-file")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--train-split", default="train")
    parser.add_argument("--val-split", default="val")
    parser.add_argument("--test-split", default="test")
    parser.add_argument(
        "--top-k",
        type=int,
        default=None,
        help="Use this fixed top-k instead of selecting k on the validation split.",
    )
    parser.add_argument(
        "--top-k-candidates",
        default="1,2,3,4,5,6,7,8,9,10",
        help="Comma-separated candidate k values for validation-based selection.",
    )
    parser.add_argument(
        "--min-positive-train",
        type=int,
        default=2,
        help="Minimum number of positive training examples required to fit a skill classifier.",
    )
    parser.add_argument("--max-iter", type=int, default=1000)
    parser.add_argument("--random-state", type=int, default=42)
    return parser.parse_args(argv)


def ensure_file_exists(path: Path, label: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"{label} not found: {path}")


def resolve_embeddings_file(explicit_path: str | None, entity_name: str) -> Path:
    if explicit_path:
        path = Path(explicit_path)
        ensure_file_exists(path, f"{entity_name} embeddings file")
        return path

    for candidate in ENTITY_CONFIGS[entity_name]["default_embeddings_candidates"]:
        if candidate.exists():
            return candidate

    checked = ", ".join(
        str(path) for path in ENTITY_CONFIGS[entity_name]["default_embeddings_candidates"]
    )
    raise FileNotFoundError(f"No default {entity_name} embeddings file found. Checked: {checked}")


def resolve_skill_embeddings_file(explicit_path: str | None) -> Path:
    if explicit_path:
        path = Path(explicit_path)
        ensure_file_exists(path, "skills embeddings file")
        return path

    for candidate in ENTITY_CONFIGS["jobs"]["default_skills_embeddings_candidates"]:
        if candidate.exists():
            return candidate

    checked = ", ".join(
        str(path) for path in ENTITY_CONFIGS["jobs"]["default_skills_embeddings_candidates"]
    )
    raise FileNotFoundError(f"No default skills embeddings file found. Checked: {checked}")


def normalize_text(value: Any) -> str:
    if pd.isna(value):
        return ""
    text = str(value).strip()
    if not text or text.lower() == "nan":
        return ""
    return text


def parse_skill_values(value: Any) -> list[str]:
    text = normalize_text(value)
    if not text:
        return []

    if text.startswith("["):
        try:
            raw = json.loads(text)
        except json.JSONDecodeError:
            raw = []
        if isinstance(raw, list):
            return [normalize_text(item) for item in raw if normalize_text(item)]

    if "|" in text:
        return [part for part in (normalize_text(item) for item in text.split("|")) if part]

    return [text]


def load_skill_names(skills_embeddings_file: Path) -> list[str]:
    skill_names: list[str] = []
    with skills_embeddings_file.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            record = json.loads(stripped)
            skill_name = normalize_text(record.get("skill_name"))
            if not skill_name:
                raise ValueError(
                    f"Skill embeddings record on line {line_number} is missing a valid skill_name."
                )
            skill_names.append(skill_name)
    if not skill_names:
        raise ValueError(f"No skill names found in {skills_embeddings_file}.")
    return skill_names


def parse_top_k_candidates(text: str) -> list[int]:
    candidates: list[int] = []
    for part in text.split(","):
        value = part.strip()
        if not value:
            continue
        parsed = int(value)
        if parsed <= 0:
            raise ValueError("--top-k-candidates values must be positive integers.")
        candidates.append(parsed)
    if not candidates:
        raise ValueError("--top-k-candidates must include at least one positive integer.")
    return sorted(set(candidates))


def load_entity_rows(entity_name: str, data_file: Path) -> dict[str, dict[str, Any]]:
    config = ENTITY_CONFIGS[entity_name]
    df = pd.read_csv(data_file)
    required_columns = (
        config["data_id_column"],
        config["title_column"],
        config["skills_column"],
    )
    missing_columns = [column for column in required_columns if column not in df.columns]
    if missing_columns:
        raise ValueError(
            f"{entity_name} file is missing required column(s): {', '.join(missing_columns)}. "
            f"Available columns: {', '.join(df.columns.astype(str))}"
        )

    rows: dict[str, dict[str, Any]] = {}
    for row in df.itertuples(index=False):
        record_id = normalize_text(getattr(row, config["data_id_column"]))
        if not record_id:
            continue
        rows[record_id] = {
            "record_id": record_id,
            "title": normalize_text(getattr(row, config["title_column"])),
            "skills": parse_skill_values(getattr(row, config["skills_column"])),
        }
    return rows


def load_embedding_rows(entity_name: str, embeddings_file: Path) -> list[dict[str, Any]]:
    config = ENTITY_CONFIGS[entity_name]
    rows: list[dict[str, Any]] = []
    with embeddings_file.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            record = json.loads(stripped)
            record_id = normalize_text(record.get(config["embedding_id_key"]))
            split = normalize_text(record.get("split"))
            embedding = record.get("embedding")
            if not record_id or not split or not isinstance(embedding, list):
                raise ValueError(
                    f"{entity_name} embedding record on line {line_number} is missing a valid "
                    f"{config['embedding_id_key']}, split, or embedding."
                )
            rows.append(
                {
                    "record_id": record_id,
                    "title": normalize_text(record.get("title")),
                    "split": split,
                    "embedding": np.asarray(embedding, dtype=np.float32),
                }
            )
    return rows


def combine_rows(
    entity_name: str,
    embedding_rows: list[dict[str, Any]],
    entity_rows: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    combined: list[dict[str, Any]] = []
    missing_ids: list[str] = []

    for record in embedding_rows:
        entity_row = entity_rows.get(record["record_id"])
        if entity_row is None:
            missing_ids.append(record["record_id"])
            continue
        combined.append(
            {
                "record_id": record["record_id"],
                "title": entity_row["title"] or record["title"],
                "split": record["split"],
                "skills": entity_row["skills"],
                "embedding": record["embedding"],
            }
        )

    if missing_ids:
        preview = ", ".join(sorted(set(missing_ids))[:5])
        raise ValueError(
            f"Some {entity_name} embedding rows could not be matched to the source CSV. "
            f"Examples: {preview}"
        )

    return combined


def build_indicator_matrix(label_lists: list[list[str]], class_names: list[str]) -> np.ndarray:
    class_to_index = {skill: index for index, skill in enumerate(class_names)}
    matrix = np.zeros((len(label_lists), len(class_names)), dtype=np.uint8)
    for row_index, labels in enumerate(label_lists):
        for skill in labels:
            column_index = class_to_index.get(skill)
            if column_index is not None:
                matrix[row_index, column_index] = 1
    return matrix


def select_split_rows(rows: list[dict[str, Any]], split_name: str) -> list[dict[str, Any]]:
    return [row for row in rows if row["split"] == split_name]


def fit_label_binarizer(
    train_rows: list[dict[str, Any]],
    *,
    min_positive_train: int,
) -> tuple[MultiLabelBinarizer, np.ndarray, Counter[str], list[str]]:
    raw_binarizer = MultiLabelBinarizer()
    y_train_raw = raw_binarizer.fit_transform([row["skills"] for row in train_rows])
    raw_classes = list(raw_binarizer.classes_)
    train_counts = Counter(
        {
            skill: int(count)
            for skill, count in zip(raw_classes, y_train_raw.sum(axis=0), strict=True)
        }
    )

    kept_classes = [
        skill
        for skill in raw_classes
        if train_counts[skill] >= min_positive_train and train_counts[skill] < len(train_rows)
    ]
    dropped_classes = [skill for skill in raw_classes if skill not in kept_classes]

    if not kept_classes:
        raise ValueError(
            "No trainable skills remain after filtering. "
            "Try reducing --min-positive-train or checking the input labels."
        )

    kept_class_set = set(kept_classes)
    filtered_train_labels = [
        [skill for skill in row["skills"] if skill in kept_class_set]
        for row in train_rows
    ]

    binarizer = MultiLabelBinarizer(classes=kept_classes)
    y_train = binarizer.fit_transform(filtered_train_labels)
    train_counts = Counter(
        {
            skill: int(count)
            for skill, count in zip(binarizer.classes_, y_train.sum(axis=0), strict=True)
        }
    )
    return binarizer, y_train, train_counts, dropped_classes


def transform_labels(
    rows: list[dict[str, Any]],
    class_names: list[str],
) -> tuple[np.ndarray, Counter[str], list[str]]:
    y = build_indicator_matrix([row["skills"] for row in rows], class_names)
    counts = Counter(
        {
            skill: int(count)
            for skill, count in zip(class_names, y.sum(axis=0), strict=True)
        }
    )
    ignored_skills = sorted(
        {
            skill
            for row in rows
            for skill in row["skills"]
            if skill not in class_names
        }
    )
    return y, counts, ignored_skills


def fit_models(
    x_train: np.ndarray,
    y_train: np.ndarray,
    class_names: list[str],
    *,
    max_iter: int,
    random_state: int,
) -> tuple[list[LogisticRegression], list[dict[str, Any]]]:
    models: list[LogisticRegression] = []
    model_summaries: list[dict[str, Any]] = []

    for class_index, skill_name in enumerate(class_names):
        target = y_train[:, class_index]
        positive_count = int(target.sum())
        negative_count = int(len(target) - positive_count)
        if positive_count == 0 or negative_count == 0:
            raise ValueError(f"Skill '{skill_name}' is not trainable after filtering.")

        model = LogisticRegression(
            class_weight="balanced",
            max_iter=max_iter,
            random_state=random_state,
            solver="liblinear",
        )
        model.fit(x_train, target)
        models.append(model)
        model_summaries.append(
            {
                "skill": skill_name,
                "train_positive_count": positive_count,
                "train_negative_count": negative_count,
                "coef_l2_norm": float(np.linalg.norm(model.coef_)),
                "intercept": float(model.intercept_[0]),
            }
        )

    return models, model_summaries


def predict_probabilities(models: list[LogisticRegression], x_data: np.ndarray) -> np.ndarray:
    probabilities = np.zeros((len(x_data), len(models)), dtype=np.float32)
    for class_index, model in enumerate(models):
        probabilities[:, class_index] = model.predict_proba(x_data)[:, 1]
    return probabilities


def align_probabilities_to_universe(
    probabilities: np.ndarray,
    trained_class_names: list[str],
    full_class_names: list[str],
) -> np.ndarray:
    full_probabilities = np.zeros((probabilities.shape[0], len(full_class_names)), dtype=np.float32)
    full_index = {skill: index for index, skill in enumerate(full_class_names)}
    for trained_index, skill_name in enumerate(trained_class_names):
        full_index_value = full_index.get(skill_name)
        if full_index_value is not None:
            full_probabilities[:, full_index_value] = probabilities[:, trained_index]
    return full_probabilities


def _micro_metrics_from_counts(tp: int, fp: int, fn: int) -> tuple[float, float, float]:
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 0.0 if precision + recall == 0.0 else (2 * precision * recall) / (precision + recall)
    return precision, recall, f1


def _is_better_top_k_candidate(
    candidate: tuple[float, float, float, int],
    incumbent: tuple[float, float, float, int],
) -> bool:
    c_f1, c_recall, c_macro_f1, c_k = candidate
    i_f1, i_recall, i_macro_f1, i_k = incumbent

    if c_f1 > i_f1 + EPS:
        return True
    if i_f1 > c_f1 + EPS:
        return False

    if c_recall > i_recall + EPS:
        return True
    if i_recall > c_recall + EPS:
        return False

    if c_macro_f1 > i_macro_f1 + EPS:
        return True
    if i_macro_f1 > c_macro_f1 + EPS:
        return False

    return c_k < i_k


def evaluate_with_top_k(
    rows: list[dict[str, Any]],
    class_names: list[str],
    y_true: np.ndarray,
    probabilities: np.ndarray,
    *,
    top_k: int,
) -> tuple[dict[str, Any], pd.DataFrame]:
    row_count = len(rows)
    num_classes = len(class_names)
    predictions = np.zeros((row_count, num_classes), dtype=bool)

    for row_index in range(row_count):
        if top_k <= 0 or num_classes == 0:
            continue
        limit = min(top_k, num_classes)
        top_indices = np.argsort(-probabilities[row_index])[:limit]
        predictions[row_index, top_indices] = True

    positives = y_true == 1
    tp_cols = np.logical_and(predictions, positives).sum(axis=0).astype(np.int64)
    fp_cols = np.logical_and(predictions, ~positives).sum(axis=0).astype(np.int64)
    fn_cols = np.logical_and(~predictions, positives).sum(axis=0).astype(np.int64)

    total_tp = int(tp_cols.sum())
    total_fp = int(fp_cols.sum())
    total_fn = int(fn_cols.sum())
    micro_precision, micro_recall, micro_f1 = _micro_metrics_from_counts(total_tp, total_fp, total_fn)
    macro_precision, macro_recall, macro_f1, _ = precision_recall_fscore_support(
        y_true,
        predictions,
        average="macro",
        zero_division=0,
    )

    modeled_skill_set = set(class_names)
    per_row_metrics: list[dict[str, Any]] = []
    sample_precisions: list[float] = []
    sample_recalls: list[float] = []
    sample_f1_scores: list[float] = []
    hit_flags: list[float] = []
    exact_match_flags: list[float] = []
    predicted_skill_counts: list[int] = []
    true_skill_counts: list[int] = []

    for row_index, row in enumerate(rows):
        true_skills = [skill for skill in row["skills"] if skill in modeled_skill_set]
        predicted_indices = np.flatnonzero(predictions[row_index])
        if predicted_indices.size:
            sort_order = np.argsort(-probabilities[row_index, predicted_indices])
            predicted_indices = predicted_indices[sort_order]

        predicted_skills = [class_names[index] for index in predicted_indices.tolist()]
        predicted_scores = [float(probabilities[row_index, index]) for index in predicted_indices]

        true_set = set(true_skills)
        predicted_set = set(predicted_skills)
        overlap = [skill for skill in predicted_skills if skill in true_set]

        precision = len(overlap) / len(predicted_skills) if predicted_skills else 0.0
        recall = len(overlap) / len(true_set) if true_set else 0.0
        f1_score = 0.0 if precision + recall == 0.0 else (2 * precision * recall) / (precision + recall)
        hit_flag = 1.0 if overlap else 0.0
        exact_match_flag = 1.0 if predicted_set == true_set else 0.0

        sample_precisions.append(precision)
        sample_recalls.append(recall)
        sample_f1_scores.append(f1_score)
        hit_flags.append(hit_flag)
        exact_match_flags.append(exact_match_flag)
        predicted_skill_counts.append(len(predicted_skills))
        true_skill_counts.append(len(true_skills))

        per_row_metrics.append(
            {
                "record_id": row["record_id"],
                "title": row["title"],
                "split": row["split"],
                "true_skills": " | ".join(true_skills),
                "predicted_top_k_skills": " | ".join(predicted_skills),
                "predicted_top_k_scores": json.dumps(
                    [
                        {"skill": skill, "probability": round(score, 6)}
                        for skill, score in zip(predicted_skills, predicted_scores, strict=True)
                    ]
                ),
                "correct_top_k_skills": " | ".join(overlap),
                "num_true_skills": len(true_skills),
                "num_predicted_skills": len(predicted_skills),
                "num_correct_top_k_skills": len(overlap),
                "precision_at_k": precision,
                "recall_at_k": recall,
                "f1_at_k": f1_score,
                "hit_at_k": hit_flag,
                "exact_match": exact_match_flag,
            }
        )

    metrics = {
        "top_k": int(top_k),
        "test_rows": len(rows),
        "candidate_skills": len(class_names),
        "micro_precision": micro_precision,
        "micro_recall": micro_recall,
        "micro_f1": micro_f1,
        "macro_precision": float(macro_precision),
        "macro_recall": float(macro_recall),
        "macro_f1": float(macro_f1),
        "sample_precision": float(np.mean(sample_precisions)) if sample_precisions else 0.0,
        "sample_recall": float(np.mean(sample_recalls)) if sample_recalls else 0.0,
        "sample_f1": float(np.mean(sample_f1_scores)) if sample_f1_scores else 0.0,
        "hit_rate": float(np.mean(hit_flags)) if hit_flags else 0.0,
        "exact_match_accuracy": float(np.mean(exact_match_flags)) if exact_match_flags else 0.0,
        "avg_true_skills_per_record": float(np.mean(true_skill_counts)) if true_skill_counts else 0.0,
        "avg_predicted_skills_per_record": (
            float(np.mean(predicted_skill_counts)) if predicted_skill_counts else 0.0
        ),
    }
    return metrics, pd.DataFrame(per_row_metrics)


def find_best_top_k(
    rows: list[dict[str, Any]],
    class_names: list[str],
    labels: np.ndarray,
    probabilities: np.ndarray,
    *,
    candidates: list[int],
) -> tuple[int, dict[str, float]]:
    best: tuple[float, float, float, int] | None = None
    best_metrics: dict[str, float] | None = None

    for top_k in candidates:
        metrics, _ = evaluate_with_top_k(rows, class_names, labels, probabilities, top_k=top_k)
        candidate = (
            float(metrics["micro_f1"]),
            float(metrics["micro_recall"]),
            float(metrics["macro_f1"]),
            int(top_k),
        )
        if best is None or _is_better_top_k_candidate(candidate, best):
            best = candidate
            best_metrics = {
                "micro_precision": float(metrics["micro_precision"]),
                "micro_recall": float(metrics["micro_recall"]),
                "micro_f1": float(metrics["micro_f1"]),
                "macro_f1": float(metrics["macro_f1"]),
            }

    assert best is not None and best_metrics is not None
    return best[3], best_metrics


def build_top_k_df(
    class_names: list[str],
    *,
    selected_top_k: int,
    train_counts: Counter[str],
    val_counts: Counter[str],
    test_counts: Counter[str],
) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "skill_name": class_names,
            "selected_top_k": [int(selected_top_k)] * len(class_names),
            "train_positive_support": [int(train_counts[skill]) for skill in class_names],
            "val_positive_support": [int(val_counts[skill]) for skill in class_names],
            "test_positive_support": [int(test_counts[skill]) for skill in class_names],
        }
    )


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def run_entity(
    entity_name: str,
    *,
    data_file: Path,
    embeddings_file: Path,
    output_root: Path,
    train_split: str,
    val_split: str,
    test_split: str,
    fixed_top_k: int | None,
    top_k_candidates: list[int],
    skills_embeddings_file: Path,
    min_positive_train: int,
    max_iter: int,
    random_state: int,
) -> dict[str, Any]:
    entity_rows = load_entity_rows(entity_name, data_file)
    embedding_rows = load_embedding_rows(entity_name, embeddings_file)
    combined_rows = combine_rows(entity_name, embedding_rows, entity_rows)
    skill_names = load_skill_names(skills_embeddings_file)

    split_counts = Counter(row["split"] for row in combined_rows)
    train_rows = select_split_rows(combined_rows, train_split)
    val_rows = select_split_rows(combined_rows, val_split)
    test_rows = select_split_rows(combined_rows, test_split)

    if not train_rows:
        raise ValueError(f"No rows found for {entity_name} train split '{train_split}'.")
    if not val_rows:
        raise ValueError(f"No rows found for {entity_name} val split '{val_split}'.")
    if not test_rows:
        raise ValueError(f"No rows found for {entity_name} test split '{test_split}'.")

    binarizer, y_train, train_counts, dropped_classes = fit_label_binarizer(
        train_rows,
        min_positive_train=min_positive_train,
    )
    y_train_full, train_full_counts, ignored_train_only_skills = transform_labels(train_rows, skill_names)
    y_val_full, val_full_counts, ignored_val_only_skills = transform_labels(val_rows, skill_names)
    y_test_full, test_full_counts, ignored_test_only_skills = transform_labels(test_rows, skill_names)

    x_train = np.vstack([row["embedding"] for row in train_rows])
    x_val = np.vstack([row["embedding"] for row in val_rows])
    x_test = np.vstack([row["embedding"] for row in test_rows])

    class_names = list(binarizer.classes_)
    models, model_summaries = fit_models(
        x_train,
        y_train,
        class_names,
        max_iter=max_iter,
        random_state=random_state,
    )

    val_probabilities = predict_probabilities(models, x_val)
    test_probabilities = predict_probabilities(models, x_test)
    val_probabilities = align_probabilities_to_universe(val_probabilities, class_names, skill_names)
    test_probabilities = align_probabilities_to_universe(test_probabilities, class_names, skill_names)

    if fixed_top_k is not None:
        selected_top_k = fixed_top_k
        top_k_selection_metrics, _ = evaluate_with_top_k(
            val_rows,
            skill_names,
            y_val_full,
            val_probabilities,
            top_k=selected_top_k,
        )
    else:
        selected_top_k, top_k_selection_metrics = find_best_top_k(
            val_rows,
            skill_names,
            y_val_full,
            val_probabilities,
            candidates=top_k_candidates,
        )

    metrics, predictions_df = evaluate_with_top_k(
        test_rows,
        skill_names,
        y_test_full,
        test_probabilities,
        top_k=selected_top_k,
    )
    top_k_df = build_top_k_df(
        skill_names,
        selected_top_k=selected_top_k,
        train_counts=train_full_counts,
        val_counts=val_full_counts,
        test_counts=test_full_counts,
    )

    output_dir = output_root / entity_name
    output_dir.mkdir(parents=True, exist_ok=True)

    summary = {
        "entity": entity_name,
        "inputs": {
            "data_file": str(data_file),
            "embeddings_file": str(embeddings_file),
            "skills_embeddings_file": str(skills_embeddings_file),
            "skills_column": ENTITY_CONFIGS[entity_name]["skills_column"],
            "train_split": train_split,
            "val_split": val_split,
            "test_split": test_split,
        },
        "settings": {
            "prediction_mode": "top_k",
            "fixed_top_k": fixed_top_k,
            "top_k_candidates": top_k_candidates,
            "min_positive_train": min_positive_train,
            "max_iter": max_iter,
            "random_state": random_state,
        },
        "dataset": {
            "total_rows": len(combined_rows),
            "split_counts": dict(split_counts),
            "train_rows": len(train_rows),
            "val_rows": len(val_rows),
            "test_rows": len(test_rows),
            "trained_skills": len(class_names),
            "evaluation_skills": len(skill_names),
            "dropped_train_only_skills": dropped_classes,
            "ignored_val_only_skills": ignored_val_only_skills,
            "ignored_test_only_skills": ignored_test_only_skills,
        },
        "label_counts": {
            "train": dict(sorted(train_full_counts.items())),
            "val": dict(sorted(val_full_counts.items())),
            "test": dict(sorted(test_full_counts.items())),
        },
        "top_k_selection": {
            "split": val_split,
            "selected_top_k": int(selected_top_k),
            **top_k_selection_metrics,
        },
        "metrics": metrics,
    }

    metrics_path = output_dir / "metrics.json"
    top_k_path = output_dir / "top_k_selection.csv"
    predictions_path = output_dir / "predictions.csv"
    models_path = output_dir / "trained_skills.csv"

    write_json(metrics_path, summary)
    top_k_df.to_csv(top_k_path, index=False)
    predictions_df.to_csv(predictions_path, index=False)
    pd.DataFrame(model_summaries).to_csv(models_path, index=False)

    return {
        "entity": entity_name,
        "embeddings_file": embeddings_file,
        "train_rows": len(train_rows),
        "val_rows": len(val_rows),
        "test_rows": len(test_rows),
        "trained_skills": len(class_names),
        "dropped_skills": len(dropped_classes),
        "evaluation_skills": len(skill_names),
        "selected_top_k": selected_top_k,
        "metrics": metrics,
        "metrics_path": metrics_path,
        "top_k_path": top_k_path,
        "predictions_path": predictions_path,
        "models_path": models_path,
    }


def fit_acc_logreg_topk(
    entity: str = "jobs",
    data_file: str | Path | None = None,
    embeddings_file: str | Path | None = None,
    output_dir: str | Path | None = None,
    train_split: str = "train",
    val_split: str = "val",
    test_split: str = "test",
    top_k: int | None = None,
    top_k_candidates: tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    min_positive_train: int = 2,
    max_iter: int = 1000,
    random_state: int = 42,
    skills_embeddings_file: str | Path | None = None,
):
    result = run_entity(
        entity,
        data_file=Path(data_file) if data_file else ENTITY_CONFIGS[entity]["default_data_file"],
        embeddings_file=Path(embeddings_file) if embeddings_file else resolve_embeddings_file(None, entity),
        output_root=Path(output_dir) if output_dir else DEFAULT_OUTPUT_DIR,
        train_split=train_split,
        val_split=val_split,
        test_split=test_split,
        fixed_top_k=top_k,
        top_k_candidates=list(top_k_candidates),
        skills_embeddings_file=resolve_skill_embeddings_file(str(skills_embeddings_file) if skills_embeddings_file else None),
        min_positive_train=min_positive_train,
        max_iter=max_iter,
        random_state=random_state,
    )

    summary = json.loads(Path(result["metrics_path"]).read_text(encoding="utf-8"))
    metrics = summary["metrics"]
    dataset = summary["dataset"]
    inputs = summary["inputs"]
    top_k_selection = summary["top_k_selection"]

    metrics_df = pd.DataFrame(
        [
            {
                "entity": entity,
                "num_rows": summary["dataset"]["total_rows"],
                "train_rows": dataset["train_rows"],
                "val_rows": dataset["val_rows"],
                "test_rows": dataset["test_rows"],
                "num_skills": dataset["evaluation_skills"],
                "train_split": train_split,
                "val_split": val_split,
                "test_split": test_split,
                "selected_top_k": top_k_selection["selected_top_k"],
                "val_selection_micro_precision": top_k_selection["micro_precision"],
                "val_selection_micro_recall": top_k_selection["micro_recall"],
                "val_selection_micro_f1": top_k_selection["micro_f1"],
                "val_selection_macro_f1": top_k_selection["macro_f1"],
                "micro_precision": metrics["micro_precision"],
                "micro_recall": metrics["micro_recall"],
                "micro_f1": metrics["micro_f1"],
                "macro_precision": metrics["macro_precision"],
                "macro_recall": metrics["macro_recall"],
                "macro_f1": metrics["macro_f1"],
                "sample_precision": metrics["sample_precision"],
                "sample_recall": metrics["sample_recall"],
                "sample_f1": metrics["sample_f1"],
                "hit_rate": metrics["hit_rate"],
                "exact_match_accuracy": metrics["exact_match_accuracy"],
                "avg_true_skills_per_record": metrics["avg_true_skills_per_record"],
                "avg_predicted_skills_per_record": metrics["avg_predicted_skills_per_record"],
                "num_dropped_train_only_skills": len(dataset["dropped_train_only_skills"]),
                "num_ignored_val_only_skills": len(dataset["ignored_val_only_skills"]),
                "num_ignored_test_only_skills": len(dataset["ignored_test_only_skills"]),
                "split_counts": json.dumps(summary["dataset"]["split_counts"], sort_keys=True),
            }
        ]
    )

    top_k_df = pd.read_csv(result["top_k_path"])
    predictions_df = pd.read_csv(result["predictions_path"])
    trained_skills_df = pd.read_csv(result["models_path"])
    return summary, metrics_df, top_k_df, predictions_df, trained_skills_df


COMPULSORY_ACC_MODULE_CODES = {
    "ACC1701",
    "ACC2706",
    "ACC2707",
    "ACC2708",
    "ACC2709",
    "ACC2727",
    "ACC3701",
    "ACC3702",
    "ACC3703",
    "ACC3704",
    "ACC3705",
    "ACC3706",
    "ACC3707",
    "ACC3727",
}
HIGH_DEMAND_THRESHOLD_PERCENT = 10.0


def canonical_accountancy_module_code(module_code: Any) -> str:
    code = str(module_code).strip().upper()
    if code in COMPULSORY_ACC_MODULE_CODES:
        return code
    if code and code[-1].isalpha() and code[:-1] in COMPULSORY_ACC_MODULE_CODES:
        return code[:-1]
    return code


def build_entity_dataframe(
    entity_name: str,
    *,
    data_file: str | Path | None = None,
    embeddings_file: str | Path | None = None,
) -> pd.DataFrame:
    config = ENTITY_CONFIGS[entity_name]
    data_path = Path(data_file) if data_file else config["default_data_file"]
    embeddings_path = Path(embeddings_file) if embeddings_file else resolve_embeddings_file(None, entity_name)

    entity_rows = load_entity_rows(entity_name, data_path)
    embedding_rows = load_embedding_rows(entity_name, embeddings_path)
    combined_rows = combine_rows(entity_name, embedding_rows, entity_rows)

    return pd.DataFrame(
        {
            "entity_type": [entity_name[:-1]] * len(combined_rows),
            "entity_id": [row["record_id"] for row in combined_rows],
            "display_title": [row["title"] for row in combined_rows],
            "actual_skill_lists": [row["skills"] for row in combined_rows],
            "embedding": [row["embedding"] for row in combined_rows],
            "split": [row["split"] for row in combined_rows],
        }
    )


def predict_top_k_matrix(probabilities: np.ndarray, top_k: int) -> np.ndarray:
    predictions = np.zeros_like(probabilities, dtype=np.uint8)
    if top_k <= 0 or probabilities.size == 0:
        return predictions

    limit = min(top_k, probabilities.shape[1])
    top_indices = np.argpartition(-probabilities, kth=limit - 1, axis=1)[:, :limit]
    row_indices = np.arange(probabilities.shape[0])[:, None]
    predictions[row_indices, top_indices] = 1
    return predictions


def build_final_acc_gap_table(
    selected_top_k: int,
    *,
    jobs_data_file: str | Path | None = None,
    jobs_embeddings_file: str | Path | None = None,
    courses_data_file: str | Path | None = None,
    courses_embeddings_file: str | Path | None = None,
    skills_embeddings_file: str | Path | None = None,
    high_demand_threshold_percent: float = HIGH_DEMAND_THRESHOLD_PERCENT,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    jobs_all_df = build_entity_dataframe(
        "jobs",
        data_file=jobs_data_file,
        embeddings_file=jobs_embeddings_file,
    ).reset_index(drop=True)
    courses_all_df = build_entity_dataframe(
        "courses",
        data_file=courses_data_file,
        embeddings_file=courses_embeddings_file,
    ).reset_index(drop=True)
    full_fit_df = pd.concat([jobs_all_df, courses_all_df], ignore_index=True)

    skills_path = resolve_skill_embeddings_file(str(skills_embeddings_file) if skills_embeddings_file else None)
    skill_names = load_skill_names(skills_path)

    x_full_fit = np.vstack(full_fit_df["embedding"].to_numpy()).astype(np.float32)
    y_full_fit = build_indicator_matrix(full_fit_df["actual_skill_lists"].tolist(), skill_names)
    x_jobs_all = np.vstack(jobs_all_df["embedding"].to_numpy()).astype(np.float32)
    x_courses_all = np.vstack(courses_all_df["embedding"].to_numpy()).astype(np.float32)

    jobs_full_proba = np.zeros((x_jobs_all.shape[0], len(skill_names)), dtype=np.float32)
    courses_full_proba = np.zeros((x_courses_all.shape[0], len(skill_names)), dtype=np.float32)
    full_fitted_mask = np.zeros(len(skill_names), dtype=bool)
    full_skipped_skills: list[str] = []

    for skill_index, skill_name in enumerate(skill_names):
        y_full_j = y_full_fit[:, skill_index]
        if len(np.unique(y_full_j)) < 2:
            full_skipped_skills.append(skill_name)
            continue

        model = LogisticRegression(
            class_weight="balanced",
            max_iter=2000,
            random_state=42,
            solver="liblinear",
        )
        model.fit(x_full_fit, y_full_j)
        jobs_full_proba[:, skill_index] = model.predict_proba(x_jobs_all)[:, 1]
        courses_full_proba[:, skill_index] = model.predict_proba(x_courses_all)[:, 1]
        full_fitted_mask[skill_index] = True

    jobs_full_pred = predict_top_k_matrix(jobs_full_proba, selected_top_k)
    courses_full_pred = predict_top_k_matrix(courses_full_proba, selected_top_k)

    job_skill_counts = jobs_full_pred.sum(axis=0).astype(int)
    course_skill_counts = courses_full_pred.sum(axis=0).astype(int)
    job_denominator = max(len(jobs_all_df), 1)
    course_codes = courses_all_df["entity_id"].astype(str).tolist()
    course_titles = courses_all_df["display_title"].astype(str).tolist()

    gap_rows: list[dict[str, Any]] = []
    for skill_index, skill_name in enumerate(skill_names):
        job_demand_percent = 100.0 * job_skill_counts[skill_index] / job_denominator
        job_demand_label = "High" if job_demand_percent >= high_demand_threshold_percent else "Low"

        course_indices = np.where(courses_full_pred[:, skill_index] == 1)[0]
        compulsory_course_labels: list[str] = []
        elective_course_labels: list[str] = []

        for course_index in course_indices:
            course_code = course_codes[course_index]
            course_title = course_titles[course_index]
            course_label = f"{course_code}: {course_title}"
            if canonical_accountancy_module_code(course_code) in COMPULSORY_ACC_MODULE_CODES:
                compulsory_course_labels.append(course_label)
            else:
                elective_course_labels.append(course_label)

        taught_in_any_course = len(course_indices) > 0
        taught_in_compulsory_course = len(compulsory_course_labels) > 0

        if taught_in_compulsory_course:
            curriculum_coverage = "Strong"
        elif taught_in_any_course:
            curriculum_coverage = "Weak"
        else:
            curriculum_coverage = "Very weak"

        if job_demand_label == "High" and taught_in_compulsory_course:
            gap_interpretation = "Well covered"
        elif job_demand_label == "High" and taught_in_any_course:
            gap_interpretation = "Important gap - High demand skill but course not compulsory"
        elif job_demand_label == "High":
            gap_interpretation = "Critical gap - High demand skill not taught in ACC courses"
        elif taught_in_compulsory_course:
            gap_interpretation = "Compulsory coverage for lower-demand skill"
        elif taught_in_any_course:
            gap_interpretation = "Elective coverage for lower-demand skill"
        else:
            gap_interpretation = "Low demand and limited coverage"

        gap_rows.append(
            {
                "skill_name": skill_name,
                "job_demand_percent": float(job_demand_percent),
                "job_demand": job_demand_label,
                "job_postings_with_skill": int(job_skill_counts[skill_index]),
                "taught_in_any_course": "Yes" if taught_in_any_course else "No",
                "taught_in_compulsory_course": "Yes" if taught_in_compulsory_course else "No",
                "courses_covering_skill": int(course_skill_counts[skill_index]),
                "curriculum_coverage": curriculum_coverage,
                "gap_interpretation": gap_interpretation,
                "compulsory_courses": " | ".join(compulsory_course_labels[:5]),
                "elective_courses": " | ".join(elective_course_labels[:5]),
            }
        )

    full_model_gap_table_df = pd.DataFrame(gap_rows).sort_values(
        by=["job_demand", "job_demand_percent", "curriculum_coverage", "skill_name"],
        ascending=[False, False, True, True],
    ).reset_index(drop=True)

    high_demand_gap_table_df = full_model_gap_table_df.loc[
        full_model_gap_table_df["job_demand"] == "High"
    ].reset_index(drop=True)

    final_model_refit_summary_df = pd.DataFrame(
        {
            "selected_top_k": [int(selected_top_k)],
            "full_fit_rows": [len(full_fit_df)],
            "jobs_scored": [len(jobs_all_df)],
            "courses_scored": [len(courses_all_df)],
            "fitted_skills_after_refit": [int(full_fitted_mask.sum())],
            "skipped_skills_after_refit": [len(full_skipped_skills)],
            "high_demand_threshold_percent": [high_demand_threshold_percent],
        }
    )

    return final_model_refit_summary_df, full_model_gap_table_df, high_demand_gap_table_df


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    output_root = Path(args.output_dir)
    top_k_candidates = parse_top_k_candidates(args.top_k_candidates)

    if args.top_k is not None and args.top_k <= 0:
        raise ValueError("--top-k must be a positive integer.")

    selected_entities = ["jobs", "courses"] if args.entity == "both" else [args.entity]
    file_args = {
        "jobs": {
            "data_file": Path(args.jobs_file),
            "embeddings_file": resolve_embeddings_file(args.jobs_embeddings_file, "jobs"),
        },
        "courses": {
            "data_file": Path(args.courses_file),
            "embeddings_file": resolve_embeddings_file(args.courses_embeddings_file, "courses"),
        },
    }
    skills_embeddings_file = resolve_skill_embeddings_file(args.skills_embeddings_file)

    for entity_name in selected_entities:
        ensure_file_exists(file_args[entity_name]["data_file"], f"{entity_name} file")

    results = []
    for entity_name in selected_entities:
        result = run_entity(
            entity_name,
            data_file=file_args[entity_name]["data_file"],
            embeddings_file=file_args[entity_name]["embeddings_file"],
            output_root=output_root,
            train_split=args.train_split,
            val_split=args.val_split,
            test_split=args.test_split,
            fixed_top_k=args.top_k,
            top_k_candidates=top_k_candidates,
            skills_embeddings_file=skills_embeddings_file,
            min_positive_train=args.min_positive_train,
            max_iter=args.max_iter,
            random_state=args.random_state,
        )
        results.append(result)

    for result in results:
        metrics = result["metrics"]
        print(f"Entity: {result['entity']}")
        print(f"Embeddings file: {result['embeddings_file']}")
        print(f"Train rows: {result['train_rows']}")
        print(f"Val rows: {result['val_rows']}")
        print(f"Test rows: {result['test_rows']}")
        print(f"Trained skills: {result['trained_skills']}")
        print(f"Dropped skills: {result['dropped_skills']}")
        print(f"Selected top-k: {result['selected_top_k']}")
        print(f"Sample F1: {metrics['sample_f1']:.4f}")
        print(f"Micro F1: {metrics['micro_f1']:.4f}")
        print(f"Macro F1: {metrics['macro_f1']:.4f}")
        print(f"Hit rate: {metrics['hit_rate']:.4f}")
        print(f"Predictions written to: {result['predictions_path']}")
        print(f"Top-k summary written to: {result['top_k_path']}")
        print(f"Metrics written to: {result['metrics_path']}")
        print(f"Model summary written to: {result['models_path']}")
        print("")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
