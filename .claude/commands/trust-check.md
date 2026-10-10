---
description: Audit the working tree against the trust-promise rules — verifier integrity, user isolation, vendor boundaries, secrets. Reports findings; does not fix them.
argument-hint: "[optional path to narrow the audit]"
---

# /trust-check

Audit this repo against the rules that the product's trust promise depends on.
Scope: **$ARGUMENTS** (whole repo if empty).

Read `docs/TESTING.md` for the full must-pass list first. Then check each of the following
**against the actual code**, not against what the docs claim. Report what you find; do not
fix anything unless asked.

## 1. Verifier integrity

- Are all four checks present, and are checks 1–3 free of any dependency on Jev?
- Is there a path where a citation reaches the user without passing all four?
- Does anything citation-shaped stream before the single post-verification `citations` event?
- Does every failure write to `invented_citation_log` with one of the four reasons?
- Does the AI ever retype or reformat a stored citation string?

## 2. User isolation

- Does **every** query against `user_documents` go through the one shared, `user_id`-filtered
  data-access function? Grep for direct uses of the uploads collection.
- Is there any path where a missing filter fails open rather than closed?

## 3. Vendor boundaries

- Does exactly one file in `adapters/` import each vendor library? Grep for imports outside
  `adapters/`.
- Can upload text reach **Jev, Langfuse or Sentry** on any path, including error handlers?
- Is any model configured that is not on no-training terms, or any Gemini free tier?

## 4. Config, not code

- Any hard-coded model name, price, plan limit, threshold, product name or collection name?
- Is `PRODUCT_NAME` read from config everywhere it appears?

## 5. Data display

- Is `judges`, `petitioner` or `respondent` displayed anywhere?
- Is an in-force flag shown where `act_status` is empty, without the
  "in-force status not checked" label?
- Is the data-as-of date, the CC BY credit and the not-legal-advice notice present on every
  answer, stats page and Act page?

## 6. Secrets

- Is `.env` tracked? Is any key, token or credential literal in the diff or the tree?

## Output

A short table: **check · pass/fail/not-yet-built · evidence (file:line)**. Say "not yet
built" plainly where the code does not exist — do not report a pass for absent code.
