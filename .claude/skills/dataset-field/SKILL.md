---
name: dataset-field
description: Use before reading, filtering on, or displaying any field from the legal corpus - judges, petitioner, respondent, citation, disposition, outcome_label, in_force, act_status, section_number, source_url, pdf_url, case_id, case_number, court, decision_date. Also use when building a search filter, a stats page, an Act page, a judgment view, or any UI that shows data from the dataset, and when counting cases or documents.
---

# Dataset field

The corpus was audited on 6 October 2026 with DuckDB across all 75 parquet files. **Several
fields are unusable and one is actively misleading.** Full table: `docs/DATASET.md`.

A tool sold on trust cannot show wrong names. Check here before using any field.

## Never display

| Field | Fill rate | Why |
|---|---|---|
| `judges` | 32.7% | Sampled values were extraction garbage — "another", "apply for bail" |
| `petitioner` / `respondent` | 99.9% | Often counsel names or sentence fragments, not party names |

High fill rate is not quality. `petitioner` is 99.9% filled and still wrong.

## Handle with care

| Field | Rule |
|---|---|
| `act_status` | Filled for only **1,568 of 22,264 acts**. Show the in-force flag **only** where it is filled; label everything else **"in-force status not checked"** |
| `in_force` | 100% filled **as a field**, but see `act_status` above. Do not treat 100% as "we know the status" |
| `citation` | **100%** for Supreme Court, **0.0%** for all 25 High Courts. High Court answers show no citation string. Show SC strings **exactly as stored**, never retyped by the AI |
| `source_url` | **0.0% for judgments** — use `pdf_url`. 100% for legislation |
| `disposition` | 98.8% filled but **577 distinct values** — a High Court problem. The SC concentrates in ~10. Use `outcome_label` after cleaning, never raw `disposition` |
| `is_final_outcome` | Statistics count **only** rows where this is true |
| `case_id` | **Not one per case.** Rajasthan: 1,056,767 `case_id` vs 308,342 distinct `case_number`. **Never present a count of `case_id` as a count of cases, and never compete on document counts** |

## Safe to rely on

`section_number` (98.5% of legislation rows) · `pdf_url` for judgments · `record_id` ·
`court` · `decision_date` · SC `citation`.

## Coverage, when claiming breadth

v1 serves **Supreme Court + `acts_india` only**. For historical work the corpus is a
Supreme Court archive (78.0% before 2015) with a thin High Court layer — Allahabad, Andhra
Pradesh and Calcutta have **0.0%** of cases before 2015, despite the card advertising 1960
onward. **Any claim of "all 25 High Courts since 1950" would be false.**

## Always, on anything derived from the corpus

- The **data-as-of date** (from `court_coverage`, per court)
- `Data: Open India Law by Vaquill AI, CC BY 4.0`
- The not-legal-advice notice
- **No advocate names anywhere** (BCI Rule 36)
- Outcome statistics are **descriptive** — counts, never predictions or win chances

Supreme Court stats go live only after the 50-judgment hand check passes. High Court stats
wait for their own.
