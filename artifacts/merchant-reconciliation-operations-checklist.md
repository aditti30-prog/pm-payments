
# Merchant payment reconciliation — investigation and close checklist

**Audience:** Merchant Payments PM, reconciliation/finance analyst, treasury, PSP operations and engineering. **Not** a scheme-level acquirer or issuer settlement manual. This is an educational aid; actual sign conventions, accounting and close policy require finance and provider confirmation.

**Read:** [Chapter 16](../book/04-disputes-reconciliation-and-operations/16-payment-reconciliation-and-payouts.md).

## 1. Establish the data contract before matching

| Data / question | Evidence to supply | Owner |
|---|---|---|
| Merchant scope | Legal entity, MID, PSP account, payment rail/channel, settlement currency, payout bank account | PM + finance |
| Calendar and SLA | PSP cutoff, timezone, expected settlement file date, payout due date, bank holidays, allowed late postings | PSP operations + treasury |
| Order and tender | Order version, final payable, tender amounts, capture/refund intent, cancellation and fulfilment | Commerce engineering |
| Merchant payment ledger | Order, payment, attempt, capture, refund, void and dispute IDs with raw status/event times | Payments engineering |
| Provider financial journal | Unique financial journal ID; linked operation; signed amount; fee/FX/reserve details; payout batch | PSP operations |
| Bank and cash ledger | Statement transaction ID, legal entity, destination account, signed amount, value date | Treasury / finance |
| Audit, access and freshness | Immutable original files, ingestion and reporting timestamps, privacy controls and missing-file alerts | Data engineering + security |

**Do not match across different merchant entities, MIDs or settlement currencies merely because amounts happen to agree.** Keep a versioned mapping between provider-specific fields and canonical merchant fields. Confirm the file is complete before labeling transactions missing.

## 2. Execute four matches in order

1. **Order ↔ tender and capture.** Verify actual paid order, partial fulfilment, split tender, voids, refunds owed, fulfilled-without-payment and charged-without-order. Auth is not captured cash.
2. **Merchant financial event ↔ PSP financial entry.** Match capture/refund/dispute/adjustment IDs with correct status, amount, sign, currency, type, account and allowed late-arrival. Separate duplicated webhook delivery from real duplicate capture.
3. **PSP settlement entries ↔ payout bridge.** Calculate the gross-to-net payout from provider journal components: refunds, fees, disputes, reserves, FX, earlier-period adjustments. Reserves require their own tracked balances, not automatic fee expense.
4. **Payout ↔ bank / GL.** Match provider transfer reference, account, currency and bank value date. Reconcile approved clearing/receivable entries. Initiated is not bank received.

## 3. Exception register (copy one row per exception)

| Field | Capture |
|---|---|
| Exception ID / classification | Missing merchant, missing PSP journal, amount mismatch, duplicated financial operation, FX/fee/reserve difference, refund pending, payout in transit, bank unmatched |
| Scope | Merchant legal entity, PSP/MID, country, bank destination, currency, cutoff |
| Lineage | Order, payment, attempt, capture/refund/dispute, PSP journal, settlement batch, payout and bank IDs |
| Value | Expected and actual signed value, absolute exposure and customer count |
| Timeline | First seen, event time, report ingestion time, expected due date, age bucket |
| Hypothesis and proof | Missing/late file? Wrong status? Different entity? Real fee/reserve? Duplicate? Bank split transfer? |
| Owner and escalation | PM, finance, engineering, PSP ticket, treasury and support where needed |
| Final outcome | Reconciled authoritative events; valid late posting; or finance-approved correction/write-off with separate journal |
| Closure evidence | Immutable source IDs, approved remediation, actual cash/PSP outcome, customer resolution and reviewer |

**Never close based on a zero net difference alone.** An orphaned refund offset by an unsupported fee can net to zero and still represent two unresolved financial events. Never create an unexplained journal plug. Preserve evidence of changes.

## 4. Metrics to review

- Transaction **count match rate**: distinct eligible mature financial-event IDs matched / eligible events, with explicit cutoff.
- Transaction **value match rate**: absolute eligible matched value / absolute eligible total, by currency (avoid combining denominations without an explicit FX policy).
- **Unresolved absolute exposure** and count, separated by age, customer harm, MID, PSP and payment method; do not net signs.
- Due vs **bank-confirmed payout** count and value; transfer-in-transit aging.
- Confirmed duplicate captures, charged-without-order, overdue customer refunds and re-opened exceptions.
- Auto-match versus manually investigated items and cost/time to resolution.

## 5. Worked practice (fictional SGD)

Merchant financial captured value is **S$10,000**. PSP financial journal confirms refunds **S$500**, chargeback debit **S$200**, fees **S$250** and reserve hold **S$300**: expected payout **S$8,750**. Bank shows **S$8,700** by the expected date. The financial journal may be complete but the cash match is **S$50 short**. Trace the PSP transfer reference, bank destination, value date and possible split transfer. Until evidenced, keep an aged exception. If the later S$50 arrives, close with bank row ID and trace. Keep any transaction-level unmatched refund open regardless of the payout tie-out.

Related: [HarborCart case](../editorial/harborcart-case-lab.md) and [incident runbooks](../book/04-disputes-reconciliation-and-operations/17-payment-outages-incidents-and-operations.md).
