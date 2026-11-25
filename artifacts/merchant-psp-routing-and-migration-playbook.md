
# Merchant PSP routing and migration — decision worksheet

**For:** Merchant Payments PMs evaluating PSP A versus PSP B or running an orchestration layer. **Not:** A gateway/acquirer operating playbook or universal scheme/network advice.

**Read:** [Chapter 6 — gateways, orchestration and merchant strategy](../book/02-payment-products-and-infrastructure/06-payment-gateways-routing-and-orchestration.md); [PSP timeout and duplicate-charge case](../cases/02-ambiguous-authorization-routing.md).

## 1. Strategy and decision hierarchy

State the objective as **resilience, payment success, or total cost**, with evidence from the relevant merchant cohorts. Apply hard gates first: legal/entity coverage, payment-method/merchant eligibility, data security, 3DS and risk obligations, token capability, safe money-state semantics, refunds and finance/reconciliation.

| Objective | Primary measure | Countermetrics |
|---|---|---|
| Resilience | Paid-order completion during provider degradation; eligible failover coverage; incident recovery time | Duplicate charges, long-pending payment state, lost settlement evidence |
| Success | Incremental legitimate paid-and-fulfilled orders per eligible order initiating payment | Fraud loss on mature cohorts, 3DS abandonment, provider costs |
| Cost | Loss-adjusted contribution or total cost per legitimate paid order | Fewer completed good orders, higher latency, provider concentration and operational costs |

The cheapest route or highest raw approval rate is **not** automatically the best route. Cost, success and provider health must be evaluated on comparable eligible populations.

## 2. Route eligibility and dependency map

| Question | PSP A | PSP B | Gate owner |
|---|---|---|---|
| Legal merchant entity/MID, market, card scheme, currency, method and amount supported? | ___ | ___ | PSP + payments |
| Supported 3DS/SCA, risk controls, captures, partial captures, pre-auth adjustments and refunds? | ___ | ___ | Payments + risk |
| Existing card-on-file PSP vault token or eligible network token usable on B? | ___ | ___ | PSP + security |
| Idempotency scope, status queries, callback integrity and unknown-outcome handling documented? | ___ | ___ | Engineering |
| Financial journal, settlement cutoff, invoice, payout and dispute report available? | ___ | ___ | Finance |
| Distinct acquirer/processor/network/cloud failure domain or common dependency? | ___ | ___ | Engineering/SRE |
| Rate contract, minimum commitment, FX fees and exit obligations understood? | ___ | ___ | Finance + commercial |

**No-go examples:** a route cannot legally process a method; a charge can complete but not be reconciled; callbacks are non-unique with no safe financial-event deduplication; high-risk credential portability is assumed without evidence.

## 3. Compare like-for-like route performance

Write the **eligible merchant cohort**: market ___; customer-initiated/recurring ___; card network/issuer/BIN group ___; amount band ___; device/channel ___; 3DS treatment ___; risk segment ___; time window ___.

| Metric | Route A | Route B | Meaning |
|---|---|---|---|
| First-attempt eligible card approval | ___ | ___ | Comparable actual issuer decisions, not all payment errors |
| Unique paid orders per payment-started order | ___ | ___ | Main merchant success metric |
| 3DS challenge rate, completion and p95 latency | ___ | ___ | Separate authentication friction |
| Technical errors, unknown operations and recovery age | ___ | ___ | True resilience / integrity |
| Effective cost per initiated order | ___ | ___ | All applicable processing, retry, fixed, FX and operating costs |
| Mature fraud/dispute loss | ___ | ___ | Use matched cohorts and current scheme-defined metrics where relevant |
| Loss-adjusted contribution per initiated order | ___ | ___ | Include incremental good-order value and variable costs |

**Illustrative comparison:** For 10,000 equivalent initiated orders, route A yields 9,000 legitimately paid/fulfilled orders at S$20 pre-payment contribution each and S$0.45 total cost per initiated order; route B yields 9,200 such orders at S$0.65 cost. Expected per-initiated-order contribution is **S$17.55** versus **S$17.75**. The difference, **S$0.20 per order**, is an economic *hypothesis*, not proof. Check sample confidence, issuer mix, long-tail dispute losses, engineering effort, and contract minima.

## 4. Be precise about "switching"

| Situation | Eligible action | Unsafe action |
|---|---|---|
| Planned optimization | Send small portion of **new eligible** orders to B, with valid control/holdout and cohort balance | Assume better blended approval proves B caused lift |
| Provider A degraded | Stop **new, not-yet-submitted** operations on A and choose B when eligible | Blindly retry submitted but outcome-unknown A requests on B |
| Definitively declined A transaction | Apply approved retry/reattempt rules, customer experience and valid new attempt ID | Treat all declines as retriable |
| A timed out after submission | Keep **unknown** state, query A and verify provider events, reconcile before new money movement | Assume merchant order ID or idempotency key prevents B duplicate authorization |

## 5. Release and rollback gates

- **Before 1%:** Provider B onboarding, business and legal constraints, 3DS/payment method eligibility, credential handling, partial captures and refunds, exception states, status-query/idempotency guarantees, contract/SLA review, signed operational runbooks and **finance receipt/settlement traceability**.
- **Canary:** Begin with approved low-risk eligible **new** traffic and a comparison that preserves issuer, method, market, amount and 3DS composition. Record actual initial percentages as a *merchant-approved plan*, not universal defaults.
- **Scale:** Check unique paid-order conversion, good-order contribution, p95/p99 latency, mature loss expectations, technical errors, unknown statuses, duplicate captures, refund SLA, settlement match and support volume.
- **Stop/rollback:** Set explicit merchant-specific thresholds for customer harm, financial untraceability, processing errors, fraud/risk breach, 3DS friction or material loss-adjusted conversion decline. Do not override mandatory controls.
- **After moving checkout:** Keep historical A capture/refund/chargeback/dispute servicing and reporting until every obligation is closed, even if all *new* card traffic goes to B.

## 6. Incident and daily operating questions

**Incident:** Which dependency failed? Which attempts were *never submitted*, *definitively declined*, *approved*, or *unknown after submission*? What proportion of new orders can safely use B? Does B depend on the same acquirer, cloud or 3DS service? Can finance identify every A/B settlement event and customer remediation?

**Weekly:** Which segments genuinely benefit from B after adjusting for traffic and risk? Are expected savings visible in invoices and cost per **successful paid order**? Has redundancy been tested, not just configured?

**Decide:** Keep A primary, choose B primary for specified cohorts, split by country/method, maintain B as warm backup, or do not migrate. Document the baseline, counterfactual, approvals, monitoring, follow-up owner and exit/rollback path.
