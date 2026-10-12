# Shaan: Week 6 (Data + Core + Lead), 4 h a day

**Theme: uploads work.** By Saturday a lawyer can ask about their own document and get an
answer that keeps **"Your document says"** apart from **"Supreme Court judgments say"**,
with page numbers, verified the same way as any other answer.

You own the parts that decide answer quality: **how a document is cut into passages, how
they're embedded and found, and how the answer uses them.** Akash's worker calls your
functions.

Pipeline steps touched: **5 (search)** for uploads, **8 (answer)** and **9 (verify)** for
document citations. Steps 3 and 4 learn two new rules: **upload text never goes to Jev, and
document chats are never cached.**

Follow the design you wrote on Sat 14 Nov (`docs/ARCHITECTURE.md`, Uploads).

---

## Before Day 1

- [ ] Ranveer's Voyage status (Fri 13 Nov)
- [ ] Akash's shared uploads function merged (Week 5). **Everything this week goes through
      it**

---

## Day 1, Mon 16 Nov: the embedding choice + cutting documents into passages

### 1.1 Decide the upload embedding model (45 min)
`docs/DECISIONS.md`: **voyage-4 first, bge-m3 (free, on our own server) as the fallback.**

| If | Then |
|---|---|
| Voyage's written terms arrived **and** say no training, short retention, an acceptable location | voyage-4 |
| No terms, unacceptable terms, or the legal opinion wants client text kept in India | **bge-m3** behind the same adapter |

Record it with `/decision`. bge-m3 needs about 2 GB of memory (Estimate) on a 16 GB server
already holding Qdrant, so **note that in `docs/RISKS.md`** if you choose it.

### 1.2 `core/uploads/chunk.py` (2.5 h)
Cuts extracted text into passages that **keep their page number and exact character
positions** (`page_no`, `char_start`, `char_end`). Those positions are what let a citation
jump to the exact spot.
- Never cut across a page boundary
- Passage size close to the judgments' chunks, so answers behave the same
- **The key test:** for every passage, `page_text[char_start:char_end] == passage text`,
  exactly. Run it on text PDFs, OCR output and Word text

**Branch:** `shaan/upload-chunks`

---

## Day 2, Tue 17 Nov: indexing

### 2.1 `core/uploads/index.py` (3 h)
`index_document(user_id, document_id, passages)`:
- Embeds the passages with the chosen model, through `adapters/embeddings.py` (one adapter;
  the model comes from config)
- Writes vectors **only through the shared uploads function**, each carrying `user_id`,
  `document_id`, `page_no`, `char_start`, `char_end`
- Writes the passage rows to `document_chunks` through `core/store/`
- All or nothing: if anything fails, nothing half-written is left behind

Akash's worker calls this on Friday, so **merge it by Wednesday**.

**Branch:** `shaan/upload-index`

---

## Day 3, Wed 18 Nov: finding passages in a document

### 3.1 Upload search (3 h)
- Searches the user's document **through the shared function** (it adds `user_id` and
  `document_id` itself)
- Top passages are labelled **D1 to D8**, separate from the judgments' S1 to S8
- Questions that also need the law ("does this agreement's notice clause meet Section 138?")
  search **both**: the document (D-labels) and the judgments (S-labels)

Tests: a user can **never** get another user's passage, even by passing their
`document_id`. That must come back empty, not an error that confirms it exists.

**Branch:** `shaan/upload-search`

---

## Day 4, Thu 19 Nov: answering from a document

### 4.1 The document answer (2.5 h)
`core/prompts/answer_document.md`, and the answer step learning D-labels:
- **"Your document says"** (D-labels, with page numbers) kept apart from **"Supreme Court
  judgments say"** (S-labels)
- Never mixes them in one sentence's citation

### 4.2 Verifying document citations (1.5 h)
| Check | For a document citation |
|---|---|
| 1. Retrieved | The D-label was given to the model **this turn** |
| 2. Exists | The passage exists **for this user** (through the shared function) |
| 3. Quotes match | Quoted words appear in the passage exactly |
| 4. Supported | Through **Gemini, never Jev**. The adapter's guard enforces it; a test proves it |

**Branch:** `shaan/upload-answers`

---

## Day 5, Fri 20 Nov: where upload text can and can't go

### 5.1 Privacy tests (3 h)
Upload text is a lawyer's client material. Prove, with tests that run in CI:
- [ ] **Never sent to Jev**, at any step (scope, filters, safety, gate, claim)
- [ ] **Never cached**: a document chat answer never enters the answer cache
- [ ] **Masked in Langfuse**: a trace from a document chat holds `[UPLOAD_TEXT]`, never the
      words
- [ ] **Never in Sentry**: an error during a document chat carries no passage text
- [ ] The citations event for a document citation carries `document_id`, `page_no`,
      `char_start` and `char_end`, so Meghna's viewer can highlight it

### 5.2 Help Akash wire the worker (1 h)

**Branch:** `shaan/upload-privacy-tests`

---

## Day 6, Sat 21 Nov: try it for real

### 6.1 Ten document questions (2.5 h)
Three **public** documents only: an old Supreme Court judgment PDF that's a **scan**
(from `pdf_url`), a text judgment PDF, and a sample agreement written for testing. Ask ten
questions across them, some needing the law too. Record in
`evals/runs/week6-documents.md`: right / partly / wrong; whether page jumps land correctly.

### 6.2 Wrap (1 h)
"Done means" in [README.md](README.md); adjust Week 7 issues; open **Standup: Week 7**.

---

## Pull requests to expect

| Day | From Akash | From Meghna | Yours |
|---|---|---|---|
| 1 | `akash/pdf-text` | `meghna/document-viewer` | `shaan/upload-chunks` |
| 2 | `akash/word-and-pages` | `meghna/document-chat` | `shaan/upload-index` |
| 3 | `akash/ocr` | `meghna/document-citations` | `shaan/upload-search` |
| 4 | `akash/ocr-measure` | `meghna/feedback` | `shaan/upload-answers` |
| 5 | `akash/worker-wired` | `meghna/uploads-live` | `shaan/upload-privacy-tests` |
| 6 | `akash/document-conversations` | `meghna/document-polish` | |

## Done by Saturday

- [ ] Upload embedding model decided and recorded
- [ ] Passages keep exact page and character positions (tested on all three file kinds)
- [ ] Indexing through the shared function only; all or nothing
- [ ] Upload search with D-labels; another user's document returns nothing
- [ ] Answers keep "your document says" apart; check 4 through Gemini only
- [ ] Privacy tests for Jev, the cache, Langfuse and Sentry, in CI
- [ ] Ten document questions written up
