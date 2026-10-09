# Decisions

Two lists: **settled** (do not relitigate without a new entry here) and **open** (each with
what will settle it). From the Tech Stack's "Open decisions" and change log.

When you settle an open decision while building, move the row up, add the date and the
evidence, and note it in the commit.

---

## Settled

| # | Decision | Choice | Why |
|---|---|---|---|
| D1 | Supreme Court outcome statistics | Ship in v1, gated on the 50-judgment hand check | Disposition values are concentrated in ~10 readable outcomes (Measured) |
| D2 | Data refresh pipeline | **Not in MVP.** Ship on snapshot v2026.08 with a data-as-of date; refresh goes to the post-MVP backlog | Keeps v1 small; overrides the request to add it as a build step |
| D3 | Hindi | P1 — within 3 months of launch, P0 if the 20 interviews show strong demand | Needs a Devanagari-aware BM25 tokenizer; not a v1 blocker |
| D4 | CC BY credit text | `Data: Open India Law by Vaquill AI, CC BY 4.0` on every result, page and share card | Licence condition |
| D5 | Launch gate condition 6 | "Data-as-of date shown prominently" replaces "first data refresh complete" | Follows from D2 |
| D6 | Not-legal-advice notice | On every answer, stats page and Act page; stronger when Jev flags personal advice | BCI Rule 36 + the information/advice line |
| — | Keyword search | BM25 sparse vectors inside Qdrant | Settles the PRD's PostgreSQL-FTS vs Qdrant choice; also covers "Voyage is down" |
| — | Agent framework inside the product | **None.** Fixed pipeline | Guarantees every answer hits the verifier; cheaper, faster, debuggable |
| — | Send upload text to Jev | **Never.** Upload chats use Gemini (paid tier) for those checks | Privilege and DPDP risk; Jev runs in the US |
| — | Answer cache lifetime | 7 days | Tune from real use |
| — | Re-embed SC chunks with a header | Keep Vaquill's vectors as they are | Compare on the test questions in build step 1 |
| — | Hosting the website | Same EC2 server | Move only if the server gets busy |
| — | Supabase / Cognito migration | Stay on Firebase | Move only on the triggers in Login and payments |
| — | Phase 2 court order | Bombay, Telangana, Kerala | Archive depth: 45.0%, 45.4%, 39.9% of cases predate 2015 (Measured). Delhi next, for practical demand |
| — | OCR for scans | Tesseract only | Textract later if 20 real court scans show it is needed |
| — | Re-ranker backup | Open-source bge-reranker on the server | If it fits in 16 GB alongside everything else |
| — | Model routing (easy/hard) | **Off at launch** | Turns on only once a stronger model is chosen |
| — | Jev gate threshold | Start at 0.6 (Estimate) | Set from the 200-question test set |
| — | Voyage free allowance | Assume 200M tokens once, not monthly | Confirm with Voyage |
| — | Upload embedding model | voyage-4 first, free local model (bge-m3) as fallback | Depends on Voyage's upload terms and the legal opinion |
| — | What `DELETE /me` keeps | Payment and invoice records only | Needs counsel to confirm the retention period |

---

## Open — blocking or near-blocking

| Decision | Options | Working choice | What settles it |
|---|---|---|---|
| **Final product name** | KanoonBuddy (working) or Praman (PRD's pick) | Undecided | Trademark search with IP India |
| **Supreme Court point count and server size** | r7g.large (16 GB) or r7g.xlarge (32 GB) | r7g.large | Count points in build step 1; load-test search with quantization |
| **Court field name in the Qdrant payload** | Unknown | None | Inspect 5 Supreme Court points locally |
| **50-judgment SC pass rule** | How many must match for stats to go live | Undecided | Agree with the advocate **before** checking |
| **Upload auto-delete period** | 7, 30 or 90 days | Undecided | Advocate's legal opinion |
| **Upload size and page limits** | e.g. 25 MB and 200 pages | Undecided | OCR time on real scans; what interviewees upload |
| **Backup AI provider** | OpenRouter, Groq, or a second big vendor | Undecided | Each provider's no-training terms |
| **GST in shown prices** | Included or added | Undecided | Accountant |
| **Data-refresh method** | Run scrapers, or license a daily sync from Vaquill | Undecided (post-MVP, D2) | Vaquill's reply on price and deltas |
| **Snapshot v2026.08.1** | Upgrade (fills `source_url` on 83.3% of rows) or stay | Undecided | Build step 1, evaluated against download time |
| **AI model per plan** | Gemini Flash-Lite family, Claude, GPT, Kimi K3 | Free: Gemini 2.5 Flash-Lite; Student/Pro: Gemini 3.1 Flash-Lite | Week-1 test on 50 real questions: correctness, cost, speed |
| **Order to switch on Jev uses** | All at launch, or one at a time | Offline cleaning first, then gate and claim support, then the rest | Test results and early-access availability |
| **Which notes beyond the first set** | Grow by topic, or only where answers go wrong | Only where answers go wrong | Wrong-answer reports and test-set failures |
| **Who reviews knowledge notes** | Advocate advisor, or a paid one-off reviewer | Advocate advisor | Quote for reviewing the law maps |
| **Interface language** | Hindi-first or English-first | Open (from the PRD) | The 20 interviews |
| **Naming an advocate advisor publicly** | Counts as publicity under BCI Rule 36? | Unknown | Needs counsel |

---

## Known documentation conflict

| Doc | Launch courts |
|---|---|
| PRD p.2 | Supreme Court + `acts_india` only; Bombay, Telangana, Kerala in phase 2 |
| Website Design Doc v2 (as received) | Supreme Court + Delhi, Bombay, Madras High Courts |

**Resolved 9 Oct 2026: the PRD is correct.** The website design doc was corrected in this
repo. Delhi and Madras appear nowhere in the PRD's phase-2 list — if the website copy came
from a third source, that source is also wrong.
