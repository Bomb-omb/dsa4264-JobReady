# Revised SkillsFuture-Centered Hybrid Plan
adapted from methodology of https://link.springer.com/chapter/10.1007/978-981-96-8197-6_24
## Summary
- Use `data/raw/jobsandskills-skillsfuture-unique-skills-list.xlsx` as the primary v1 SkillsFuture taxonomy source.
- Whatever new skills that we add in while doing manual labelling will be added on to the taxonomy?
- Keep the 3-stage pipeline shape from the paper, but implement it with OpenAI-hosted components:
  - fine-tuned structured-output span extraction,
  - embedding-based semantic mapping,
  - fine-tuned or reinforcement-fine-tuned reranking.
- Assume CPU-only local orchestration and caching; no local GPU path is required.

## Key Changes
- Ingest the workbook and validate both sheets:
  - `Legend` is used only to confirm intended field meanings.
  - `Unique Skills List` is the authoritative data sheet for v1.
- Clean the taxonomy into a canonical artifact with these fields:
  - `skill_id`
  - `skill_title`
  - `skill_description`
  - `skill_type`
  - `is_emerging_skill`
  - `is_casl_skill`
  - `normalized_title`
  - `source_file`
  - `source_row_number`
- Apply these cleaning rules:
  - Rename `parent_skill_title` -> `skill_title`
  - Rename `parent_skill_description` -> `skill_description`
  - Normalize `skill_type` to lowercase enum values
  - Convert `Emerging Skills` and `CASL Skills` from string booleans to actual booleans
  - Strip whitespace, normalize Unicode punctuation, and preserve original casing for display
  - Generate `skill_id` deterministically from normalized title plus description hash
- Do not add automatic alias generation in baseline v1.
  - Use only `skill_title`, `normalized_title`, and `skill_description` for retrieval.
  - Defer alias expansion to a later pass driven by unmapped spans.
- Stage 1 extraction:
  - Fine-tune an OpenAI model to emit structured JSON spans from course/job text.
  - Target schema: `[{span_text, start_char, end_char, label}]`
  - Labels are limited to `skill` and `knowledge`
  - Chunk long documents before inference and preserve document-level offsets
- Stage 2 semantic mapping:
  - Embed cleaned taxonomy entries as `skill_title + ": " + skill_description`
  - Embed extracted spans with minimal surrounding context
  - Retrieve top-10 candidate skills per extracted span
  - Tune the acceptance threshold on validation data with precision as the primary objective and F1 as the tie-breaker
- Stage 3 reranking:
  - Fine-tune or reinforcement-fine-tune an OpenAI model on `(document context, extracted span, top-k candidate skills)` to return ranked candidate IDs
  - Use reranking only on the top semantic candidates, not the full taxonomy
  - Keep both pre-rerank embedding scores and post-rerank ordering for auditability
- Scope v1 taxonomy to this workbook only.
  - Do not block on a separate SkillsFuture tools/applications dataset.
  - If that dataset appears later, append it as a second candidate source without redesigning the pipeline.

## Outputs
- `skillsfuture_taxonomy_clean`
  - cleaned canonical skill table derived from the workbook
- `span_predictions`
  - extracted spans with offsets and extraction confidence
- `semantic_candidates`
  - top-k taxonomy matches with embedding similarity scores
- `rerank_predictions`
  - final candidate ordering and kept/rejected flag
- `final_skill_mappings`
  - normalized final skill assignments per document
- `run_report`
  - extraction metrics, mapping metrics, reranking lift, API cost, latency, and cache hit rate

## Test Plan
- Taxonomy ingestion test:
  - confirm `2201` rows load, titles remain unique, and no cleaned row loses title or description
- Schema correction test:
  - verify the renamed `skill_title` and `skill_description` fields reflect the actual workbook content, not the misleading exported headers
- Extraction test:
  - structured outputs validate against schema and offsets align to source text
- Mapping test:
  - known lexical variants map to the right SkillsFuture skill using title plus description retrieval
- Reranking test:
  - reranking improves `Precision@5` and `Precision@10` over embedding-only retrieval
- End-to-end test:
  - run separately on course and job corpora and report precision, recall, and F1 for final normalized skills
- Operational test:
  - repeat runs reuse cached API outputs and reduce cost materially

## Assumptions
- This workbook is the authoritative v1 SkillsFuture skill list.
- The `parent_` column names are treated as an export artifact, not as true parent-level hierarchy fields.
- Stable IDs do not exist in the source file, so synthetic deterministic IDs are acceptable for v1.
- No local GPU is available, so model training and inference should rely on OpenAI-hosted services plus local caching.
- This is a methodology-shaped implementation, not a strict paper reproduction, because extraction and reranking are OpenAI fine-tuned approximations rather than local BERT and cross-encoder models.
