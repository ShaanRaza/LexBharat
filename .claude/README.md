# .claude

Project-scoped skills and slash commands. They live in the repo, so they travel with it —
anyone who clones this gets them, and they are versioned alongside the rules they enforce.

## How Claude actually finds a skill

**Claude does not read this file to choose a skill.** It matches the `description` field in
each `SKILL.md` frontmatter against what is happening in the conversation, and loads the
skill when it fits.

So **the description is the routing logic**. This index is for humans.

That means a skill is only as good as its description. Write descriptions that name the
concrete triggers — file names, table names, vendor names, the words someone would actually
type — not abstract topics. Compare:

- Weak: *"Use for data quality."*
- Strong: *"Use before reading, filtering on, or displaying any field from the legal corpus —
  judges, petitioner, respondent, citation, disposition, act_status…"*

The second one fires when it should. The first one does not.

## Skills — loaded automatically when they fit

| Skill | Fires when you are |
|---|---|
| [`citation-verifier`](skills/citation-verifier/SKILL.md) | Touching the verifier, badges, source IDs, the invented-citation log, or pipeline steps 7 and 9 |
| [`pipeline-step`](skills/pipeline-step/SKILL.md) | Changing any of the 11 pipeline steps, passage counts, thresholds — or about to add a runtime agent |
| [`outside-service`](skills/outside-service/SKILL.md) | Integrating or swapping any vendor: Voyage, Gemini, Jev, Firebase, Razorpay, S3, OCR |
| [`dataset-field`](skills/dataset-field/SKILL.md) | Reading, filtering on or displaying any corpus field, or counting cases |
| [`upload-privacy`](skills/upload-privacy/SKILL.md) | Touching uploads, `user_documents`, OCR, or any query that could cross users |
| [`knowledge-note`](skills/knowledge-note/SKILL.md) | Drafting or checking an OKF note in `knowledge/` |

Each one carries the non-negotiables inline and points at the full document in `docs/`.
They exist because these are the rules an agent forgets three sessions in — and each one,
broken, costs more than a bug: a leaked client file, a fabricated citation in a filing, a
wrong judge's name on a page.

## Commands — you type these

| Command | Does |
|---|---|
| `/trust-check [path]` | Audits the tree against the trust rules: verifier integrity, user isolation, vendor boundaries, secrets. Reports, does not fix |
| `/decision <text>` | Records a decision in `docs/DECISIONS.md`, moving it from open to settled with its evidence |
| `/where` | Where the build actually stands — what exists, current build step, and which blockers need a person rather than a commit |
| `/ship` | Pre-deploy gate. Runs the must-pass checks and says ship or do not ship. Never deploys |

## Shared with the team automatically

- **Project skills and commands** in this folder.
- **Marketplace plugins** `engineering-skills` and `engineering-advanced-skills`, declared in
  [`settings.json`](settings.json). Claude Code offers to install them when a teammate opens
  the repo.
- **`impeccable`**, copied into [`skills/impeccable/`](skills/impeccable/VENDORED.md) with its
  Apache 2.0 licence. It doesn't update itself; see its `VENDORED.md`.

Personal overrides go in `settings.local.json`, which git ignores.

## Installed skills worth reaching for here

These are not in this repo — they come from the plugin marketplace and user-level skills.
Listed so the right one gets used at the right build step instead of being rediscovered.

| Build step | Skill | For |
|---|---|---|
| 1 — data | `data-quality-auditor` | The judges/party-name garbage check; reconciling the chunk gap |
| 1 — data | `senior-data-engineer` | DuckDB over 75 parquet files, building the launch collection |
| 2 — pipeline | **`rag-architect`** | Chunking, embedding choice, and retrieval evaluation — precision@k, recall@k, NDCG. The plan has no retrieval-quality metric; this supplies one |
| 2 — pipeline | `llm-cost-optimizer` | Cost per answer and the per-plan margin check, both unmeasured |
| 2 — pipeline | `senior-prompt-engineer` | `core/prompts/` |
| 3 — API | `api-design-reviewer`, `api-test-suite-builder` | The v1 routes and the SSE contract |
| 3 — API | `database-schema-designer`, `migration-architect` | 17 tables, Alembic |
| 4 — web | **`impeccable`** | The website. `docs/KanoonBuddy-Website-Design-Doc-v2.md` is a ready brief |
| 4 — web | `a11y-audit` | Advocates on phones, weak networks |
| 6 — server | `aws-solution-architect`, `docker-development` | EC2 Mumbai, ARM/Graviton, Compose |
| 6 — server | `env-secrets-manager`, `observability-designer` | Secrets Manager; Langfuse masking, Sentry scrubbing |
| 6 — server | `runbook-generator`, `slo-architect` | `docs/RUNBOOK.md` is a stub; the 99.5% target is unrehearsed |
| 9–10 — beta | **`ux-researcher-designer`** | The 20 validation interviews — the biggest blocker, and not engineering work |
| 9–10 — beta | `product-discovery` | The assumption table in `docs/METRICS.md` |
| Any time | `ai-security` | Prompt injection. User questions **and uploaded documents** reach models; a hostile PDF is an attack surface nobody has reviewed |
| Any time | `tdd-guide`, `adversarial-reviewer` | Rule 6; a second perspective on verifier changes |

### Looks relevant, is not

Reaching for these would produce confidently wrong work:

| Skill | Why not |
|---|---|
| `gdpr-dsgvo-expert`, `gdpr-audit-prep` | **EU GDPR, not India's DPDP.** Different consent model, different breach timeline, different roles |
| `eu-ai-act-specialist`, `ai-act-readiness` | EU regulation; launch is India-only |
| `stripe-integration-expert` | The product uses **Razorpay** |
| `kubernetes-operator`, `helm-chart-builder`, `terraform-patterns` | One EC2 box with Docker Compose, by decision |
| `azure-cloud-architect`, `gcp-cloud-architect` | AWS, Mumbai |
| `soc2-compliance`, `iso13485-*`, `fda-*`, `mdr-745-*` | Wrong frameworks entirely |

`decision-logger` and `ship-gate` overlap `/decision` and `/ship` above. The local ones know
this repo's specifics — prefer them.

## Adding a skill

```
.claude/skills/<name>/SKILL.md
```

```yaml
---
name: <kebab-case, matches the folder>
description: Use when <concrete triggers — file names, table names, the words someone types>. Also use when <secondary cases>. Not for <the nearest thing it should not catch>.
---
```

Then the body: the non-negotiables inline, a checklist, and a link to the full doc in
`docs/`. Keep it short — it is loaded into a working context, so every line competes with
the actual task.

Add a skill when a rule has been **broken or nearly broken more than once**, or when
getting it wrong is expensive and the rule lives three documents away. Do not add one for
something `CLAUDE.md` already states plainly — duplication drifts.

## Adding a command

```
.claude/commands/<name>.md
```

```yaml
---
description: <what it does, one line>
argument-hint: "<expected argument>"
---
```

Use `$ARGUMENTS` in the body for what the user typed.

## Related

- [`../CLAUDE.md`](../CLAUDE.md) — the rules every session reads first
- [`../docs/`](../docs/) — the source of truth these skills point at
- `.claude/launch.json` — dev server config for the preview pane (not yet written)
