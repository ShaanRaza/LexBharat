# Week 1: Tue 13 Oct to Sat 17 Oct 2026

**Goal:** everyone is building from Day 1, in parallel. Search data ready, API skeleton
running, the first screens up on fake data, and Ranveer's legal requests sent. Uploads are
in the MVP, and the legal sign-off for them takes the longest, so it starts **this week**.

Hours: Shaan 4 h · Akash 4 h · Meghna 3 h a day. Ranveer as available.

## Before Day 1

- [ ] **Akash:** accept the GitHub invite (sent to `mrharit`).
- [ ] **Ranveer:** make a GitHub account and send Shaan the username.
- [ ] **Everyone:** clone the repo, open it in VS Code, read [`README.md`](README.md) and
      [`../CLAUDE.md`](../CLAUDE.md) §1, §5 and §6.

## Day by day: Shaan, Akash, Meghna

| | **Shaan: Data + Core (4 h)** | **Akash: Platform (4 h)** | **Meghna: Web (3 h)** |
|---|---|---|---|
| **Day 1** Tue 13 | 30-min kickoff call with all four. Count the Supreme Court records in the local Qdrant; find the court field name. Start exporting the **practice dataset** | Python setup: `pyproject.toml`, ruff, pytest. One settings module that reads `.env`. CI's Python check switches on | Next.js + TypeScript + Tailwind in `web/`. Colours and the Plus Jakarta Sans font from the design doc, as tokens. CI's web check switches on |
| **Day 2** Wed 14 | **Share the practice dataset**: about 2,000 SC passages + 500 Act sections with their vectors, under 5 MB in `tests/fixtures/`. Apply for **Jev early access** | Docker Compose: PostgreSQL 16, Redis and Qdrant on a private network. **Confirm every image has an ARM build.** Alembic set up | App shell: header, navigation, phone-first layout. A strings file with all the wording from [`../docs/UX-COPY.md`](../docs/UX-COPY.md) |
| **Day 3** Thu 15 | Start building the search collection: meaning vectors from the existing collections, plus keyword (BM25) vectors. Long job: start it, let it run | API skeleton: `/api/v1/healthz`, the one error format, a request ID on every response, OpenAPI published. Load the practice dataset into PostgreSQL and Qdrant | **Chat screen on a fake stream** that follows [`../docs/API.md`](../docs/API.md): text streams in, then **one** citations event, with a tick or warning **per citation**, the data-as-of date, the CC BY credit and the notice |
| **Day 4** Fri 16 | Finish the collection (quantization on). **Check 20 searches by hand.** Reconcile the chunk-gap counts | Migrations for the core tables: `users`, `consents`, `conversations`, `messages`, `message_sources`, `invented_citation_log`, `documents`, `document_chunks`, `audit_log`, `usage_daily`. **Shaan reviews before merge** | Every failure screen: not found, keyword results only, sources without an answer, out of scope, and the stronger notice for personal-advice questions |
| **Day 5** Sat 17 | Adapters with test fakes: embeddings, re-rank, AI models via LiteLLM. Start the verifier's three free checks, with tests. Merge the week. **Write Week 2** | Act section route (in-force rule) and judgment route (paragraph anchors), on the practice data, with tests | Judgment view (text first, paragraph anchors, PDF only on tap with its size) and the Act section page, on Akash's routes, or on fixtures if those aren't merged yet |
| **Every day** | 30 min reviewing and merging pull requests. Standup by 10 PM | Standup by 10 PM | Standup by 10 PM |

## Ranveer this week

In order of urgency:

1. **Advocate: commission the written legal opinion.** Ask for a quote now. It must cover
   privilege, the DPDP roles for uploaded client documents, and the information-versus-advice
   line. **Uploads can't be switched on for lawyers' real documents without it.** It's the
   longest wait in the whole plan.
2. **Voyage: ask for written terms** for uploaded text (no training, how long it's kept,
   where it's processed). Also needed before uploads go to real users.
3. **Vaquill: send the three questions** in [`../docs/DATASET.md`](../docs/DATASET.md)
   (licence for caching, refresh pricing, judgments endpoint).
4. **Interviews:** write the script from the assumptions table in
   [`../docs/METRICS.md`](../docs/METRICS.md). List 20 people: 8 district-court advocates,
   6 High Court advocates, 6 law students. Book 5; do the first 2 or 3. Anonymised notes only.
5. Start a list of **real legal questions** people ask in interviews. They become 100 of the
   200 test questions.

## Done means, by Saturday 17 Oct

- [ ] Practice dataset shared; search collection built; 20 searches checked by hand
- [ ] `docker compose up` starts PostgreSQL, Redis and Qdrant; CI Python and web checks green
- [ ] API returns a health check, an Act section and a judgment, with request IDs
- [ ] Core tables exist as migrations, reviewed by Shaan
- [ ] Chat screen, failure screens, judgment and Act pages visible on fake data
- [ ] Legal opinion and Voyage terms **requested**; Vaquill emailed; 5 interviews booked

## Who waits on whom

| Waiting | On | By |
|---|---|---|
| Akash, Day 3 (load practice data) | Shaan's practice dataset | Day 2 |
| Shaan, Day 5 (verifier tests) | Akash's pytest setup | Day 1 |
| Meghna, Day 5 (real judgment page) | Akash's routes | Day 5 (or she uses fixtures) |
| **Uploads for real lawyers, Week 8** | **Ranveer's legal opinion and Voyage terms** | **Requested this week** |
