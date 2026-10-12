# Week 6 in detail: Mon 16 Nov to Sat 21 Nov 2026

**Theme: uploads work.** Month overview: [`../MONTH-2.md`](../MONTH-2.md).

| Person | File | Hours |
|---|---|---|
| Shaan | [shaan.md](shaan.md) | 4 h a day |
| Akash | [akash.md](akash.md) | 4 h a day |
| Meghna | [meghna.md](meghna.md) | 3 h a day |
| Ranveer | [ranveer.md](ranveer.md) | When available, with deadlines |

**Week goal:** text PDFs, Word files and scans become searchable passages that keep their
exact page and position. A lawyer asks about their own document and gets **"Your document
says"** kept apart from **"Supreme Court judgments say"**, verified, with citations that jump
to the passage. OCR speed is measured, and the upload limits are set from it.

**Pipeline steps touched:** 5 (search) for uploads, 8 (answer), 9 (verify), and the rules
in 3 and 4 that keep upload text away from Jev and out of the cache.

**Tracking:** every task is a GitHub issue in the
[Week 6 milestone](https://github.com/ShaanRaza/LexBharat/milestone/6). **Status lives in the issues.**

| Person | Issues |
|---|---|
| Shaan | #113 embedding choice + passages · #114 indexing · #115 upload search · #116 document answers · #117 privacy tests · #118 ten questions + wrap |
| Akash | #119 text PDFs · #120 Word + page route · #121 OCR · #122 measure scans · #123 worker end to end · #124 document chats |
| Meghna | #125 viewer · #126 document chat · #127 jump + highlight · #128 feedback · #129 uploads live · #130 polish |
| Ranveer | #131 beta recruitment · #132 sign-off + checks · #133 domain |

> **Written ahead of time.** Adjusted on Sat 14 Nov to match what really got done.

**Test files: public documents only.** Old Supreme Court judgment PDFs from `pdf_url`
(many are scans) and agreements written for testing. **Never a real client document.**

---

## Who waits on whom

| Who is waiting | For | From | Needed by |
|---|---|---|---|
| Shaan, Day 1 | Voyage's status | Ranveer | **Mon 16 Nov** |
| Akash, Day 5 | `chunk` and `index_document` | Shaan | **End of Day 3** |
| Shaan, Day 1 | The shared uploads function (Week 5) | Akash | Already merged |
| Meghna, Day 1 | The page text route | Akash | Day 2 (she mocks it until then) |
| Meghna, Days 2 and 3 | What a document citation looks like in the citations event | Shaan (Week 5 design) | Day 1 |
| Meghna, Day 5 | The worker wired end to end | Akash | Day 5 |
| Akash, Day 4 | Shaan's call on the upload limits | Shaan | Day 4 |
| Akash, Day 2 | Shaan's call on Word "pages" | Shaan | Day 2 |

## Decisions this week (Shaan, recorded with `/decision`)

| Decision | Day |
|---|---|
| Upload embeddings: **voyage-4 or bge-m3** | Day 1 |
| What a "page" is in a Word file | Day 2 |
| `UPLOAD_MAX_PAGES`, `UPLOAD_MAX_MB` and the OCR threshold, **from 20 measured scans** | Day 4 |
| The server's domain (with Ranveer) | Day 5 |

## The privacy tests (must stay green from now on)

Upload text: **never** to Jev, **never** cached, **masked** in Langfuse, **absent** from
Sentry. And a user can never reach another user's passage, even with its `document_id`.

## Done means, by Saturday 21 Nov

- [ ] All three file kinds extracted per page; unreadable scans fail early, uncharged
- [ ] Passages keep exact positions (`page_text[start:end]` equals the passage, tested)
- [ ] Indexing only through the shared function; all or nothing
- [ ] Document answers split "your document says" / "Supreme Court judgments say"; check 4
      through Gemini only
- [ ] Privacy tests green in CI
- [ ] 20 scans measured; limits and threshold decided
- [ ] Viewer, document chat, jump-and-highlight, feedback buttons, all on real uploads
- [ ] Beta recruitment started; 200-question sign-off in; domain agreed
- [ ] Week 7 issues adjusted; **Standup: Week 7** opened
