# 13B. Scam protection and regulatory scoping: Singapore examples

**Part III — Building Payment Products** · **Estimated study time:** ~19 minutes · **Prerequisites:** [Risk controls](13-fraud-risk-and-payment-controls.md), [compliance ownership](13a-compliance-and-control-ownership.md) · **Source review:** 16 November 2026 · **Status:** Working draft

> **Guiding question:** A payment can be properly authorized and still be a scam. What can the product prevent, and who is responsible for the customer's loss?

## Learning outcomes

Distinguish unauthorized-payment fraud from authorized-push-payment (APP) scam patterns; design interventions that preserve legitimate access; map product features to legal/scheme/provider obligations; and avoid applying Singapore guidance globally.

## 13B.1 Not every scam looks like a stolen-card transaction

| Situation | Payment state | Customer's understanding | Product implications |
|---|---|---|---|
| Stolen card CNP purchase | May be cardholder-unapproved | Cardholder did not make purchase | Authentication, fraud signals, dispute routes |
| APP scam / social engineering | Payer may initiate valid bank transfer | Payer deceived about recipient/purpose | Beneficiary checks, warnings, cooling-off, recovery escalation |
| Account takeover | Attacker controls channel/account | Legitimate user did not intend transfer | Account recovery, device/session controls, transaction limits |
| Refund scam / fake support | Customer persuaded to pay or reveal credentials | Misrepresented counterparty | Report flow, verified support channels, communication |

**Fraud indicators are not proof of criminal behavior.** More prompts can stop some losses but also block vulnerable or unfamiliar customers. A PM must measure scam loss **and** false blocks, complaint outcomes, accessibility and customer support burden.

## 13B.2 Build a protection journey, not merely a blocking rule

```mermaid
flowchart TD
  A[Customer starts transfer] --> B[Recipient / device / behavioral risk assessment]
  B --> C{Within permitted control policy?}
  C -->|Lower risk| D[Continue with clear recipient confirmation]
  C -->|Elevated| E[Contextual warning, independent verification / cooling-off if required]
  E --> F{Customer allowed to continue?}
  F -->|Yes, permitted| D
  F -->|No or blocked| G[Safe halt + support / review]
  D --> H[Send / outcome tracking]
  H --> I[Report scam, attempt recovery, preserve evidence]
```

Design intervention choices with risk/legal approval: beneficiary-name confirmation where available, new-payee friction, unusually large transfer thresholds, device-change protection, time-limited hold for specific approved circumstances, accessible emergency reporting and trusted callback channels. Avoid promising recall/funds recovery on irreversible rails.

## 13B.3 Singapore: distinguish SRF phishing from authorised-payment scams

**Scope anchor — checked 16 November 2026:** The MAS/IMDA **Shared Responsibility Framework (SRF)** took effect on **16 December 2024**. Its loss-sharing rules concern a *defined phishing-credential compromise* sequence: a scammer impersonates a legitimate organisation, obtains account credentials through a digital message and fabricated platform, and uses them to execute a transaction the account user **did not intend**. SRF is **not** a general reimbursement scheme for customers who intentionally initiate payments after being deceived, such as typical investment or romance scams. [MAS/IMDA SRF Guidelines](https://www.imda.gov.sg/-/media/imda/files/regulations-and-licensing/regulations/consultations/2024/shared-responsibility-framework-for-phishing-scams/guidelines-on-shared-responsibility-framework.pdf); [MAS scam overview](https://www.mas.gov.sg/regulation/combatting-scams).

**Separate card treatment:** SRF's loss-sharing provisions explicitly **exclude transactions on Singapore-issued credit, charge and debit cards** (footnote 1 of the Guidelines). Card-specific and other applicable protections require separate analysis.

**Authorised-transfer scam intervention:** Singapore's **Protection from Scams Act 2025** commenced **1 July 2025**. It empowers **Police**—when statutory criteria are met—to issue Restriction Orders to banks restricting access to relevant banking and credit facilities to help prevent transfers or withdrawals benefitting scammers. It is **not** blanket authority for a product team to block any payment it dislikes. [Ministry of Home Affairs commencement notice](https://www.mha.gov.sg/media-room/newsroom/commencement-of-the-protection-from-scams-act/).

| Fictional situation | SRF status | Operational PM action |
|---|---|---|
| A phishing site captures protected-account credentials; attacker transfers money | **Potentially in scope**, only if all statutory/guideline facts and duties fit | Secure account, preserve records and apply appropriate investigation/reporting workflow |
| Customer voluntarily sends funds to a fake investment adviser | **Generally out of scope** of SRF's phishing-credential definition | Immediate bank/police reporting, trace/recall if supported, authorised controls and scam-support response |
| Customer disputes a scam card transaction on a Singapore-issued card | **Excluded from SRF loss-sharing rules** | Follow applicable card, bank, dispute and fraud pathways |

**Product requirement:** Record payment instrument, account, who initiated the transaction, credentials compromised, scam type, legal basis, response owner, reporting and remediation promises. Compliance/legal determines scheme/regulatory scope; the PM makes the approved policy implementable.

## 13B.4 Regulatory scoping is a product discovery task

For a new payments capability, create an **activity-by-jurisdiction matrix**, rather than choosing a licence label from the API vendor's brochure.

| Product change | Questions to investigate | Product deliverable |
|---|---|---|
| Launch a Singapore consumer wallet | Are we issuing an account or e-money? Who safeguards balances? | Licensed-entity and funds custody map |
| Merchant acquiring | Who processes merchant receipts and underwrites merchants? | Provider/merchant responsibility matrix |
| Cross-border remittance | Are we facilitating inbound/outbound transfers or only providing software? | Currency/corridor partner and licence map |
| Card-on-file recurring checkout | Which merchant, scheme and authentication obligations apply? | Stored-credential consent and retention map |
| AI shopping agent | Who is credential provider, agent, MoR and regulated PSP? | Explicit authorization and liability model |

**Singapore legal anchor:** MAS's [Payment Services Act overview](https://www.mas.gov.sg/regulation/payments) and [licensing page](https://www.mas.gov.sg/regulation/payments/licensing-for-payment-service-providers) distinguish activity classes; actual applicability is fact-dependent and can change. A licence of a PSP does **not** automatically authorize an unrelated platform to provide every underlying service. Other countries require separate mapping rather than copying MAS classifications.

## 13B.5 Test and metrics

Instrument attempted and confirmed scam loss separately, risk-trigger cohorts, false positives, fraction of high-risk transfers with validated recipient confirmation, time to freeze/report, recovery attempt rate and customer support resolution. Use an adequate maturation window: a scam reported after two weeks must be attributed to the original transaction cohort, not solely the report date.

**Worked case:** Fraud operations asks for a 24-hour hold on all newly added beneficiaries. The PM should not accept or reject based only on aggregate loss reduction. Segment by transfer amount, destination and real risk signals; check legal authority and user harm; estimate false positives and urgent bill-payment consequences; design a risk-approved limited experiment and customer-appeal path.

## Exercise and answer check

**Question:** A Singapore customer is tricked into voluntarily sending money to a scammer. Is the bank necessarily liable under SRF?  
**Answer:** Generally **no**. A transfer the customer voluntarily initiated after deception usually falls **outside** the SRF's defined phishing-credential transaction scope. Verify the facts, but don't present SRF as general compensation. Trigger immediate bank/police reporting, trace/recovery where possible, approved scam controls and consideration of other legal protections (including the Protection from Scams Act). Authentication does not prove the customer was not deceived.

**Next:** [14. Payments PM craft](14-payments-pm-craft.md).

## Primary references

- [MAS/IMDA — SRF Guidelines (effective 16 December 2024)](https://www.imda.gov.sg/-/media/imda/files/regulations-and-licensing/regulations/consultations/2024/shared-responsibility-framework-for-phishing-scams/guidelines-on-shared-responsibility-framework.pdf) (definition, duties and card exclusion).
- [MHA — Protection from Scams Act commenced 1 July 2025](https://www.mha.gov.sg/media-room/newsroom/commencement-of-the-protection-from-scams-act/) (Police-issued restriction orders).

- [MAS — Combatting scams and the Shared Responsibility Framework](https://www.mas.gov.sg/regulation/combatting-scams) (Singapore only; accessed 16 November 2026).
- [MAS — Payment Services Act regulatory overview](https://www.mas.gov.sg/regulation/payments) (Singapore only; accessed 16 November 2026).
- [MAS — Licensing for payment service providers](https://www.mas.gov.sg/regulation/payments/licensing-for-payment-service-providers) (Singapore only; accessed 16 November 2026).
