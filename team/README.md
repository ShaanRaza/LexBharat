# Team

| Person | GitHub | Lane | Share | Hours |
|---|---|---|---|---|
| Shaan (lead) | `ShaanRaza` | **Data + Core + Lead** | 40% | 4 h/day |
| Akash | `mrharit` | **Platform** | 30% | 3 h/day |
| Meghna | `meghnarana-2016` | **Validation** | 30% | 3 h/day |

The split comes from the hours: 4 + 3 + 3 = 10, which gives 40 / 30 / 30.

## What each lane owns

Separate folders mean no one edits the same files as anyone else.

| Lane | Owns | What it covers |
|---|---|---|
| **Data + Core + Lead** | `data/` `core/` `adapters/` `knowledge/` `tests/fixtures/` | The dataset lives on the lead's SSD, so all corpus work happens there. The pipeline and the citation verifier, which the lead must be able to defend. Outside conversations (Jev, Vaquill, the advocate). Reviewing and merging every pull request |
| **Platform** | `api/` `infra/` `migrations/` `workers/` `pyproject.toml` | The runnable skeleton: Docker Compose, the API shell, database migrations, CI. Mostly setup work |
| **Validation** | `evals/` `docs/research/` | The 20 user interviews, the 200-question test set, preparing the 50-judgment hand check |
| Nobody yet | `web/` | Build step 4, in a later week |

If you need to change a file outside your lane, say so in the standup first.

## How work reaches `main`

`main` belongs to the lead. **Nobody else pushes to it.**

```
make a branch      akash/compose-setup   or   meghna/test-set-traps
        |          one small task per branch
open a pull request
        |          fill in the PR checklist
CI must be green
        |
lead reviews  ->  lead merges (squash)  ->  delete the branch
```

- Branch names start with your first name: `akash/...`, `meghna/...`, `shaan/...`
- Keep pull requests small: one task each, ideally under a day's work.
- Start every work session with `git pull origin main` so you work on the latest code.

> GitHub cannot lock `main` on a free private repo, so this rule is an **agreement**, not
> something GitHub enforces. A direct push to `main` would show up in CI and in the nightly
> log.

## Daily report: by 10 PM, every working day

Comment on this week's **Standup** issue (label: `standup`). Copy this:

```
**Done today:** (link each pull request)
**Hours:**
**Tomorrow:**
**Blocked on:** (or "nothing")
```

Two minutes, four lines. "Blocked on" matters most: say it the same day, not on Friday.

The lead's 11:52 PM log reads these comments, plus everyone's pushed branches, so the whole
team's day lands in one note. **Work that isn't pushed or reported doesn't appear in it.**

## Rules everyone follows

Everything in [`../CLAUDE.md`](../CLAUDE.md) applies to every person and every AI agent. In
particular:

- **Never commit a secret.** Keys go in your own `.env`, which git ignores.
- **Never commit corpus data.** The practice dataset in `tests/fixtures/` stays small (under
  ~5 MB); anything bigger is shared outside git.
- **Interview notes are anonymised.** No names, phone numbers or emails of interviewees in
  the repo. Ever. Recordings never go in the repo.
- If you use Claude Code, it reads `CLAUDE.md` automatically. Read §1, §5 and §6 yourself
  once.

## Plans

- [**V1 plan**: all 16 weeks to the private beta](V1-PLAN.md)
- [Week 1: 13 to 17 Oct](WEEK-1.md) (day by day)
