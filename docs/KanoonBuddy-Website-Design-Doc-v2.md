# KanoonBuddy Website: Design Doc (v2)

**Date:** 9 Oct 2026
**Product:** Legal research AI for Indian courts. Launch scope: Supreme Court, Delhi, Bombay and Madras High Courts, Central Acts.
**Change from v1:** v1 had 12 technical sections and a black and white theme. v2 is simple and consumer friendly: one search bar, one orange accent, three pages.

## 1. Goal
A first-time visitor understands the product in 5 seconds and tries it in 10: type a legal question, get a plain answer with sources they can open.

## 2. Audience
Everyone: advocates, law students and the general public. Copy uses plain words. No technical terms.

## 3. Pages

| Page | What is on it |
|---|---|
| **Home** | Headline, search bar, 3 example questions, courts covered, live sample answer with sources |
| **Features** | Three features shown one at a time, each with a "You type / You get" example |
| **Pricing** | Free and Pro plans, early-access sign-up form |

Nav: logo, Features, Pricing, "Get early access". Sticky at the top. Footer carries the "legal information, not legal advice" line.

## 4. App flow (Home)
1. Visitor types a question or taps an example.
2. Status shows: Searching courts and Acts, then Checking each source.
3. Answer appears: short, plain language.
4. Sources appear with a tick. Tapping a source opens the exact text. Nothing opens by default.
5. If nothing reliable is found, the page says "We could not find a reliable answer" and shows no sources. It never guesses.

## 5. Features shown
- **Ask a legal question:** plain answer with the law behind it.
- **Find a judgment:** Supreme Court and High Court cases, with the key paragraph.
- **Old law to new law:** IPC, CrPC and Evidence Act section to its new BNS, BNSS or BSA section.

## 6. Visual system
- **Colour:** white page, warm off-white panels, one orange accent. Light theme only, no dark mode.

| Role | Value |
|---|---|
| Text | #0F1B33 |
| Accent (buttons, key word) | #D9480F, hover #B43A0A |
| Panel background | #FFF5EE, tint #FFE3D0 |
| Lines | #F3E1D4 |
| Verified tick | green #1F7A4D |
| "Not found" status | amber #B45309 |

- **Type:** one font, Plus Jakarta Sans. Headlines 800, body 400, labels 600 to 700.
- **Layout:** 1040 px max width, one centred column on Home, rounded cards, thin borders, no heavy shadows.
- **Phone:** everything stacks to one column. Nav links hide, the sign-up button stays.

## 7. Interactions
- Three example chips on Home fill the search bar and run a sample answer.
- Answer panel shows a sample at rest, so the first screen is never empty.
- Source buttons expand and collapse the exact text, one at a time.
- Features page uses a tab list: tap a feature, see its example.
- Navigation switches views inside one page. Separate page files did not work inside the viewer and sent users back to Home.

## 8. Content rules
- Sample content is labelled "Sample".
- No customer logos, testimonials, uptime or security claims until they exist.
- Competitors are not named.
- Headline is a placeholder until the team picks the final line.

## 9. Before launch
- [ ] Verify the sample excerpts (BNS 318(4), BNS 103, IPC 420, IPC 302, NI Act s.138) against official texts
- [ ] Replace the 3 sample answers with the real answer engine
- [ ] Confirm pricing and free-plan limits (Free ₹0, Pro ₹799 are samples)
- [ ] Connect the sign-up form to a mailing list
- [ ] Decide the final headline
- [ ] Add a trust page: who we are, how sources are checked
- [ ] Check the name "KanoonBuddy" for trademark clash with Indian Kanoon and KanoonGPT
- [ ] Test navigation and chips on phone, inside the live viewer
