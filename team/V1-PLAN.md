# V1 plan: MVP before January

**Version 2, written 12 Oct 2026.** It replaces the 16-week version. Re-plan every Saturday,
and properly at the **end of Week 3**, when there are real speed numbers.

**Target:** the MVP is finished by **Sat 26 Dec 2026**. The private beta with real advocates
and law students starts **Mon 4 Jan 2027**.

---

## 1. What changed, and why it now fits

| Change | Effect |
|---|---|
| **Ranveer takes all the lawyer-facing work**: interviews, the advocate, counsel, Vaquill, beta users | Frees about 100 hours of builder time |
| **Uploads are in the MVP** | Adds about 85 hours. Its legal sign-off starts in Week 1, because it's the slowest thing in the plan |
| **Things a free beta doesn't need move to January** (list below) | Removes about 150 hours |
| **Builders work Mon to Sat; Akash goes to 4 h a day** | Capacity rises from 50 to **66 hours a week** |

### What's in the MVP

- Research chat with **verified citations**: a tick or warning per citation
- Act and section lookup; judgment view
- **Upload-and-chat**: PDFs, Word files and scans, with the hard delete
- Sign-in, consent notice, monthly usage limits, account deletion and export (DPDP)
- Every failure screen; the data-as-of date, CC BY credit and not-legal-advice notice everywhere
- Live on the AWS server in Mumbai
- The 200-question test set and the invented-citation log
- The IPC → BNS, CrPC → BNSS and Evidence Act → BSA law maps, reviewed by the advocate

### Moved to January, during the beta

| Moved | Why it's safe to wait |
|---|---|
| Payments (Razorpay) | The beta is free |
| Chambers team accounts | Beta users are individuals |
| Public statistics pages, share cards, sitemap | Marketing features, not needed for lawyers to review the product |
| Outcome-label cleaning + the 50-judgment hand check | Only the statistics need them |
| Marketing site | A simple landing page is enough for a private beta |
| Limitation and leading-case notes | The law maps are the notes that matter most; the rest follow |
| Snapshot v2026.08.1 and the re-embedding experiment | Optional improvements; the current data works |

Each of these is **Shaan's call**. Any of them can come back into the MVP, at a cost in time.

---

## 2. The arithmetic

| Work | Hours (est.) | Lane |
|---|---|---|
| Data: search collection, loading cases and Acts | ~40 | Shaan |
| The answer pipeline and the verifier | ~110 | Shaan |
| Measuring: 50 real questions, two full 200-question runs, fixes | ~40 | Shaan |
| Knowledge-notes system + law maps | ~25 | Shaan + Meghna |
| API, database, sign-in, usage meter, consent, deletion and export | ~120 | Akash |
| AWS server, backups, deploys, the rebuild rehearsal | ~40 | Akash |
| Upload backend (storage, OCR, isolation, hard delete) + upload answering | ~85 | Akash + Shaan |
| Every screen, including uploads; phone pass; bug bashes | ~150 | Meghna |
| Security reviews and hardening | ~30 | Shaan + Akash |
| Reviewing pull requests, coordination | ~45 | Mostly Shaan |
| **Total** | **~600 to 700** | |

**Capacity:** Week 1 is 5 days × 11 h = 55 h. Weeks 2 to 10 are 9 × 66 h = 594 h. Week 11 is
Christmas, so about half: ~33 h. **Total ≈ 680 hours.**

**It fits, with very little room.** Shaan's and Akash's lanes are both near 100%. Meghna has a
small margin. **Week 11 is the only buffer.**

### If "four weeks" meant four weeks

It isn't realistic for this product. Four weeks at 66 h is about 260 hours, under half of
what's needed. What four weeks *could* produce is a **demo on a laptop**: research chat with
verified citations and Act lookup. No uploads, no sign-in, no server.

### If we fall behind

Check at the end of Week 3 and Week 5. Drop things **in this order**, and say so in the
standup:

1. Installable-app (PWA) polish
2. Law maps beyond IPC → BNS
3. Word-file uploads (keep PDFs)
4. OCR for scanned PDFs (keep PDFs that already have text)
5. The data-export screen (keep the API route)

**Never dropped:** the verifier, the user-isolation tests, the 200-question runs, the consent
notice, the hard delete. Those *are* the product.

---

## 3. The 11 weeks on one page

| Week | Dates | Theme | By Saturday |
|---|---|---|---|
| 1 | 13 to 17 Oct | Start everything | Search data built; API skeleton; first screens; legal requests sent |
| 2 | 19 to 24 Oct | Search works | Search → re-rank → relevance gate; conversations API; screens on the real API |
| 3 | 26 to 31 Oct | **Answers are verified** | All four verifier checks; streaming answers; sign-in. **Re-plan** |
| 4 | 2 to 7 Nov | The whole engine | Memory, cache, usage meter, monitoring; interviews done. **Decision point** |
| 5 | 9 to 14 Nov | Measured | 50 real questions measured; model chosen; upload storage started |
| 6 | 16 to 21 Nov | **Uploads work** | OCR worker; asking questions about your own document |
| 7 | 23 to 28 Nov | Uploads are safe | Isolation tests; hard delete; knowledge notes; first full test run |
| 8 | 30 Nov to 5 Dec | **On the real server** | Live on AWS; prompt-injection review; uploads go/no-go |
| 9 | 7 to 12 Dec | Hardening | Rebuild rehearsed; second test run; first bug bash |
| 10 | 14 to 19 Dec | **MVP done** | Final test run; go/no-go checklist; second bug bash |
| 11 | 21 to 26 Dec | Buffer *(Christmas)* | Slipped work caught up. **Beta invites out** |
| | **Mon 4 Jan 2027** | **Private beta starts** | 20 students + 10 advocates |

---

## 4. Week by week, person by person

Shaan **24 h** · Akash **24 h** · Meghna **18 h** a week (Week 1: 20 / 20 / 15). Shaan also
spends about 30 minutes a day reviewing pull requests; it isn't repeated below. Ranveer's
column is a **weekly** list.

### Weeks 1 to 4: build the engine

| Week | Shaan: Data + Core | Akash: Platform | Meghna: Web | Ranveer: Lawyers + Outreach |
|---|---|---|---|---|
| **1** | Practice dataset for the team. Search collection built; 20 searches checked by hand. Adapters with test fakes. Start the verifier. *(Daily: [WEEK-1.md](WEEK-1.md))* | Python setup + CI. Compose (ARM checked). API skeleton. Core table migrations. Act and judgment routes | Next.js app + design tokens. App shell + strings. Chat screen on a fake stream. Failure screens. Judgment and Act pages | **Commission the legal opinion.** Ask Voyage for written terms. Email Vaquill. Interview script; book 5; do 2 or 3 |
| **2** | Load all SC cases and Act sections into PostgreSQL. **Search** (meaning + keyword + exact filters, top 50) → **re-rank** (top 10) → **relevance gate** (up to 8, S1 to S8). Decisions adapter with its Gemini fallback *(Daily: [WEEK-2.md](WEEK-2.md))* | Remaining tables. Filter-only search route. Conversation routes (start, list, history). Audit-log entries. Paging | API client generated from OpenAPI. Judgment and Act pages plus the conversation list on the **real** API. Sign-in screens on a mock | Interviews 4 to 10. Agree the legal opinion's scope and date. Start the trademark search for the product name |
| **3** | The answer step and its prompt. **The verifier: all four checks**, the invented-citation log, a test for every failure reason, and the Jev-off and Jev-timeout paths *(Daily: [WEEK-3.md](WEEK-3.md))* | **Streaming answers**: text, then one citations event, then done, with a test that no citation leaves early. **Sign-in**: Firebase token check, `users` table, "answers left" | **Chat screen on the real stream**: ticks and warnings from real events. Conversation history | Interviews 11 to 16. With the advocate, draft **50 trap questions** (cases that don't exist, wrong section numbers, events after the snapshot) |
| **4** | Memory (last 6 turns + summary), query rewrite, the decide step (scope, filters, safety). **Answer cache** (verified answers only, 7 days) *(Daily: [WEEK-4.md](WEEK-4.md))* | **Usage meter**: counted before any AI call, cache hits free, limits in headers, clear error at the limit. Consent at sign-up. Langfuse masking, Sentry scrubbing | Real sign-in and consent screens. Answers-left display. **Format the 200-question set** in `evals/` (lookups + traps + real questions) | Interviews 17 to 20. **Decision memo** with Shaan. Send the 200 questions to the advocate for sign-off |

**End of Week 3: re-plan.** If Weeks 1 to 3 took noticeably longer than planned, the rest
will too. Move the date or use the drop list, and say so.

**End of Week 4: decision point.** The interviews may change what lawyers need: prices,
Hindi, phone versus desktop, whether they'd upload at all. Change Weeks 5 to 10 now, not
later.

### Weeks 5 to 8: uploads and the real server

Detail in [MONTH-2.md](MONTH-2.md). One change from this table: the shared `user_id`-filtered
uploads function moves from Week 7 to **Week 5**, so nothing is ever written to the uploads
collection around it.

| Week | Shaan | Akash | Meghna | Ranveer |
|---|---|---|---|---|
| **5** | **Run 50 real questions end to end**: cost per answer, speed, Gemini 2.5 vs 3.1 Flash-Lite (plus one stronger model), Jev on vs off. Set the gate threshold. Record the decisions *(Daily: [WEEK-5.md](WEEK-5.md))* | **Upload storage**: pre-signed S3 links (resumable, size limit shown first), document records and status. Worker skeleton (1 CPU, one job at a time) | **Upload screens**: limits shown before upload, privilege warning, status steps (uploaded → extracting → indexing → ready / failed), delete | Chase the legal opinion (needed by Week 8). Draft the consent notice, privacy policy, terms and upload warning (Claude can draft from the docs) and **send them to counsel** |
| **6** | **Answering from uploads**: "your document says" kept apart from "Supreme Court judgments say". The claim check uses Gemini, **never Jev**. Upload embeddings: Voyage, or the local model if Voyage's terms haven't arrived *(Daily: [WEEK-6.md](WEEK-6.md))* | **OCR worker**: text PDFs, Word files, Tesseract for scans (English + Hindi). Unreadable files fail early and aren't charged. Every chunk keeps its page and character positions | A citation into an uploaded file **jumps to that page and highlights the passage**. "Report a wrong answer" button + thumbs up/down | Start beta recruitment: 20 students + 10 advocates, interviewees first |
| **7** | **Knowledge-notes system**: only reviewed notes used; a check script (records exist, quotes match); the decide step picks notes. **First full 200-question run** *(Daily: [WEEK-7.md](WEEK-7.md))* | **The shared `user_id`-filtered function + isolation tests** that fail closed. **Hard delete** (S3 + PostgreSQL + Qdrant) + nightly leftover check. Account deletion + export | **Draft the law maps** (IPC → BNS, CrPC → BNSS, Evidence Act → BSA) from the official tables, each line linked to its record. Delete-account and export screens | The legal opinion should arrive. Consent notice back from counsel. **Send the law maps to the advocate** |
| **8** | Fix the worst failures from the 200-question run. **Prompt-injection review** of questions *and* uploaded documents (`ai-security`), then fixes *(Daily: [WEEK-8.md](WEEK-8.md))* | **The AWS server**: EC2 in Mumbai (ARM), Compose on a private network, HTTPS, encrypted disks, Secrets Manager. Restore the search collection (then delete the snapshot file). Daily backups. Deploy workflow on | Phone and slow-network pass (text first, installable). Accessibility check (`a11y-audit`) | **Uploads go/no-go with Shaan**, based on the legal opinion and Voyage's terms. Finalise the beta list |

### Weeks 9 to 11: make it trustworthy, then hand it over

| Week | Shaan | Akash | Meghna | Ranveer |
|---|---|---|---|---|
| **9** | **Second full 200-question run.** Mark advocate-approved notes `reviewed`. Hostile review of the verifier and isolation (`adversarial-reviewer`) | **Rehearse rebuilding the server from backup, and time it** (target under 1 hour); write it into the runbook. Speed checks on the server (first word under 3 s; upload-ready times). Confirm masking and scrubbing on the live server | **Bug bash 1** on the server: every screen, on a phone and a laptop. Fix what's found | Legal documents live. Beta onboarding guide (with Meghna). Trademark result |
| **10** | **Final 200-question run.** Beta go/no-go checklist (below). Finish the breach playbook | Production fixes. Set the uploads switch per the go/no-go decision. Alerts for errors and downtime | **Bug bash 2.** Welcome and onboarding screens. Feedback form wired up | Beta invites drafted. Book kickoff calls for 4 to 8 Jan |
| **11** *(Christmas)* | **Buffer.** Catch up what slipped. No new features | Buffer and fixes | Buffer and fixes | **Send the beta invites** |

---

## 5. Ready for beta means

A proposal. **Shaan decides.**

- [ ] Live on the AWS server, with sign-in and the consent notice (reviewed by counsel)
- [ ] Research chat with a tick **per citation**; Act lookup; judgment view
- [ ] Upload-and-chat working: PDF, Word and scans; hard delete proven
- [ ] Isolation tests pass: one user can never see another's uploads
- [ ] Data-as-of date, CC BY credit and not-legal-advice notice everywhere
- [ ] The final 200-question run is reviewed, with **no confirmed fabricated citation**
- [ ] **Uploads for real client documents:** only if the advocate's written opinion **and**
      Voyage's written terms (or the local embedding model) are in place. Otherwise uploads
      stay on, but with a clear "don't upload client documents yet" warning. Shaan decides
      in Week 8.

---

## 6. People outside the team: Ranveer owns these

| What | Ask by | Needed by | If it's late |
|---|---|---|---|
| **Advocate's written legal opinion** (privilege, DPDP roles, uploads, the advice line) | **Week 1** | **Week 8** | Uploads ship with the "no client documents yet" warning |
| **Voyage's written terms for upload text** | **Week 1** | Week 6 | Use the free local embedding model for uploads |
| **Counsel review of the consent notice** | Week 5 | **Week 9** | **Blocks the beta.** Nobody can sign up without it |
| Advocate signs off the 200 questions | Week 4 | Week 7 | Run them anyway; mark the results provisional |
| Advocate reviews the law maps | Week 7 | Week 9 | Those notes stay out of live answers |
| Trademark search | Week 2 | Before any public branding | Doesn't block the beta |
| Vaquill's answers | Week 1 | Before public launch | Doesn't block the beta |
| Jev early access (Shaan applies) | Week 1 | Week 4 | The Gemini fallback, already designed |

---

## 7. After the MVP

| When | What |
|---|---|
| Jan 2027 (4 weeks) | **Private beta.** Meanwhile, build the moved items: payments, Chambers, statistics pages, the hand check, the marketing site |
| End of the beta | **Launch gate**: every condition in [METRICS.md](../docs/METRICS.md) |
| Feb 2027 at the earliest | **Public launch**, only if the gate passes. If not, the date moves |

## 8. How this plan stays honest

- **Every Saturday:** compare done vs planned; adjust next week's `WEEK-N.md` and its issues
  (Weeks 2 to 8 are already written), or write it if it doesn't exist yet.
- **End of Week 3:** a real re-plan. If it's slipping, move the date or drop from the list in
  §2, **out loud**. Don't quietly squeeze later weeks.
- **Never** cut the verifier, the isolation tests or the 200-question runs to save time.
