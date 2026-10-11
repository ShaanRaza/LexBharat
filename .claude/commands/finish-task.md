---
description: Finish the current task - check it for real, open the pull request, and update the GitHub issue. Never closes the issue itself; merging does.
argument-hint: "<issue number>"
---

# /finish-task

Finish issue **#$ARGUMENTS**. **Done means proven, not claimed.** If any check fails or
can't be run, the task is **not finished**: say so plainly and stop before step 4.

## 1. Run the checks for real, and show the output
- Python work: `ruff format --check . && ruff check . && pytest -q`
- Web work (in `web/`): `npm run lint && npx tsc --noEmit && npm run build`
- Anything with a screen: screenshots at 375 px and 1280 px
- If a check can't run (for example no database, or no drive plugged in), write
  **"not verified"** and why. Never write "passes" for something that didn't run.

## 2. Walk the done-when checklist
For each item in the issue's checklist, write **verified** (with the evidence: the test
name, the command output, the screenshot) or **not verified** (with the reason).

## 3. Safety checks before pushing
- `git diff main --stat`: the change stays inside this task's lane and scope
- No secret in the diff: `git diff main | grep -nE "sk-|ghp_|gho_|AKIA|password\s*="` finds nothing
- No corpus data beyond `tests/fixtures/` (keep that under about 5 MB)

## 4. Open the pull request
```bash
git push -u origin HEAD
```
Open a PR whose body starts with **`Closes #$ARGUMENTS`** and fills in
`.github/pull_request_template.md`. Merging it closes the issue automatically. **Only
Shaan merges.**

## 5. Update the issue
1. **Tick the checklist** items you verified (edit the issue body: `- [ ]` → `- [x]`
   for verified items only).
2. **Comment** with a plain-language summary:
   ```
   **Done in this session**
   - What was built, in plain words
   - Files: path:line for the important parts
   - How it was checked: test names / command output summary / screenshots
   - Not verified: (anything, with the reason) or "nothing"
   - Left for later: (anything, with a proposed follow-up issue) or "nothing"
   - PR: #<number>
   ```
3. Labels: `gh issue edit $ARGUMENTS --repo ShaanRaza/LexBharat --remove-label in-progress --add-label in-review`

## 6. Close the session
Tell the person, in two or three plain sentences: what's done, what's waiting on Shaan's
review, and what the next task in their week file is. **Start the next task in a new
session.**
