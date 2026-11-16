# Primary sources and editorial notes

**Source review date:** 16 November 2026 (new compliance, measurement and v0.5 topic references; older chapters still require periodic specialist review). These references supplement the original explanation in this textbook; they do not imply provider endorsement.

## Payment lifecycle and implementation

1. **Adyen — Payments lifecycle**: https://docs.adyen.com/account/payments-lifecycle  
   Useful for understanding how one PSP distinguishes authorized, captured, settled, payout-related and unsuccessful statuses. **Provider-specific**, not a universal state machine.
2. **Adyen — Payment result codes**: https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes/  
   Shows payment result semantics, including refusal, cancellation and partial-authorization examples. **Provider-specific**.
3. **Adyen — Refusal reasons**: https://docs.adyen.com/development-resources/refusal-reasons  
   Explains refusal reason codes and why an HTTP success response is not necessarily a payment approval. **Provider-specific**.
4. **Adyen — Response handling**: https://docs.adyen.com/development-resources/overview-response-handling/  
   Relevant to mapping processor and acquirer responses. **Provider-specific**.
5. **Stripe — Payment Intents**: https://docs.stripe.com/payments/payment-intents  
   Illustrates payment intent, lifecycle, cart/session reuse and post-payment webhook guidance. **Provider-specific**.
6. **Stripe — Idempotent requests**: https://docs.stripe.com/api/idempotent_requests  
   Describes one provider's idempotency semantics; API versions differ and key retention can matter. **Provider-specific**.

## Standards and security

7. **EMVCo — EMV 3-D Secure**: https://www.emvco.com/emv-technologies/3-d-secure/  
   Standards-maintainer entry point for EMV 3DS, including frictionless and challenge authentication.
8. **EMVCo — 3DS White Paper introduction**: https://www.emvco.com/dynamic/emv-3-d-secure-whitepaper-v2/introduction/  
   Discusses protocol features and scenarios; implementations can vary by 3DS program.
9. **PCI Security Standards Council — Document Library**: https://www.pcisecuritystandards.org/document_library/  
   Official place to retrieve the applicable PCI DSS standard. The presence of a source link does not establish an individual merchant's assessment scope or compliance.

## Editorial fact-check checklist

Before publishing or updating a payments claim:

- Name the **payment method, region, provider and scenario** when behavior varies.
- Separate **issuer authorization**, **payment capture**, **settlement** and **merchant payout**.
- Mark any statements about retrying declines, liability shifts, or authentication exemptions as **conditional** unless supported by current applicable rules.
- Use verified primary documents for provider status codes and API semantics.
- Treat security, regulatory and scheme matters as needing specialist sign-off.
- Label hypothetical statistics and sample customer journeys as illustrative.

See [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution standards.

## v0.4 — Compliance scope and operational decisions (checked 16 November 2026)

- **PCI SSC — SAQ A embedded script FAQ #1588**: https://www.pcisecuritystandards.org/faqs/1588/ — specific eligibility guidance; consult full current SAQ and acquirer.
- **PCI SSC — SAQ A ASV scanning FAQ #1604**: https://www.pcisecuritystandards.org/faqs/1604/ — scope of remaining scanning obligations even with outsourced payment processing.
- **FATF — Recommendations, updated June 2026**: https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html — international AML/CFT framework implemented per jurisdiction.
- **MAS — Payment Services Act**: https://www.mas.gov.sg/regulation/payments — Singapore licensing and payments regulation overview.
- **MAS — Notice PSN01**: https://www.mas.gov.sg/regulation/notices/psn01-aml-cft-notice---specified-payment-services — rules for specified payment service providers, not a universal merchant rule.
- **Stripe — Comparing authorization metrics**: https://stripe.com/guides/maintaining-payments-performance-when-adopting-stripe — first-attempt, raw and de-duplicated definitions (provider-specific).
- **OWASP — Webhook Security Cheat Sheet**: https://cheatsheetseries.owasp.org/cheatsheets/Webhook_Security_Cheat_Sheet.html — signature/replay/duplicate safety.
- **Adyen — Invoice reconciliation**: https://docs.adyen.com/reporting/invoice-reconciliation/ — provider-specific settlement/cost reporting.

## v0.5 — Platform funds flow, modern rails and agentic commerce (checked 16 November 2026)

- **Adyen — Marketplace split transactions:** https://docs.adyen.com/platforms/online-payments/split-transactions — specific provider allocation behavior, not universal PayFac law.
- **Adyen — Offline POS payments:** https://docs.adyen.com/point-of-sale/offline-payment — offline EMV and store-and-forward, including merchant exposure.
- **Adyen — Stored credential payments:** https://docs.adyen.com/online-payments/tokenization/make-token-payments — shopper-initiated vs merchant-initiated distinctions.
- **FSB — Cross-border payment targets:** https://www.fsb.org/work-of-the-fsb/financial-innovation-and-structural-change/cross-border-payments/g20-targets-for-enhancing-cross-border-payments-2/ — targets, not a claim of achieved outcomes.
- **BIS — FX settlement risk (June 2026):** https://www.bis.org/publ/qtrpdf/r_qt2606c.htm — risk evidence.
- **MAS — Combatting scams and SRF:** https://www.mas.gov.sg/regulation/combatting-scams — defined Singapore phishing-scam scope, not a universal reimbursement guarantee.
- **ABS — PayNow:** https://www.abs.org.sg/e-payments/pay-now — Singapore alias/FAST mechanism.
- **UK Open Banking — PIS guidelines (March 2026):** https://standards.openbanking.org.uk/customer-experience-guidelines/payment-initiation-services/latest/ — UK-specific payment initiation.
- **Circle — USDC terms:** https://www.circle.com/legal/usdc-terms — issuer-specific redemption and transfer risks.
- **MAS — Stablecoin consultation (September 2026):** https://www.mas.gov.sg/publications/consultations/2026/consultation-on-proposed-amendments-to-the-payment-services-act-for-stablecoin-regulation — proposal, not enacted law.
- **Stripe — ACP:** https://stripe.com/blog/developing-an-open-standard-for-agentic-commerce — OpenAI/Stripe commerce standard announcement.
- **UCP — Protocol announcements and version updates:** https://github.com/Universal-Commerce-Protocol/ucp/blob/main/docs/documentation/announcements.md — versioned commerce protocol.
- **Google — AP2 v0.2 specification:** https://github.com/google-agentic-commerce/AP2/blob/main/docs/ap2/specification.md — Checkout/Payment Mandates, not automatic issuer approval.
- **Visa — Intelligent Commerce:** https://developer.visa.com/capabilities/visa-intelligent-commerce/overview — Visa-specific program, restrictions.
- **Mastercard — Agent Pay:** https://www.mastercard.com/sg/en/news-and-trends/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai.html — Mastercard-specific network-token program.

**Version discipline:** Where sources describe **AP2 v0.2**, do not substitute older `CartMandate` examples for `CheckoutMandate`. An open protocol, preview, pilot or partner announcement does not demonstrate universal market or merchant availability.
