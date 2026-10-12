# Akash: Week 7 (Platform), 4 h a day

**Theme: uploads are safe.** By Saturday it's **proven by tests** that one user can never
reach another's documents, a deleted document is really gone from all three places, a
nightly job catches anything left behind, and a user can delete their whole account or
download a copy of their data (DPDP).

Three of these are on the "never dropped" list: **isolation tests, hard delete, and the
consent notice**. Shaan reviews the first two carefully.

> **Tue 24 Nov is Guru Nanak Jayanti.** If you take it off, **the nightly check (3.1)
> moves to Saturday morning** and **export (5.1) to Week 9**. **AWS basics (6.1) stay on
> Saturday**: Shaan's big upload starts that day and needs the bucket.

---

## Day 1, Mon 23 Nov: isolation tests

### 1.1 Two users, every path (3.5 h)
User A and user B, each with a ready document. Prove B can reach **nothing** of A's, through:

| Path | B tries |
|---|---|
| `GET /documents`, `/documents/{id}`, `/documents/{id}/pages/{n}` | A's IDs |
| `DELETE /documents/{id}` | Deleting A's document |
| `POST /conversations` with `module: document` | A's `document_id` |
| A document chat | A question that would match A's text |
| The shared uploads function directly | Called with B's `user_id` and A's `document_id` |

Every one returns **404 or nothing**, never an error that confirms A's document exists.
And the shared function **raises** when called without a `user_id` ("fails closed").

These are **must-pass before any deploy** (`docs/TESTING.md`).

**Branch:** `akash/isolation-tests`

---

## Day 2, Tue 24 Nov (Guru Nanak Jayanti): hard delete

### 2.1 `DELETE /api/v1/documents/{id}` (3 h)
One background job removes **all three**, by `document_id`:
1. The file from storage
2. The extracted text from `document_chunks`
3. Every vector from `user_documents` (through the shared function)

Then: the document row marked `deleted_at`, a `delete` row in the audit log (never text),
and the job **logs success or failure**. A failed step is retried; it never reports success
when something's left.

### 2.2 The must-pass test (1 h)
After a delete, check each of the three places directly: **nothing** with that
`document_id` remains.

**Branch:** `akash/hard-delete`

---

## Day 3, Wed 25 Nov: the nightly leftover check

### 3.1 The nightly job (2.5 h)
An ARQ scheduled job: find any file, text or vector whose document is deleted or doesn't
exist, delete it, and **raise an alert** (it should never find anything; if it does,
something's wrong). Test it by planting a leftover.

### 3.2 Auto-delete after a period (1 h)
`docs/RETENTION.md`: uploads are deleted automatically after a fixed period, **which needs
counsel**. Build it on a setting (`UPLOAD_RETENTION_DAYS`); **empty means off**. Don't pick
a number. Add the setting to `.env.example` and `docs/ENVIRONMENT.md`.

**Branch:** `akash/leftover-check`

---

## Day 4, Thu 26 Nov: delete my account

### 4.1 `DELETE /api/v1/me` (3.5 h)
Removes the account and its data (DPDP):
- Every document, **through the hard delete job**
- Conversations, messages, sources, feedback, usage
- The Firebase user (through the Firebase adapter)
- What's **kept** is a short written list in the code, pending counsel (`docs/RETENTION.md`):
  for now the consent records and audit-log rows, with no document text
- Payments don't exist yet (January), so there's nothing to cancel

Test: after deletion, nothing belonging to the user is reachable, and signing in again
creates a **new, empty** account.

**Branch:** `akash/delete-account`

---

## Day 5, Fri 27 Nov: export my data

### 5.1 `GET /api/v1/me/export` (3 h)
A copy of the user's account data, chats (with sources) and **upload list** (names, dates,
pages, not the files) as one download. An `export` row in the audit log. It may take a
while, so build it as a background job with a download link that **expires in minutes**.

**Branch:** `akash/export`

---

## Day 6, Sat 28 Nov: AWS basics

### 6.1 The account, safely (3 h)
Before anything runs in AWS:
- [ ] The root account has **MFA**, and nobody uses it day to day
- [ ] A **billing alarm** (an email if the month's cost passes an agreed amount)
- [ ] Your own IAM user with MFA; least privilege
- [ ] Region **Mumbai (ap-south-1)** for everything
- [ ] The **backups bucket**: private, encrypted with a KMS key, public access blocked. Give
      Shaan upload access **today**: his search collection upload starts this afternoon
- [ ] Write every step into `infra/aws/README.md`, so it can be done again without
      guessing. No undocumented clicking

**Branch:** `akash/aws-basics`

---

## Done by Saturday

- [ ] Isolation tests on every upload path; the shared function fails closed
- [ ] Hard delete from all three places, logged, with the must-pass test
- [ ] Nightly leftover check (tested with a planted leftover); auto-delete on a setting, off
- [ ] Delete account; export my data
- [ ] AWS account secured; backups bucket ready for Shaan's upload
