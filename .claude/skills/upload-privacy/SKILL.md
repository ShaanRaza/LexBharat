---
name: upload-privacy
description: Use when touching uploads, uploaded documents, the documents or document_chunks tables, the user_documents Qdrant collection, OCR, PyMuPDF, Tesseract, pre-signed S3 links, document chat, upload deletion, or anything that reads or stores a user's own file. Also use when writing any query that could return another user's data, or when adding a feature that handles client material.
---

# Upload privacy

Uploaded documents are **confidential client material**, possibly privileged. This is the
area where a bug does not embarrass the product — it ends it.

Full detail: `docs/SECURITY-AND-COMPLIANCE.md` and `docs/ARCHITECTURE.md`.

## The one rule that matters most

**Every query touching uploads goes through one shared data-access function that always
adds the `user_id` filter.** No feature writes its own Qdrant or upload query.

A missing filter leaks one lawyer's client files to another. There is a test directory for
exactly this — `tests/isolation/` — and a build check that no other module queries
`user_documents` directly. Do not work around either.

## Where upload text may and may not go

| Destination | Allowed? |
|---|---|
| Our Mumbai server, S3 (encrypted, KMS) | Yes |
| **Jev** | **Never.** In upload chats, the claim-support check and any decision touching upload text use **Gemini (paid tier)** instead |
| **Langfuse** | **Never** — masked before sending |
| **Sentry** | **Never** — scrubbed before sending |
| Voyage (embedding chunks) | Only once Voyage's **written** no-training and retention terms for upload text are in hand. Free local model (bge-m3) is the fallback |
| Gemini | Paid tier, **only the passages needed for an answer** — never whole files |

## Hard rules

- **Delete means hard delete**: the S3 object, the extracted text in PostgreSQL, **and**
  all vectors in Qdrant by `document_id` — one job, logged, with a nightly leftover check.
- `audit_log` records who opened or deleted what. **It never stores document text.**
- **No staff access by default.** Any access needs a logged reason.
- A warning about privileged material is shown **before** upload.
- Unreadable scans fail early, say so plainly, and **are not charged** to the usage meter.
- Upload chats are **never cached**.
- Every chunk keeps `page_no`, `char_start`, `char_end` — that is what lets a citation jump
  to the exact passage. Do not drop them.
- Answers label **"your document says"** separately from "Supreme Court judgments say".

## Feature state

`FEATURE_UPLOADS` is **off at launch**. It ships only after three things: the advocate's
written opinion on privilege and DPDP roles, Voyage's written terms, and the upload size
and page limits being set. **Do not turn it on to make a test pass.**

## Before you call it done

- [ ] The new query goes through the shared data-access function
- [ ] A test proves it fails closed without a `user_id`
- [ ] No upload text can reach Jev, Langfuse or Sentry on any path, including errors
- [ ] Hard delete still removes all three stores
