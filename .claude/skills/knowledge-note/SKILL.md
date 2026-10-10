---
name: knowledge-note
description: Use when drafting, editing, reviewing or checking an OKF knowledge note in the knowledge folder - law maps such as IPC to BNS, CrPC to BNSS or Evidence Act to BSA, leading cases, limitation periods, coverage rules, court hierarchy or legal terms. Also use when an answer needs background the search cannot retrieve, or when deciding whether a fact belongs in a note or in the corpus.
---

# Knowledge note

A few hundred reviewed Markdown files carrying facts that search cannot get right on its
own — above all **which old law maps to which new law**. Old judgments do not know the law
changed on 1 July 2024, so retrieval alone cannot fix this.

Full detail: `knowledge/index.md`.

## The trust rule

**A note never counts as a citation by itself.** When an answer uses a note, it cites the
judgment or section the note points to, and the verifier checks that record as usual. Notes
are labelled **"background notes"** to the AI, kept apart from the retrieved passages.

**Only notes with `status: reviewed` are used in live answers.** A wrong note gives wrong
answers confidently, so the advocate review cannot be skipped.

## Front matter — required on every note

```yaml
---
title:
status: draft          # draft | reviewed — only `reviewed` reaches live answers
reviewed_by:
last_checked:
source_records: [ ]    # record_ids backing every fact in this note
related: [ ]           # links to related notes
---
```

**Every fact links to the record ID it came from.** A note with an empty `source_records`
is not a note, it is a guess.

## Folders

`law-maps/` · `leading-cases/` · `limitation/` · `coverage/` · `terms/`

## Who reviews what

| Content | Reviewer |
|---|---|
| Law maps, leading cases, limitation periods | **Advocate advisor** |
| Coverage rules, terms, disposition labels | Founder |

Never set `status: reviewed` yourself. Drafting is your job; review is theirs.

## Process

1. Draft as Markdown, every fact linked to its record ID.
2. Run the check script: every linked record exists, every quote matches. Failing drafts are
   fixed or dropped.
3. Send for review.
4. After each data refresh, the check script flags notes whose source records changed —
   **only those** go back for review.

## Which notes to add

**Only where answers go wrong** — driven by wrong-answer reports and test-set failures, not
by topic coverage for its own sake.
