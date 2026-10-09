# Knowledge notes (OKF)

Checked facts that search cannot get right on its own, as plain Markdown files in this
folder. **RAG still searches the judgments; these notes add checked background.**

The Open Knowledge Format is Google Cloud's open standard (v0.1, 12 June 2026) for giving
AI curated knowledge as linked Markdown files. Google calls it a starting point, not a
finished standard. KanoonBuddy uses it **simply as a folder of Markdown files in the
code** — no OKF tool is required.

## Why this exists

In the PRD's hands-on test, even a strong competitor said Section 377 IPC "remains active"
without noting the BNS replacement from 1 July 2024. **Old judgments do not know the law
changed**, so retrieval alone cannot fix this. A note mapping IPC sections to BNS sections
can.

## Trust rules

- **A note never counts as a citation by itself.** When an answer uses a note, it cites the
  judgment or section the note points to, and the citation verifier checks that record as
  usual.
- Notes are labelled **"background notes"** to the AI, kept apart from the retrieved
  passages (S1–S8).
- **Only notes with `status: reviewed` are used in live answers.**
- A wrong note gives wrong answers confidently, so the advocate review cannot be skipped.

## Folders

| Folder | Holds |
|---|---|
| `law-maps/` | IPC → BNS, CrPC → BNSS, Evidence Act → BSA (from 1 July 2024) |
| `leading-cases/` | Leading Supreme Court cases per topic |
| `limitation/` | Limitation periods from the Schedule to the Limitation Act |
| `coverage/` | What KanoonBuddy covers, and the coverage message |
| `terms/` | Court hierarchy and legal terms |

## First notes to build

| Note | Drafted by | Source | Checked by |
|---|---|---|---|
| IPC → BNS, CrPC → BNSS, Evidence Act → BSA maps | AI, as tables | Official correspondence tables and the new Acts in `acts_india` | Advocate |
| Limitation periods | Script | Schedule to the Limitation Act in `acts_india` | Advocate |
| Leading Supreme Court cases per topic | AI | A script extracts citation strings from each judgment's full text, matches them to the citation field, and counts the most-cited (Needs verification on 50 judgments) | Advocate |
| Disposition label meanings | Jev cleaning job | The dataset | Owner |
| Court hierarchy and legal terms | AI | Act text and general knowledge | Owner |
| What KanoonBuddy covers | Owner | The PRD | Owner |

## How notes are made and kept correct

1. A script drafts each note as Markdown. **Every fact links to the record ID it came from.**
2. A check script confirms every linked record exists and every quote matches. Failing
   drafts are fixed or dropped.
3. A person reviews: an **advocate** for law maps, leading cases and limitation periods;
   the owner for coverage rules and terms.
4. After each data refresh, the check script flags notes whose source records changed, and
   **only those** go back for review.

## File header

Every note starts with this front matter:

```yaml
---
title:
status: draft          # draft | reviewed — only `reviewed` is used in live answers
reviewed_by:
last_checked:
source_records: [ ]    # record_ids backing every fact in this note
related: [ ]           # links to related notes
---
```

## Which notes to add next

**Only where answers go wrong** — driven by wrong-answer reports and test-set failures, not
by topic coverage for its own sake.
