# LexBharat

Product and engineering documentation for **KanoonBuddy**, an AI legal research and
drafting tool for Indian lawyers and law students, built by LexBharat.

> **Working name.** "KanoonBuddy" is a working name only, pending a trademark search.
> The PRD recommends "Praman" as the replacement. Per the Tech Stack, the product name
> sits in a single config value (`PRODUCT_NAME`), so a final brand is a config change,
> not a code change.

## Documents

| Document | Date | Contents |
|---|---|---|
| [Product Requirements Document](docs/KanoonBuddy-Product-Requirements-Document.pdf) | 9 Oct 2026 | Positioning, competitor teardown (Prism), pricing, launch scope, dataset audit. 59 pp. |
| [Tech Stack](docs/KanoonBuddy-Tech-Stack.pdf) | 6 Oct 2026, rev. 9 Oct 2026 | v1 architecture, service choices, adapter rule, running cost, decisions D1–D6. 48 pp. |
| [System Architecture Reference (HLD + LLD)](docs/KanoonBuddy-System-Architecture-Reference-HLD-LLD.pdf) | 6 Oct 2026 | High- and low-level design reference accompanying the PRD. |
| [Website Design Doc v2](docs/KanoonBuddy-Website-Design-Doc-v2.md) | 9 Oct 2026 | Marketing site: three pages, visual system, copy rules, pre-launch checklist. |

## Precedence

Where the PRD and the Tech Stack disagree, **the Tech Stack wins** (stated in the PRD's
review key).

## Evidence labels

Facts in the PRD and Tech Stack carry one of six labels, used consistently across both:

- **Measured** — checked on a local copy of the dataset
- **Checked** — confirmed on a public page, with the date
- **Dataset card** — claimed by the dataset's own pages
- **Competitor claim** — from a competitor's website or blog
- **Estimate** — worked out from stated inputs, not measured
- **Needs verification** — not confirmed, with a note on how to confirm it

## Status

Pre-launch. Nothing here is a public commitment: pricing, launch courts, and the
product name are all still open. The product serves legal information, not legal advice.
