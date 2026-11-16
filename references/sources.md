# Primary sources and editorial notes

**Source review date:** 15 November 2026. These references supplement the original explanation in this textbook; they do not imply provider endorsement.

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
