# Breach playbook

**Status: skeleton. Must be completed and approved before launch** — the DPDP Rules
require a written plan, and the PRD lists it as a build-step-9 deliverable.

> **The reporting clock is 72 hours** to the Data Protection Board (EY summary; **Needs
> verification against the Rules**). Assume it starts at the moment of becoming aware, not
> at the moment of confirmation.

## 1. Detect and contain — immediately

- [ ] Record the time of discovery, in IST, and who discovered it
- [ ] Capture the request ID, Sentry event and Langfuse trace
- [ ] Contain: rotate the affected credentials, revoke tokens, take the affected path
      offline if needed
- [ ] **Do not delete logs.** They are the evidence

## 2. Assess — within hours

- [ ] What data types were involved? (Account data, chats, **uploaded client documents**,
      payment data, audit log)
- [ ] How many users, and which ones?
- [ ] Were **uploaded client documents** involved? If so, privilege is in play and counsel
      is needed immediately — the advocate, not just KanoonBuddy, has obligations
- [ ] Was any data sent to a vendor outside India?
- [ ] Is the exposure ongoing?

## 3. Notify

- [ ] **Affected users** — plain language: what happened, what data, what they should do
- [ ] **The Data Protection Board** — a detailed report **within 72 hours**
- [ ] Counsel, before any external statement
- [ ] Affected vendors, if their systems are involved

Draft notification templates in advance and keep them in [`../legal/`](../legal/).

## 4. Record and fix

- [ ] Write the incident up: timeline, cause, data involved, who was notified and when
- [ ] Fix the cause; add a test that would have caught it
- [ ] Review whether the retention schedule would have reduced the blast radius

## Contacts — fill in before launch

| Role | Who | Contact |
|---|---|---|
| Decision maker | Akshita Johari (founder) | — |
| Counsel (data protection) | — | — |
| Advocate advisor (privilege questions) | — | — |
| AWS support tier | — | — |
| Security tester | — | — |

## Open items

- [ ] Confirm the 72-hour requirement and the report's required contents against the DPDP
      Rules 2025 (currently an EY summary, **Needs verification**)
- [ ] Confirm our role — fiduciary or processor — for uploaded client documents, since the
      notification duty differs (**Needs counsel**)
- [ ] Write the policy for **how we answer legal orders** for user data
- [ ] Write the **takedown request process** (the dataset card names `contact@vaquill.ai`
      for redaction requests against the source data)
