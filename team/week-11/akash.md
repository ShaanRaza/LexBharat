# Akash: Week 11 (Buffer, Christmas), about 2 h a day

**Theme: buffer.** No new features. Fix what slipped, make sure the server is ready to be
left alone over the holidays, and check you can get it back if it falls over.

> **Fri 25 Dec is Christmas: off.**

---

## Days 1 to 3: catch up (about 5 h)

Production fixes that didn't make the release, **only if they're small and safe**. Every one
through a pull request, the tests and the deploy workflow.

**Branch:** `akash/buffer`

---

## Day 4, Thu 24 Dec: ready to be left alone

### 2.1 Before the holidays (2 h)
- [ ] **Backups**: last night's PostgreSQL and Qdrant backups exist; restore last night's
      PostgreSQL into a scratch database once more and count rows
- [ ] **Disk**: under 70%, with room for two weeks of uploads and logs
- [ ] **Certificates**: HTTPS doesn't expire before February
- [ ] **Alerts**: send one test alert to whoever is on the holiday rota that day
- [ ] **Costs**: AWS billing alarm set; the month's projection noted
- [ ] **The rebuild runbook** is where the person on cover can find it

---

## Day 6, Sat 26 Dec: wrap (1 h)

- [ ] Anything still open from the "Ready for the beta" list: tell Shaan, with a date
- [ ] Standup

---

## Done by Saturday

- [ ] Slipped fixes in, or moved to January out loud
- [ ] Backups restored once more; disk, certificates and alerts checked
- [ ] Holiday cover knows where the runbook is
