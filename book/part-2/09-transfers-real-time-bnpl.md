# 9. Account transfers, real-time rails and buy now, pay later

**Part II — Payment Products & Infrastructure** · Prerequisites: Chapters 1–4

## Learning outcomes

Explain the distinction between push and pull account payments, how proxy addressing differs from settlement infrastructure, and why BNPL combines a checkout payment experience with financing and credit servicing.

## 9.1 Push and pull

In a **push** payment, the payer authorizes their institution to send funds to a recipient. In a **pull** arrangement, an authorized payee/payment provider initiates collection under a mandate, subject to the rail's and jurisdiction's protections. Direct debit and bank-transfer products therefore differ in consent, dispute, reversibility, failure handling and operational risk. A PM must design the mandate and cancellation journey as carefully as the first payment.

## 9.2 What 'instant' really means

A faster payment rail can transfer funds quickly between participating institutions; this does not guarantee that a merchant app immediately knows which order was paid, that a refund is instantaneous, or that a mistaken recipient can always be reversed. Merchant reconciliation still depends on accurate references, notifications and bank statement mapping. Availability of cross-border transfer may depend on currency corridors, participants and FX arrangements.

In Singapore, **FAST** is the fund-transfer infrastructure and **PayNow** provides recipient addressing via supported proxies. When a bank app resolves a phone number, that is not necessarily the same step as transferring funds. An account lookup can succeed while the subsequent payment fails. Never mark an order paid based on address resolution alone.

## 9.3 Open banking payment initiation

Some systems allow a third party, with appropriate authorization, to initiate payment from a customer's bank account. The service may redirect to bank authentication or use other approved authentication flows. Critical questions: what is the scope of consent; who is the licensed party; who is liable for failed/misdirected payments; how long does the consent last; and how can a merchant receive reliable outcome notifications? Country rules differ considerably; do not generalize European PSD2 flows to Singapore or the US.

## 9.4 BNPL is also credit

**Buy now, pay later** lets a shopper obtain goods/services while repayment is spread according to an agreement. The merchant may be paid by a financing provider subject to commercial terms, while the provider or its partners manage customer eligibility, credit exposure, collections and servicing. The checkout journey may look like one more tender, but the underlying product includes underwriting, repayment schedules, late-payment policy, refunds, disputes, partner funding and consumer protection.

### BNPL worked example

A shopper chooses a hypothetical **S$240 purchase in four S$60 installments**, with no assumed fees or interest for this example. The PM must specify: when the merchant is funded; how the customer's repayment obligations arise; how a partial S$40 return adjusts the schedule; who owns disputes about non-delivery; how missed installments are handled; and which disclosures are required. Do not conclude that "four payments" implies a zero-cost product or a universal underwriting model.

## 9.5 Which method should a merchant add?

Make the decision by **eligible customer reach**, completion lift versus cannibalization, contribution margin, reliability, fraud and operational risk, refund quality and settlement complexity. A new local payment method may unlock a market where card penetration is weak. It can also create extra support work if matching bank transfers to orders requires manual investigation.

## Practice

A merchant offers cards, FAST bank transfers, and BNPL. Build a comparison table covering payment confirmation, payout, refund mechanism, customer recourse, merchant cost and operational burden. Identify where you need provider-specific evidence.

**Exercises:** [Worked solutions](../../answers/chapter-exercises.md#09-transfers-real-time-bnpl) (companion answer key; review your reasoning before opening).

**Next:** [9A. Cross-border FX, treasury and payouts](09a-cross-border-fx-and-treasury.md).

## Further reading

- [MAS — E-payments](https://www.mas.gov.sg/development/e-payments)
- [BIS — Next-generation monetary and financial system](https://www.bis.org/publications/aer-2025/next-generation-monetary-financial-system)
