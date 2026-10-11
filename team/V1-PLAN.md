# V1 plan: from today to the private beta

**Version 1, written 12 Oct 2026.** Re-plan every Saturday, and properly at the end of
Week 3, when we have real speed numbers instead of guesses.

"Done" here means **ready for the private beta**: real advocates and law students using it
and reviewing it (build step 10 in [`../docs/BUILD-ORDER.md`](../docs/BUILD-ORDER.md)).
Public launch comes after the beta, and only if the launch gate passes.

---

## 1. How long will it take?

**About 16 weeks. The private beta starts around Mon 1 Feb 2027.** A realistic range is
**14 to 20 weeks**.

### The arithmetic

| | Hours | Where the number comes from |
|---|---|---|
| Build steps 2 to 9 (pipeline, API, website, login, server, uploads, payments, admin and public pages) | 400 to 640 | The Tech Stack's own estimate: **10 to 16 weeks for one person working full time** with AI coding agents (40 h a week) |
| Step 1: the data work | ~60 | Counting, building the search collection, cleaning outcomes, the hand check |
| 20 user interviews + making sense of them | ~50 | About 2 h per interview, including booking and notes |
| Beta preparation: security review, legal drafts, recruiting beta users | ~70 | Estimate |
| Team overhead: reviewing pull requests, standups, handovers | ~45 | Three people need coordinating; one person doesn't |
| **Total** | **~625 to 865** | |

**Team capacity:** Shaan 4 h + Akash 3 h + Meghna 3 h = 10 h a day. Over 5 days that's **50
hours a week**.

625 to 865 hours ÷ 50 a week = **12.5 to 17.3 weeks**. The plan uses **15 weeks of work + 1
buffer week = 16**.

### Why it could take longer

- **Holidays.** Diwali (early November), Christmas and New Year all fall inside this plan.
  Weeks 11 and 12 are planned light for that reason. The buffer week exists for it.
- **Nothing is measured yet.** Every number above is an estimate. The Tech Stack itself says
  to time the first steps and re-plan. That happens at the end of Week 3.
- **People outside the team.** The advocate, Jev's early access, Vaquill and the counsel
  review of the consent notice can all be slow. The plan works around most of them (for
  example, Gemini stands in if Jev access doesn't come), but not all.
- **Meghna building screens.** From Week 6 this plan has Meghna building the website with
  Claude Code's help. If that doesn't suit her, the screens move to Akash and the plan
  grows by **about 3 weeks**.

### A faster option (Shaan's call)

Payments, Chambers team accounts and uploads are **not needed for a free beta**. Uploads
start switched off anyway. Moving those three into the beta period would make the product
**beta-ready around Week 13 (early January)**, about 3 weeks sooner. The trade-off is that
the beta tests less of the product.

---

## 2. The whole plan on one page

| Week | Dates | Phase | By the end of the week |
|---|---|---|---|
| 1 | 13 to 17 Oct | Foundations | Practice dataset shared; skeleton runs; interviews started |
| 2 | 19 to 23 Oct | Foundations | Data numbers reconciled; full database schema; test questions drafted |
| 3 | 26 to 30 Oct | Foundations | **Step 1 done.** Outcomes cleaned; hand check done; Act and judgment API. **Re-plan** |
| 4 | 2 to 6 Nov | Answer engine | Search, re-rank and the relevance gate work |
| 5 | 9 to 13 Nov | Answer engine | Answers written and **verified**; all 20 interviews done; **decision point** |
| 6 | 16 to 20 Nov | Answer engine | Memory, cache, usage meter, monitoring |
| 7 | 23 to 27 Nov | Answer engine | **Steps 2 and 3 done.** 50 real questions measured; model chosen |
| 8 | 30 Nov to 4 Dec | Product | Chat screen; login; knowledge notes system |
| 9 | 7 to 11 Dec | Product | Judgment and Act pages; consent, account deletion and export |
| 10 | 14 to 18 Dec | Product | **Steps 4 and 5 done.** The full website works on a laptop |
| 11 | 21 to 25 Dec | Production *(light: Christmas)* | Server live; first full 200-question run |
| 12 | 28 Dec to 1 Jan | Production *(light: New Year)* | **Step 6 done.** Rebuild rehearsed; law maps sent to the advocate |
| 13 | 4 to 8 Jan | Uploads | Upload-and-chat built (switched **off**); legal drafts with counsel |
| 14 | 11 to 15 Jan | Uploads + payments | **Steps 7 and 8 done.** Payments in test mode |
| 15 | 18 to 22 Jan | Beta hardening | Security review; Chambers; beta users recruited |
| 16 | 25 to 29 Jan | **Buffer** + beta launch | Bug bash; slipped work caught up; invites out Friday |
| | **Mon 1 Feb 2027** | **Private beta starts** | 20 students + 10 advocates |

---

## 3. Week by week, person by person

Shaan **20 h** · Akash **15 h** · Meghna **15 h** a week. Shaan also spends about 30 minutes a
day reviewing and merging pull requests in every week. That isn't repeated below.

### Phase A: Foundations (Weeks 1 to 3)

*Goal: the data can be trusted, the skeleton runs, and the interviews are underway.*

| Week | Shaan: Data + Core + Lead | Akash: Platform | Meghna: Validation |
|---|---|---|---|
| **1** | Count the Supreme Court records; find the court field name. **Make the practice dataset** for the team. Send the Jev, Vaquill and advocate emails. Build the search collection; check 20 searches by hand. Start the verifier's free checks. *(Day by day: [WEEK-1.md](WEEK-1.md))* | Python setup + CI. Docker Compose (PostgreSQL, Redis, Qdrant), checking ARM builds. API skeleton (health check, error format, request ID). Migrations + first tables. Load the practice dataset | Interview script. List of 20 people. Book 5 interviews. Draft 50 Act-lookup + 50 trap questions. Hand-check sheet + proposed pass rule. First 2 or 3 interviews |
| **2** | Reconcile the chunk gap (55k or 1.15M?) and the three judgment counts. Test re-embedding with a header and keep it only if search improves. Weigh snapshot v2026.08.1. **Agree the pass rule with the advocate.** Adapter skeletons (embeddings, re-rank, AI models via LiteLLM) with test fakes | All **17 database tables** as migrations (Shaan reviews: the data model is his). Paging, error and request-ID middleware. Publish the API description (OpenAPI). Load cases and Act sections from the practice dataset into PostgreSQL | Interviews 4 to 8. Finalise the 50 lookups + 50 traps. Start a list of the real questions people ask. Manual check of judge and party-name fields on a sample |
| **3** | Clean the Supreme Court outcome labels (Jev if access has arrived, otherwise the Gemini fallback). Load all SC cases and Act sections into PostgreSQL. Decisions adapter with its fallback. **End of week: re-plan from measured speed** | Act lookup route (in-force rule), judgment route with paragraph anchors, filter-only search route, all with tests | **Run the 50-judgment hand check** against the agreed rule. Interviews 9 to 13 |

**Phase A finish line:** build step 1 done; the API serves Acts and judgments; 13
interviews done; the plan updated with real numbers.

### Phase B: The answer engine (Weeks 4 to 7)

*Goal: a question goes in and an answer with verified citations comes out. This is the
riskiest part, so it comes first.*

| Week | Shaan | Akash | Meghna |
|---|---|---|---|
| **4** | Search (meaning + keyword + exact filters, top 50) → re-rank (top 10) → relevance gate (up to 8, labelled S1 to S8). Check that the search stage takes under 800 ms | Conversation routes (start, list, history). Saving messages. Audit-log entries | Interviews 14 to 20 *(Diwali week: some may slip)*. Collect the 100 real questions |
| **5** | The answer step and its prompt. **The citation verifier: all four checks**, the invented-citation log, a test for each failure reason, and the Jev-off and Jev-timeout paths | The streaming answer route: text word by word, then **one** citations event, then done. A test proving no citation leaves early | **Make sense of the interviews**: update the assumptions table and write Shaan a one-page decision memo (prices, Hindi, phone or desktop, uploads, whether statistics are wanted). **Freeze the 200-question set** and send it to the advocate for sign-off |
| **6** | Memory, query rewrite, and the decide step (scope, filters, safety, which notes apply). The answer cache (verified answers only, 7 days). Langfuse with masking; Sentry with scrubbing | **The usage meter**: counted before any AI call, cache hits free, limits in headers, a clear error at the limit. Tests | Put the user-facing wording from [UX-COPY.md](../docs/UX-COPY.md) into one strings file. Start the marketing site (Home, Features, Pricing) from the design doc, using the `impeccable` skill |
| **7** | **Run 50 real questions end to end**: cost per answer, speed, Gemini 2.5 vs 3.1 Flash-Lite (plus one stronger model), Jev on vs off. Set the gate threshold. Record the decisions | Plug Shaan's pipeline into the streaming route, end to end, with a test. Statistics route, behind its switch | Finish the marketing site. Generate the website's API client from OpenAPI. App shell: Next.js, installable (PWA), layout and navigation |

**Decision point, end of Week 5:** Shaan reads the interview memo. If lawyers want something
different (Hindi first, desktop not phone, no uploads, different prices), Weeks 8 to 14
change here, not later.

**Phase B finish line:** steps 2 and 3 done. The API answers real questions with verified
citations, and the cost per answer is measured.

### Phase C: The product people touch (Weeks 8 to 10)

*Goal: a person can sign in, ask, and read the sources, on a laptop.*

| Week | Shaan | Akash | Meghna |
|---|---|---|---|
| **8** | Knowledge-notes system: load only reviewed notes; a check script (records exist, quotes match); the decide step picks notes. Scripts that draft the IPC → BNS, CrPC → BNSS and Evidence Act → BSA maps | **Login**: Firebase token check in the API; `users` table keyed by Firebase ID; "answers left this month" | **The chat screen**: ask, watch the answer stream in, then citations with a tick or warning **per citation**, the data-as-of date, the CC BY credit and the notice. *(Shaan checks it against the verifier rules)* |
| **9** | Outcome-statistics queries; turn the statistics switch on **only if** the hand check passed. Heavy review week | Consent at sign-up (saved with the notice version). Account deletion. Data export. Plan limits read from config | Judgment view (text first, paragraph anchors, PDF only on tap with its size shown). **Public Act pages**, built on the server so Google can read them, with the in-force rule |
| **10** | Admin page backend: run the 200-question set, raw scores from each search, invented-citation rate. **Get quotes for the security test** | Start the server: EC2 in Mumbai (ARM), ARM images, Compose on a private network, HTTPS, encrypted disks, keys in Secrets Manager | Sign-in and consent screens. Usage shown in plain numbers. **Every failure screen**: not found, keyword results only, sources without an answer, out of scope |

**Phase C finish line:** steps 4 and 5 done. The whole website works on a laptop.

### Phase D: Production, uploads, payments (Weeks 11 to 14)

*Goal: it runs on the real server, and the remaining v1 features are built.*

| Week | Shaan | Akash | Meghna |
|---|---|---|---|
| **11** *(light)* | **First full 200-question run.** Fix the worst search and verifier failures | Restore the search collection on the server (then delete the snapshot file). Daily backups. Turn on the deploy workflow. Smoke test after deploy | Statistics pages, share cards, sitemap. A pass over phone use and slow connections |
| **12** *(light)* | Law-map and limitation notes complete → **send to the advocate for review**. Coverage note | **Rehearse rebuilding the server from backup and time it** (target under 1 hour). Write it into [RUNBOOK.md](../docs/RUNBOOK.md) | Admin page screens (test runner, scores, invented-citation rate). Accessibility check (`a11y-audit`) |
| **13** | **Prompt-injection review** of user questions and uploaded documents (`ai-security`), then fixes. Upload answer prompt ("your document says…") | **Uploads**, switched off: pre-signed S3 links, OCR worker (1 CPU, one job at a time), chunks that keep page and character positions, the shared `user_id`-filtered function, isolation tests | Drafts for counsel: consent notice v1, privacy policy (vendor table), terms, upload warning, not-legal-advice wording, retention list. **The consent notice blocks sign-up for beta users, so it must reach counsel this week** |
| **14** | Second full 200-question run; track the rates. Mark advocate-approved notes as `reviewed` | Hard delete (S3 + PostgreSQL + Qdrant) and the nightly leftover check. **Razorpay** subscriptions and a signed webhook, in test mode | Upload screens (status steps, warning, delete), behind the switch. Pricing page with plain-number limits |

**Phase D finish line:** steps 6, 7 and 8 done. The product is live on the server, uploads
are built but off, and payments work in test mode.

### Phase E: Ready for real users (Weeks 15 and 16)

| Week | Shaan | Akash | Meghna |
|---|---|---|---|
| **15** | Hostile review of the verifier and user isolation (`adversarial-reviewer`). Complete the breach playbook. **Beta go / no-go checklist** | Chambers team accounts (minimum 3 seats). Speed check on the server (first word under 3 seconds). Confirm Langfuse masking and Sentry scrubbing work for real | **Recruit the beta**: 20 students + 10 advocates, starting with the people interviewed. Onboarding guide. "Report a wrong answer" and feedback form working |
| **16** | **Buffer.** Bug bash with everyone. Catch up whatever slipped. Final 200-question run. Send invites on Friday | Buffer and bug fixes | Buffer, bug fixes, beta welcome messages |

---

## 4. Ready for beta means

A proposal. **Shaan decides.**

- [ ] Running on the real server, with sign-in
- [ ] Research chat with a tick **per citation**; Act lookup; judgment view
- [ ] Data-as-of date, CC BY credit and not-legal-advice notice on every answer and page
- [ ] The 200-question set has been run; the verified-citation and removed-citation rates are
      measured, and the advocate has looked at the results
- [ ] **No confirmed fabricated citation** in the last full run
- [ ] Consent notice reviewed by counsel and live at sign-up
- [ ] Uploads **off** unless the advocate's written opinion and Voyage's written terms have
      both arrived
- [ ] Payments off or in test mode: **the beta is free**

---

## 5. Things that wait on people outside the team

| What | Ask by | Needed by | If it's late |
|---|---|---|---|
| Jev early access | Week 1 | Week 3 | Gemini fallback, already designed. Not a blocker |
| Vaquill's answers (licence, refresh, counts) | Week 1 | Before public launch | Doesn't block the beta |
| Advocate: agree the hand-check pass rule | Week 1 | Week 2 | **Blocks** the hand check, and so the statistics |
| Advocate: sign off the 200-question set | Week 5 | Week 7 | Run it unsigned; mark the results provisional |
| Advocate: review the law maps | Week 12 | Week 14 | Those notes stay out of live answers |
| Counsel: consent notice | Week 13 | Week 15 | **Blocks the beta.** Nobody can sign up without it |
| Advocate's written legal opinion | Week 2 (quote) | Before uploads are switched on, and before public launch | Uploads stay off |
| Voyage's written terms for upload text | Week 2 | Before uploads are switched on | Uploads stay off, or use the local model |
| Security test | Week 10 (quotes) | Before public launch | Doesn't block the beta |

---

## 6. After Week 16

| When | What |
|---|---|
| Feb 2027 (4 weeks) | **Private beta.** Wrong-answer reports triaged within 2 days; 200-question set re-run on every release |
| End of beta | **Launch gate**: all conditions in [METRICS.md](../docs/METRICS.md). A 98%+ verified-citation rate; 6 of 10 advocates would pay; zero fabricated citations reaching users; the legal opinion; Voyage's terms; the security test; data-as-of dates shown |
| March 2027 at the earliest | **Public launch**, only if every gate condition passes. If one fails, the date moves. Shaan decides |
| Within 3 months of launch | Drafting, review and compare; Hindi (sooner if the interviews demand it) |

---

## 7. How this plan stays honest

- **Every Saturday:** compare what got done with this plan. Update the next week's rows, and
  write a `WEEK-N.md` for the coming week as detailed as [WEEK-1.md](WEEK-1.md).
- **End of Week 3:** real re-plan. If Weeks 1 to 3 took twice as long as planned, so will the
  rest, so the beta date moves and gets said out loud. Don't quietly squeeze the later weeks.
- **End of Week 5:** the interviews may change what gets built. That's the point of doing
  them first.
- **Never** cut the verifier, the isolation tests or the 200-question runs to save time.
  Those are the product.
