# 19. Stablecoins, settlement and programmable money

**Part V — Modern and Emerging Payments** · **Reading time:** ~26 minutes · **Prerequisites:** [Payment economics](../part-1/04-payment-economics.md), [cross-border/treasury](../part-2/09a-cross-border-fx-and-treasury.md), [compliance](../part-3/13a-compliance-and-control-ownership.md) · **Source review:** 16 November 2026 · **Status:** Working draft

> **Guiding question:** If a token moves in seconds, has the merchant received usable money—and what could still fail?

## Learning outcomes

Separate the token, the issuer's redemption obligation, the distributed ledger, the exchange/on-ramp and the bank payout; explain mint/burn, custody, depeg and operational failure paths; and design practical PM guardrails for fiat-backed stablecoin payment use cases.

## 19.1 What is a stablecoin in a payment product?

A stablecoin is a token intended to maintain a stable value relative to a reference asset or currency. **A promise or mechanism to target a value is not a guarantee of redemption at par under every condition.** Different issuers, reserve arrangements, legal claims, chains and custodians create materially different risks. Do not treat all stablecoins as cash in a bank.

For example, Circle describes a business depositing USD with Circle to **mint USDC**, and depositing USDC for **redemption/burning**; ordinary holders may instead exchange via intermediaries. Redemption eligibility and legal terms matter. [Circle — USDC](https://www.circle.com/usdc); [Circle — USDC Terms](https://www.circle.com/legal/usdc-terms).

## 19.2 A stablecoin payment has at least two settlement layers

```mermaid
sequenceDiagram
  participant P as Payer / wallet
  participant Net as Blockchain / token ledger
  participant Cust as Merchant custodian/wallet
  participant Off as Off-ramp / issuer
  participant Bank as Merchant bank
  P->>Net: Send token to approved address
  Net-->>Cust: Token transfer confirmed under chain policy
  Cust->>Off: Request eligible conversion/redemption
  Off-->>Cust: KYC/limits/rate/processing status
  Off->>Bank: Fiat payout through bank rails
  Bank-->>Cust: Fiat credit confirmation
```

**On-chain confirmation** establishes a token-ledger event, not automatically the merchant's ability to spend fiat, the beneficiary's bank credit or the issuer's solvency. Chain reorganizations, wrong network, wrong destination, lost keys, sanctions blocks, custodial failures, off-ramp downtime and inadequate fiat liquidity can break the real-world journey.

## 19.3 Payments PM questions by layer

| Layer | Failure and risk | PM requirement |
|---|---|---|
| Issuer and reserve | Redemption restrictions, depeg, reserve exposure | Asset/issuer eligibility and escalation policy |
| Wallet and custody | Key loss, unauthorized transfer, signer compromise | Custody permissions, approvals, recovery controls |
| Network | Congestion, gas costs, reorg, wrong chain | Finality threshold, supported-chain allowlist and timeout status |
| Screening | Sanctioned address, illicit origin, beneficiary identity | Risk/compliance approval and hold/reject paths |
| Off-ramp | Exchange spread, FX, limited bank hours | Quote disclosure, bank payout ETA and reconciliation |
| Merchant accounting | Token value changes after sale | Valuation timestamp, posting currency, gain/loss and audit trail |
| Refund/dispute | No card-scheme chargeback by default | Separate refund authorization, return address verification and support process |

In many chains, a transfer to an incorrect address cannot simply be reversed by calling an API. Circle's own terms warn that third-party on-chain transfers may be irreversible; architecture should not promise reversibility. [Circle — USDC Terms](https://www.circle.com/legal/usdc-terms).

## 19.4 Worked case: token settled, fiat delayed

**Fictional:** A platform accepts 1,000 units of a USD-linked token for an invoice. The on-chain deposit reaches its chain-confirmation policy at 10:05. Its approved off-ramp blocks conversion pending review and USD payout has not arrived by close. The order can be `TOKEN_RECEIVED_CONFIRMED` while finance's `FIAT_PAYOUT_PENDING` remains outstanding. A product displaying `merchant_paid_out` would be wrong.

For an illustrative scenario, assume the platform sells the 1,000 token units for USD 997 after execution spread and fees. The USD 3 difference must be assigned to a documented fee/spread/valuation treatment according to finance policy. Never infer the legally permitted gain/loss treatment from the arithmetic alone.

## 19.5 Why programmable money is a PM problem

Smart contracts can condition actions on on-chain events (e.g., escrow or programmatic disbursement), but **smart contract execution cannot verify off-chain delivery or consumer consent without trusted external evidence**. Dispute outcomes, delivery proof, human overrides and fraud investigations must be handled in product policy and/or trusted intermediaries. Do not market an escrow contract as risk-free simply because it uses code.

Consider a split-merchant settlement: funds are released to a seller only after a delivery oracle reports success. What if the buyer disputes delivery, the oracle is compromised or a shipment is partially delivered? Product policy needs state, governance, deadlines, review and auditable override mechanisms. Fully automated irreversible release can worsen rather than improve customer outcomes.

## 19.6 Regulatory status must be dated

**Singapore anchor, checked 16 November 2026:** MAS published a stablecoin-framework consultation dated **1 September 2026** proposing legislative amendments to the Payment Services Act. A consultation is **not itself enacted law**. Do not claim an issuer or product is MAS-approved solely on that basis. Confirm current licences, notices, legal interpretation, reserve and redemption obligations with responsible counsel. [MAS consultation, 1 September 2026](https://www.mas.gov.sg/publications/consultations/2026/consultation-on-proposed-amendments-to-the-payment-services-act-for-stablecoin-regulation).

BIS analysis highlights systemic concerns about stablecoin integrity, convertibility and liquidity under stress; those concerns should be evaluated rather than assumed away by an issuer's marketing. [BIS Annual Economic Report 2025](https://www.bis.org/publications/aer-2025/next-generation-monetary-financial-system).

## 19.7 PM metrics and decision gates

Monitor rate of token transfers that reach your finality policy, on-chain-to-usable-fiat duration, on/off-ramp failure by corridor, withdrawal failures, depeg exposure, unconfirmed/incomplete deposits, exceptions unresolved after cutoff, fraud/sanctions control performance and loss-adjusted contribution after all fees. Launch gates include licensed partners where required, treasury liquidity, redemptions tested, wallet recovery, screening and accounting sign-off.

## Exercise and answer check

**Question:** A buyer sends token value to a merchant wallet, but the app shows “payment failed” due to an indexer outage. Should the app request the buyer send again?  
**Answer check:** No. The transfer may have occurred. Query authoritative chain/provider references and reconcile wallet receipts before enabling another payment. Preserve transaction hash, chain ID, destination, token contract and intended invoice; do not treat an app indexing failure as proof that no money moved.

**Next:** [20. Agentic commerce and delegated payments](20-agentic-commerce-delegated-payments.md).

## Primary sources

- [Circle — USDC mint/burn model](https://www.circle.com/usdc) (one issuer, not a universal stablecoin rule).
- [Circle — USDC Terms](https://www.circle.com/legal/usdc-terms) (issuer-specific legal terms; accessed 16 November 2026).
- [MAS — September 2026 stablecoin regulatory consultation](https://www.mas.gov.sg/publications/consultations/2026/consultation-on-proposed-amendments-to-the-payment-services-act-for-stablecoin-regulation) (proposal, not proof of enactment).
- [BIS — The next-generation monetary system, 2025](https://www.bis.org/publications/aer-2025/next-generation-monetary-financial-system) (risk analysis, not product implementation guidance).
