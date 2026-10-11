# LexBharat — KanoonBuddy

AI legal research for Indian lawyers and law students. Ask a legal question in plain
language; get a short plain answer where **every claim carries a citation that has been
mechanically verified against the dataset**.

> **Working name.** "KanoonBuddy" is a working name pending a trademark search; the PRD
> recommends "Praman". `PRODUCT_NAME` is a single config value, so the final brand is a
> config change, not a code change. Never hard-code it.

**v1 serves the Supreme Court and `acts_india` (Central Acts) only.** High Courts are
phase 2. Data is a frozen snapshot, **v2026.08** — every result shows its data-as-of date.

KanoonBuddy gives legal information, **not legal advice**.

---

## Start here

| If you are | Read |
|---|---|
| A coding agent | **[CLAUDE.md](CLAUDE.md)** — first, every session |
| Picking up the build | [docs/BUILD-ORDER.md](docs/BUILD-ORDER.md) |
| Trying to understand the system | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) |
| Wondering why something is the way it is | [docs/DECISIONS.md](docs/DECISIONS.md) |

## Repo layout

```
web/          Next.js + TypeScript + Tailwind website (PWA)
api/          FastAPI app — routes only
core/         pipeline steps: search, rerank, answer, verify (+ prompts/)
adapters/     one file per outside service
workers/      background jobs: OCR, indexing uploads
data/         scripts to build the launch collection from parquet + Qdrant
knowledge/    OKF knowledge notes (reviewed Markdown)
evals/        200-question test set and scorer
tests/        unit and integration tests
migrations/   Alembic — numbered, reversible
infra/        docker-compose, deploy scripts
legal/        versioned consent notice, privacy policy, terms
docs/         specs and reference
skills-used/  record of which skills were planned, used or rejected
team/         who works on what, branch rules, weekly plans
.github/      PR template; CI workflows go in .github/workflows/
```

## Documentation

### Specs (source of truth)

| Document | Date | Contents |
|---|---|---|
| [Product Requirements Document](docs/KanoonBuddy-Product-Requirements-Document.pdf) | 9 Oct 2026 | Positioning, competitor teardown, pricing, launch scope, dataset audit. 59 pp. |
| [Tech Stack](docs/KanoonBuddy-Tech-Stack.pdf) | 6 Oct 2026, rev. 9 Oct | v1 architecture, service choices, running cost, decisions D1–D6. 48 pp. |
| [System Architecture Reference (HLD + LLD)](docs/KanoonBuddy-System-Architecture-Reference-HLD-LLD.pdf) | 6 Oct 2026 | High- and low-level design |
| [Website Design Doc v2](docs/KanoonBuddy-Website-Design-Doc-v2.md) | 9 Oct 2026 | Marketing site: pages, visual system, copy rules |

**Where the PRD and the Tech Stack disagree, the Tech Stack wins** (stated in the PRD's
review key).

### Working docs

**Product**

| Document | Covers |
|---|---|
| [docs/PRODUCT.md](docs/PRODUCT.md) | Problem, goals, users, MVP scope, plans and pricing, go-to-market, naming |
| [docs/ROADMAP.md](docs/ROADMAP.md) | Phases, effort estimates, the data refresh plan |
| [docs/METRICS.md](docs/METRICS.md) | Success metrics, the launch gate, the validation plan |
| [docs/UX-COPY.md](docs/UX-COPY.md) | Failure states, badge wording, standing notices, copy rules |
| [docs/RISKS.md](docs/RISKS.md) | Combined risk register with mitigations |

**Engineering**

| Document | Covers |
|---|---|
| [CLAUDE.md](CLAUDE.md) | Rules for coding agents: scope, the seven rules, hard limits |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | The 11-step pipeline, stack by layer, search, Jev, uploads |
| [docs/DECISIONS.md](docs/DECISIONS.md) | **Top 5 questions before any code**, plus settled and open decisions |
| [docs/DATASET.md](docs/DATASET.md) | What the corpus holds, the audit, field quality, licence, Vaquill |
| [docs/DATA-MODEL.md](docs/DATA-MODEL.md) | 17 PostgreSQL tables, 2 Qdrant collections |
| [docs/API.md](docs/API.md) | v1 routes, error format, SSE contract |
| [docs/CITATION-VERIFIER.md](docs/CITATION-VERIFIER.md) | The four checks; what the tick means and does not |
| [docs/BUILD-ORDER.md](docs/BUILD-ORDER.md) | 11 build steps and the launch gate |
| [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md) | Config contract and feature switches |
| [docs/TESTING.md](docs/TESTING.md) | Must-pass list, CI, and the 200-question test set |
| [docs/RUNBOOK.md](docs/RUNBOOK.md) | Rebuild plan, backups, monitoring, release checklist, incidents |
| [docs/GLOSSARY.md](docs/GLOSSARY.md) | Every term, in plain words |
| [knowledge/index.md](knowledge/index.md) | How OKF knowledge notes work |

**Legal and compliance**

| Document | Covers |
|---|---|
| [docs/SECURITY-AND-COMPLIANCE.md](docs/SECURITY-AND-COMPLIANCE.md) | DPDP, BCI Rule 36, privilege, security, uploads |
| [docs/RETENTION.md](docs/RETENTION.md) | Retention per data type — **undecided, needs counsel** |
| [docs/BREACH-PLAYBOOK.md](docs/BREACH-PLAYBOOK.md) | The 72-hour plan — **skeleton** |
| [legal/README.md](legal/README.md) | The user-facing documents that must exist before sign-up |

## Evidence labels

Facts in these docs carry one of six labels, used consistently. Keep them; do not promote
an Estimate to a fact without measuring it.

**Measured** (checked on a local copy of the dataset) · **Checked** (confirmed on a public
page, with the date) · **Dataset card** (claimed by the dataset's own pages) ·
**Competitor claim** (from a competitor's site) · **Estimate** (worked out from stated
inputs) · **Needs verification** (not confirmed, with how to confirm it)

## Getting set up

```bash
cp .env.example .env     # then fill it in — see docs/ENVIRONMENT.md
```

Nothing is scaffolded yet. The first thing to build is **build step 1 (data)** and then
**step 2 (the pipeline in a script)** — the riskiest parts first. See
[docs/BUILD-ORDER.md](docs/BUILD-ORDER.md).

Before writing much code, read the **top 5 open questions** in
[docs/DECISIONS.md](docs/DECISIONS.md). Several of them are not engineering work — 20 user
interviews, a 100-judgment hand check, and conversations with counsel and with Vaquill —
and their answers change the plan.

## Status

Pre-launch. Pricing, launch courts, upload limits and the product name are all still open;
see [docs/DECISIONS.md](docs/DECISIONS.md). Nothing here is a public commitment.

Data: Open India Law by Vaquill AI, CC BY 4.0.
