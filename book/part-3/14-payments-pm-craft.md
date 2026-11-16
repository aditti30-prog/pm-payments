# 14. Payments PM craft: discovery, requirements, delivery and learning

**Part III — Building Payment Products** · **Reading time:** ~17 minutes · **Prerequisites:** [The PM's decision rights](../part-0/00-payments-pm-ownership.md), [payment lifecycle](../part-1/03-card-payment-lifecycle.md), and [checkout state](10-checkout-and-payment-state.md).  
**Editorial status:** Working draft, 16 November 2026.

## Learning outcomes

By the end, you should be able to turn an ambiguous payments issue into a research plan, a bounded product decision, a testable API and operations contract, and a launch with appropriate economic, risk and finance guardrails.

## 14.1 Product discovery in payments is investigation, not only interviews

Talk to customers and merchants, but triangulate their account with transaction states, provider logs and operational evidence. A complaint such as **“I was charged twice”** could mean two authorizations, two captures, a pending hold plus settled debit, a repeated order, or a duplicated user-facing entry. Each has a different remediation and potentially different liability.

An effective discovery brief states the **unit of analysis**: customer, merchant, order, payment intent, authorization attempt, capture, settlement entry or payout. Use consistent identifiers; join across systems before interpreting a percentage.

### Example: checkout errors increased

Start with a taxonomy, not a redesign request:

| Hypothesis | Where to look | PM action if confirmed |
|---|---|---|
| Customer abandons challenge | ACS challenge result, challenge timestamp, funnel | Improve messaging, fallback and recovery within applicable 3DS rules |
| Credentials stale | Network/issuer response, stored credential lifecycle | Study updater/network-token lifecycle and retry eligibility |
| PSP timeout with unknown outcome | Request ID, status-query response, webhook history | Introduce pending state and idempotent status resolution |
| Merchant order not confirmed after capture | Capture reference, order service/queue logs | Repair order/payment coordination and customer-support procedures |
| Increase in local validation failure | Frontend/server schema, API versions | Fix bad request data rather than changing the issuer routing |

The responsible PM does not assume a provider decline, a shopper error, or a conversion opportunity until the evidence supports it.

## 14.2 A Payments PRD should specify financial truth

A basic PRD names a customer, problem, expected behavior and metrics. A payment PRD must additionally cover:

1. **System boundaries:** merchant, gateway/PSP, acquirer, issuer, scheme, internal ledger and bank where relevant.
2. **State and time:** initial, pending/unknown, authorized, captured, settled, paid out, reversed/refunded and disputed; which events are authoritative and what may arrive out of order.
3. **Idempotency and duplicates:** request identity, retry policy, late callback behavior and protection against multiple financial effects.
4. **External constraints:** scheme, provider, contract, data-handling and jurisdictional requirements with owners and effective dates.
5. **Failure and repair:** outage, timeout, provider mismatch, refund failure, payout shortfall, chargeback and accounting exception path.
6. **Success and guardrails:** unit, denominator, cohort window, settlement/dispute lag, fraud-adjusted economic outcome, customer harm and operability.
7. **Launch contract:** opt-in/flag, cohort eligibility, support runbook, risk/finance sign-offs, monitoring and rollback.

Start from the [example payment recovery PRD](../../artifacts/sample-prd-payment-recovery.md), but adapt it for your actual processing and merchant model. No sample PRD proves a system compliant with a particular standard.

## 14.3 PM versus engineering: who writes what?

PM should write **observable behavior and the required guarantees**: “A single payment intent must not result in more than one confirmed capture for the same payable order under our designed recovery path.” Engineering specifies the implementation strategy, keys, transaction logs, provider adapter behavior, database constraints and test harness. Finance confirms the ledger effect; risk validates appropriate loss controls.

A PM who can review state diagrams and API responses will make a better product decision, but should not silently assume ownership of a scheme certification, cryptographic protocol or financial accounting policy.

### Example acceptance criteria

- A timeout after authorization submission produces `pending_verification`, **not** `failed`, until an authoritative response or a documented terminal procedure resolves it.
- Duplicate PSP events do not create additional capture, shipment or ledger credit entries.
- Status checks preserve original provider reference and record source-of-truth timestamp.
- Support staff can see safe customer-facing context and status without viewing card credentials.
- Finance can match capture/refund/dispute entries to provider report and bank movement using stable IDs.

These are requirements; the concrete guarantees depend on system capabilities and provider contracts.

## 14.4 Product metrics need multiple clocks

The checkout funnel is measured in seconds and minutes. Some provider outcomes resolve over hours. Settlement and payouts can lag days and depend on cutoffs. Disputes and fraud outcomes can lag weeks or longer. Therefore a PM should differentiate **launch monitoring** from **mature outcome evaluation**.

Use a dashboard with primary metrics and countermetrics:

| Objective | Primary metric | Countermetric |
|---|---|---|
| More payments complete | Unique paid orders / orders initiating payment | Fraud loss, customer complaint, duplicate settled charge |
| Better auth acceptance | Approved eligible authorization attempts / eligible attempts | Order-level success, routing fee, issuer/3DS cohort mix |
| Faster recovery | Median time to resolve unknown status | Incorrect final state, unresolved aged cases |
| Better merchant payout | On-time reconciled payouts / due payouts | Bank exceptions, negative balances, reserve exposure |

For a diagnostic example, use the [94% → 89% authorization case](../../cases/01-authorization-rate-drop.md). Report both numerator and denominator; model retries and customer order deduplication explicitly.

## 14.5 Stakeholder decision review

Bring a one-page decision record to engineering, risk, finance and operations. Clearly label **what is decided**, **what is an unresolved hypothesis**, **who can approve the risk/control**, and **what telemetry could overturn the proposal**. The PM coordinates this process but should not claim that collaborating specialists automatically approve the design.

For vendor/API work, see [PSP selection and SLAs](../part-0/00c-psp-selection-and-slas.md). For competing obligations, see [payment prioritization](../part-0/00b-prioritization-and-tradeoffs.md).

## Exercises with answer checks

1. **A provider reports a 2-point increase in approval rate, but order conversion is flat. Give two possible explanations.**  
   *Answer check:* Attempt mix or retries changed; an authorization may not translate into a paid order; post-payment order failures or unrelated checkout friction may offset lift.
2. **A PM writes “retry on error.” What is missing?**  
   *Answer check:* Error taxonomy, unknown-state resolution, provider and scheme retry permissions, idempotency scopes, max attempts, customer messaging, risk constraints and finance checks.
3. **Who should approve a reconciliation mapping change?**  
   *Answer check:* The ledger/finance accountable owner, with engineering implementation review and operations/PSP reconciliation confirmation; PM ensures customer/product requirements and controls are represented.

**Next:** [15. Chargebacks and disputes](../part-4/15-chargebacks-and-disputes.md).
