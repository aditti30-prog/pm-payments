# Editorial roadmap — Merchant Payments PM Handbook

**Audience and scope:** Merchant-side Payments PMs responsible for online/in-store payment acceptance, payment methods, provider integrations, conversion, payment economics, risk, refunds, reconciliation, payouts and operations. Issuing, acquiring, gateway internals and scheme/banking regulation are explained for merchant-side dependencies, not as complete specialist infrastructure operating guidance.

The textbook is organized around **the PM job → understanding payments → products/infrastructure → building → operating → emerging systems**. This structure does not replace detailed payment-system education with generic role advice.

## Current manuscript status

| Part | Chapters | Status |
|---|---|---|
| 0 — Payments PM role and operating model | Four working chapters (00–00C) | Drafts: archetypes, 90-day guide, prioritization and PSP selection |
| I — Understanding payments | 1–4 | Written first drafts; follow-up review for depth and citations |
| II — Products/infrastructure | 5–9 plus 5A, 7A, 8A and 9A | Drafts: marketplaces, network tokens, POS/offline, FX, payouts and treasury |
| III — Building | 10–14 plus 10A, 13A and 13B | Drafts: subscriptions/dunning, 3DS, authorization, compliance and scam-risk controls |
| IV — Operating | 15–17, including 16A | Working drafts; 15 (disputes), 16 (3-way recon), 16A (metrics) and 17 (runbooks) contain deep dives |
| V — Emerging | 18–20 | All three drafted: real-time/open banking, stablecoins and agentic commerce; specialist review pending |

**Written draft** does not mean expert-reviewed, production-ready or complete.

## Delivered in v0.4 (16 November 2026)

- [x] Added **13A: Compliance and control ownership** (PCI DSS integration questions, SAQ caveats, merchant KYB/AML, underwriting boundaries, dated primary sources).
- [x] Added **16A: Payments metrics and observability** (metric contracts, attempt/order denominator separation, synthetic HarborCart case, operational alerting).
- [x] Expanded **Chapter 17** into actionable runbooks for uncertain outcomes, duplicate charges, settlement/payout delays, three-party reconciliation breaks and dispute workflow failures.
- [x] Added **five practical artifacts**: compliance RACI, payment API checklist, metrics dashboard specification, incident review and merchant onboarding PRD.
- [x] Added synthetic cohort CSV, reproducible metrics checks and CI validation.

The added chapters and examples are **drafts** requiring practitioner review; the workflow checks links and arithmetic, not legal or scheme compliance.

## Delivered in v0.5 (16 November 2026)

- [x] Added 5A: Marketplace/PayFac funds-flow boundaries, split booking, negative balances and seller payouts.
- [x] Added 8A: Card-present/POS and offline acceptance; merchant exposure and terminal-reference reconciliation.
- [x] Added 9A: FX, corridors, treasury/prefunding, quote expiry and payout finality.
- [x] Added 10A: Stored-credential subscriptions, dunning, recovery and entitlement states.
- [x] Added 13B: Scam patterns, APP-fraud distinction and a Singapore-specific regulatory scope map.
- [x] Drafted Part V Chapters 18–20; Chapter 20 includes dated ACP/UCP/AP2 and network-program comparisons.
- [x] Added funds-flow, subscription-recovery, cross-border payout and agentic-intent artifacts, plus synthetic tests.
- [ ] Independent specialist review, complete scheme-rulebook updates and production implementation validation remain open; worked solutions are included in v0.6.

## Delivered in v0.5.1 — editorial quality patch (16 November 2026)

- [x] Tightened Chapter 13B's SRF coverage: defined phishing scope, Singapore-issued card exclusion and Protection from Scams Act restriction orders; renamed heading to Singapore-focused scoping.
- [x] Dated MAS stablecoin consultation close and added MiCA/GENIUS comparison in Chapter 19.
- [x] Explained AP2 v0.2 release and FIDO Alliance stewardship; separated AP2 mandates from stablecoin/x402 settlement examples.
- [x] Added Chapter 9A treasury-liquidity arithmetic and FATF Recommendation 16; linked its payout checklist and Chapter 10A's subscription PRD.
- [x] Replaced static metric assertions with CSV-driven funnel calculations; aligned onboarding states and incident timestamp.
- [ ] Complete specialist legal and technical review; educational scope notes are not a substitute.
- [ ] Add all-chapter answer keys and deeper worked scenarios.
- [x] Add weekly scheduled external-link audit; 403/429 and network restrictions remain explicitly unverified.

## Delivered in v0.6 — editorial quality pass (16 November 2026)

- [x] Published [worked solutions](answers/chapter-exercises.md) across all 32 chapters and a reader-facing answer-key index.
- [x] Added a [transaction-to-payout case lab](editorial/harborcart-case-lab.md) with a reproducible S$100 authorization, S$80 capture, S$10 refund, S$1.80 fee and S$68.20 payout.
- [x] Added a dated [public primary-source audit](editorial/primary-source-audit-2026-11-16.md) and a [specialist review framework](editorial/specialist-review-program.md).
- [ ] Independent reviewers, production provider-contract checks and comprehensive current scheme-rulebook validation remain **open**. Public-source verification is not a substitute for specialist sign-off.

## Delivered in v0.6.1 — operational depth and review readiness (16 November 2026)

- [x] Added [PSP failover and ambiguous-authorization case lab](cases/02-ambiguous-authorization-routing.md): differentiated issuer approval, paid-order outcome, 3DS challenge, duplicate callbacks and unknown status. *Fictional scenario.*
- [x] Added [marketplace reserve/refund/dispute case lab](cases/03-marketplace-reserve-refund-dispute.md): S$250 gross-to-net waterfall, S$20 seller reserve, S$40 post-payout refund and S$60 later dispute. *Fictional contractual model.*
- [x] Added a [reproducible JSON fixture](cases/data/operational-case-inputs.json) and [Python numeric check](scripts/verify_operational_cases.py) to GitHub Actions CI.
- [x] Standardized existing time estimates as *estimated study time*, and added explicit learning outcomes to the two Part 0 chapters that lacked them.
- [x] Published a structured [technical-review issue form](.github/ISSUE_TEMPLATE/technical-review.yml) to collect claims, scoped counterexamples and first-party evidence without implying sign-off.
- [x] Cross-linked both case labs from gateway, 3DS, authorization, acquiring/PayFac, disputes, reconciliation and payment-operations chapters.
- [x] Extended the [specialist review packet](editorial/specialist-review-packet.md) with explicit counterexample tests and the [primary-source audit](editorial/primary-source-audit-2026-11-16.md) with provider-specific anchors.
- [ ] **Unchanged:** No independent professional/scheme review or certified provider-contract validation has occurred. Automated tests establish consistency, not legal compliance or a commercially supportable design.

## Merchant-side operating depth added (November 2026)

- [x] Clarify merchant-side audience throughout the entry points; avoid promising full gateway, issuing, acquiring or fintech infrastructure training.
- [x] Expand Chapter 16 to four merchant reconciliation passes, normalized sources, method-specific differences, discrepancy hypotheses, evidence-based exception closure and operating metrics.
- [x] Expand Chapter 13 with a merchant fraud framework combining customer behavior, transaction behavior and transaction context; risk decisions, false-positive measurement and controlled rollout.
- [x] Add practical merchant reconciliation and fraud worksheets.
- [ ] Validate the new material with independent merchant finance, fraud, PSP operations and risk experts; provider/accounting rules remain implementation-specific.

## Planned improvements

### P0 — Editorial and navigation quality
- [x] Correct chapter 3, 12 and 14 headings, old cross-references, math delimiter and forward reading path.
- [x] Fix metadata to match this GitHub repository; delete the previous publishing scaffold.
- [x] Upgrade local checks to validate chapter order, headings, Next navigation and chapter-numbered references.
- [x] Add worked solutions for every chapter exercise and an automated coverage check (v0.6).
- [ ] Ask at least one specialist in issuing, acquiring, disputes and reconciliation for review.

### P1 — The PM role
- [x] Add Part 0 with role archetypes, example RACI, first 90 days, prioritization and PSP partner-selection mechanics.
- [x] Add decision record and PSP evaluation templates.
- [ ] Add anonymized field notes only after the author verifies non-confidential facts and permissions.

### Editorial accuracy
- Add source-date and rule-scope notes to brand- and geography-specific chapters.
- Ask specialists in issuing, acquiring, fraud, reconciliation and disputes to review technical details.
- Validate each external link, jurisdiction-specific claim and exercise answer against current documentation.

### Deepen core chapters
- Chapter 4: more worked economics with settlement fees, risk exposure, MDR/interchange and platform economics.
- Chapter 5: merchant underwriting, reserves, limits and KYB journey with detailed examples.
- Chapter 6: multi-PSP routing, token portability and transaction state diagrams.
- Chapter 7: issuing systems, BIN sponsorship, processor responsibilities and program controls.
- Chapter 8: QR identity versus QR payment, merchant-presented/customer-presented, wallets and APM refund models.
- Chapter 9: Singapore FAST/PayNow, cross-border transfers and BNPL accounting (with dated official sources).

### Additional coverage gaps
- [x] Draft cross-border/FX, treasury/payouts, marketplace/PayFac funds flow (see 5A, 9A).
- [x] Draft card-present/POS integrations and subscription billing/dunning (see 8A, 10A).
- [ ] Expand jurisdiction-by-jurisdiction regulation mapping and scheme-monitoring; 13B is Singapore-anchored, not a global legal inventory.
- [x] Draft scam-fraud and Singapore SRF decision framework in Chapter 13B; seek specialist review.
- More worked PRDs, answer keys and dated rule anchor boxes.

### New chapters
- [x] **18** — Real-time payments, open banking and payment initiation (working draft).
- [x] **19** — Stablecoins, on/off ramps, redemption and compliance considerations (working draft).
- [x] **20** — Agentic payments, delegated tokens, consent, instructions, disputes and boundaries of autonomy (working draft).

### Developer and reader tooling
- Add explanatory interactive diagrams only after the underlying chapters are reviewed.
- Add optional chapter quizzes and companion synthetic datasets.
- [x] Improve the Markdown structure/forward-link checker (relative files, numbered references, headings, and Next chain).
- [x] Add GitHub Actions CI for local-link/reading-chain validation and synthetic case checks.
- [ ] Add an optional documentation-site build.

## How to propose an edit

Open an issue describing the exact passage, corrected statement, supporting source and how the change affects the reader's mental model. See [CONTRIBUTING.md](CONTRIBUTING.md).
