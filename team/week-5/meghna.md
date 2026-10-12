# Meghna: Week 5 (Web), 3 h a day

**Theme: the upload screens.** By Saturday a user can pick a file, see the limits and the
privilege warning **before** uploading, watch it upload on a weak connection, and follow
its status until it's ready or has failed with a clear reason.

Uploads stay **switched off for real users** until Week 8. Build them fully anyway.

> **Mon 9 Nov is Govardhan Puja: light day.** **Wed 11 Nov is Bhai Dooj.** If you take it
> off, **upload progress (3.1) moves to Thursday** and the **documents list (5.1) to
> Saturday**. Say so in the standup.

---

## Before Day 1

- [ ] Anything left from Month 1 first, especially real sign-in and consent
- [ ] Read the Uploads section of [`../../docs/ARCHITECTURE.md`](../../docs/ARCHITECTURE.md)
      and "Upload security" in
      [`../../docs/SECURITY-AND-COMPLIANCE.md`](../../docs/SECURITY-AND-COMPLIANCE.md)

**For testing, upload only public documents**: judgment PDFs from the dataset's `pdf_url`
links, or a sample agreement written for testing. **Never a real client document.**

---

## Day 1, Mon 9 Nov (Govardhan Puja): light, about 1 h

### 1.1 Sketch the flow (1 h)
With **`impeccable`**: every state of an upload on one page (choose → warning → uploading →
processing → ready / failed), at 375 px and 1280 px. Agree it with Shaan in the standup
before building.

---

## Day 2, Tue 10 Nov: the upload screen

### 2.1 "My documents" page (3 h)
- **Limits shown before choosing a file**: maximum size and pages, in plain numbers. They
  come from the API, not typed into the website, because Week 6 changes them
- **The privilege warning**, every time, before the upload starts. Its wording comes from
  `legal/upload-warning`, which counsel is reviewing, so show the **"Draft"** mark until
  it's final
- File picker plus drag and drop on laptops. PDF and Word only
- Too big or the wrong type → say so **before** uploading anything

**Branch:** `meghna/upload-screen`

---

## Day 3, Wed 11 Nov (Bhai Dooj): the upload itself

### 3.1 Upload with progress (3 h)
- Ask the API for a link, then send the file **straight to storage** with a progress bar
- Big files go in parts, so a dropped connection **resumes** instead of starting again
- Tell the API when it's done (`/complete`)
- Leaving the page mid-upload asks "are you sure?"

**Branch:** `meghna/upload-progress`

---

## Day 4, Thu 12 Nov: status steps

### 4.1 Status (3 h)
Uploaded → extracting text → indexing → ready, shown as steps, checking every few
seconds while it's working (and stopping once it's ready or failed).

| Failure | What the user sees (wording from `docs/UX-COPY.md` through the strings file) |
|---|---|
| Unreadable scan | "We could not read this file. Try a clearer scan or paste the text." Plus: **nothing was charged** |
| Too long / too big | The limit, in plain numbers |
| Not a PDF or Word file | Which types are accepted |

**Branch:** `meghna/upload-status`

---

## Day 5, Fri 13 Nov: the documents list

### 5.1 List (2.5 h)
`GET /documents`: name, pages, status, date; "load more" paging. "Ask about this document"
on ready ones (it opens the document chat, which arrives in Week 6; disabled until then).
Delete comes in Week 7.

### 5.2 When uploads are off (30 min)
With `FEATURE_UPLOADS` off, "My documents" is **hidden from the navigation**, and opening
its address shows a plain "not available yet" page.

**Branch:** `meghna/documents-list`

---

## Day 6, Sat 14 Nov: phone pass + numbers

- [ ] The whole upload flow at 375 px, and on "Slow 3G" in the browser tools (1.5 h)
- [ ] Planned vs done for Weeks 1 to 5 to Shaan, for the **drop-list check** (30 min)
- [ ] Standup (15 min)

---

## Done by Saturday

- [ ] Limits and the privilege warning shown before any upload
- [ ] Upload with progress that resumes after a dropped connection
- [ ] Status steps and every failure message, from the strings file
- [ ] Documents list; hidden when uploads are switched off
- [ ] Checked at 375 px and on a slow connection
