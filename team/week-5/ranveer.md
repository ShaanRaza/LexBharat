# Ranveer: Week 5 (Lawyers + Outreach)

**This week starts the legal paperwork that decides whether the beta can open.** Nobody can
sign up without a consent notice reviewed by counsel, and counsel's review must be back by
**Week 9**. Drafts go out this week.

> **Mon 9 Nov is Govardhan Puja and Wed 11 Nov is Bhai Dooj.** Lawyers will be slow to
> reply this week. Send early, and chase next week.

---

## This week at a glance

| # | Task | By | Why it matters |
|---|---|---|---|
| 1 | **Draft the five user-facing legal documents** | Thu 12 Nov | Sign-up can't work without them |
| 2 | **Send them to counsel**, with the retention questions | **Fri 13 Nov** | Review must be back by **Week 9**, or the beta can't open |
| 3 | Legal opinion: check it's on track for **28 Nov** | Tue 10 Nov | Uploads for real client documents depend on it |
| 4 | Voyage: final chase; tell Shaan where it stands | Fri 13 Nov | Week 6 picks the upload embedding model from this |
| 5 | Chase the advocate's **sign-off on the 200 questions** | Fri 13 Nov | Due Week 6 |
| 6 | Ask the advocate to **book time for the law maps** | Fri 13 Nov | Sent to them Week 7; needed back by Week 9 |
| 7 | **Beta recruitment: the plan and the form** | Sat 14 Nov | Recruiting starts Week 6 |

---

## 1. The five documents (Thu 12 Nov)

Use Claude (the app is fine) to draft each one **from our own docs**, then read every line.
Save them as drafts; Shaan commits them to `legal/`.

| Document | Draft from | Must say |
|---|---|---|
| `consent-notice-v1-draft.md` | `docs/SECURITY-AND-COMPLIANCE.md` (DPDP), `docs/RETENTION.md` | What we collect, why, how long we keep it, how to withdraw |
| `privacy-policy-v1-draft.md` | The "Where data goes" table in `docs/SECURITY-AND-COMPLIANCE.md` | Every vendor, what it receives, where it processes |
| `terms-of-service-v1-draft.md` | The same, plus `docs/PRODUCT.md` | Information, not legal advice. Who's responsible for uploaded client documents (**a question for counsel**) |
| `upload-warning-v1-draft.md` | "Privilege" in `docs/SECURITY-AND-COMPLIANCE.md` | Plain warning about privileged material, before every upload |
| `not-legal-advice-v1-draft.md` | `docs/UX-COPY.md` (standing notices) | The standard notice and the stronger personal-advice version |

**Leave every retention period blank**, marked "for counsel". Don't invent periods.

## 2. Send to counsel (Fri 13 Nov)

> Dear [Name], attached are drafts of our consent notice, privacy policy, terms of service, upload warning and not-legal-advice notice. Could you review them for DPDP compliance and the information/advice line? We also need your advice on **retention periods** for each type of data (listed in the attached table), which the consent notice must state. We need the reviewed versions by **[date in Week 9]** to open a private beta. Could you confirm the fee and timeline? Regards, Ranveer

Attach the table from `docs/RETENTION.md`.

## 3. Legal opinion on track (Tue 10 Nov)

A short, polite check: is **28 November** still realistic? If not, tell Shaan **that day**.
Without it, uploads open with a "don't upload client documents yet" warning.

## 4. Voyage (Fri 13 Nov)

One last chase. Then tell Shaan plainly: **terms received / promised by a date / no
answer**. If there's no answer, uploads will use the free local model (bge-m3) on our own
server. That's fine; it just needs deciding by Monday.

## 5 and 6. The advocate

- [ ] Gently chase the **200-question sign-off** (due Week 6)
- [ ] Ask them to keep **a few hours in Weeks 7 to 9** for reviewing the law maps (IPC →
      BNS, CrPC → BNSS, Evidence Act → BSA)

## 7. Beta recruitment plan (Sat 14 Nov)

Target: **20 law students and 10 advocates**, starting Mon 4 Jan. Interviewees who said
yes to early access come first.
- [ ] A short sign-up form: role, city, court or college, device, what they research most.
      **No questions about their clients**
- [ ] A list: interviewees first, then their introductions
- [ ] One message to send next week. **Promise "early access", never a date**

---

## Done by Saturday 14 Nov

- [ ] Five drafts written and read line by line
- [ ] Sent to counsel with the retention table; fee and date asked
- [ ] Legal opinion date confirmed (or the delay reported)
- [ ] Voyage status told to Shaan
- [ ] Advocate chased for the sign-off; law-map time requested
- [ ] Beta plan, form and list ready
