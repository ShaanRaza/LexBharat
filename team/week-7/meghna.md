# Meghna: Week 7 (Web), 3 h a day

**Theme: the law maps, and deleting things properly.** Most of your week goes into a
different kind of work: drafting the **law maps**, the tables that tell the product which
new section replaced which old one (IPC → BNS, CrPC → BNSS, Evidence Act → BSA, from
1 July 2024). Old judgments don't know the law changed, so these maps fix answers that
search alone gets wrong. You also build the screens for deleting a document, deleting an
account and downloading your data.

> **Tue 24 Nov is Guru Nanak Jayanti.** If you take it off, **CrPC → BNSS (3.1) moves to
> Thursday** and **Evidence Act → BSA (4.1) to Saturday**. If the maps run long, the V1
> plan's drop list allows **IPC → BNS only**; say so in the standup.

---

## Before Day 1

- [ ] Read [`../../knowledge/index.md`](../../knowledge/index.md), especially the trust
      rules and the file header
- [ ] Find the **official correspondence tables** (old section → new section) for all three
      pairs, published by the government. Save the links; they're the source

---

## Day 1, Mon 23 Nov: delete a document

### 1.1 Delete (3 h)
On the documents list and the viewer:
- A confirmation that says plainly **what is deleted now** (the file, its text, the search
  data) and that **backups age out on their normal cycle** (`docs/RETENTION.md`)
- Wording from the strings file. The backup sentence isn't in `docs/UX-COPY.md` yet, so ask
  Shaan for it on Monday morning
- After deleting: the document disappears, and any chat about it says the document was
  deleted

**Branch:** `meghna/delete-document`

---

## Days 2 to 4: the law maps

### How every map is built
One note per pair in `knowledge/law-maps/`, for example `ipc-to-bns.md`:
- The front matter from `knowledge/index.md`, with **`status: draft`**. Only the advocate
  makes it `reviewed`
- A table: old section, its title, new section(s), its title, a note where it isn't one to
  one (split, merged, dropped, new)
- **Every row links to the `record_id` of both sections** in the Act data, so the checker
  can confirm they exist. Use a small script to look the IDs up; don't type them

**Ask Claude Code:**
> Using the official correspondence table at <link>, draft knowledge/law-maps/ipc-to-bns.md per knowledge/index.md. Look up each section's record_id from act_sections with a script; don't type IDs. Mark rows that aren't one-to-one. status: draft. Then run knowledge/check.py and show me the result.

### Day 2, Tue 24 Nov (Guru Nanak Jayanti): IPC → BNS (3 h)
The most important map: criminal law questions hit it constantly.

### Day 3, Wed 25 Nov: finish IPC → BNS; CrPC → BNSS (3 h)

### Day 4, Thu 26 Nov: Evidence Act → BSA; run the checker (3 h)
- Draft the third map
- Run Shaan's `knowledge/check.py` on all three. Every record must exist. Fix or mark
  every failure
- **Check first** that the Evidence Act and the BSA are in the Act data at all (**unverified**).
  If one is missing, say so in the standup; don't invent rows

**Branch:** `meghna/law-maps`

---

## Day 5, Fri 27 Nov: delete account + export

### 5.1 Screens (3 h)
On the account page:
- **Delete my account**: explains exactly what's deleted, what's kept for legal reasons (the
  short list from Akash's route), and that it **can't be undone**. The user types a
  confirmation word
- **Download my data**: starts the export, says it may take a few minutes, then offers the
  download link (which expires quickly)

**Branch:** `meghna/account-delete-export`

---

## Day 6, Sat 28 Nov: the maps go to the advocate

- [ ] Final law-map PR to Shaan; checker green (1.5 h)
- [ ] A **readable copy** of the three maps (plain tables) for Ranveer to send to the
      advocate (45 min)
- [ ] Standup (15 min)

---

## Done by Saturday

- [ ] Delete document, delete account and export screens, with plain explanations
- [ ] Three law maps drafted, every row linked to real records, checker green
- [ ] Readable copy sent to Ranveer for the advocate
