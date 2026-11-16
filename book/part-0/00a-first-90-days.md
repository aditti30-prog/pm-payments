# Part 0 · First 90 days as a Payments PM

**Reading time:** ~15 minutes · **Prerequisites:** [Payments PM ownership](00-payments-pm-ownership.md) · **Status:** Editorial draft, 16 November 2026

> Your first objective is not to ship a payment feature. It is to know where a transaction can go wrong, who notices, who is accountable, and which data can be trusted.

## 0A.1 What you should produce by day 90

A **payment-system map**, **metric dictionary**, **risk and obligations register**, **top three customer/merchant problems**, **prioritized opportunity portfolio**, and **at least one instrumented, low-risk improvement or validated design**. These deliverables are examples, not a universal hiring scorecard.

## 0A.2 Days 1–30: map the business, system and controls

**Customer and business:** Who pays? Who receives funds? Who is merchant of record? What contract governs acquiring, card processing, gateway service or bank sponsorship? Where are fees earned? Which markets, payment methods and user segments matter?

**Technical journey:** Observe one payment from customer action through merchant intent → authentication where applicable → authorization → capture → settlement report → merchant payout → bank credit. Trace a refund and one dispute separately. Record authoritative identifiers and which team owns each transition.

**Operational journey:** Shadow payment operations, support, finance/reconciliation and one incident review. Ask what is often missing: provider transaction ID, issuer response, webhook history, settlement batch, refund correlation or dispute deadline. Observe, don't assume, what “payment completed” means in each dashboard.

**Controls and external dependencies:** Meet risk, compliance, security, legal, PSP/acquirer and any issuer or sponsor-bank counterparts. Learn non-negotiable constraints and actual escalation agreements. Do not make irreversible payment changes solely from an interview with engineering.

**Deliverable 1 — a one-page system diagram.** Include actors, interfaces, key transaction IDs, settlement/payout paths, failure modes, and where PII/payment data is stored. Document both merchant and provider states.

**Deliverable 2 — metric dictionary.** A short example:

| Metric | Example denominator | Owner of definition | Common trap |
|---|---|---|---|
| Authorization approval rate | Eligible submitted authorization attempts | Payments analytics + risk | Counting local validation failures as issuer declines |
| Paid-order conversion | Unique orders initiating payment within an agreed window | Commerce PM + finance | Treating repeated attempts as new orders |
| Reconciliation match rate | Expected financial entries available for the same cutoff | Finance/treasury | Comparing differing settlement periods or currencies |
| Duplicate settled charges | Confirmed duplicate financial captures per paid-order cohort | Finance + operations | Counting duplicate auth attempts as settled doubles |

## 0A.3 Days 31–60: prioritize one problem with evidence

Run segmentation on real cohorts. Prioritize by customer harm, financial exposure, contractual/regulatory urgency, frequency, reversibility and effort. Investigate at least three hypotheses before prescribing a payment feature.

Example: checkout conversion falls. Before changing the UI, split failures into **not submitted**, **authentication abandoned**, **issuer declined**, **PSP technical errors**, **timeouts with unknown status**, and **post-payment order failures**. The correct PM response differs across these buckets.

**Deliverable 3 — opportunity brief** with (i) a validated baseline, (ii) affected customer segments, (iii) estimated value and exposure, (iv) decision constraints, (v) options including *do nothing*, and (vi) an owner for every dependency.

**Deliverable 4 — decision record.** Use [the template](../../artifacts/payment-decision-record-template.md). Include what would cause you to reverse the decision.

## 0A.4 Days 61–90: deliver a controlled, observable change

Pick an intervention where eligibility, rollout and rollback can be explicit: clearer pending-payment status, better decline-code mapping, logging a missing reconciliation reference, or a targeted error-recovery change. Avoid treating aggressive routing/retry changes or lowered fraud rules as starter tasks.

**Before release:** verify the state machine, API contracts, idempotency, error taxonomy, compliance/risk review, finance booking, support runbook and telemetry. Ensure the experiment can identify **unique paid orders** and not just successful attempts.

**After release:** monitor the primary metric and countermetrics through a relevant settlement/dispute maturity window. A same-day authorization uplift does not establish improved contribution margin or sustainable fraud performance.

**Deliverable 5 — a learning memo:** hypothesis, observed impact, uncertainty, operational cost, decision to scale or rollback, and unresolved risks.

## 0A.5 Role-specific emphasis

| If you join... | Add to first-month investigation |
|---|---|
| Merchant checkout | Order/payment mismatch, payment method penetration, recovery UX, refunds |
| Issuer/card program | Authorization policy, card controls, token provisioning, fraud and processor dependency |
| Gateway/orchestrator | Provider SLAs, outage playbooks, status contract, multi-PSP observability |
| Acquirer/PayFac | Merchant lifecycle, KYB, reserves, settlement payout, disputes and underwriting |
| Wallet/QR | Acceptance footprint, enrollment, identity versus payment, redemption and POS integration |
| Risk / payment platform | Who owns each rule and threshold, change-approval and rollback path, false-positive measurement, dispute tooling and authentication/tokenization dependencies |

## 0A.6 Ten questions for your first payments architecture review

1. Which event confirms an **approved authorization**? Which confirms capture?
2. How do we distinguish *declined*, *failed*, and *unknown*?
3. What is the idempotency scope and lifetime per operation?
4. What happens if the same webhook is delivered twice or late?
5. Which identifiers survive from order through bank payout?
6. Where are scheme, issuer, provider and our own decline codes mapped?
7. What is our settlement cutoff and timezone per currency?
8. Who can place an account or merchant on hold, and why?
9. What is the customer-support response for a “paid but not ordered” complaint?
10. What did our last payment incident reveal that the roadmap missed?

## 0A.7 Exercise and answer check

**Exercise:** You have 2,000 daily checkout failures, but the provider reports only 1,400 declines. Is the data inconsistent? Write a three-part investigation.  
**Answer check:** Not necessarily. Map populations and denominators; reconcile failures before PSP submission, 3DS abandonment and unresolved/pending states; join by order and attempt IDs, rather than assuming all checkout failures are issuer declines.

**Next:** [Prioritization under competing obligations](00b-prioritization-and-tradeoffs.md).
