# Roadmap

Phases from the PRD. The **build order** inside phase 2 is in
[BUILD-ORDER.md](BUILD-ORDER.md), which is the one to work from day to day.

The PRD's week numbers assume **3 full-time engineers**. The decision is **one solo builder
with AI coding agents**, which takes longer: the same 18.5 person-weeks is about **18 weeks
or more** before any speed-up from the agents, and that figure leaves out Jev, the
knowledge notes, upload and OCR, the answer cache, the invented-citation log and the admin
page. **Do not promise a date.** Time build steps 1 and 2, then re-plan.

## Phase 1 — weeks 1 to 2: audit and validation

Mostly **not code**. Several items block everything downstream.

- The fill-rate audit of all 75 files is **done** (Measured, 6 Oct 2026).
- Garbage check of judges and party names for the launch courts.
- **Hand-check 100 judgments** against their disposition value — 50 Supreme Court, 50 High
  Court — to see whether it describes the case outcome or an interlocutory order. The
  Supreme Court half can unblock Supreme Court statistics on its own. **Agree the pass rule
  before checking.**
- Reconcile the chunk gap (55,000 or 1,153,189?) and the three judgment counts in
  circulation (12.8M+, 32.5M, 15,693,540).
- Get the Voyage cost per search; test 3 LLM options on 50 real questions.
- Run the 1-week pipeline spike.
- **Confirm every Docker image has an ARM build** — r7g is Graviton.
- Apply for **Jev early access**; email TypeSafe for written data terms.
- Count Supreme Court points in Qdrant; build the launch collection.
- Evaluate upgrading to snapshot **v2026.08.1** against mirror speeds (0.03–11.6 MB/s).
- Request per-file checksums from Vaquill — only 1 of 75 files can be integrity-checked.
- **Start the 20 interviews.**
- Email Vaquill the three questions; ask an advocate for a quote for the legal opinion.

## Phase 2 — weeks 3 to 10 (3-engineer plan; longer solo)

Research chat, Act and section lookup, the citation verifier with the Jev claim-support
check, the Jev decision layer, OKF knowledge notes, the Redis answer cache and
invented-citation log, the usage meter, login and billing, source credit, and the cleaned
outcome labels. **Upload and chat is built in this phase and ships in v1.**

PRD effort estimate, 3-engineer plan:

| Item | Person-weeks |
|---|---|
| Research chat pipeline (retrieve, re-rank, prompt, streaming UI) | 4 |
| Act and section lookup | 2 |
| Citation verifier | 2 |
| Usage meter | 1.5 |
| Login and Razorpay billing | 3 |
| Source credit and data-as-of display | 1 |
| First pass of the data refresh pipeline | 3 |
| Test set and evaluation harness | 2 |
| Jev, knowledge notes, upload and OCR, answer cache, invented-citation log, admin page, account deletion and export, Chambers accounts | **not estimated** |
| **Total of what was estimated** | **18.5** |

Eight weeks of 3 engineers is 24 person-weeks against 18.5 estimated, leaving ~5.5 for
design, bug fixing and security. **The plan fits only with 3 engineers and little slack.**

> The 3-engineer roles are kept for comparison only: tech lead (retrieval, verifier,
> refresh), full-stack (PWA, login, billing, public pages), data and evaluation engineer
> (audit, outcome cleaning, test set), designer, advocate advisor, support and operations,
> growth owner. In the solo plan the founder owns all of them except the advocate advisor.

## Phase 3 — weeks 11 to 14: beta

Free public pages. **Outcome statistics only if the audit passed.** Upload and chat is part
of the private beta. Private beta with **20 law students and 10 advocates**.

## Before public launch

The [launch gate](METRICS.md#launch-gate) — all seven conditions.

## Phase 4 — months 4 to 5: public launch

Drafting, document review, Hindi support, public launch with a data-as-of date on every
result.

## Phase 5 — month 6 onward

Quarterly data refreshes, counter arguments, moot court, team workspace.

---

## Data refresh plan (post-MVP, decision D2)

**Why it matters.** The snapshot is v2026.08 and public launch is months 4 to 5, so
KanoonBuddy would ship with law up to about **8 months old** (Estimate). Lawyers will
notice a missing recent judgment. The mitigation at launch is the data-as-of date, shown
prominently.

| Item | Plan |
|---|---|
| Owner | The founder runs it and is accountable |
| Cadence | Quarterly, with the first refresh finished before public launch. Decide later whether the Supreme Court needs monthly updates |
| Cost | Needs verification — three parts: Voyage cost to embed new chunks, compute for scraping and parsing, and engineer time. Time the first run |
| Acceptance test | Row counts reconcile, a hand-checked sample of new judgments looks right, and the data-as-of date is updated **per court** |

**Technical approach: refresh incrementally. Do not re-download the snapshot.**

1. Run the project's scrapers (Apache-2.0) from an Indian IP for each court, for dates
   after the snapshot. Needs verification: which scrapers still work, since government
   sites change.
2. Parse into the same schema as the snapshot.
3. Chunk and embed new chunks with **voyage-4** — it must match the existing vectors.
4. Add the new points to Qdrant. Store each court's data-as-of date in `court_coverage`
   and show it on every result. **Clear the answer cache after each refresh.**
5. Reconcile counts, re-run the audit sample, publish a short change log.

**Why not a full re-download.** The mirror is slow and erratic: measured 0.03–11.6 MB/s.
The snapshot is ~517 GB. At the best measured speed that is ~12 hours of continuous
transfer; at the worst, about 200 days. Every full refresh would be a multi-day operation
at best.
