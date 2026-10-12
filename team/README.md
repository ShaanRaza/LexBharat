# Team

| Person | Role | GitHub | Lane | Hours |
|---|---|---|---|---|
| **Shaan** | Co-founder, technical lead | `ShaanRaza` | **Data + Core**: search, the answer pipeline, the citation verifier. Reviews and merges everything | 4 h/day, Mon to Sat |
| **Akash** | Co-founder, technical | `mrharit` | **Platform**: API, database, login, server, the upload backend | 4 h/day, Mon to Sat |
| **Meghna** | Intern | `meghnarana-2016` | **Web**: every screen people see, plus formatting the test set | 3 h/day, Mon to Sat |
| **Ranveer** | Co-founder, lawyers and outreach | *not on GitHub yet* | **Lawyers + Outreach**: interviews, the advocate, counsel, Vaquill, beta users | When available |

Shaan, Akash and Meghna have tasks **every working day**. Ranveer has a task list **for each
week**. His work runs alongside the build and often unblocks it.

## What each lane owns

Separate folders mean nobody edits the same files as anyone else.

| Lane | Owns | Covers |
|---|---|---|
| **Data + Core** (Shaan) | `data/` `core/` `adapters/` `knowledge/` `tests/fixtures/` `evals/` scripts | The dataset lives on Shaan's SSD, so corpus work happens there. The 11-step pipeline and the verifier: the parts Shaan must be able to defend |
| **Platform** (Akash) | `api/` `infra/` `migrations/` `workers/` `pyproject.toml` | The API, the database, sign-in, the usage meter, the AWS server, and the upload backend (storage, OCR worker, hard delete) |
| **Web** (Meghna) | `web/` and the question files in `evals/` | Every screen: chat, citations, judgment and Act pages, sign-in, uploads, failure screens |
| **Lawyers + Outreach** (Ranveer) | `docs/research/` (interview notes), drafts for `legal/` | People outside the team. He doesn't need to write code; someone else commits his files if he isn't using git |

If you need to change a file outside your lane, say so in the standup first.

## First-time setup (each builder, once)

1. Your **own** Claude account with Claude Code. Logins are never shared.
2. Clone the repo and open it in Claude Code. It reads `CLAUDE.md` and the project skills by
   itself.
3. When Claude Code offers to install the **`claude-code-skills`** plugins (declared in
   `.claude/settings.json`), **accept**. They hold the specialist skills the plan refers to
   (`rag-architect`, `ai-security`, `a11y-audit`, …). The `impeccable` design skill is
   already inside the repo.
4. In Terminal, once: `gh auth login` with your own GitHub account. `/start-task` and
   `/finish-task` use it.
5. Your own `.env` (copy `.env.example`). Never commit it.

## One task, one session

Every task is a GitHub issue, sized to finish in **one Claude Code session**.

```
/start-task 12     Claude reads issue #12, makes the branch, explains the plan, waits for your yes
   ... build ...
/finish-task 12    Claude runs the checks for real, opens the PR ("Closes #12"),
                   ticks the verified items and comments a summary on the issue
```

Start the next task in a **new** session. Shaan merges the PR, which closes the issue.

## How work reaches `main`

`main` belongs to Shaan. **Nobody else pushes to it.**

```
make a branch      akash/upload-worker   or   meghna/chat-screen
        |          one small task per branch
open a pull request
        |          fill in the PR checklist
CI must be green
        |
Shaan reviews  ->  Shaan merges (squash)  ->  delete the branch
```

- Branch names start with your first name: `shaan/...`, `akash/...`, `meghna/...`
- Keep pull requests small: one task each, ideally under a day's work.
- Start every session with `git pull origin main`.

> GitHub cannot lock `main` on a free private repo, so this is an **agreement**, not
> something GitHub enforces. A direct push to `main` shows up in the nightly log.

## Daily report: by 10 PM

Comment on this week's **Standup** issue (label `standup`):

```
**Done today:** (link each pull request)
**Hours:**
**Tomorrow:**
**Blocked on:** (or "nothing")
```

- **Shaan, Akash, Meghna:** every working day.
- **Ranveer:** every day he works on LexBharat. Once he has a GitHub account, he posts in the
  same issue. Until then, he sends the same four lines to Shaan, who pastes them in.

Shaan's 11:52 PM log reads these comments and everyone's pushed branches, so the whole team
lands in one note. **Work that isn't pushed or reported doesn't appear.**

## Rules everyone follows

Everything in [`../CLAUDE.md`](../CLAUDE.md) applies to every person and every AI agent:

- **Never commit a secret.** Keys go in your own `.env`, which git ignores.
- **Never commit corpus data.** `tests/fixtures/` stays under about 5 MB.
- **Interview notes are anonymised.** No names, phone numbers or emails of the people
  interviewed. Recordings never go in the repo.
- If you use Claude Code, it reads `CLAUDE.md` itself. Read §1, §5 and §6 yourself once.

## Plans

- [**V1 plan**: 11 weeks to the MVP, beta from early January](V1-PLAN.md)
- [Week 1: 13 to 17 Oct](WEEK-1.md): start everything
- [Week 2: 19 to 24 Oct](WEEK-2.md): search works
- [Week 3: 26 to 31 Oct](WEEK-3.md): answers are verified, then the re-plan
- [Week 4: 2 to 7 Nov](WEEK-4.md): the whole engine, then the decision point
- [**Month 2**: Weeks 5 to 8, 9 Nov to 5 Dec](MONTH-2.md): measured, uploads, safety, the real server
  - [Week 5](WEEK-5.md) · [Week 6](WEEK-6.md) · [Week 7](WEEK-7.md) · [Week 8](WEEK-8.md)
- [**Month 3**: Weeks 9 to 11, 7 to 26 Dec](MONTH-3.md): hardening, MVP done, buffer; the beta from 4 Jan
  - [Week 9](WEEK-9.md) · [Week 10](WEEK-10.md) · [Week 11](WEEK-11.md)

Weeks 2 to 11 were written ahead of time. Each Saturday they're adjusted to what really got
done, and the GitHub issues change with them.
