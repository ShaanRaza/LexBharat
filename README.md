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
core/         pipeline steps: search, rerank, answer, verify
adapters/     one file per outside service
workers/      background jobs: OCR, indexing uploads
data/         scripts to build kanoon_v1 from parquet + Qdrant
knowledge/    OKF knowledge notes (reviewed Markdown)
evals/        200-question test set and scorer
infra/        docker-compose, deploy scripts
docs/         specs and reference
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

| Document | Covers |
|---|---|
| [CLAUDE.md](CLAUDE.md) | Rules for coding agents: scope, the seven rules, hard limits |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | The 11-step pipeline, stack by layer, search, Jev, uploads |
| [docs/DECISIONS.md](docs/DECISIONS.md) | Settled and open decisions, each with what settles it |
| [docs/DATA-MODEL.md](docs/DATA-MODEL.md) | 17 PostgreSQL tables, 2 Qdrant collections |
| [docs/API.md](docs/API.md) | v1 routes, error format, SSE contract |
| [docs/CITATION-VERIFIER.md](docs/CITATION-VERIFIER.md) | The four checks; what the tick means and does not |
| [docs/BUILD-ORDER.md](docs/BUILD-ORDER.md) | 11 build steps and the launch gate |
| [docs/SECURITY-AND-COMPLIANCE.md](docs/SECURITY-AND-COMPLIANCE.md) | DPDP, BCI Rule 36, security, uploads |
| [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md) | Config contract and feature switches |
| [docs/TESTING.md](docs/TESTING.md) | Must-pass list and the 200-question test set |
| [docs/GLOSSARY.md](docs/GLOSSARY.md) | Every term, in plain words |
| [knowledge/index.md](knowledge/index.md) | How OKF knowledge notes work |

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

## Status

Pre-launch. Pricing, launch courts, upload limits and the product name are all still open;
see [docs/DECISIONS.md](docs/DECISIONS.md). Nothing here is a public commitment.

Data: Open India Law by Vaquill AI, CC BY 4.0.
