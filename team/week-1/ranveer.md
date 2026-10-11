# Ranveer: Week 1 (Lawyers + Outreach)

You don't write code. Your work is the part **nobody else can do**: getting answers from
lawyers and outside companies. Two of this week's requests are the **slowest things in the
whole plan**, so they go out first.

No fixed daily hours; work to the **deadlines** below. On every day you work, send Shaan
four lines (WhatsApp is fine) and he posts them in the standup:

```
Done today:
Hours:
Tomorrow:
Blocked on:
```

---

## This week at a glance

| # | Task | Send / finish by | Why it matters |
|---|---|---|---|
| 1 | **Legal opinion request** to the advocate | **Wed 14 Oct** | Uploads can't be opened to real client documents without it. Needed by **Week 8** |
| 2 | **Written terms request** to Voyage | **Wed 14 Oct** | Uploaded text goes to Voyage for search. Needed by **Week 6** |
| 3 | Three questions to **Vaquill** | Thu 15 Oct | Licence and data questions. Doesn't block the beta |
| 4 | **Interview script** | Wed 14 Oct | Every interview uses the same questions |
| 5 | **List of 20 people** to interview | Wed 14 Oct | 8 district-court advocates, 6 High Court advocates, 6 law students |
| 6 | **Book 5 interviews**; do the first 2 or 3 | Book by Fri 16; do by Sat 17 | They decide prices, Hindi, phone vs desktop, and uploads |
| 7 | Start the **real questions** list | All week | 100 of the 200 test questions come from here |
| 8 | **GitHub account**; send Shaan the username | Tue 13 Oct | So you can read the plan and post your own standups |

---

## 1. Legal opinion request (send by Wed 14 Oct)

To the advocate advising LexBharat. Change anything that doesn't sound like you.

> **Subject:** Request for a written opinion: AI legal research tool (LexBharat)
>
> Dear [Name],
>
> We're building an AI legal research tool for Indian advocates and law students. It answers questions from Supreme Court judgments and Central Acts, and shows a checked citation for every point. Users will also be able to upload their own documents (for example a bail application or an agreement) and ask questions about them.
>
> Before we open this to real users, we'd like your written opinion on:
>
> 1. **Privilege.** If an advocate uploads a client's document to a third-party tool like ours, could that weaken privilege under Section 132 of the Bharatiya Sakshya Adhiniyam, 2023? What safeguards would you expect from us?
> 2. **DPDP roles.** For uploaded client documents, is the advocate the data fiduciary and are we a processor? What must our terms say? How should we treat third parties named in uploads, such as opposing parties and witnesses?
> 3. **Information versus advice.** Our free tier may be used by non-lawyers. Does our "information, not legal advice" approach hold, and is there a practice-of-law concern?
> 4. **BCI Rule 36.** We won't list, rank or recommend advocates. Could naming an advocate advisor on our website count as advertising?
> 5. **Retention.** How long should we keep account data, chats, uploads and the audit log? What must we keep after a user deletes their account?
>
> Could you share a quote and a timeline? We'd need the opinion by **28 November** at the latest.
>
> Separately, we'd value your help over the next few weeks: agreeing a checking rule, reviewing a set of test questions, and reviewing tables mapping old IPC, CrPC and Evidence Act sections to the new BNS, BNSS and BSA sections.
>
> Regards,
> Ranveer [Surname], Co-founder, LexBharat

**Done when:** sent, and the reply date noted in your daily update.

---

## 2. Voyage written terms (send by Wed 14 Oct)

To Voyage AI support or sales.

> **Subject:** Data terms for document text sent to the embeddings API
>
> Hello,
>
> We're building a legal research product in India using voyage-4 embeddings and rerank-2.5-lite. Some of the text we embed will come from documents our users upload, which may include confidential client material.
>
> Before we send any such text, could you confirm in writing:
>
> 1. Is text sent to the embeddings and rerank APIs **ever used to train** your models?
> 2. **How long is it kept**, and is it deleted after processing?
> 3. **Where is it processed and stored** (which countries)?
> 4. Is the first **200 million tokens free** a one-time allowance or monthly?
>
> Thank you,
> Ranveer [Surname], Co-founder, LexBharat

**Done when:** sent. If there's no reply within a week, chase.

---

## 3. Vaquill: three questions (send by Thu 15 Oct)

To `contact@vaquill.ai`. The background is in
[`../../docs/DATASET.md`](../../docs/DATASET.md) under "Dependence on Vaquill".

> **Subject:** Questions about open-india-law (commercial use, updates, checksums)
>
> Hello,
>
> We're building a legal research product on the open-india-law dataset (snapshot v2026.08), crediting it as "Data: Open India Law by Vaquill AI, CC BY 4.0".
>
> Could you help with a few questions?
>
> 1. Can we confirm in writing that **commercial use** under CC BY 4.0 is fine for our product?
> 2. Does the India **API licence** allow caching responses and showing them to our users, including on public pages that search engines index?
> 3. What does **bulk or daily-sync licensing** cost for the India judgment corpus, and does it include incremental updates?
> 4. Is a **judgments endpoint** planned for the India API?
> 5. Could you publish **per-file checksums**? Only one of the 75 files currently has one.
> 6. Which judgment count is correct: 12.8M+, 32.5M chunks, or about 15.7M case records?
>
> Thank you,
> Ranveer [Surname], Co-founder, LexBharat

---

## 4. Interview script (by Wed 14 Oct)

30 to 45 minutes. Built from the assumptions in
[`../../docs/METRICS.md`](../../docs/METRICS.md). **Ask; don't sell.**

**Start (2 min):** thank them. Say notes are anonymous and no recording happens without
their yes. Say they'll get free access later as thanks.

| Part | Ask | What we're testing |
|---|---|---|
| **Their work (8 min)** | Walk me through the last time you researched a legal point. Which tools? What frustrated you? | Whether free tools like Indian Kanoon are already enough |
| **Real questions (8 min)** | What questions did you research last week? *(Write them down word for word, with no names)* | These become our test questions |
| **Device (3 min)** | Phone or laptop when you research? What connection, in court? | Whether to build phone-first |
| **Trust (8 min)** | Show 2 or 3 sample answers with "Record found in dataset" ticks. *"What would you still check yourself?"* | Whether the tick actually earns trust |
| **Uploads (5 min)** | Would you upload a client's document to ask questions about it? What would worry you? | Whether uploads are wanted, and what the warning should say |
| **Language (2 min)** | Do you research in English, Hindi, or both? | Whether Hindi moves up |
| **Price (5 min)** | Would you pay ₹499 a month? What about ₹199 for students? What do you pay now? | Pricing, before we build payments |
| **Close (2 min)** | Can we contact you when early access opens? Who else should we talk to? | Beta recruiting, and more interviews |

**Student version:** swap "court" for "moot court and exams", and ask about ₹199.

## 5. Recruitment message

> Hi [Name], I'm Ranveer, co-founder of LexBharat. We're building a legal research tool for Indian advocates and students, and I'd love 30 minutes of your time to learn how you research today. No pitch: we want to hear what's hard. You'd get free early access as thanks. Would [day] or [day] suit you?

## 6. Interview notes: one file per interview, anonymous

Send to Shaan or Meghna, who save them as `docs/research/interview-01.md` and so on.

```
Interview #:            Date:
Role:                   (district-court advocate / High Court advocate / law student)
City size:              (metro / tier 2 / tier 3)
Device and connection:
Tools used today:
Biggest frustration:
Real questions they asked:   (word for word, no names)
Reaction to the ticks:
Would upload client documents?  Why / why not:
Language:
Price reaction:
Open to the January beta?
```

**Never write down** names, phone numbers, emails, firm names or anything that identifies
a client or a case they're handling.

---

## Please don't

- **Promise dates or features in public.** The plan can change.
- **Use the name "KanoonBuddy" in public branding.** The trademark search isn't done.
- **Name, rank or recommend any advocate**, even in passing (BCI Rule 36).
- **Record an interview** without a clear yes.
- **Share anyone's contact details** in the repo, the standup or a group chat.

## Done by Saturday 17 Oct

- [ ] Legal opinion request **sent**
- [ ] Voyage request **sent**
- [ ] Vaquill email **sent**
- [ ] Interview script ready; list of 20 people
- [ ] 5 interviews booked; first 2 or 3 done, notes sent
- [ ] GitHub username sent to Shaan
