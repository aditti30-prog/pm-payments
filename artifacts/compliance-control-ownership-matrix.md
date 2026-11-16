# Artifact — Compliance & Control Ownership Matrix

**Status:** Educational template · Companion: [Chapter 13A](../book/part-3/13a-compliance-and-control-ownership.md)

Fill one row per **specific product change and jurisdiction**. This is not legal advice, certification, a scheme attestation or a substitute for legal/security sign-off.

## Business context

- Product and launch markets: **[fill]**
- Legal contracting entity and licensed party: **[fill]**
- Merchant of record / funds custodian / acquirer / sponsor: **[fill]**
- Rails, payment channels (web, app, POS, card, transfer): **[fill]**
- Cardholder/account data flows and system owners: **[link to diagram]**
- Relevant regulations/standard/rules, exact version and checked-as-of date: **[fill]**
- Named compliance, risk, security and finance approvers: **[fill]**

## Control-to-delivery map

| Requirement / source / version | Applies? With rationale | Accountable specialist | PM requirement | Evidence and audit location | Exception/override approval | Launch gate / retest date |
| --- | --- | --- | --- | --- | --- | --- |
| PCI scoping + applicable SAQ / assessor route | TBD; depends on integration and acquirer assessment | Security / PCI owner | Data flow, page/script boundaries, provider integration contract | Data-flow diagram, provider attestations | PCI owner | Scope confirmed |
| AML/CDD for named licensed activity | TBD; confirm with legal/compliance | Compliance | Intake states and audit trail, permitted user communications | Approval trail, applicable notices | Compliance | Required checks pass |
| Merchant risk/underwriting | TBD; acquiring contract and segment | Risk + finance | Payout holds, limits, disclosures, exceptions | Risk policy version, signed decision, reserve ledger | Risk + finance | Controls configured and tested |
| Dispute handling and deadlines | TBD; scheme/acquirer/product | Acquirer/scheme operations | Case tracking, due dates, evidence UX | Dispute IDs and confirmed submission | Acquirer operations | Deadline dry run |
| Customer complaints and data retention | TBD; laws and merchant policy | Legal/compliance | Redacted support records and escalation | Policies and retention schedule | Legal/compliance | Review complete |

## Worked example: fictional provider iframe migration

A merchant wants to replace a PSP-hosted redirect with an embedded provider iframe. **Do not infer SAQ A status** merely because the card fields are hosted by the processor. The PM must supply a browser page/script data-flow diagram, receive PCI/security guidance on SAQ eligibility, verify provider compliance for the selected implementation, assess requirements such as applicable ASV scans, and confirm customer data/logging changes. The product may launch only after those owners sign the named gates.

**Source anchors (checked 16 November 2026):** [PCI SSC FAQ #1588](https://www.pcisecuritystandards.org/faqs/1588/) and [PCI SSC FAQ #1604](https://www.pcisecuritystandards.org/faqs/1604/). These explain specific SAQ A questions but do not individually determine an organization's compliance status.
