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
