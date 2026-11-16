# 1. What is a payment?

**Part I — Understanding Payments** · Prerequisites: none

## Learning outcomes

By the end of this chapter, you should be able to distinguish the **customer's instruction**, the **payment message**, the **transfer of value**, and the **commercial obligation**; describe the difference between a card purchase and a bank transfer; and explain why a successful screen does not necessarily prove final settlement.

## 1.1 The deceptively simple promise

A payment moves purchasing power from a payer to a payee to satisfy an obligation. In practice, a payment product must answer six questions: **who** is paying, **who** should receive it, **how much** and in **which currency**, **with whose authority**, **through which rail**, and **how both parties know what happened**. The customer often sees one button. Behind it may be authentication, authorisation, risk checks, messaging, ledger entries, settlement, notifications, and exceptions.

Keep four layers separate:

1. **Commerce layer:** An order or invoice represents what a customer owes. It may be cancelled, adjusted, partially fulfilled, or refunded.
2. **Instruction layer:** Someone initiates or authorizes a payment request. The instruction could be rejected before money moves.
3. **Processing and settlement layer:** A payment rail or network communicates the instruction and participating institutions discharge financial obligations. Timing and finality depend on the rail.
4. **Accounting layer:** Merchants and institutions record receivables, payables, fees, liabilities, refunds, and exceptions in ledgers. Reconciliation confirms whether independent records agree.
This is why `order_placed`, `payment_authorised`, `payment_captured`, `merchant_paid_out`, and `bank_reconciled` are not interchangeable facts.

## 1.2 Money is not necessarily a packet travelling across the internet

Imagine a customer with an account at Bank A paying a merchant banking with Bank B. Many payment systems move **messages and accounting claims**; balances are adjusted in the relevant institutions, with settlement via the payment system's rules. A card transaction commonly involves an issuer's approval followed by later clearing and settlement. An instant bank credit transfer can have a very different operational and finality model.

Do not assume that any given rail is immediate, irrevocable, universal, or available 24/7. The right statements depend on the scheme, jurisdiction, participant, and type of payment.

### Card payment versus push bank transfer

| Question | Typical online card purchase | Typical push bank transfer |
|---|---|---|
| Who starts it? | Shopper confirms a merchant payment; merchant submits through its processor | Payer instructs their bank/payment provider |
| Who decides? | Issuer responds to an authorization request subject to its controls | Payer's institution validates and initiates the transfer; recipient-side checks can also apply |
| Is the merchant paid immediately? | Not necessarily: authorization, capture, clearing, settlement and payout are distinct | Depends on rail and merchant integration; funds availability and business confirmation differ |
| How are errors recovered? | Void/reversal, refund or dispute depending on stage and rules | Return/recall/investigation mechanisms are rail-specific; not necessarily card-style chargebacks |
| What should the PM monitor? | Order conversion, attempt success, captures, settlement, disputes | Valid instructions, transfer outcomes, posting, reconciliation, mistaken transfers |

## 1.3 Three kinds of certainty

**Technical acknowledgement:** an API received the request. **Payment outcome:** the institution or payment system confirmed a specific state. **Financial certainty:** the appropriate ledger entries and settlement/payout obligations have actually been posted and reconciled. A 200 HTTP response proves little unless its business state is inspected. An asynchronous webhook may arrive later; duplicates and out-of-order messages are possible.

### Worked example: one basket, multiple money events

A grocery customer checks out with a **S$100** basket. The platform authorizes S$100 before picking. One unavailable item reduces the final total to **S$93**. If the provider and scheme support the required flow, the merchant can capture S$93 and release or let lapse the unused authorized portion; otherwise another adjustment model may be needed. The merchant's receipt, customer's bank view, PSP reports, internal order ledger, and settlement report can temporarily show different amounts or statuses without all being incorrect.

A robust design identifies **which system is authoritative for each question**. OMS is authoritative for the final basket; PSP or acquirer records for payment authorization/capture results; finance ledger for recognized balances; bank statement for actual cash movement. It also connects the records with stable identifiers.

## 1.4 The nonfunctional properties of money movement

- **Correctness:** no double capture, lost payment, or unaccounted refund.
- **Availability:** systems handle partner degradation without falsely reporting failures.
- **Idempotency:** repeating an intended operation does not multiply financial effects. Provider-specific scopes and retention periods must be understood.
- **Auditability:** investigators can trace an order to its attempts, captures, refunds, fees, and payouts.
- **Security and consent:** no unapproved use of credentials; limit sensitive-data exposure.
- **Recoverability:** an ambiguous outcome triggers verification, not a blind replay.
- **Fairness and transparency:** clear amounts, FX, fees, merchant identity, and customer remedy.

## 1.5 What the Payments PM asks

A feature request says, "Add a Pay button to the mobile app." A product review asks: Which customer obligation is being discharged? Who can initiate the payment? What state tells fulfillment to start? What if authorization completes but the response times out? Can the amount change? How will finance match a payment with an order? Who explains a delayed refund?

This is the essential shift: from **button and API** to **contract, money state, and recovery**.

## Check your understanding

1. A card payment is authorized but not captured. Has the merchant received a payout? Why not?
2. A payment API returns HTTP 200 with `status=pending`. What should the app display?
3. Why might the final order value differ from the original authorized amount?
4. Design a minimal identifier scheme linking order, payment, attempt, capture, refund, and payout.

**Next:** [2. The payments ecosystem](02-ecosystem.md).

## Further reading

- [Adyen — Payments lifecycle](https://docs.adyen.com/account/payments-lifecycle)
- [MAS — E-payments systems and Singapore infrastructure](https://www.mas.gov.sg/development/e-payments)
