# Shaan: Week 7 (Data + Core + Lead), 4 h a day

**Theme: uploads are safe, and the first full test run.** By Saturday reviewed knowledge
notes can reach answers **without ever becoming citations themselves**, all 200 test
questions have run once, and you know the worst failures to fix next week.

Pipeline steps touched: **3 (decide)** picks knowledge notes; **8 (answer)** reads them as
background; **9 (verify)** is unchanged and must stay that way.

Two careful reviews this week: Akash's **isolation tests** and **hard delete**. Both are
on the "never dropped" list.

> **Tue 24 Nov is Guru Nanak Jayanti.** If you take it off, **the check script (2.1) moves
> to Wednesday morning** and **the coverage notes (3.2) to Saturday**.

> **Sat 28 Nov:** the legal opinion is due, and you **start the long upload of the search
> collection to S3**. Don't leave it to Week 8.

---

## Day 1, Mon 23 Nov: how notes reach an answer

### 1.1 Decide first (1 h)
CLAUDE.md: **a note never counts as a citation by itself**; the answer cites the record the
note points to, and the verifier checks it. But check 1 fails any record that wasn't
**retrieved this turn**. So how does a note's record get into the answer?

| Option | Effect |
|---|---|
| **A. Note's records join the passages** (recommended) | When a note applies, fetch the records it lists and add them to the passages, inside the limit of 8 (they replace the lowest-ranked). They get S-labels and are verified like any other |
| B. Background only | The model can use the note for context but can only cite what search found. Simpler, but a law-map answer may have nothing to cite |

Record your choice with `/decision`.

### 1.2 `core/knowledge.py` (2.5 h)
Loads `knowledge/**/*.md`, reads the front matter (`knowledge/index.md`, File header), and
keeps **only `status: reviewed`**. A note with a missing field or no `source_records` is
skipped and reported, never used.

**Branch:** `shaan/knowledge-notes`

---

## Day 2, Tue 24 Nov (Guru Nanak Jayanti): the note checker

### 2.1 `knowledge/check.py` (3 h)
For every note, draft or reviewed:
- [ ] Every `source_records` ID exists in the collection
- [ ] Every quote in the note appears in its record's text
- [ ] Front matter complete
CI runs it whenever `knowledge/` changes, and fails on any broken note. Meghna runs it on
the law maps on Thursday.

**Branch:** `shaan/knowledge-check`

---

## Day 3, Wed 25 Nov: notes in the pipeline

### 3.1 The decide step picks notes (2 h)
Decide chooses which notes apply (a few at most). The answer prompt shows them as
**"Background notes"**, kept apart from the passages. Implement the option you chose on
Monday.

Tests: a note's text never appears as a citation; with option A, the note's records go
through all four checks like any passage.

### 3.2 Notes only you can write (1.5 h)
- `knowledge/coverage/what-v1-covers.md`: Supreme Court + Central Acts, snapshot
  v2026.08, what isn't covered. From the PRD
- `knowledge/terms/court-hierarchy.md`
Both owner-reviewed: `status: reviewed`, `reviewed_by: Shaan`.

**Branch:** `shaan/knowledge-in-pipeline`

---

## Day 4, Thu 26 Nov: the first full 200-question run

### 4.1 Run it (3 h)
`evals/run.py` on all of `evals/questions.jsonl`, with the settings chosen in Week 5.
- No advocate sign-off yet? Run anyway, and label the run **"provisional"**
- Cost: about 200 answers. Check the estimate before starting

### 4.2 First look (1 h)
The two launch numbers: **verified-citation rate (target 98%+)** and **answers with a
removed citation (target under 0.5%)**. Then the traps: **every trap answered confidently is
a serious failure**, whatever the overall score.

---

## Day 5, Fri 27 Nov: the fix list + two careful reviews

### 5.1 The fix list (2 h)
`evals/runs/<date>-full-200/fix-list.md`: the worst 20 failures, grouped by cause (search
missed it / gate dropped it / answer wrong / verifier passed something it shouldn't /
scope check wrong). Ranked. This **is** next week's plan.

### 5.2 Review Akash's isolation and delete work (2 h)
Don't rubber-stamp it:
- [ ] Every upload path tested with **two users**
- [ ] The shared function **raises** without a `user_id`
- [ ] Hard delete removes **all three**: the file, the text, the vectors
- [ ] The nightly check would actually find a leftover (it was tested with a planted one)

---

## Day 6, Sat 28 Nov: the legal opinion + start the big upload

### 6.1 Start the search collection upload (1 h, then it runs)
Akash creates the backups bucket by today. Then:
- Take a **Qdrant snapshot** of the search collection on the SSD
- Upload it to the S3 backups bucket in Mumbai, with `caffeinate -i` and a log file
- It's about 6 to 20 GB (Estimate), so **it may take hours**. Keep LAWSSD plugged
  in and Colima running until it finishes; check it on Sunday
- Afterwards: `colima ssh -- sudo fstrim /var/lib/docker`

### 6.2 Read the legal opinion (1.5 h)
If it's arrived: read it, list what it means for uploads, consent and the advice notice,
and bring that to next Saturday's go/no-go. If it hasn't: say so in the standup, and the
go/no-go plans for the warning.

### 6.3 Wrap (30 min)
"Done means" in [README.md](README.md); adjust Week 8 issues; open **Standup: Week 8**.

---

## Pull requests to expect

| Day | From Akash | From Meghna | Yours |
|---|---|---|---|
| 1 | `akash/isolation-tests` (**careful**) | `meghna/delete-document` | `shaan/knowledge-notes` |
| 2 | `akash/hard-delete` (**careful**) | | `shaan/knowledge-check` |
| 3 | `akash/leftover-check` | | `shaan/knowledge-in-pipeline` |
| 4 | `akash/delete-account` | `meghna/law-maps` (draft PR, early look) | |
| 5 | `akash/export` | `meghna/account-delete-export` | `shaan/first-full-run` |
| 6 | `akash/aws-basics` | `meghna/law-maps` (final) | |

## Done by Saturday

- [ ] How notes reach answers decided; only reviewed notes loaded
- [ ] Note checker in CI
- [ ] Notes in the pipeline; never a citation themselves (tested)
- [ ] Coverage and court-hierarchy notes written and owner-reviewed
- [ ] **First full 200-question run**; fix list ranked
- [ ] Isolation tests and hard delete reviewed carefully
- [ ] **Search collection upload to S3 started**; legal opinion read (or its absence reported)
