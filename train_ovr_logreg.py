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
DEFAULT_OUTPUT_DIR = BASE_DIR / "embedding" / "acc" / "logreg_threshold"
EPS = 1e-12

ENTITY_CONFIGS: dict[str, dict[str, Any]] = {
    "jobs": {
        "label": "jobs",
        "default_data_file": BASE_DIR / "data" / "acc" / "audit_tax_accounting_jobs.csv",
        "default_embeddings_candidates": (
            BASE_DIR / "embedding" / "acc" / "acc_jobs_embeddings.jsonl",
            BASE_DIR / "embedding" / "acc" / "jobs_embeddings.jsonl",
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
        "data_id_column": "moduleCode",
        "title_column": "title",
        "skills_column": "extracted_skills",
        "embedding_id_key": "course_code",
    },
}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Train one-vs-rest logistic regression models on accounting job and ACC course "
            "embeddings, then evaluate multilabel skill prediction with a shared global "
            "threshold selected like model/cosine_sim_thres.ipynb."
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
    parser.add_argument(
        "--courses-file",
        default=str(ENTITY_CONFIGS["courses"]["default_data_file"]),
    )
    parser.add_argument("--courses-embeddings-file")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--train-split", default="train")
    parser.add_argument("--test-split", default="test")
    parser.add_argument(
        "--top-k",
        type=int,
        default=None,
        help=argparse.SUPPRESS,
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


def select_split_rows(rows: list[dict[str, Any]], split_name: str) -> list[dict[str, Any]]:
    return [row for row in rows if row["split"] == split_name]


def fit_label_binarizer(
    train_rows: list[dict[str, Any]],
    test_rows: list[dict[str, Any]],
    *,
    min_positive_train: int,
) -> tuple[
    MultiLabelBinarizer,
    np.ndarray,
    np.ndarray,
    Counter[str],
    Counter[str],
    list[str],
    list[str],
]:
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
        if train_counts[skill] >= min_positive_train
        and train_counts[skill] < len(train_rows)
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
    filtered_test_labels = [
        [skill for skill in row["skills"] if skill in kept_class_set]
        for row in test_rows
    ]
    ignored_test_only_skills = sorted(
        {
            skill
            for row in test_rows
            for skill in row["skills"]
            if skill not in kept_class_set
        }
    )

    binarizer = MultiLabelBinarizer(classes=kept_classes)
    y_train = binarizer.fit_transform(filtered_train_labels)
    y_test = binarizer.transform(filtered_test_labels)

    train_counts = Counter(
        {
            skill: int(count)
            for skill, count in zip(binarizer.classes_, y_train.sum(axis=0), strict=True)
        }
    )
    test_counts = Counter(
        {
            skill: int(count)
            for skill, count in zip(binarizer.classes_, y_test.sum(axis=0), strict=True)
        }
    )

    return (
        binarizer,
        y_train,
        y_test,
        train_counts,
        test_counts,
        dropped_classes,
        ignored_test_only_skills,
    )


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


def _binary_f1(tp: np.ndarray, fp: np.ndarray, fn: np.ndarray) -> np.ndarray:
    denominator = (2 * tp) + fp + fn
    result = np.zeros_like(denominator, dtype=np.float64)
    valid = denominator > 0
    result[valid] = (2.0 * tp[valid]) / denominator[valid]
    return result


def _micro_metrics_from_counts(tp: int, fp: int, fn: int) -> tuple[float, float, float]:
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 0.0 if precision + recall == 0.0 else (2 * precision * recall) / (precision + recall)
    return precision, recall, f1


def _is_better_candidate(
    candidate: tuple[float, float, float, float],
    incumbent: tuple[float, float, float, float],
) -> bool:
    c_f1, c_recall, c_macro_f1, c_threshold = candidate
    i_f1, i_recall, i_macro_f1, i_threshold = incumbent

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

    return c_threshold < i_threshold - EPS


def find_best_global_threshold(
    probabilities: np.ndarray,
    labels: np.ndarray,
) -> tuple[float, dict[str, float]]:
    flat_scores = probabilities.ravel()
    flat_labels = labels.ravel().astype(bool)
    candidates = np.unique(flat_scores)
    if candidates.size == 0:
        raise ValueError("Cannot select a threshold from an empty probability matrix.")

    best: tuple[float, float, float, float] | None = None

    for threshold in candidates:
        pred = flat_scores >= threshold
        tp = int(np.logical_and(pred, flat_labels).sum())
        fp = int(np.logical_and(pred, ~flat_labels).sum())
        fn = int(np.logical_and(~pred, flat_labels).sum())
        micro_precision, micro_recall, micro_f1 = _micro_metrics_from_counts(tp, fp, fn)

        pred_2d = probabilities >= threshold
        positives = labels == 1
        tp_cols = np.logical_and(pred_2d, positives).sum(axis=0)
        fp_cols = np.logical_and(pred_2d, ~positives).sum(axis=0)
        fn_cols = np.logical_and(~pred_2d, positives).sum(axis=0)
        macro_f1 = float(_binary_f1(tp_cols, fp_cols, fn_cols).mean())

        candidate = (micro_f1, micro_recall, macro_f1, float(threshold))
        if best is None or _is_better_candidate(candidate, best):
            best = candidate
            best_metrics = {
                "micro_precision": micro_precision,
                "micro_recall": micro_recall,
                "micro_f1": micro_f1,
                "macro_f1": macro_f1,
            }

    assert best is not None
    return best[3], best_metrics


def evaluate_with_threshold(
    rows: list[dict[str, Any]],
    class_names: list[str],
    y_true: np.ndarray,
    probabilities: np.ndarray,
    *,
    threshold: float,
) -> tuple[dict[str, Any], pd.DataFrame]:
    predictions = probabilities >= threshold
    positives = y_true == 1

    tp_cols = np.logical_and(predictions, positives).sum(axis=0).astype(np.int64)
    fp_cols = np.logical_and(predictions, ~positives).sum(axis=0).astype(np.int64)
    fn_cols = np.logical_and(~predictions, positives).sum(axis=0).astype(np.int64)

    total_tp = int(tp_cols.sum())
    total_fp = int(fp_cols.sum())
    total_fn = int(fn_cols.sum())
    micro_precision, micro_recall, micro_f1 = _micro_metrics_from_counts(
        total_tp,
        total_fp,
        total_fn,
    )
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
        split_label = row.get("split", "test")

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
                "split": split_label,
                "true_skills": " | ".join(true_skills),
                "predicted_skills": " | ".join(predicted_skills),
                "predicted_skill_scores": json.dumps(
                    [
                        {"skill": skill, "probability": round(score, 6)}
                        for skill, score in zip(predicted_skills, predicted_scores, strict=True)
                    ]
                ),
                "correct_skills": " | ".join(overlap),
                "tp": len(overlap),
                "fp": len(predicted_set - true_set),
                "fn": len(true_set - predicted_set),
                "num_true_skills": len(true_skills),
                "num_predicted_skills": len(predicted_skills),
                "precision": precision,
                "recall": recall,
                "f1": f1_score,
                "hit": hit_flag,
                "exact_match": exact_match_flag,
            }
        )

    metrics = {
        "global_threshold": float(threshold),
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


def build_thresholds_df(
    class_names: list[str],
    *,
    threshold: float,
    train_counts: Counter[str],
    test_counts: Counter[str],
) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "skill_name": class_names,
            "threshold": [float(threshold)] * len(class_names),
            "train_positive_support": [int(train_counts[skill]) for skill in class_names],
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
    test_split: str,
    min_positive_train: int,
    max_iter: int,
    random_state: int,
) -> dict[str, Any]:
    entity_rows = load_entity_rows(entity_name, data_file)
    embedding_rows = load_embedding_rows(entity_name, embeddings_file)
    combined_rows = combine_rows(entity_name, embedding_rows, entity_rows)

    split_counts = Counter(row["split"] for row in combined_rows)
    train_rows = select_split_rows(combined_rows, train_split)
    test_rows = select_split_rows(combined_rows, test_split)

    if not train_rows:
        raise ValueError(f"No rows found for {entity_name} train split '{train_split}'.")
    if not test_rows:
        raise ValueError(f"No rows found for {entity_name} test split '{test_split}'.")

    (
        binarizer,
        y_train,
        y_test,
        train_counts,
        test_counts,
        dropped_classes,
        ignored_test_only_skills,
    ) = fit_label_binarizer(train_rows, test_rows, min_positive_train=min_positive_train)

    x_train = np.vstack([row["embedding"] for row in train_rows])
    x_test = np.vstack([row["embedding"] for row in test_rows])

    class_names = list(binarizer.classes_)
    models, model_summaries = fit_models(
        x_train,
        y_train,
        class_names,
        max_iter=max_iter,
        random_state=random_state,
    )

    train_probabilities = predict_probabilities(models, x_train)
    test_probabilities = predict_probabilities(models, x_test)

    global_threshold, threshold_selection_metrics = find_best_global_threshold(
        train_probabilities,
        y_train,
    )
    metrics, predictions_df = evaluate_with_threshold(
        test_rows,
        class_names,
        y_test,
        test_probabilities,
        threshold=global_threshold,
    )
    thresholds_df = build_thresholds_df(
        class_names,
        threshold=global_threshold,
        train_counts=train_counts,
        test_counts=test_counts,
    )

    output_dir = output_root / entity_name
    output_dir.mkdir(parents=True, exist_ok=True)

    summary = {
        "entity": entity_name,
        "inputs": {
            "data_file": str(data_file),
            "embeddings_file": str(embeddings_file),
            "skills_column": ENTITY_CONFIGS[entity_name]["skills_column"],
            "train_split": train_split,
            "test_split": test_split,
        },
        "settings": {
            "prediction_mode": "global_threshold",
            "min_positive_train": min_positive_train,
            "max_iter": max_iter,
            "random_state": random_state,
        },
        "dataset": {
            "total_rows": len(combined_rows),
            "split_counts": dict(split_counts),
            "train_rows": len(train_rows),
            "test_rows": len(test_rows),
            "trained_skills": len(class_names),
            "dropped_train_only_skills": dropped_classes,
            "ignored_test_only_skills": ignored_test_only_skills,
        },
        "label_counts": {
            "train": dict(sorted(train_counts.items())),
            "test": dict(sorted(test_counts.items())),
        },
        "threshold_selection": {
            "split": train_split,
            "global_threshold": float(global_threshold),
            **threshold_selection_metrics,
        },
        "metrics": metrics,
    }

    metrics_path = output_dir / "metrics.json"
    thresholds_path = output_dir / "thresholds.csv"
    predictions_path = output_dir / "predictions.csv"
    models_path = output_dir / "trained_skills.csv"

    write_json(metrics_path, summary)
    thresholds_df.to_csv(thresholds_path, index=False)
    predictions_df.to_csv(predictions_path, index=False)
    pd.DataFrame(model_summaries).to_csv(models_path, index=False)

    return {
        "entity": entity_name,
        "embeddings_file": embeddings_file,
        "train_rows": len(train_rows),
        "test_rows": len(test_rows),
        "trained_skills": len(class_names),
        "dropped_skills": len(dropped_classes),
        "threshold": global_threshold,
        "metrics": metrics,
        "metrics_path": metrics_path,
        "thresholds_path": thresholds_path,
        "predictions_path": predictions_path,
        "models_path": models_path,
    }


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    output_root = Path(args.output_dir)

    if args.top_k is not None:
        print("Ignoring deprecated --top-k argument; using shared global threshold predictions.")

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
            test_split=args.test_split,
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
        print(f"Test rows: {result['test_rows']}")
        print(f"Trained skills: {result['trained_skills']}")
        print(f"Dropped skills: {result['dropped_skills']}")
        print(f"Global threshold: {result['threshold']:.6f}")
        print(f"Sample F1: {metrics['sample_f1']:.4f}")
        print(f"Micro F1: {metrics['micro_f1']:.4f}")
        print(f"Macro F1: {metrics['macro_f1']:.4f}")
        print(f"Hit rate: {metrics['hit_rate']:.4f}")
        print(f"Predictions written to: {result['predictions_path']}")
        print(f"Thresholds written to: {result['thresholds_path']}")
        print(f"Metrics written to: {result['metrics_path']}")
        print(f"Model summary written to: {result['models_path']}")
        print("")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
