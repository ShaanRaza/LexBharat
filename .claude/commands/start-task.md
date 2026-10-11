---
description: Start one task from its GitHub issue. One task = one issue = one branch = one pull request = one Claude session.
argument-hint: "<issue number>"
---

# /start-task

Start work on issue **#$ARGUMENTS**. This session does **this task and nothing else**.

## 1. Read the task
- `gh issue view $ARGUMENTS --repo ShaanRaza/LexBharat --comments`
- Note the **lane label**, the **branch name**, the **done-when checklist**, the deadline,
  and the linked plan file. Read that file's section for this task.
- If the issue is closed, has no done-when checklist, or isn't assigned to the person
  you're working with, **stop and say so**.

## 2. Check it's ready to start
- Look for "Waits on" in the issue. If what it waits on isn't merged yet, say so plainly
  and suggest what can be done meanwhile (for example, working against fixtures).
- Check the task stays inside its lane's folders (see `team/README.md`). If it would touch
  another lane's files, flag it before writing any code.

## 3. Set up the branch
```bash
git checkout main && git pull origin main && git checkout -b <branch name from the issue>
```
If the branch already exists (a previous session), switch to it instead and read its
commits to see what's already done.

## 4. Mark it started
```bash
gh issue edit $ARGUMENTS --repo ShaanRaza/LexBharat --add-label in-progress
```

## 5. Say the plan in plain words, then wait
Before writing code, explain in a few short bullets:
- what you'll build, and which files you'll touch
- which of the 11 pipeline steps it touches, if any
- how you'll prove it works (the tests, or what to look at)
- anything in `CLAUDE.md` §5 or §6 that applies (verifier, isolation, secrets, data you
  must not trust)

**Wait for a yes** before starting, because of CLAUDE.md §8 "Who leads the design". For
pure setup work (config, lint, scaffolding), a short plan is enough.

## Scope rule
If the task turns out bigger than one session, **don't stretch it.** Finish a clean,
working slice, then propose a follow-up issue for the rest, with its own done-when list.
Ask before creating it.

When the work is done, run `/finish-task $ARGUMENTS`.
