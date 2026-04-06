import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics.pairwise import cosine_similarity


EPS = 1e-12


def parse_skill_list(value):
    if pd.isna(value):
        return []
    text = str(value).strip()
    if not text or text.lower() == "nan":
        return []

    seen = set()
    skills = []
    for raw in text.split("|"):
        skill = raw.strip()
        if skill and skill not in seen:
            seen.add(skill)
            skills.append(skill)
    return skills


def load_jsonl(path):
    records = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    if not records:
        raise ValueError(f"No records found in {path}")
    return records


def build_indicator_matrix(skill_lists, skill_names):
    skill_to_idx = {skill: idx for idx, skill in enumerate(skill_names)}
    indicator = np.zeros((len(skill_lists), len(skill_names)), dtype=np.uint8)

    for row_idx, skills in enumerate(skill_lists):
        for skill in skills:
            if skill in skill_to_idx:
                indicator[row_idx, skill_to_idx[skill]] = 1

    return indicator


def _safe_div(numerator, denominator):
    numerator = np.asarray(numerator, dtype=np.float64)
    denominator = np.asarray(denominator, dtype=np.float64)
    result = np.zeros_like(numerator, dtype=np.float64)
    np.divide(numerator, denominator, out=result, where=denominator != 0)
    return result


def _binary_f1(tp, fp, fn):
    precision = _safe_div(tp, tp + fp)
    recall = _safe_div(tp, tp + fn)
    return _safe_div(2.0 * precision * recall, precision + recall)


def _micro_metrics_from_counts(tp, fp, fn):
    precision = float(tp / (tp + fp)) if (tp + fp) else 0.0
    recall = float(tp / (tp + fn)) if (tp + fn) else 0.0
    f1 = float((2.0 * precision * recall) / (precision + recall)) if (precision + recall) else 0.0
    return precision, recall, f1


def _is_better_candidate(candidate, incumbent):
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


def _find_best_global_threshold(similarity, labels):
    flat_scores = similarity.ravel()
    flat_labels = labels.ravel().astype(bool)

    candidates = np.unique(flat_scores)
    candidates = np.r_[candidates, flat_scores.max() + 1e-9]

    best = None
    best_threshold = None

    for threshold in candidates:
        pred = flat_scores >= threshold
        tp = int(np.logical_and(pred, flat_labels).sum())
        fp = int(np.logical_and(pred, ~flat_labels).sum())
        fn = int(np.logical_and(~pred, flat_labels).sum())
        _, micro_recall, micro_f1 = _micro_metrics_from_counts(tp, fp, fn)

        pred_2d = similarity >= threshold
        tp_cols = np.logical_and(pred_2d, labels == 1).sum(axis=0)
        fp_cols = np.logical_and(pred_2d, labels == 0).sum(axis=0)
        fn_cols = np.logical_and(~pred_2d, labels == 1).sum(axis=0)
        macro_f1 = float(_binary_f1(tp_cols, fp_cols, fn_cols).mean())

        candidate = (micro_f1, micro_recall, macro_f1, float(threshold))
        if best is None or _is_better_candidate(candidate, best):
            best = candidate
            best_threshold = float(threshold)

    return best_threshold


def _find_best_threshold_for_one_skill(scores, labels, default_threshold):
    candidates = np.unique(scores)
    candidates = np.r_[candidates, scores.max() + 1e-9]

    best = None
    best_threshold = float(default_threshold)

    for threshold in candidates:
        pred = scores >= threshold

        tp = int(np.logical_and(pred, labels == 1).sum())
        fp = int(np.logical_and(pred, labels == 0).sum())
        fn = int(np.logical_and(~pred, labels == 1).sum())

        precision = float(tp / (tp + fp)) if (tp + fp) else 0.0
        recall = float(tp / (tp + fn)) if (tp + fn) else 0.0
        f1 = float((2.0 * precision * recall) / (precision + recall)) if (precision + recall) else 0.0

        candidate = (f1, recall, -float(threshold))
        if best is None or candidate > best:
            best = candidate
            best_threshold = float(threshold)

    return best_threshold


def _evaluate_micro_f1_with_thresholds(similarity, labels, thresholds):
    predictions = similarity >= thresholds[np.newaxis, :]
    positives = labels == 1

    tp_cols = np.logical_and(predictions, positives).sum(axis=0).astype(np.int64)
    fp_cols = np.logical_and(predictions, ~positives).sum(axis=0).astype(np.int64)
    fn_cols = np.logical_and(~predictions, positives).sum(axis=0).astype(np.int64)

    total_tp = int(tp_cols.sum())
    total_fp = int(fp_cols.sum())
    total_fn = int(fn_cols.sum())

    micro_precision, micro_recall, micro_f1 = _micro_metrics_from_counts(total_tp, total_fp, total_fn)

    return {
        "predictions": predictions,
        "tp_cols": tp_cols,
        "fp_cols": fp_cols,
        "fn_cols": fn_cols,
        "total_tp": total_tp,
        "total_fp": total_fp,
        "total_fn": total_fn,
        "micro_precision": micro_precision,
        "micro_recall": micro_recall,
        "micro_f1": micro_f1,
    }


def _find_best_threshold_for_one_skill_by_global_micro_f1(
    similarity,
    labels,
    thresholds,
    skill_idx,
):
    current_threshold = float(thresholds[skill_idx])
    candidates = np.unique(similarity[:, skill_idx])
    candidates = np.r_[candidates, similarity[:, skill_idx].max() + 1e-9]

    base_eval = _evaluate_micro_f1_with_thresholds(similarity, labels, thresholds)
    best_micro_f1 = base_eval["micro_f1"]
    best_micro_recall = base_eval["micro_recall"]
    best_threshold = current_threshold

    for threshold in candidates:
        trial_thresholds = thresholds.copy()
        trial_thresholds[skill_idx] = float(threshold)

        trial_eval = _evaluate_micro_f1_with_thresholds(similarity, labels, trial_thresholds)
        trial_micro_f1 = trial_eval["micro_f1"]
        trial_micro_recall = trial_eval["micro_recall"]

        if trial_micro_f1 > best_micro_f1 + EPS:
            best_micro_f1 = trial_micro_f1
            best_micro_recall = trial_micro_recall
            best_threshold = float(threshold)
        elif abs(trial_micro_f1 - best_micro_f1) <= EPS:
            if trial_micro_recall > best_micro_recall + EPS:
                best_micro_recall = trial_micro_recall
                best_threshold = float(threshold)
            elif abs(trial_micro_recall - best_micro_recall) <= EPS:
                if float(threshold) < best_threshold - EPS:
                    best_threshold = float(threshold)

    return best_threshold, best_micro_f1


def _greedy_optimize_thresholds_for_micro_f1(
    similarity,
    labels,
    initial_thresholds,
    max_rounds=3,
):
    thresholds = initial_thresholds.astype(np.float32).copy()
    num_skills = similarity.shape[1]

    initial_eval = _evaluate_micro_f1_with_thresholds(similarity, labels, thresholds)
    best_micro_f1 = initial_eval["micro_f1"]

    threshold_origin = np.array(["global"] * num_skills, dtype=object)

    for _ in range(max_rounds):
        improved_this_round = False

        for skill_idx in range(num_skills):
            current_threshold = float(thresholds[skill_idx])

            best_threshold, candidate_micro_f1 = _find_best_threshold_for_one_skill_by_global_micro_f1(
                similarity=similarity,
                labels=labels,
                thresholds=thresholds,
                skill_idx=skill_idx,
            )

            if abs(best_threshold - current_threshold) > EPS and candidate_micro_f1 > best_micro_f1 + EPS:
                thresholds[skill_idx] = best_threshold
                best_micro_f1 = candidate_micro_f1
                threshold_origin[skill_idx] = "greedy_skill_specific"
                improved_this_round = True

        if not improved_this_round:
            break

    return thresholds, threshold_origin


def load_labeled_entities_from_embeddings(label_csv, embeddings_jsonl, *, entity_type, entity_id_col, embedding_id_key):
    labels_df = pd.read_csv(label_csv, usecols=[entity_id_col, "title", "extracted_skills"]).rename(
        columns={entity_id_col: "entity_id", "title": "label_title"}
    )
    embedding_records = load_jsonl(embeddings_jsonl)

    embeddings_df = pd.DataFrame(
        {
            "entity_type": entity_type,
            "entity_id": [record[embedding_id_key] for record in embedding_records],
            "embedded_title": [record.get("title", "") for record in embedding_records],
            "embedding": [record["embedding"] for record in embedding_records],
        }
    )

    merged = embeddings_df.merge(labels_df, on="entity_id", how="left")
    missing_labels = int(merged["label_title"].isna().sum())
    if missing_labels:
        raise ValueError(f"{missing_labels} embedded {entity_type} rows have no matching labels in {label_csv}")

    merged["title"] = merged["label_title"].fillna(merged["embedded_title"]).astype(str)
    merged["actual_skill_lists"] = merged["extracted_skills"].map(parse_skill_list)

    summary = {
        "entity_type": entity_type,
        "embedded_rows": len(embedding_records),
        "matched_labels": len(merged),
        "missing_labels": missing_labels,
        "rows_with_extracted_skills": int(merged["actual_skill_lists"].map(bool).sum()),
    }

    return merged[["entity_type", "entity_id", "title", "embedding", "actual_skill_lists"]].copy(), summary


def prepare_acc_similarity_problem(entities_df, skill_embeddings_jsonl):
    skill_records = load_jsonl(skill_embeddings_jsonl)
    skill_names = [record["skill_name"] for record in skill_records]

    entity_matrix = np.vstack(entities_df["embedding"].to_numpy()).astype(np.float32)
    skill_matrix = np.vstack([record["embedding"] for record in skill_records]).astype(np.float32)

    similarity = cosine_similarity(entity_matrix, skill_matrix)
    labels = build_indicator_matrix(entities_df["actual_skill_lists"].tolist(), skill_names)

    if similarity.shape != labels.shape:
        raise ValueError(
            f"Similarity matrix shape {similarity.shape} does not match label matrix shape {labels.shape}"
        )

    return {
        "entities_df": entities_df.reset_index(drop=True).copy(),
        "skill_names": skill_names,
        "similarity": similarity,
        "labels": labels,
    }


def _build_result_frames(problem, thresholds, predictions, global_threshold, *, dataset_variant, model_variant, metric_extras=None, threshold_extras=None):
    entities_df = problem["entities_df"]
    skill_names = problem["skill_names"]
    labels = problem["labels"]

    positives = labels == 1
    tp_cols = np.logical_and(predictions, positives).sum(axis=0).astype(np.int64)
    fp_cols = np.logical_and(predictions, ~positives).sum(axis=0).astype(np.int64)
    fn_cols = np.logical_and(~predictions, positives).sum(axis=0).astype(np.int64)

    total_tp = int(tp_cols.sum())
    total_fp = int(fp_cols.sum())
    total_fn = int(fn_cols.sum())

    micro_precision, micro_recall, micro_f1 = _micro_metrics_from_counts(total_tp, total_fp, total_fn)
    macro_precision, macro_recall, macro_f1, _ = precision_recall_fscore_support(
        labels,
        predictions,
        average="macro",
        zero_division=0,
    )

    counts = entities_df["entity_type"].value_counts()
    positive_support = labels.sum(axis=0).astype(int)

    metrics_record = {
        "dataset_variant": dataset_variant,
        "model_variant": model_variant,
        "num_jobs": int(counts.get("job", 0)),
        "num_courses": int(counts.get("course", 0)),
        "num_entities": len(entities_df),
        "num_skills": len(skill_names),
        "global_threshold": float(global_threshold),
        "micro_precision": micro_precision,
        "micro_recall": micro_recall,
        "micro_f1": micro_f1,
        "macro_precision": float(macro_precision),
        "macro_recall": float(macro_recall),
        "macro_f1": float(macro_f1),
    }
    if metric_extras:
        metrics_record.update(metric_extras)

    thresholds_data = {
        "dataset_variant": dataset_variant,
        "model_variant": model_variant,
        "skill_name": skill_names,
        "threshold": thresholds.astype(float),
        "positive_support": positive_support,
        "tp": tp_cols,
        "fp": fp_cols,
        "fn": fn_cols,
        "precision": _safe_div(tp_cols, tp_cols + fp_cols),
        "recall": _safe_div(tp_cols, tp_cols + fn_cols),
        "f1": _binary_f1(tp_cols, fp_cols, fn_cols),
    }
    if threshold_extras:
        thresholds_data.update(threshold_extras)

    predicted_skill_lists = [
        [skill_names[idx] for idx, is_on in enumerate(row) if is_on]
        for row in predictions
    ]
    actual_skill_lists = entities_df["actual_skill_lists"].tolist()

    predictions_df = pd.DataFrame(
        {
            "entity_type": entities_df["entity_type"],
            "entity_id": entities_df["entity_id"],
            "title": entities_df["title"].astype(str),
            "actual_skills": [" | ".join(skills) for skills in actual_skill_lists],
            "predicted_skills": [" | ".join(skills) for skills in predicted_skill_lists],
            "tp": [len(set(a) & set(p)) for a, p in zip(actual_skill_lists, predicted_skill_lists)],
            "fp": [len(set(p) - set(a)) for a, p in zip(actual_skill_lists, predicted_skill_lists)],
            "fn": [len(set(a) - set(p)) for a, p in zip(actual_skill_lists, predicted_skill_lists)],
        }
    )

    return pd.DataFrame([metrics_record]), pd.DataFrame(thresholds_data), predictions_df


def _validate_matching_skill_names(job_problem, course_problem):
    if job_problem["skill_names"] != course_problem["skill_names"]:
        raise ValueError("Job and course problems do not share the same skill ordering")
    return job_problem["skill_names"]


def _build_two_part_combined_problem(job_problem, course_problem):
    skill_names = _validate_matching_skill_names(job_problem, course_problem)
    return {
        "entities_df": pd.concat(
            [job_problem["entities_df"], course_problem["entities_df"]],
            ignore_index=True,
        ),
        "skill_names": skill_names,
        "labels": np.vstack([job_problem["labels"], course_problem["labels"]]),
    }


def _fit_two_part_greedy_component(problem, *, dataset_variant, entity_type, max_greedy_rounds):
    similarity = problem["similarity"]
    labels = problem["labels"]
    global_threshold = _find_best_global_threshold(similarity, labels)
    initial_thresholds = np.full(labels.shape[1], global_threshold, dtype=np.float32)

    thresholds, threshold_origin = _greedy_optimize_thresholds_for_micro_f1(
        similarity=similarity,
        labels=labels,
        initial_thresholds=initial_thresholds,
        max_rounds=max_greedy_rounds,
    )

    predictions = similarity >= thresholds[np.newaxis, :]
    metrics_df, thresholds_df, predictions_df = _build_result_frames(
        problem,
        thresholds,
        predictions,
        global_threshold,
        dataset_variant=dataset_variant,
        model_variant="two_part_greedy_micro_f1",
        metric_extras={
            "entity_type": entity_type,
            "max_greedy_rounds": max_greedy_rounds,
            "num_skill_specific_thresholds": int((threshold_origin == "greedy_skill_specific").sum()),
        },
        threshold_extras={
            "entity_type": entity_type,
            "threshold_origin": threshold_origin,
        },
    )

    return {
        "entity_type": entity_type,
        "global_threshold": float(global_threshold),
        "thresholds": thresholds,
        "threshold_origin": threshold_origin,
        "predictions": predictions,
        "metrics_df": metrics_df,
        "thresholds_df": thresholds_df,
        "predictions_df": predictions_df,
    }


def _align_thresholds_for_entity_type(thresholds_df, skill_names, entity_type):
    entity_thresholds_df = thresholds_df.loc[thresholds_df["entity_type"] == entity_type].copy()
    if entity_thresholds_df.empty:
        raise ValueError(f"thresholds_df does not contain rows for entity_type={entity_type!r}")

    duplicate_skill_names = entity_thresholds_df.loc[
        entity_thresholds_df["skill_name"].duplicated(),
        "skill_name",
    ].tolist()
    if duplicate_skill_names:
        raise ValueError(
            f"thresholds_df has duplicate skill_name values for entity_type={entity_type!r}: "
            + ", ".join(map(str, duplicate_skill_names[:10]))
            + (" ..." if len(duplicate_skill_names) > 10 else "")
        )

    aligned_thresholds_df = entity_thresholds_df.set_index("skill_name").reindex(skill_names)
    missing_skill_names = aligned_thresholds_df.index[aligned_thresholds_df["threshold"].isna()].tolist()
    if missing_skill_names:
        raise ValueError(
            f"Learned threshold table is missing thresholds for entity_type={entity_type!r}: "
            + ", ".join(map(str, missing_skill_names[:10]))
            + (" ..." if len(missing_skill_names) > 10 else "")
        )

    return aligned_thresholds_df.reset_index()


def fit_global_threshold_model(problem, *, dataset_variant):
    similarity = problem["similarity"]
    labels = problem["labels"]
    global_threshold = _find_best_global_threshold(similarity, labels)
    thresholds = np.full(labels.shape[1], global_threshold, dtype=np.float32)
    predictions = similarity >= global_threshold
    return _build_result_frames(
        problem,
        thresholds,
        predictions,
        global_threshold,
        dataset_variant=dataset_variant,
        model_variant="global_threshold",
    )


def fit_common_skill_threshold_model(problem, *, dataset_variant, min_positives_for_skill_tuning=10):
    similarity = problem["similarity"]
    labels = problem["labels"]
    global_threshold = _find_best_global_threshold(similarity, labels)

    positive_support = labels.sum(axis=0).astype(int)
    thresholds = np.full(labels.shape[1], global_threshold, dtype=np.float32)
    tuning_type = np.array(["global"] * labels.shape[1], dtype=object)

    for skill_idx in range(labels.shape[1]):
        if positive_support[skill_idx] >= min_positives_for_skill_tuning:
            thresholds[skill_idx] = _find_best_threshold_for_one_skill(
                scores=similarity[:, skill_idx],
                labels=labels[:, skill_idx],
                default_threshold=global_threshold,
            )
            tuning_type[skill_idx] = "skill_specific"

    predictions = similarity >= thresholds[np.newaxis, :]
    return _build_result_frames(
        problem,
        thresholds,
        predictions,
        global_threshold,
        dataset_variant=dataset_variant,
        model_variant="common_skill_tuning",
        metric_extras={
            "min_positives_for_skill_tuning": min_positives_for_skill_tuning,
            "num_skill_specific_thresholds": int((tuning_type == "skill_specific").sum()),
        },
        threshold_extras={"tuning_type": tuning_type},
    )


def fit_greedy_threshold_model(problem, *, dataset_variant, max_greedy_rounds=3):
    similarity = problem["similarity"]
    labels = problem["labels"]
    global_threshold = _find_best_global_threshold(similarity, labels)
    initial_thresholds = np.full(labels.shape[1], global_threshold, dtype=np.float32)

    thresholds, threshold_origin = _greedy_optimize_thresholds_for_micro_f1(
        similarity=similarity,
        labels=labels,
        initial_thresholds=initial_thresholds,
        max_rounds=max_greedy_rounds,
    )

    predictions = similarity >= thresholds[np.newaxis, :]
    return _build_result_frames(
        problem,
        thresholds,
        predictions,
        global_threshold,
        dataset_variant=dataset_variant,
        model_variant="greedy_micro_f1",
        metric_extras={
            "max_greedy_rounds": max_greedy_rounds,
            "num_skill_specific_thresholds": int((threshold_origin == "greedy_skill_specific").sum()),
        },
        threshold_extras={"threshold_origin": threshold_origin},
    )


def fit_two_part_greedy_threshold_model(job_problem, course_problem, *, dataset_variant, max_greedy_rounds=3):
    skill_names = _validate_matching_skill_names(job_problem, course_problem)

    job_result = _fit_two_part_greedy_component(
        job_problem,
        dataset_variant=dataset_variant,
        entity_type="job",
        max_greedy_rounds=max_greedy_rounds,
    )
    course_result = _fit_two_part_greedy_component(
        course_problem,
        dataset_variant=dataset_variant,
        entity_type="course",
        max_greedy_rounds=max_greedy_rounds,
    )

    combined_problem = _build_two_part_combined_problem(job_problem, course_problem)
    combined_predictions = np.vstack([job_result["predictions"], course_result["predictions"]])

    overall_metrics_df, _, predictions_df = _build_result_frames(
        combined_problem,
        np.full(len(skill_names), np.nan, dtype=np.float32),
        combined_predictions,
        np.nan,
        dataset_variant=dataset_variant,
        model_variant="two_part_greedy_micro_f1",
        metric_extras={
            "job_global_threshold": job_result["global_threshold"],
            "course_global_threshold": course_result["global_threshold"],
            "max_greedy_rounds": max_greedy_rounds,
            "num_skill_specific_thresholds": int(
                (job_result["threshold_origin"] == "greedy_skill_specific").sum()
                + (course_result["threshold_origin"] == "greedy_skill_specific").sum()
            ),
        },
    )

    split_metrics_df = pd.concat(
        [job_result["metrics_df"], course_result["metrics_df"]],
        ignore_index=True,
    )
    thresholds_df = pd.concat(
        [job_result["thresholds_df"], course_result["thresholds_df"]],
        ignore_index=True,
    )

    return overall_metrics_df, split_metrics_df, thresholds_df, predictions_df


def run_all_models_for_dataset(problem, *, dataset_variant, min_positives_for_skill_tuning=10, max_greedy_rounds=3):
    return {
        "global_threshold": fit_global_threshold_model(problem, dataset_variant=dataset_variant),
        "common_skill_tuning": fit_common_skill_threshold_model(
            problem,
            dataset_variant=dataset_variant,
            min_positives_for_skill_tuning=min_positives_for_skill_tuning,
        ),
        "greedy_micro_f1": fit_greedy_threshold_model(
            problem,
            dataset_variant=dataset_variant,
            max_greedy_rounds=max_greedy_rounds,
        ),
    }


def evaluate_fixed_threshold_model(problem, *, thresholds_df, dataset_variant, model_variant, global_threshold, metric_extras=None, threshold_extras=None):
    required_columns = {"skill_name", "threshold"}
    missing_columns = required_columns.difference(thresholds_df.columns)
    if missing_columns:
        raise ValueError(
            "thresholds_df is missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    duplicate_skill_names = thresholds_df.loc[thresholds_df["skill_name"].duplicated(), "skill_name"].tolist()
    if duplicate_skill_names:
        raise ValueError(
            "thresholds_df has duplicate skill_name values: "
            + ", ".join(map(str, duplicate_skill_names[:10]))
            + (" ..." if len(duplicate_skill_names) > 10 else "")
        )

    skill_names = problem["skill_names"]
    aligned_thresholds_df = thresholds_df.set_index("skill_name").reindex(skill_names)

    missing_skill_names = aligned_thresholds_df.index[aligned_thresholds_df["threshold"].isna()].tolist()
    if missing_skill_names:
        raise ValueError(
            "Learned threshold table is missing thresholds for validation skills: "
            + ", ".join(map(str, missing_skill_names[:10]))
            + (" ..." if len(missing_skill_names) > 10 else "")
        )

    thresholds = aligned_thresholds_df["threshold"].to_numpy(dtype=np.float32)
    predictions = problem["similarity"] >= thresholds[np.newaxis, :]

    resolved_threshold_extras = dict(threshold_extras or {})
    if "threshold_origin" in aligned_thresholds_df.columns and "threshold_origin" not in resolved_threshold_extras:
        resolved_threshold_extras["threshold_origin"] = aligned_thresholds_df["threshold_origin"].fillna("global").to_numpy(dtype=object)

    return _build_result_frames(
        problem,
        thresholds,
        predictions,
        global_threshold,
        dataset_variant=dataset_variant,
        model_variant=model_variant,
        metric_extras=metric_extras,
        threshold_extras=resolved_threshold_extras or None,
    )


def evaluate_two_part_fixed_threshold_model(job_problem, course_problem, *, thresholds_df, dataset_variant, model_variant, metric_extras=None, threshold_extras=None):
    required_columns = {"entity_type", "skill_name", "threshold"}
    missing_columns = required_columns.difference(thresholds_df.columns)
    if missing_columns:
        raise ValueError(
            "thresholds_df is missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    duplicate_pairs = thresholds_df.loc[
        thresholds_df.duplicated(subset=["entity_type", "skill_name"]),
        ["entity_type", "skill_name"],
    ]
    if not duplicate_pairs.empty:
        duplicate_values = [tuple(row) for row in duplicate_pairs.head(10).itertuples(index=False, name=None)]
        raise ValueError(
            "thresholds_df has duplicate (entity_type, skill_name) values: "
            + ", ".join(map(str, duplicate_values))
            + (" ..." if len(duplicate_pairs) > 10 else "")
        )

    skill_names = _validate_matching_skill_names(job_problem, course_problem)
    resolved_metric_extras = dict(metric_extras or {})
    resolved_threshold_extras = dict(threshold_extras or {})

    job_global_threshold = float(resolved_metric_extras.get("job_global_threshold", np.nan))
    course_global_threshold = float(resolved_metric_extras.get("course_global_threshold", np.nan))

    split_results = []
    for entity_type, problem, global_threshold in [
        ("job", job_problem, job_global_threshold),
        ("course", course_problem, course_global_threshold),
    ]:
        aligned_thresholds_df = _align_thresholds_for_entity_type(thresholds_df, skill_names, entity_type)
        thresholds = aligned_thresholds_df["threshold"].to_numpy(dtype=np.float32)
        predictions = problem["similarity"] >= thresholds[np.newaxis, :]

        current_threshold_extras = dict(resolved_threshold_extras)
        current_threshold_extras["entity_type"] = entity_type
        if "threshold_origin" in aligned_thresholds_df.columns and "threshold_origin" not in current_threshold_extras:
            current_threshold_extras["threshold_origin"] = aligned_thresholds_df["threshold_origin"].fillna("global").to_numpy(dtype=object)

        current_metric_extras = dict(resolved_metric_extras)
        current_metric_extras["entity_type"] = entity_type

        metrics_df, aligned_result_thresholds_df, _ = _build_result_frames(
            problem,
            thresholds,
            predictions,
            global_threshold,
            dataset_variant=dataset_variant,
            model_variant=model_variant,
            metric_extras=current_metric_extras,
            threshold_extras=current_threshold_extras,
        )
        split_results.append((metrics_df, aligned_result_thresholds_df, predictions))

    combined_problem = _build_two_part_combined_problem(job_problem, course_problem)
    combined_predictions = np.vstack([split_results[0][2], split_results[1][2]])
    overall_metrics_df, _, predictions_df = _build_result_frames(
        combined_problem,
        np.full(len(skill_names), np.nan, dtype=np.float32),
        combined_predictions,
        np.nan,
        dataset_variant=dataset_variant,
        model_variant=model_variant,
        metric_extras=resolved_metric_extras or None,
    )

    split_metrics_df = pd.concat([result[0] for result in split_results], ignore_index=True)
    aligned_thresholds_df = pd.concat([result[1] for result in split_results], ignore_index=True)

    return overall_metrics_df, split_metrics_df, aligned_thresholds_df, predictions_df
