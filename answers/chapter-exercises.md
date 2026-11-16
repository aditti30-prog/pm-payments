# Worked solutions to every chapter exercise

> **Companion key — editorial draft, 16 November 2026.** These are teaching solutions, not network operating instructions, legal advice, or verified provider behavior. All worked commercial data and names are hypothetical. A case can have several valid answers if its assumptions differ. For each solution, test whether the reader defined the state, actor, identifier, denominator, decision owner and financial guardrail.

The chapter names below are stable anchors. Return to the corresponding chapter to read the questions; use these solutions to compare reasoning, not memorize an answer. Do not treat a quoted rule or service-level estimate as timeless; consult the [dated source register](../editorial/primary-source-audit-2026-11-16.md) and the responsible provider/specialist.

## 00-payments-pm-ownership

**Chapter:** [Part 0 · The job — What a Payments Product Manager owns](../book/part-0/00-payments-pm-ownership.md)

1. **Issuer approval is not a PM-controlled switch.** Define the cohort (eligible card authorization attempts, issuer region, payment type and time window), establish baseline and counterfactual, and examine the controllable inputs: credential freshness, request data, 3DS integration, routing where permitted and customer recovery. A target of 98% must be a *testable hypothesis*, not a guarantee. Monitor unique-order success, fraudulent approvals, cost per paid order and disputes, not the attempt rate alone.
2. **Instant payouts create a funding and loss decision.** First map the acquirer/PSP settlement clock, the bank-payout clock and the provider balance; identify whether the proposed speed requires prefunding or credit. Then define reserve/hold decisions, merchant underwriting and negative-balance recovery, beneficiary verification, bank cutoffs, reconciliation IDs and liquidity stress limits. The PM can propose a service tier; treasury, credit/risk, compliance and the provider must approve controls.
3. **There is no unilateral growth-versus-fraud override.** Agree on the risk appetite and who can change policy. Use legitimate *paid-order* conversion, false-positive rate by segment, confirmed fraud loss by matured cohort, dispute rate and loss-adjusted contribution. If a proposal breaches an approved control ceiling, route it through the required governance; experiment only inside approved limits.

---

## 00a-first-90-days

**Chapter:** [Part 0 · First 90 days as a Payments PM](../book/part-0/00a-first-90-days.md)

A 2,000-versus-1,400 mismatch does **not** establish bad data: checkout *failures* and PSP *declines* may have different populations. A defensible three-stage investigation is: (1) define the start/end events and denominators for `checkout_failed`, `payment_attempted`, `PSP_declined`, `3DS_abandoned` and `outcome_unknown`; (2) join on order, payment-intent and attempt IDs, then reconcile pre-submission validation, authentication abandonment, rejected authorization, timeouts and order-creation failures; (3) sample individual sessions and verify PSP callbacks, final state, duplicates and event time windows. Deliver a funnel table showing where the remaining 600 cases sit, plus an *unresolved* bucket rather than arbitrarily labeling them declines. A useful first-90-days outcome is an agreed metric dictionary with finance and provider operations.

---

## 00b-prioritization-and-tradeoffs

**Chapter:** [Part 0 · Prioritizing payment work when everything seems urgent](../book/part-0/00b-prioritization-and-tradeoffs.md)

**Do not remove authentication solely to recover checkout conversion.** First identify applicable SCA, network and contractual requirements and which authentication choices the merchant may actually influence. Ask risk to quantify current fraud losses and false-positive harms; examine challenge eligibility, abandonment by ACS/issuer, device rendering defects and permitted exemption paths. Escalate any change to approved policy to the accountable risk/compliance owner. In the chapter's 12-engineer-week portfolio, an unresolved high-severity duplicate-capture issue may consume 6 weeks as a non-discretionary fix. Remaining capacity can fund *one* of A (5), B (4) or C (3), not all. Compare their validated, non-overlapping customer benefit and risk-adjusted economics. Document why deferred work is not violating an obligation.

---

## 00c-psp-selection-and-slas

**Chapter:** [Part 0 · Selecting PSPs, managing partners and writing useful SLAs](../book/part-0/00c-psp-selection-and-slas.md)

**Treat payment-state certainty and finance close as entry gates, not merely scored preferences.** A 15 bps fee saving equals S$0.15 per S$100 settled, before other differences. If status queries are unreliable, a timeout can leave an order unknown; switching providers or blindly retrying may duplicate operations. Reports two days late can breach a daily close requirement. Require an integration proof for timeout → callback/status resolution, refund linkage, provider references and settlement files; involve finance in acceptance criteria. If A fails mandatory gates, pick B or negotiate remediation despite A's lower quote. Run the comparison on cost per confirmed paid order and reconciliation effort, not MDR alone. Specify SLA metrics, exclusions, remedies and exit/data portability before signing.

---

## 01-what-is-a-payment

**Chapter:** [1. What is a payment?](../book/part-1/01-what-is-a-payment.md)

1. **No payout follows from an authorization alone.** It is an issuer approval or hold in a common card flow; capture, clearing/settlement, merchant ledger postings and PSP/bank payout remain separate. Verify whether the hold will be reversed or expire under the applicable rules.
2. HTTP 200 says the *API request* succeeded, not that the money did. Show **Payment pending—checking status**, preserve the same payment operation ID, poll/query a documented status endpoint or await signed callbacks, and avoid a new charge until the first attempt is resolved.
3. Grocery substitutions, final taxes, partial fulfillment, variable tips and shipping adjustments can change the amount. Determine whether partial capture, incremental authorization, void/re-authorize or refund is supported and permitted.
4. Example: `order_id` → `payment_intent_id` → `attempt_id` → zero or more `authorization_id`s → `capture_id`s → `settlement_batch_id`/`payout_id`, with `refund_id` or `dispute_id` referencing the relevant capture. IDs must be unique within a documented namespace; don't match by amount alone.

---

## 02-ecosystem

**Chapter:** [2. The payments ecosystem: who does what, who takes risk?](../book/part-1/02-ecosystem.md)

1. **Yes.** A full-stack PSP may supply both gateway integration and acquiring capabilities. But distinguish legal acquirer, technical gateway, settlement-report producer, merchant contract and liability; consolidating services reduces integrations but increases provider concentration and potential credential lock-in.
2. An issuer may reject risky spend to protect cardholders and reduce losses; a merchant wants high legitimate conversion. An intervention that boosts merchant approvals may alter issuer fraud exposure and scheme thresholds. Align on fraud-adjusted outcomes and approved controls, not a shared approval target without context.
3. **SGQR is a common QR labeling/presentation standard, not a settlement rail.** The payment is completed through a participating scheme/account provider and the underlying transfer arrangements. Success and reversal semantics therefore depend on that provider and rail.
4. **Sequence:** buyer → platform checkout → provider/acquirer → payment confirmation → order/seller services. **Funds:** buyer funding source → appropriate settlement/funds-holding party → seller A and B payouts and platform fee, with refunds/reserves represented separately. Diagram contractually correct merchant-of-record and regulated responsibilities; do not infer custody from the API sequence.

---

## 03-card-payment-lifecycle

**Chapter:** [3. How a card payment works, end to end](../book/part-1/03-card-payment-lifecycle.md)

1. S$50 **authorized but uncaptured** is not settled merchant money. Customer may see a pending hold; the order must not be labeled *paid* unless the business explicitly defines a reserved/guaranteed-to-capture state. Finance tracks auth exposure and the missing capture, not settled revenue, and investigates capture errors before retry.
2. Verify callback signatures, deduplicate on stable provider event ID, apply state transitions atomically with the internal ledger/outbox and make fulfillment idempotent by order. Duplicate delivery is expected; exactly-once network delivery is usually not promised.
3. Evaluate partial capture of the revised amount, reversal of unused authorization, new auth if rules/expiry require, restoration of loyalty/coupon values, refund if full capture already occurred, and what the PSP supports. Keep one source of truth for the final order and per-tender allocations.
4. **Authentication:** checking the payer. **Authorization:** issuer agrees to the proposed card transaction. **Capture:** merchant submits an approved amount for financial processing. **Payout:** acquiring/PSP sends net funds to the merchant. None alone proves the next stage finished.
5. Success: confirmed payment/order state and receipt; failure: definitive decline with a permitted new method; unknown: truthful pending UI and status resolution, not an automatic second charge. For each retain order and attempt identifiers, timestamps and escalation path.

---

## 04-payment-economics

**Chapter:** [4. Payment economics: who earns, who pays, who bears risk?](../book/part-1/04-payment-economics.md)

1. MDR is a merchant-facing price, not retained PSP margin. Interchange paid to issuers, network charges, acquiring/processing costs, FX, fraud, servicing and other variable costs may all consume it. Pricing contracts may contain fixed fees or interchange-plus structures.
2. 1,000 × S$20 = **S$20,000 volume**. Percentage fee: 2% × 20,000 = **S$400**. Fixed component: 1,000 × S$0.15 = **S$150**. Total **S$550**, equivalent to **2.75%** of S$20,000 and **S$0.55 per transaction**. Tax, refunds, other fees and chargeback costs are excluded.
3. More GMV can coincide with worse contribution if new volume has low basket size (higher fixed-fee burden), high fraud, heavy cross-border fees, elevated refunds or paid traffic costs. Evaluate contribution *after* relevant payment and risk expenses.
4. Request settlement timing and dispute/reversal tails, merchant sector, average delivery lead time, refund/chargeback distribution, existing collateral/reserves, negative balances and financial capacity. Risk/treasury set the policy; the PM designs the merchant-facing experience and monitoring.

---

## 05-merchant-acquiring

**Chapter:** [5. Merchant acquiring and onboarding](../book/part-2/05-merchant-acquiring.md)

**Café / QR:** identity and business verification appropriate to the product; beneficial-owner screening where required; settlement account verification; QR alias/provider configuration; first-test transaction; reconciliation/payout confirmation; fraud, refund and suspicious-activity monitoring. Where a QR code merely identifies a merchant, check the underlying provider/rail and receipt source. Activation must not be equated to completed due diligence.

**Pre-order travel / cards:** add sector/geography and delivery-timeline underwriting, advanced-payment exposure, cancellation/refund policy, scheme/acquirer eligibility, card-not-present security controls, reserve or delayed-payout assessment, monitoring of fraud/dispute trends and future-delivery liability. Separate `application_submitted`, `KYB_verified`, `underwriting_approved`, `MID_activated`, `first_payment`, and `payout_eligible`; don't let a UI shortcut bypass a control decision. The risk difference is particularly *future service delivery and chargeback funding* exposure, not that QR payments have no risk.

---

## 05a-marketplaces-payfac-funds-flow

**Chapter:** [5A. Marketplaces, payment facilitators and platform funds flow](../book/part-2/05a-marketplaces-payfac-funds-flow.md)

The S$120 provider-ledger movement and S$80 bank credits belong to different ledgers and possibly different dates. Create seller-level receivables: A S$80, B S$40. Join platform transfer ID, provider balance movement ID, seller payout ID, bank transfer reference, merchant account/entity and cutoff timestamp. For B, look for pending bank processing, reserve hold, rejected beneficiary, FX/currency timing or misallocation; trace the original status before scheduling any retry. A second S$40 transfer on the assumption of loss risks duplicate payout. Escalate exceptions by aged status, amount at risk and owner, and maintain the gross-to-net bridge including platform commissions and fees.

---

## 06-gateways-orchestration

**Chapter:** [6. Payment gateways, processors and orchestration](../book/part-2/06-gateways-orchestration.md)

**Strategy A** optimizes quoted processing fee on each routed attempt. **Strategy B** estimates *expected contribution* after successful fulfillment, fees, support and fraud. B needs comparable eligible cohorts, route success and eventual captured/paid-order outcomes, PSP/issuer/region/card mix, 3DS completion, costs including fixed and FX charges, latency, refunds, matured losses and operational failures. It also needs causal testing: a route may look worse because it receives higher-risk traffic. Example: on a S$100 order with S$8 merchandise contribution, A's S$1.50 fee and 85% confirmed-order success gives `0.85 × 8 − 1.50 = S$5.30` before other costs; B's S$1.80 and 93% success gives `0.93 × 8 − 1.80 = S$5.64` if costs are charged at this simplified per-order level. Explicitly define when fees accrue and verify the causal assumptions; these illustrative numbers do not rank actual providers. Unknown outcomes must be resolved before cross-PSP retries.

---

## 07-issuing-tokenization

**Chapter:** [7. Card issuing, credentials and tokenization](../book/part-2/07-issuing-tokenization.md)

A virtual employee-expense card can cap **per-transaction amount** and **monthly spend by merchant category**, subject to processor/issuer support. Data model: corporate funding account → employee card account → card credential (funding PAN) → one or more provisioned device/merchant tokens and auth events. Store identifiers in a PCI-appropriate system; expose only safe references. `card_suspended` should trigger issuer-side authorization policy and, as supported/appropriate, token-status actions; do not assume suspending one device token cancels all underlying card credentials. Specify behavior for pending auths, clearing after suspension, reversals and dispute servicing. Guardrails include false declines, unauthorized spend, control override auditability, reconciliation of authorizations to clearing, and employee-support response time. Employer permissions and local rules must be checked.

---

## 07a-network-tokenization-fpan-dpan

**Chapter:** [7A. Network tokenization, FPAN, DPAN and card-on-file credentials](../book/part-2/07a-network-tokenization-fpan-dpan.md)

1. Model `funding_account` → `card_credential(FPAN reference, status)` → `network_token(token reference, domain, device/merchant, lifecycle status)` and a separate PSP vault-token reference where used. Card, phone token, watch token and merchant token can be suspended/updated independently, subject to issuer/TSP controls. The **DPAN** is a device-specific payment token in common wallet usage, not a second underlying funding card.
2. On lost phone, verify owner authentication; suspend/delete the affected *phone token* via issuer/TSP/wallet lifecycle controls. Decide whether the funding card or watch token also needs blocking based on compromise evidence, policy and customer choice—not automatically. Reprovision via permitted authentication.
3. Displayed last four may come from token PAN, while the physical card displays FPAN digits.
4. Proprietary PSP vault tokens typically are not portable to PSP B. A migration needs a documented token-export/provider migration or new customer entry/provisioning, plus contract, PCI and consent checks. Network token coverage and domain restrictions still need integration.
5. An active token can fail due to an inactive funding account, an invalid token cryptogram, wrong merchant/device domain, incompatible/acquirer route, 3DS/authentication failure or a discretionary issuer decline. A token is a credential-control mechanism, not an authorization guarantee.

---

## 08-wallets-qr-apms

**Chapter:** [8. Digital wallets, QR and alternative payment methods](../book/part-2/08-wallets-qr-apms.md)

| Dimension | Shopper-presented loyalty QR | Merchant-presented PayNow QR |
|---|---|---|
| Presented by / scanned by | Customer presents; POS scans | Merchant presents; customer bank/payment app scans |
| Main purpose | Identify customer or loyalty account; may carry redemption intent | Identify payee and potentially amount/reference for an account transfer |
| Payment rail | **None by itself**; separate card/cash/wallet tender | Supported bank/account-transfer arrangement used by the app |
| Strong success evidence | Loyalty record updated and any discount/points ledger reconciled | Confirmed merchant-side bank/provider credit/notification with matched reference |
| Refund | Re-credit eligible points/vouchers; separately refund the actual tender | Initiate correct rail/provider return or separate authorized merchant refund process |
| Key failure | QR identity reused/incorrect account or duplicate redemption | Spoofed payee/QR substitution, ambiguous credit, duplicate payer transfer |

Never infer financial payment from a loyalty QR scan or from the customer's transfer screenshot. Merchant-presented QR payload and rails vary by product.

---

## 08a-card-present-pos-and-offline

**Chapter:** [8A. Card-present, POS integrations and offline payment risk](../book/part-2/08a-card-present-pos-and-offline.md)

An offline receipt does **not** justify `SETTLED`. Record terminal transaction ID, batch/sequence, merchant/POS order and local provisional tender status. Under allowed offline rules, forwarding may happen later and can be declined; risk, authorization limit and customer messaging require explicit policy. If POS has no PSP reference, match later uploads and clearing by terminal IDs and batch rather than amount alone. Maintain an exception queue and finance cutoffs; ensure that re-presenting the same basket won't inadvertently produce two settled card transactions.

---

## 09-transfers-real-time-bnpl

**Chapter:** [9. Account transfers, real-time rails and buy now, pay later](../book/part-2/09-transfers-real-time-bnpl.md)

| Question | Card | FAST-style account transfer | BNPL |
|---|---|---|---|
| Confirm payment | Auth/capture and provider state; settlement later | Bank/rail confirmation correlated to merchant reference | BNPL provider purchase approval; merchant funding may follow separately |
| Merchant payout | Acquirer/PSP cycle, net of fees/adjustments | Merchant bank receipt or platform settlement arrangement | Provider contract and timing, net of fees/adjustments |
| Refund | Linked card refund/credit under network/provider rules | New return/credit instruction; cannot assume card-style reversal | BNPL cancellation/refund API; may also adjust consumer installment plan |
| Customer recourse | Card dispute channels as applicable | Bank/rail fraud and mistaken-payment processes, not generic card chargeback | Provider/consumer agreement and local protections |
| Costs | Interchange/network/acquiring/PSP components | Bank/provider fees and operational handling | Merchant discount, BNPL funding and servicing costs |
| Ops | Captures, reversals, disputes, payout recon | Remittance reference, duplicate/misdirected transfers, refunds | Purchase/loan linkage, cancellation, merchant settlement, disputes |

Verify exact finality, return eligibility, customer protection, merchant payout and refund SLAs against the *named provider and contract*—do not treat FAST bank transfer, card and BNPL as one payment state machine.

---

## 09a-cross-border-fx-and-treasury

**Chapter:** [9A. Cross-border payments, FX, treasury and payouts](../book/part-2/09a-cross-border-fx-and-treasury.md)

`processed` might mean accepted into a provider queue rather than delivered to the recipient. Map the origin instruction, FX execution/quote ID, prefunded balance or funding movement, corresponding-bank/intermediary references, destination clearing event, beneficiary bank credit/rejection, and possible return. Compare country holidays, cutoffs, sanctions/beneficiary checks, local payout rails and contract's delivery definition. Keep the attempt in `payout_pending_investigation` until authoritative delivery/return evidence exists; do not resend merely because the beneficiary sees no credit on Wednesday. Product success metrics should distinguish time to provider acceptance, time to beneficiary credit, returned payouts and aged exceptions.

---

## 10-checkout-and-payment-state

**Chapter:** [10. Checkout design: intent, payment state and customer experience](../book/part-3/10-checkout-and-payment-state.md)

The problem is **underdetermined until the removed item's price, coupon rule and loyalty-allocation policy are known**. Suppose the dropped item had S$12 pre-discount value and the S$10 coupon remains fully valid. Original payable = 60 − 10 = **S$50**; original card = **S$45** plus points = **S$5**. New pre-tender payable = 48 − 10 = **S$38**. One permitted allocation is 5 points + S$33 card. If card S$45 was only authorized, attempt a supported *partial capture* for S$33 and release/let expire unused S$12; if card S$45 was captured already, process S$12 linked refund (or adjust per provider rules). If coupon eligibility changed, recompute all tenders from a versioned pricing rule; restore points only for the portion no longer used, idempotently.

**Requirements:** persist `basket_version`, `discount_allocation_id`, `points_debit_id`, auth/capture/refund IDs, and reconciliation line items; show a revised itemized receipt and adjusted payment status. Failure states: points debit succeeds/card fails; card approved/points ledger times out; partial capture unknown; refund submitted but not settled. Never invent a revised amount without the item price and promotion policy.

---

## 10a-subscriptions-stored-credentials-and-dunning

**Chapter:** [10A. Subscriptions, stored credentials and dunning](../book/part-3/10a-subscriptions-stored-credentials-and-dunning.md)

No. A processor timeout after S$25 billing leaves the outcome **unknown**, not an unpaid invoice proof. Query by stable invoice/payment-operation IDs and ingest verified webhook events; deduplicate scheduler triggers and respect provider idempotency semantics. If first payment later settles, mark the invoice paid once and grant entitlement once. If it definitively fails, evaluate supported retry eligibility, retry windows and stored-credential flags, communicate accurately and stop duplicate billing. Document whether entitlement grace periods continue while status is pending. Chargeback/refund callbacks need separate financial state, not an invoice rewrite.

---

## 11-3d-secure

**Chapter:** [11. EMV 3-D Secure: authentication, friction and liability](../book/part-3/11-3d-secure.md)

1. **No.** 3DS authentication succeeded; a separate issuer authorization can still decline due to account, available funds, card controls or issuer risk.
2. **No.** Frictionless means 3DS data exchange/authentication occurred without a challenge, not that 3DS was skipped.
3. Identify legal SCA or exemption obligations, scheme/program rules, issuer ACS discretion and the effect on fraud, liability allocation and approved merchant risk limits. A merchant cannot guarantee frictionless treatment for high-risk users.
4. Measure fraud, chargebacks and merchant servicing costs over *matured* cohorts, not conversion on launch day alone. Also watch false declines and abandonment segmented by issuer/device.
5. Require stable `order_id`, `payment_intent_id`, `auth_attempt_id`, 3DS transaction references and scoped idempotency keys. A redirect callback may repeat; authentication result correlation must not initiate a second authorization without controlled state transitions.

---

## 12-authorization-optimization

**Chapter:** [12. Improving payment authorization rates](../book/part-3/12-authorization-optimization.md)

1. Example: 100 orders produce 100 first attempts, 80 approved; 20 failures generate 20 retries and 10 further approvals for distinct orders. Attempt approval = `(80 + 10)/(100 + 20) = 75%`, *below* the 80% first-attempt rate, while unique paid-order success improves from 80% to 90% if all approvals capture and orders complete. The examples use different denominators; don't add approvals that duplicate the same order.
2. Confounders: issuer/BIN and country mix; currency/MCC or risk mix; routing by device/card type; 3DS configuration; time-of-day or a concurrent integration release. Use a randomized eligible-cohort split if safe/contractually permitted, or carefully matched time windows, with a stable outcome definition and fraud/cost guardrails.
3. Offer another payment method, ask the customer to contact issuer, or correct user-entered data where permissible. Respect non-retryable response policy; never loop the same card automatically.
4. Metric: `count(distinct orders shown definitive failure where subsequent authoritative issuer/PSP event confirms approved or captured) / orders shown definitive failure`, by app version and provider. Include event latency and finance follow-up.
5. Improve 3DS challenge rendering and truthful pending-state recovery; also streamline error explanations, saved-method selection or token provisioning where relevant—without changing issuer acceptance logic.

---

## 13-fraud-risk-and-payment-controls

**Chapter:** [13. Payment fraud, risk decisions and controls](../book/part-3/13-fraud-risk-and-payment-controls.md)

**First-time, high-value cross-border card payment:** Do not apply a universal “block” policy based on amount or country. Start with an approved risk policy: device/account history, merchant type, velocity, customer verification, expected fulfillment and fraud signals. Depending on the product and jurisdiction, permit an eligible 3DS authentication attempt, a carefully bounded manual review, a fulfillment hold or decline under documented risk thresholds. **Risk** owns fraud policy and limits; **compliance/legal** assess applicable obligations and data/retention; **engineering** makes the decision auditable and idempotent; the **PM** owns transparent user and support journeys within approved controls. Two UX guardrails: (1) don't call an unknown/authentication-pending result a definitive decline; (2) give legitimate users a safe appeal/recovery channel without revealing exploitable rule details. Measure false-positive harm through policy-rejected-but-subsequently-validated good cases, paid-order conversion by like-for-like cohorts, manual-review latency, customer complaints and eventually matured fraud/chargebacks. Use holdout or shadow testing only with risk approval. A “good” rule should reduce *loss-adjusted customer harm*, not just fraud labels or approval noise.

---

## 13a-compliance-and-control-ownership

**Chapter:** [13A. Compliance and control ownership for Payments PMs](../book/part-3/13a-compliance-and-control-ownership.md)

**First change—the checkout architecture:** a PSP-hosted redirect and embedded provider iframe can have materially different PCI DSS eligibility and script obligations. Draw browser DOM, origins, iframe, postMessage and third-party scripts; identify whether merchant-controlled scripts can influence the payment page. PCI SSC FAQ 1588 clarifies a specific v4.0.1 SAQ A embedded-page script criterion; it does **not** grant universal SAQ A eligibility. Confirm the eligible SAQ and evidence with the acquirer/payment brand or assessor. Include provider AoC review, vulnerability scans where applicable, content-security protections and incident-response ownership.

**Second change—seller activation:** draw independent onboarding states (`application_received`, `identity_verified`, `screening_review`, `underwriting_approved`, `acceptance_enabled`, `payout_eligible`). Identify owner for KYC/KYB, AML and sanctions decisions, reserves, limits, negative-balance recovery and ongoing monitoring. The PM can optimize UX and elapsed time to first legitimate payment, but should not automatically enable payment acceptance or instant payouts because the application form completed.

---

## 13b-scams-and-regulatory-map

**Chapter:** [13B. Scam protection and regulatory scoping: Singapore examples](../book/part-3/13b-scams-and-regulatory-map.md)

**Generally no.** Singapore's Shared Responsibility Framework (effective 16 December 2024) covers a *defined phishing-credential* sequence in which the account user did **not** intend the transaction. A customer who knowingly sends money after being deceived by a fake investment adviser or a romance scammer usually falls **outside** it, and SRF loss-sharing also excludes Singapore-issued credit, charge and debit card transactions. Verify the facts (who initiated the transfer, whether credentials were phished, which instrument, who is in scope) against the current MAS/IMDA Guidelines; compliance/legal decide scope.

For the voluntary-transfer case, act on what the product can control: immediate bank and police reporting, rapid freeze/recall coordination where the rail supports it, evidence preservation (transfer, device and session references), approved friction such as beneficiary confirmation and warnings, and accurate customer messaging. The Protection from Scams Act 2025 lets Police issue restriction orders to banks when statutory criteria are met; it is not blanket authority for a product team to block payments. Distinguish an **authenticated** payment from a **non-deceived** customer: a successful login or 3DS result does not show valid intent. Track time-to-report, first-response SLA, recovery outcomes and false blocks.

---

## 14-payments-pm-craft

**Chapter:** [14. Payments PM craft: discovery, requirements, delivery and learning](../book/part-3/14-payments-pm-craft.md)

1. A 2-point issuer/PSP attempt approval lift might be driven by different traffic or extra attempts, while order success remains flat. Or captures, 3DS or post-payment order creation can offset approvals. Compare matched eligible order cohorts through paid order and fulfilled order with costs and fraud guardrails.
2. “Retry on error” lacks a failure taxonomy, retryability and authority. Specify definitive declines vs unknown outcomes; API idempotency scope and TTL; allowed maximum attempts; routing constraints; event dedup; customer messaging; reconciliation and alert thresholds; scheme/PSP and risk permissions.
3. Finance/ledger owner signs off the accounting mapping and reconciliation bridge; engineering validates transformation and idempotency; PSP operations and treasury verify raw settlement/payout files, identifiers and cutoff; PM owns product acceptance criteria, launch risk and stakeholder alignment. Approval evidence must be recorded as an artifact, not inferred from a green unit test.

---

## 15-chargebacks-and-disputes

**Chapter:** [15. Chargebacks and card disputes: lifecycle, evidence and product controls](../book/part-4/15-chargebacks-and-disputes.md)

1. Finance must ensure refund and chargeback debits do not produce unrecognized **double customer credit** or double merchant loss. Join the original capture, refund ID/status, dispute ID/reason, network/PSP adjustment and later reversals. Where permitted, submit refund evidence before applicable deadlines; never assume the network auto-recognizes a refund.
2. **No.** `information_supplied` normally indicates evidence submitted, not final issuer/network adjudication; maintain open case state and deadline clock.
3. Append a **dispute financial-adjustment event** linked to original capture/order and the payout batch; do not rewrite historical settled capture. Record associated fee separately.
4. Use transaction-date cohorts with sufficient maturation, track open cases separately, and show both disputes reported by date and by underlying transaction cohort. Excluding unresolved disputes produces survivorship bias. Make denominator and scheme metrics explicit.
5. Supply unique order/capture and authorization references, batch entries, timestamps, customer history and any evidence of reversal/refund; explain which transaction was legitimate and which was duplicated. Actual representment requirements and deadlines follow the scheme/acquirer agreement.

---

## 16-three-way-reconciliation

**Chapter:** [16. Three-party payment reconciliation: merchant, provider and bank](../book/part-4/16-three-way-reconciliation.md)

1. Difference **S$260** can bridge, for instance, S$100 processing fees + S$80 refunds + S$50 chargeback debit + S$30 reserve withholding = S$260. This is *one hypothetical* bridge, not a presumed cause. Verify sign, currency, period, and file IDs; the actual components may differ.
2. Use unique capture/settlement entry reference and provider transaction ID scoped to legal entity/account, plus payout batch ID. Amount/date alone are ambiguous.
3. Put it in **operational auth/capture exception monitoring**, not booked settled gross; investigate misleading `payment_success=true` mapping and capture absence.
4. No. Append reversal/credit adjustment in the later payout with dispute reference. Immutable history protects accounting trail.
5. No. Bank-level net match is necessary but insufficient; missing refund links leave a transaction-level mismatch. Three-way recon validates merchant order/capture/refund entries, provider financial report, and bank payout with exceptions tracked to resolution.

---

## 16a-payment-metrics-and-observability

**Chapter:** [16A. Payment metrics and observability: measuring the right thing](../book/part-4/16a-payment-metrics-and-observability.md)

A. Attempt approval is `74,000/82,000 = 90.24%`; paid-order success is `72,000/80,000 = 90%`. **Recovered-by-retry cannot be inferred**: you need first-vs-subsequent attempt sequences joined by unique orders, and authoritative capture/order outcomes. A customer may retry and still fail, and one order may create multiple authorization approvals.

B. Lower cost per paid order with higher absolute cost is possible: e.g., total fees rise from S$1,800 for 900 paid orders (S$2.00 each) to S$2,000 for 1,100 (S$1.82 each). Check cohort mix, fixed fees, cross-border FX, capture/refund/chargeback accounting and excluded cost categories.

C. `HTTP 200` is **transport/application success**, not issuer authorization. Normalize the provider's payment-level result (`refused`, `pending`, `authorized`, etc.) and its authoritative events. Build observability around state transitions, *not* only HTTP error rate.

---

## 17-reliability-and-payment-operations

**Chapter:** [17. Payment operations, incident response and financial integrity](../book/part-4/17-reliability-and-payment-operations.md)
A. A healthy second PSP is not a license to replay a timed-out money-moving operation. First preserve order/payment identity, query PSP A and correlate signed events; show pending. Even if routing to B is allowed under documented safeguards, cross-PSP idempotency is not automatic. Investigate later A captures and reconcile any duplicate risk.

B. A customer's two bank lines can be two holds, a hold plus a settled debit, or two settled captures. Compare customer-facing bank timestamps with merchant order, PSP auths, capture IDs, reversals/refunds, clearing and settlement. Communicate evidence and expected hold-release handling without inventing provider timelines.

C. Reopen an exception for S$200 under the correct cutoff and entity; validate new fee code against a contract and raw settlement report, recompute gross → adjustments → net, obtain finance approval and re-match bank payout. An unexpected fee category is not a license to book an arbitrary balancing adjustment.

---

## 18-real-time-open-banking-payment-initiation

**Chapter:** [18. Real-time payments, open banking and payment initiation](../book/part-5/18-real-time-open-banking-payment-initiation.md)

Do not release a high-value order based on a screenshot alone. Confirm the authoritative merchant-side credit/rail notification and correlate the bank reference to the order, amount, payee and currency. If webhook is delayed, use documented status lookup or bank reconciliation; keep the order pending with a clear timeout and exception owner. A high-value seller-release policy may require an extra anti-scam check even after credit, depending on the rail, merchant model and risk appetite. Separate **payer initiated**, **bank accepted**, **merchant received**, and **seller payout eligible** states. Document refunds through the relevant new transfer/credit process rather than presuming card-style reversal rights.

---

## 19-stablecoins-programmable-money

**Chapter:** [19. Stablecoins, settlement and programmable money](../book/part-5/19-stablecoins-programmable-money.md)

An indexing outage is **not** evidence the token transfer failed. Check correct chain and network, transaction hash, destination address, token contract, receipt/log events, confirmation/finality policy and provider custody ledger; verify there was no reorg or unsupported token mismatch. Reconcile the transfer to invoice amount, fees, exchange rate and customer identity as permitted. If value reached the merchant but checkout missed it, repair the invoice/order state rather than asking a second transfer. If value is irrecoverably on the wrong network/address, a normal refund may not be possible; define exception and support policy separately. Consider redemption, sanctions and custody obligations before labeling a transfer *settled* at the business layer.

---

## 20-agentic-commerce-delegated-payments

**Chapter:** [20. Agentic commerce, delegated credentials and customer consent](../book/part-5/20-agentic-commerce-delegated-payments.md)

A. **Not necessarily authorized.** A price ceiling does not permit product substitution. Validate merchant ID, SKU/category, substitution permission, delivery address, quantity, expiry and total against the original delegated intent; if an invariant changes, request a new consent artifact. Reject even cheaper unrelated goods when the user did not authorize substitution.

B. **No.** A credential or token issued does not prove an order, authorization or capture. Correlate merchant checkout session, signed order confirmation, PSP operation and callbacks by durable IDs. Unknown outcome → pending state; do not trigger new payment blindly.

C. **No.** Signed mandates help demonstrate the scope of purchase/payment authority but cannot prove physical delivery, quality or dispute eligibility. Preserve fulfillment evidence and relevant network-law-contract rules.

D. **Different layers.** ACP and UCP aim at commerce/checkout interaction and integrations; AP2 focuses on delegated payment authorization evidence and mandate semantics. Actual products can combine multiple layers with card-network credential programs; version-specific claims need as-of date and source. A protocol description is not proof the bank/merchant integration is generally available.

---
