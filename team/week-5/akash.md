# Akash: Week 5 (Platform), 4 h a day

**Theme: a safe place to put uploaded files.** By Saturday a user can get an upload link,
send a file straight to storage, and watch its status, and a background worker picks the
job up. Nothing is read from the file yet (that's Week 6).

Most important of all: **the one shared function for querying uploads**, which always adds
the `user_id` filter. It's built this week, before anything writes to the uploads
collection, so nothing is ever written around it.

> **Mon 9 Nov is Govardhan Puja: light day.** **Wed 11 Nov is Bhai Dooj.** If you take it
> off, **the document list (3.2) moves to Saturday** and **the feedback route (5.2) to
> Week 6**. Say so in the standup.

**Uploads stay switched off for users** (`FEATURE_UPLOADS=false`). You're building them,
not opening them.

---

## Before Day 1

- [ ] Anything from Month 1 that isn't finished (the meter, consent, masking, scrubbing)
      goes **first**. Going live in Week 8 needs all four

---

## Day 1, Mon 9 Nov (Govardhan Puja): light, about 1.5 h

### 1.1 Local file storage (1.5 h)
Real S3 comes with the server in Week 8. For laptops, add **MinIO** (it behaves like S3) to
`infra/docker-compose.yml`: pinned version, named volume, `127.0.0.1` only, a non-default
port, **ARM checked**. Write the port into `infra/README.md`.

**Branch:** `akash/minio-dev`

---

## Day 2, Tue 10 Nov: upload links

### 2.1 `adapters/storage_s3.py` (1.5 h)
One file for S3 (CLAUDE.md rule 1). It works the same against MinIO and real S3. Upload
and download links **expire in minutes**. A fake for tests.

### 2.2 `POST /api/v1/documents/uploads` (2.5 h)
- Checks the **size before** giving a link (`UPLOAD_MAX_MB`, from settings). The limit
  itself isn't decided yet; Week 6 sets it from real measurements, so use a placeholder
- Accepts **PDF and Word** only
- Creates the `documents` row and returns a link for uploading **straight to storage**
  (multi-part for big files, so a weak connection can resume)
- `POST /api/v1/documents/{id}/complete` once the browser finishes: checks the object is
  really there and the size matches, then sets status `uploaded` and queues the job. **This
  route isn't in `docs/API.md` yet; add it in the same PR**
- Behind `FEATURE_UPLOADS`: switched off means these routes say so in the standard format

**Branch:** `akash/upload-links`

---

## Day 3, Wed 11 Nov (Bhai Dooj): status and the list

### 3.1 `GET /api/v1/documents/{id}` (1.5 h)
Status (`uploaded → extracting → indexing → ready`, or `failed` with a reason), filename,
size, pages. Another user's document → **404**.

### 3.2 `GET /api/v1/documents` (1.5 h)
The user's documents, newest first, with the shared cursor paging. Add it to `docs/API.md`.

### 3.3 Audit (30 min)
An `upload` row in the audit log for every completed upload. Never the file's contents.

**Branch:** `akash/document-status`

---

## Day 4, Thu 12 Nov: the worker

### 4.1 Worker skeleton (3.5 h)
A separate `worker` service in Compose, running ARQ (background jobs on Redis):
- **Capped at 1 CPU, one job at a time**, so chat stays fast while files are processed
- Job `process_document(document_id)` moves through the statuses with **empty stages** for
  now (extract, chunk, index arrive in Week 6)
- A failed stage sets `failed` with a reason and **stops**; a crash is retried once, then
  marked failed
- The job reads the file by ID through the storage adapter. **It never logs file contents**

Tests: a job moves through every status; a failing stage leaves a clear reason.

**Branch:** `akash/worker-skeleton`

---

## Day 5, Fri 13 Nov: don't trust the file + feedback

### 5.1 Check the file itself (2 h)
Never trust the filename or the browser's word:
- Check the file's **first bytes** (its "magic number") to confirm it's really a PDF or
  Word file. Anything else → `failed: unsupported`
- Count pages before any heavy work; over `UPLOAD_MAX_PAGES` → `failed: too_long`
- Note in `docs/RISKS.md`: **a hostile PDF is an attack surface.** Shaan reviews it in Week 8

### 5.2 `POST /api/v1/feedback` (1.5 h)
Thumbs up/down plus a reason and comment on any answer the user owns (`feedback` table).
Meghna wires the buttons in Week 6.

**Branch:** `akash/upload-safety-feedback`

---

## Day 6, Sat 14 Nov: the shared uploads function

### 6.1 `core/store/uploads_access.py` (3 h)
**The one way into the `user_documents` collection** (CLAUDE.md §6). Every search,
insert and delete on uploads goes through it.
- Every function **requires** `user_id`. Called without one, it **raises**; it never falls
  back to searching everyone (that's "fail closed")
- Searches always filter on `user_id`, and on `document_id` when given
- Creates `user_documents` (from `QDRANT_UPLOADS_COLLECTION`) if it doesn't exist. The
  vector size depends on Week 6's embedding choice, so take it from settings

### 6.2 The guard test (1 h)
A test that **fails the build** if any file other than this one names the uploads
collection or calls Qdrant on it. A missing filter leaks one lawyer's client files to
another, so this can't rely on people remembering.

**Branch:** `akash/uploads-access`. **Shaan must review before merge.**

---

## Done by Saturday

- [ ] MinIO in Compose (ARM checked)
- [ ] Upload link, completion check, status, list; all in `docs/API.md`; behind the switch
- [ ] Worker: 1 CPU, one job at a time, clear failure reasons
- [ ] File type checked by its bytes; page count checked early
- [ ] Feedback route
- [ ] **Shared uploads function that fails closed, and a build-failing guard test**
