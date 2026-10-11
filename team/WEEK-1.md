# Week 1: Tue 13 Oct to Sat 17 Oct 2026

**Goal:** everyone unblocked. The search collection is built, the skeleton runs, and the
non-code blockers are moving.

This is a plan to **try**, not a promise. Estimates for 3 to 4 hours a day with AI coding
help are guesses until measured. Week 2 is written on Day 5 from what actually got done.

## Before Day 1

- [ ] **Akash:** accept the GitHub invite (sent to `mrharit` on 11 Oct). You can't see the
      repo until you do.
- [ ] **Everyone:** clone the repo, open it in VS Code, and read [`README.md`](README.md)
      and [`../CLAUDE.md`](../CLAUDE.md) §1, §5 and §6.

## Day by day

| | **Shaan: Data + Core + Lead (4 h)** | **Akash: Platform (3 h)** | **Meghna: Validation (3 h)** |
|---|---|---|---|
| **Day 1** Tue 13 | 30-min kickoff call. Count the Supreme Court records in the local Qdrant and find the court field name (settles two open decisions). **Make the practice dataset:** about 2,000 SC passages + 500 Act sections, small enough to share | `pyproject.toml`, ruff, pytest, which switches on CI's Python job. One settings module that reads `.env` (CLAUDE.md rule 2) | Interview script, built from the assumptions table in [`../docs/METRICS.md`](../docs/METRICS.md). List of 20 people: 8 district-court advocates, 6 High Court advocates, 6 law students |
| **Day 2** Wed 14 | Send the Jev early-access application, the Vaquill email (the three questions in [`../docs/DATASET.md`](../docs/DATASET.md)), and ask an advocate for a legal-opinion quote. Start building the search collection | `infra/docker-compose.yml`: PostgreSQL 16, Redis, Qdrant on a private network. **Confirm every image has an ARM build** (the server is Graviton) | Send interview invites. Book the first 5 |
| **Day 3** Thu 15 | Finish the search collection (dense + keyword, quantization on). Check 20 searches by hand | API skeleton: `/api/v1/healthz`, the one error format, a request ID on every response (see [`../docs/API.md`](../docs/API.md)) | Draft 50 Act-lookup questions + 50 **trap** questions (cases that don't exist, wrong section numbers, events after the snapshot) in `evals/` |
| **Day 4** Fri 16 | Start the verifier's three free checks, with tests (see [`../docs/CITATION-VERIFIER.md`](../docs/CITATION-VERIFIER.md)) | Alembic set up + first migration (`users`, `consents`). **Lead reviews before merge:** the data model is lead-owned | Hand-check sheet for 50 SC judgments from the practice dataset, plus a **proposed pass rule** to agree with the advocate *before* any checking starts |
| **Day 5** Sat 17 | Merge the week's work. Write Week 2 from what really happened | Load the practice dataset into Qdrant via Compose. Fill in the "Commands" section of CLAUDE.md with the real run commands | First 2 or 3 interviews. Anonymised notes in `docs/research/` |
| **Every day** | 30 min reviewing and merging pull requests. Standup comment by 10 PM | Standup comment by 10 PM | Standup comment by 10 PM |

## Done means, by end of Day 5

- [ ] Search collection built locally; 20 searches checked by hand
- [ ] Practice dataset shared with the team
- [ ] `docker compose up` starts PostgreSQL, Redis and Qdrant; CI Python job green
- [ ] API skeleton returns a health check with a request ID
- [ ] First migration merged
- [ ] Interview script done; 5 interviews booked; 2 or 3 completed
- [ ] 100 test questions drafted (50 lookups + 50 traps)
- [ ] Pass-rule proposal ready to take to the advocate
- [ ] Jev, Vaquill and advocate emails sent

## Dependencies: who waits on whom

| Waiting | On | By |
|---|---|---|
| Meghna, Day 4 (hand-check sheet) | Shaan's practice dataset | Day 1 |
| Akash, Day 5 (load practice data) | Shaan's practice dataset | Day 1 |
| Shaan, Day 4 (verifier tests) | Akash's pytest setup | Day 1 |
| Everyone | Akash accepting the invite | Before Day 1 |

**Day 1 is the critical day for Shaan.** If the practice dataset slips, two other tasks slip
with it. If it isn't ready by the end of Day 2, say so in the standup and we re-plan.
