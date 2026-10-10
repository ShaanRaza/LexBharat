# Skills used on this project

A **record**, not a dependency. Nothing in here makes a skill run, and nothing here is
copied from anywhere. It answers one question: *which skills did we plan to use on this
product, which did we actually use, and which did we decide not to?*

Update the **Status** column as you go. When you use a skill, write the date and one line on
what it produced. That line is what makes this useful later.

**Status key:** `Planned` · `Used` · `Skipped` (decided not to, with the reason)

> The mapping to build steps is a judgment made from each skill's name and description. The
> skills were confirmed installed on 10 Oct 2026, but most have not been run yet. Treat
> "Planned" as a hypothesis until one has actually been used.

---

## 1. Project skills — live in this repo

Written for this product. They load automatically and are the only skills actually stored
in GitHub, at [`../.claude/skills/`](../.claude/skills/).

| Skill | Covers | Status |
|---|---|---|
| `citation-verifier` | The four checks, badge wording, the invented-citation log | Planned |
| `pipeline-step` | The 11 fixed steps, the 50 / 10 / 8 funnel, no runtime agents | Planned |
| `outside-service` | One adapter per vendor, no-training terms | Planned |
| `dataset-field` | Which corpus fields are unusable (judges, party names, `act_status`) | Planned |
| `upload-privacy` | The shared `user_id`-filtered function, where upload text may never go | Planned |
| `knowledge-note` | OKF note front matter, who reviews what | Planned |

Commands, at [`../.claude/commands/`](../.claude/commands/): `/trust-check` · `/decision` ·
`/where` · `/ship`

---

## 2. Installed skills — live on your computer, not in this repo

Version in brackets is the installed plugin version, checked 10 Oct 2026.

### Build step 1 — data

| Skill | Use it for | Status |
|---|---|---|
| `data-quality-auditor` (adv 2.9.0) | Garbage check on judges and party names; reconciling the chunk gap (about 55,000 or 1.15M) | Planned |
| `senior-data-engineer` (eng 2.9.0) | DuckDB over the 75 parquet files; building the launch collection | Planned |

### Build step 2 — pipeline

| Skill | Use it for | Status |
|---|---|---|
| `rag-architect` (adv 2.9.0) | Chunking, embedding choice, and retrieval evaluation (precision@k, recall@k, NDCG). The plan has **no retrieval-quality metric** yet | Planned |
| `llm-cost-optimizer` (adv 2.9.0) | Cost per answer and the per-plan margin check, both still unmeasured | Planned |
| `senior-prompt-engineer` (eng 2.9.0) | Prompts in `core/prompts/` | Planned |

### Build step 3 — API and database

| Skill | Use it for | Status |
|---|---|---|
| `api-design-reviewer` (adv 2.9.0) | The v1 routes and the streaming contract | Planned |
| `api-test-suite-builder` (adv 2.9.0) | Route tests | Planned |
| `database-schema-designer` (adv 2.9.0) | The 17 tables | Planned |
| `migration-architect` (adv 2.9.0) | Alembic migrations | Planned |

### Build step 4 — website

| Skill | Use it for | Status |
|---|---|---|
| `impeccable` (user-level) | The website. [`../docs/KanoonBuddy-Website-Design-Doc-v2.md`](../docs/KanoonBuddy-Website-Design-Doc-v2.md) is a ready brief | Planned |
| `a11y-audit` (eng 2.9.0) | Advocates on phones and weak connections | Planned |

### Build step 6 — server

| Skill | Use it for | Status |
|---|---|---|
| `aws-solution-architect` (eng 2.9.0) | One EC2 box in Mumbai, ARM (Graviton) | Planned |
| `docker-development` (adv 2.9.0) | Docker Compose, ARM image builds | Planned |
| `env-secrets-manager` (adv 2.9.0) | AWS Secrets Manager; keeping keys out of files | Planned |
| `observability-designer` (adv 2.9.0) | Langfuse masking, Sentry scrubbing | Planned |
| `runbook-generator` (adv 2.9.0) | Finishing [`../docs/RUNBOOK.md`](../docs/RUNBOOK.md) | Planned |
| `slo-architect` (adv 2.9.0) | The 99.5% target, which nobody has rehearsed | Planned |
| `ci-cd-pipeline-builder` (adv 2.9.0) | Filling in the deploy workflow | Planned |

### Build steps 9 to 10 — beta

| Skill | Use it for | Status |
|---|---|---|
| `ux-researcher-designer` (product 2.11.1) | The 20 validation interviews, the biggest blocker and not engineering work | Planned |
| `product-discovery` (product 2.11.1) | The assumption table in [`../docs/METRICS.md`](../docs/METRICS.md) | Planned |

### Any time

| Skill | Use it for | Status |
|---|---|---|
| `ai-security` (eng 2.9.0) | Prompt injection. Questions **and uploaded PDFs** reach models; a hostile document is an attack surface nobody has reviewed | Planned |
| `tdd-guide` (eng 2.9.0) | Rule 6: tests that guard the trust promise | Planned |
| `adversarial-reviewer` (eng 2.9.0) | A second, hostile read of any change to the verifier | Planned |
| `code-reviewer` (eng 2.9.0) | General review | Planned |

---

## 3. Plugins from the Anthropic Directory

| Plugin | What it does | Status |
|---|---|---|
| **Vibe Wise** 0.1.44 (`/vibe-wise:learn`, `/vibe-wise:reset`) | Learning-first mode: you lead the design and Claude explains. Only you can start it; Claude cannot | Installed, **not started** |

---

## 4. Looked relevant, decided not to use

Keeping this list stops the same wrong skill being picked up again.

| Skill | Why not |
|---|---|
| `gdpr-dsgvo-expert`, `gdpr-audit-prep` | **EU GDPR, not India's DPDP.** Different consent model, breach timeline and roles |
| `eu-ai-act-specialist`, `ai-act-readiness` | EU regulation; launch is India-only |
| `stripe-integration-expert` | Payments use **Razorpay** |
| `kubernetes-operator`, `helm-chart-builder`, `terraform-patterns` | One EC2 box with Docker Compose, by decision |
| `azure-cloud-architect`, `gcp-cloud-architect` | The stack is AWS, Mumbai |
| `soc2-compliance`, `iso13485-*`, `fda-*`, `mdr-745-*` | Wrong frameworks entirely |
| `decision-logger`, `ship-gate` | Overlap `/decision` and `/ship`. The local ones know this repo's rules |

---

## Usage log

One line each time a skill is actually used. Newest first.

| Date | Skill | What it produced |
|---|---|---|
| | | |
