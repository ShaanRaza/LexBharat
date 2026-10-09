# legal

Versioned user-facing legal documents. **None written yet.** These are launch blockers,
not paperwork to do later — `consents.notice_version` in the database points at a specific
version of the consent notice, so sign-up cannot work until one exists.

Every document here is reviewed by counsel before it goes live. Nothing in this repo is
legal advice.

| Document | Why it is needed | Status |
|---|---|---|
| `consent-notice-v1.md` | DPDP: purpose, data collected, retention period, how to withdraw. Shown at sign-up; the accepted version is stored per user | **Not written** |
| `privacy-policy-v1.md` | Must list every vendor, what it receives, where it processes, and its retention terms. The "Where data goes" table in [SECURITY-AND-COMPLIANCE.md](../docs/SECURITY-AND-COMPLIANCE.md) is the basis | **Not written** |
| `terms-of-service-v1.md` | Must state the fiduciary/processor split for uploaded client documents (**Needs counsel**) | **Not written** |
| `not-legal-advice.md` | The standing notice and the stronger personal-advice variant. Wording lives in [UX-COPY.md](../docs/UX-COPY.md) | **Not written** |
| `upload-warning.md` | The warning shown before upload, about privileged material | **Not written** |
| `takedown-process.md` | How we handle redaction requests. The dataset card names `contact@vaquill.ai` for the source data | **Not written** |
| `legal-orders-policy.md` | How we answer legal orders for user data | **Not written** |
| `advocate-legal-opinion.md` | The advocate's **written opinion** — launch gate condition (d). Covers privilege, DPDP roles and the information/advice line | **Not obtained** |

## Versioning

Filenames carry the version (`-v1`, `-v2`). **Never edit a published version in place** —
users consented to specific text, and `consents.notice_version` must keep pointing at what
they actually saw. Add a new file and bump the version.

## Related

- [RETENTION.md](../docs/RETENTION.md) — the periods these documents must state
- [BREACH-PLAYBOOK.md](../docs/BREACH-PLAYBOOK.md) — notification templates belong here too
- [SECURITY-AND-COMPLIANCE.md](../docs/SECURITY-AND-COMPLIANCE.md) — the obligations
