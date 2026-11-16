# Editorial roadmap

The textbook is organized around **understanding payments → products/infrastructure → building → operating → emerging systems**.

## Current manuscript status

| Part | Chapters | Status |
|---|---|---|
| I — Understanding payments | 1–4 | Written first drafts; follow-up review for depth and citations |
| II — Products/infrastructure | 5–9, including 7A | Written first drafts; 7A is a detailed network-token deep dive |
| III — Building | 10–14 | Written first drafts; 11 (3DS) and 12 (authorization) are detailed |
| IV — Operating | 15–17 | Written first drafts; 15 (chargebacks) and 16 (3-way recon) are detailed |
| V — Emerging | 18–20 | Planned — no chapters yet |

**Written draft** does not mean expert-reviewed, production-ready or complete.

## Planned improvements

### Editorial accuracy
- Add source-date and rule-scope notes to brand- and geography-specific chapters.
- Ask specialists in issuing, acquiring, fraud, reconciliation and disputes to review technical details.
- Validate each external link, jurisdiction-specific claim and exercise answer against current documentation.

### Deepen the textbooks' core chapters
- Chapter 4: more worked economics with settlement fees, risk exposure, MDR/interchange and platform economics.
- Chapter 5: merchant underwriting, reserves, limits and KYB journey with detailed examples.
- Chapter 6: multi-PSP routing, token portability and transaction state diagrams.
- Chapter 7: issuing systems, BIN sponsorship, processor responsibilities and program controls.
- Chapter 8: QR identity versus QR payment, merchant-presented/customer-presented, wallets and APM refund models.
- Chapter 9: Singapore FAST/PayNow, cross-border transfers and BNPL accounting (with dated official sources).

### New chapters
- **18** — Real-time payments, open banking and payment initiation.
- **19** — Stablecoins, on/off ramps, redemption and compliance considerations.
- **20** — Agentic payments, delegated tokens, consent, instructions, disputes and boundaries of autonomy.

### Developer and reader tooling
- Add explanatory interactive diagrams only after the underlying chapters are reviewed.
- Add optional chapter quizzes and companion synthetic datasets.
- Add an automated Markdown link checker and optional documentation-site build.

## How to propose an edit

Open an issue describing the exact passage, corrected statement, supporting source and how the change affects the reader's mental model. See [CONTRIBUTING.md](CONTRIBUTING.md).
