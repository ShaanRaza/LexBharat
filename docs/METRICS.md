# Metrics, launch gate and validation

Targets below are **starting guesses**, to be adjusted once there is real usage. Owner for
all of them while the build is solo: **Akshita Johari (founder)**.

## Success metrics

| Metric | Starting target | Definition | How it is measured |
|---|---|---|---|
| **Verified-citation rate** | **98% or higher** | Share of authorities cited in answers that pass the verifier | Automatic run over the fixed 200-question test set, **on every release** |
| **Invented-citation rate** | **Under 0.5%** of answers | Share of answers with at least one removed citation, for any of the four failure reasons | The invented-citation log, reviewed on every release |
| Answer correctness | Set from the first baseline | Each answer graded correct / partly correct / wrong | **Two advocates grade each answer blind; a third settles disagreements** |
| Verifier accuracy | Set from the first baseline | Of authorities shown as verified, the share a human confirms exists with a matching quote. **Separate from correctness** | A random sample checked by hand; sample size agreed with the advisor |
| Free to paid conversion | 3% to 5% | Paying accounts ÷ free sign-ups, counted 30 days after sign-up | Billing database |
| Answers users mark helpful | 80% or higher | Thumbs-up ÷ rated answers, plus a count of wrong-answer reports | In-app rating button |
| Gross margin per paid user | 60% or higher | (Revenue − LLM, Voyage and payment fees) ÷ revenue, per month. Fixed hosting excluded and tracked separately as monthly burn | Invoices and usage logs |
| Monthly active users | **400** at 3 months after public launch | Accounts with at least one answer in 30 days | Event log that **never stores document text** |

On the MAU target: it was lowered from 2,000 to 400 because the planned channels cannot
plausibly produce 2,000. The assumed path to ~400 counts every sign-up as still active,
which no product achieves; at 60% month-on-month retention the same inputs give about 250.
Set the real number after the beta.

## The 200-question test set

Frozen so results can be compared release to release. **The advocate advisor signs it off
before it is used.**

| Part | Count |
|---|---|
| Real questions collected in the validation interviews | 100 |
| Act and section lookups | 50 |
| **Traps** — cases that do not exist, wrong section numbers, events after the snapshot date | **50** |

This mix is a proposal (Estimate). The traps are what prove the verifier and the
out-of-scope detection actually work; do not drop them to raise the score.

See [TESTING.md](TESTING.md) for how it runs.

## Launch gate

Public launch (months 4 to 5) happens only if **all** of these are true at the end of the
private beta (weeks 11 to 14):

- [ ] a. Verified-citation rate **98% or higher** on the 200-question test set
- [ ] b. At least **6 of the 10** beta advocates say they would pay the proposed Pro price
- [ ] c. **Zero** confirmed fabricated citations reaching a beta user, **and** fewer than
      0.5% of test-set answers have a removed citation
- [ ] d. The advocate's **written legal opinion** received
- [ ] e. Voyage's **written no-training and retention terms** received
- [ ] f. The **independent security test** passed
- [ ] g. The **data-as-of date shown prominently** on every result, stats page and Act page

**If any condition fails, the launch date moves. Akshita Johari decides.**

> **Note on condition (g).** The PRD's seventh condition was "the first data refresh is
> complete and reconciled". Tech Stack decisions **D2 and D5** moved the refresh pipeline to
> the post-MVP backlog and replaced that condition with the data-as-of date. The Tech Stack
> wins, so (g) above is the operative condition — but the PRD still reads the old way.

## User validation plan

**This PRD is entirely assumption-based. No lawyer has been interviewed.** Before any code
beyond the audit spike, run about **20 interviews of 30–45 minutes**:

| Group | Count |
|---|---|
| District court advocates | 8 |
| High Court advocates | 6 |
| Law students | 6 |

Recruit through own contacts, the law-school pilots, bar association introductions and
LinkedIn. Everyone interviewed gets free access.

### Assumptions being tested

| Assumption | How it is tested | A result that would change the roadmap |
|---|---|---|
| Advocates trust an answer with a "record found" badge | Show 10 sample answers; ask what they would still check | If most re-check every citation elsewhere, the badge will not sell the product — invest in one-click source viewing instead |
| Outcome statistics are wanted | Show a mock statistics page; ask what decision it would inform | If few would use it, drop it from the headline features and the free-tier wedge |
| ₹199 and ₹499 are right | Ask price questions at several price points | Follow the evidence table in [PRODUCT.md](PRODUCT.md) |
| Lawyers work from phones | Ask which device and network; watch one real research session | If most use desktops, cut the mobile budget |
| Hindi is needed | Ask which language they research in | If strongly needed, move Hindi from P1 to P0 |
| Statute lookup + SC precedent + drafting is enough for district-court advocates | Ask directly; watch one real session | If not, move the High Court phase 2 earlier, or stop treating district-court advocates as a launch target |
| Advocates will upload client documents | Ask how they feel about privilege and confidentiality | If few would, revisit the upload limits and the warning wording |
| Free tools such as Indian Kanoon are enough | Ask what they use now and what frustrates them | If they are satisfied, focus on students first |

The interviews also settle **which High Courts come first in phase 2**.

## Retention

Track week-4 retention of free users, month-3 retention of paying users, and monthly churn.
**No target is set** — none has been measured. Set it after the beta from the break-even in
the channel economics: paying users must stay long enough for their gross profit to cover
the cost of acquiring them.

Revenue a paying user brings, before model, hosting and payment costs:

| Months as a paying user | Student (₹199) | Pro (₹499) |
|---|---|---|
| 3 | ₹597 | ₹1,497 |
| 6 | ₹1,194 | ₹2,994 |
| 12 | ₹2,388 | ₹5,988 |

Scale a paid channel only when its measured acquisition cost is well below the gross profit
a user brings before churning.
