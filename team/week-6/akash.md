# Akash: Week 6 (Platform), 4 h a day

**Theme: the worker reads files.** By Saturday a text PDF, a Word file and a scanned PDF
all become searchable passages, unreadable scans fail early **without being charged**, and
a user can start a chat about a ready document.

You also measure **how slow OCR really is** on one CPU. The upload limits are set from that
number, not guessed.

**Test files: public documents only.** Old Supreme Court judgments from the dataset's
`pdf_url` links include real scans. **Never a client document.**

---

## Before Day 1

- [ ] Week 5 leftovers first, especially the shared uploads function

---

## Day 1, Mon 16 Nov: text PDFs

### 1.1 Extract (3 h)
`workers/extract.py`, using **PyMuPDF**:
- Text **per page**, with page numbers
- **Is there a text layer?** Sample a few pages; little or no text means it's a scan and
  goes to OCR (Day 3)
- Keep the text exactly as extracted. Shaan's passage positions depend on it
- **Never log the text**

Tests on a public text judgment PDF and a public scan.

**Branch:** `akash/pdf-text`

---

## Day 2, Tue 17 Nov: Word files and page text

### 2.1 Word files (1.5 h)
**python-docx.** Word files have **no fixed pages**: the page count depends on the screen
and the printer. Propose a rule to Shaan (for example, "a page = every N paragraphs" or
"page_no = section heading number") and record it with `/decision`. It decides what
"page 4" means in a Word citation.

### 2.2 `GET /api/v1/documents/{id}/pages/{n}` (2 h)
The extracted text of one page, so Meghna's viewer can show it and highlight a passage by
its character positions. Owner only; another user's document → 404. Add it to
`docs/API.md`.

**Branch:** `akash/word-and-pages`

---

## Day 3, Wed 18 Nov: OCR for scans

### 3.1 Tesseract (3 h)
In the worker's image, **ARM build checked**:
- English **and Hindi** language packs
- Page by page, with a **confidence score** per page
- Below the quality threshold → `failed: unreadable`, and **the usage meter isn't
  charged**
- The worker stays at **1 CPU and one job at a time**, so chat stays fast

**Branch:** `akash/ocr`

---

## Day 4, Thu 19 Nov: measure it

### 4.1 Twenty real scans (2.5 h)
docs/TESTING.md lists "20 real court scans" as the check that sets the limits. Use 20 old
Supreme Court judgment PDFs that are scans (from `pdf_url`), of different lengths.

For each, record in `infra/notes/ocr-week6.md`: pages, seconds per page, total time,
average confidence, and **your judgement of readability** for 3 pages.

### 4.2 Propose the limits (1 h)
With the Week 6 numbers, propose to Shaan:
- `UPLOAD_MAX_PAGES` and `UPLOAD_MAX_MB`, so a scan under the limit is ready in **under 5
  minutes** (CLAUDE.md §10) and a text PDF in **under 60 seconds**
- The OCR confidence threshold for "unreadable"

Shaan decides; record with `/decision`, labelled **Measured**.

**Branch:** `akash/ocr-measure`

---

## Day 5, Fri 20 Nov: the worker, end to end

### 5.1 Wire it (3 h)
`process_document`: extract (PDF, Word or OCR) → **Shaan's** `chunk` → **Shaan's**
`index_document` → `ready`. Each stage updates the status Meghna's screen shows.
- Time each stage; write the times to the document's record (no text)
- A failure at any stage leaves **nothing half-indexed** (Shaan's indexing is all or
  nothing; check it)

### 5.2 Timing check (1 h)
A 30-page text PDF and a 30-page scan through the whole worker. Do they meet 60 seconds
and 5 minutes? Write the numbers in the PR.

**Branch:** `akash/worker-wired`

---

## Day 6, Sat 21 Nov: chatting about a document

### 6.1 Document conversations (3 h)
- `POST /conversations` with `module: document` and a `document_id`: the document must
  belong to the user **and** be `ready`
- The streaming route passes the document to `core.pipeline.run(...)`; Shaan's pipeline does
  the rest
- **Document chats are never cached** (the cache refuses them, and a test checks the route
  never asks)
- The usage meter counts document answers like any other

### 6.2 Standup (15 min)

**Branch:** `akash/document-conversations`

---

## Done by Saturday

- [ ] Text PDFs, Word files and scans (English and Hindi) extracted per page
- [ ] Word "page" rule decided and recorded
- [ ] Page text route for the viewer, in `docs/API.md`
- [ ] Unreadable scans fail early and aren't charged
- [ ] **20 real scans measured; upload limits and OCR threshold decided from them**
- [ ] Worker runs end to end; timings recorded against 60 s and 5 min
- [ ] Document conversations, never cached
