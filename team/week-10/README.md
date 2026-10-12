# Week 10 in detail: Mon 14 Dec to Sat 19 Dec 2026

**Theme: MVP done.** Month overview: [`../MONTH-3.md`](../MONTH-3.md).

| Person | File | Hours |
|---|---|---|
| Shaan | [shaan.md](shaan.md) | 4 h a day |
| Akash | [akash.md](akash.md) | 4 h a day |
| Meghna | [meghna.md](meghna.md) | 3 h a day |
| Ranveer | [ranveer.md](ranveer.md) | When available, with deadlines |

**Week goal:** the product stops changing. The final 200-question run on a frozen setup;
bug bash 2 with the whole team; the welcome, feedback form and landing page; the uploads
switch set; every alert reaching a person; the **beta go/no-go on Friday**; `v0.1.0-beta`
released on Saturday.

**Pipeline steps touched:** none by design. Serious fixes only.

**Tracking:** every task is a GitHub issue in the
[Week 10 milestone](https://github.com/ShaanRaza/LexBharat/milestone/10). **Status lives in the issues.**

| Person | Issues |
|---|---|
| Shaan | #186 last fixes · #187 final run · #188 breach playbook · #189 beta go/no-go · #193 tag release |
| Akash | #194 prod fixes · #190 uploads switch · #191 alerts · #192 rollback + release |
| Meghna | #195 bug bash 2 · #196 welcome · #197 send feedback · #198 landing page |
| Ranveer | #199 invite + kickoffs + support plan · #200 bug bash + go/no-go |

> **Written ahead of time.** Adjusted on Sat 12 Dec to match what really got done.

---

## The freeze

| From | Rule |
|---|---|
| **Tue 15 Dec** | The setup is frozen: models, threshold, switches, prompts, notes |
| **Thu 17 Dec** | Only **serious** fixes merge: a wrong citation, a trap answered confidently, a privacy hole, a crash, lost work |
| **Sat 19 Dec** | `v0.1.0-beta` deployed. Nothing else until January, except an emergency |

## Who waits on whom

| Who is waiting | For | From | Needed by |
|---|---|---|---|
| Shaan, Day 2 | Everyone's last non-serious fixes merged | All | End of Day 1 |
| Meghna, Day 4 | General feedback route | Akash | Day 2 |
| Akash, Day 3 | The Week 8 uploads outcome | Shaan | Already recorded |
| Everyone, Day 5 | The final run read, and the checklist with evidence | Shaan | Day 5 morning |
| Ranveer, Day 3 | The product name to use in the invite | Shaan | Day 3 |
| Akash, Day 6 | Beta limit and uploads switch values | Shaan | Day 5 |

## Friday: the beta go/no-go (all four, 1 hour)

Every box in the "Ready for the beta" list ([`../MONTH-3.md`](../MONTH-3.md)), ticked with
evidence or not. **Go / go smaller / no-go.** A single **confirmed fabricated citation** in
the final run is a no-go until it's fixed. Shaan decides; it's recorded with `/decision`.

## Done means, by Saturday 19 Dec

- [ ] Final 200-question run on a frozen setup; read; zero confirmed fabricated citations
- [ ] Bug bash 2 with the whole team; serious bugs fixed
- [ ] Welcome screens, "send feedback", simple landing page (not indexed)
- [ ] Uploads switch built for the decided outcome; every alert received once; rollback tested
- [ ] Breach playbook complete
- [ ] **Beta go/no-go recorded**; beta limit set
- [ ] Invite drafted; kickoff calls booked; support plan written
- [ ] **`v0.1.0-beta` tagged and deployed**; **Standup: Week 11** opened
