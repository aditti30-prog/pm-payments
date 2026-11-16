# Part 0 · Prioritizing payment work when everything seems urgent

**Reading time:** ~16 minutes · **Prerequisites:** [First 90 days](00a-first-90-days.md) · **Status:** Editorial draft, 16 November 2026

## Learning outcomes

Distinguish non-negotiable obligations from value-optimizing bets; compare initiatives across measurable customer, financial and operational consequences; document choices that survive scrutiny from risk, finance and engineering.

## 1. Why ordinary feature prioritization breaks down

Payments roadmaps blend different kinds of work:

- **Mandatory:** contractual/regulatory or scheme changes with a verified applicability and effective date.
- **Safety-critical:** duplicate charges, financial posting errors, unbounded loss exposure, unavailable refund capability.
- **Reliability and operability:** latency, PSP availability, alerting, status recovery, exception repair.
- **Growth and economics:** conversion, more payment methods, reduced processing cost, improved authorization rates.
- **Foundational:** token migration, unified event model, reconciled reporting, partner portability.

These cannot all be ranked with one `impact × confidence ÷ effort` formula. A mandatory control cannot be postponed just because its revenue benefit is hard to estimate. But labeling every item “compliance” also destroys prioritization; insist on the specific source, obligation, owner, deadline and impacted transactions.

## 2. Two-stage decision process

**Stage 1 — Guardrail / eligibility gate.** Ask whether a proposal violates a known legal/scheme requirement, exceeds approved risk appetite, creates unmitigated customer harm or compromises financial integrity. An initiative failing the gate needs remediation or specialist approval, not a higher score. Regulatory interpretations must be checked by responsible specialists.

**Stage 2 — Compare eligible options.** Evaluate their contribution to a clearly named objective while showing uncertainty and dependencies. Possible criteria: customers affected, expected loss reduced, margin after variable processing costs, operational toil removed, reversibility, engineering effort, and time to learn.

Example decision dimensions:

| Dimension | Question | Evidence |
|---|---|---|
| Customer impact | How many distinct customers/orders are harmed? | Session/order cohorts, support contacts |
| Financial consequence | Which fees, fraud, settlement losses or lost contribution change? | Finance-approved unit economics |
| Urgency and exposure | Is there a contractual deadline or active incident? | Dated policy/contract, incident severity |
| Confidence | Have we isolated causes or only correlated symptoms? | Decline reason, logs, segmented tests |
| Operational burden | Does this reduce reconciliations, disputes or support time? | Exception queues, staffing volumes |
| Cost and reversibility | Can we safely run a limited rollout and rollback? | Eng design, partner contract, state-machine tests |

## 3. Worked trade-off: reliability vs cost vs conversion

**Fictional monthly example**, deliberately simplified and *not* a forecast:

- A merchant has 100,000 eligible monthly checkout orders; 90,000 currently become paid orders.
- Average pre-payment contribution per fulfilled order is S$10, **before** variable payment costs and fraud/dispute losses.
- Team has 20 engineer-weeks for near-term work.

| Candidate | Hypothesis | Effort | Main risk / constraint |
|---|---|---|---|
| A. Pending-state/status recovery | Recover 400 additional legitimate paid orders/month | 5 weeks | Must prove no duplicate captures; support readiness |
| B. Cheapest-route switching | Save S$0.025 per currently paid order | 4 weeks | Could increase latency/declines; requires provider validation |
| C. Improve 3DS challenge recovery | Recover 180 legitimate paid orders/month | 3 weeks | Potential fraud/chargeback changes; issuer ACS behavior |
| D. Fix a duplicate-capture incident class | Prevent 20 duplicate settled charges per month | 6 weeks | Financial-integrity issue, possible urgent priority regardless of ROI |

Rough value screens: A produces `400 × S$10 = S$4,000` in gross incremental contribution **before** added payment and risk costs. B produces `90,000 × S$0.025 = S$2,250` in direct fee savings **if approval/volume remain stable**. C produces `180 × S$10 = S$1,800` before changed risk/fees. D should not be evaluated solely as a fee-savings feature: harm, incident severity, chargeback exposure and trust may impose a higher-priority safety obligation.

**Decision example:** If D is an unresolved high-severity financial-integrity risk, fund its containment first. Then choose between A, B and C using *validated* causal impact, total contribution, guardrails and dependence on PSP capabilities. Do not add the stated impacts as if they are independent: initiatives can overlap in the same customer cohorts.

## 4. How to write a decision record that is not performative

A one-page record should include:

1. **Decision context and date:** system, geography, transaction types, cutoff.
2. **Actual choice:** options including deferral and limitations.
3. **Evidence and definitions:** eligible cohorts, units, data freshness, confidence.
4. **Financial and risk guardrails:** cost per paid order, customer harm, double charges, fraud, disputes, exception aging.
5. **Approval boundaries:** who can block, override or escalate.
6. **Reversibility:** feature flags, routing fallback, state repair, reconciliation checks.
7. **Review trigger:** what measurement or rule change reopens the decision.

Use the [decision record template](../../artifacts/payment-decision-record-template.md).

## 5. A practical prioritization ritual

At a weekly meeting, review *change in risk and evidence* rather than re-ranking every item from scratch. Separate an **obligation lane** (scope, due date, approval status), an **incident/remediation lane** (severity, financial/customer exposure), and an **investment lane** (expected product improvement). Review provider and platform dependencies in all three lanes.

If an issuer, acquirer or network deadline changes, date-stamp the source and update the decision register. A slide with the old threshold is not a defensible control artifact.

## Exercise and answer check

**Question:** The growth team wants to disable 3DS to increase conversion; the risk team reports fraud losses are already near an approved ceiling. Can the PM trade a projected conversion uplift against fraud losses and launch alone?  
**Answer check:** No. First identify applicable SCA, scheme and risk-control obligations; require risk/compliance sign-off; explore eligible low-friction authentication and better recovery. Test fraud-adjusted economics and customer outcomes, not challenge rate alone.

**Next:** [PSP selection, contracts and SLAs](00c-psp-selection-and-slas.md).
