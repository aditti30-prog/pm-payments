# Glossary — payments language for product managers

Definitions are intentionally concise and provider-neutral where possible. Specific implementations and legal meanings vary.

## Participants

| Term | Working definition |
| --- | --- |
| **Acquirer / acquiring bank** | Financial institution or licensed acquiring entity enabling a merchant to accept card payments and assuming contractual obligations in the network |
| **Issuer** | Institution that issues the customer's payment card and typically decides card authorization requests |
| **Card network / scheme** | Organization and infrastructure establishing rules and routing/messages between network participants (e.g., Visa, Mastercard) |
| **Gateway** | Technical interface that connects a merchant checkout to payment processing capabilities; may be bundled with PSP/acquiring services |
| **PSP (payment service provider)** | Provider offering payment acceptance and related processing services, often across payment methods and merchant operations |
| **Processor** | Technology/service provider processing payment transaction messages; the exact role depends on issuer/acquirer context |
| **Payment orchestrator** | Layer coordinating access to multiple payment providers or methods, potentially including routing and unified reporting |
| **Payfac / payment facilitator** | Business model enabling merchant payment acceptance under a payment facilitator's arrangements and responsibilities, subject to market/scheme rules |
| **Merchant of record** | Entity legally responsible for selling goods/services and handling relevant customer/financial obligations; not automatically the platform provider |

## Transaction lifecycle

| Term | Working definition |
| --- | --- |
| **Payment attempt** | One submitted attempt to complete payment; an order can have multiple attempts |
| **Authorization** | Issuer/financial institution decision to approve a payment request, generally reserving funds/credit in the common card flow |
| **Authentication** | Verification step establishing confidence in a payer's identity or the legitimacy of use; not the same as authorization |
| **Capture** | Action submitting an authorized payment for completion/financial processing, where the payment method supports separated authorization and capture |
| **Clearing** | Exchange and processing of financial transaction information used to establish payment obligations |
| **Settlement** | Financial discharge/transfer of obligations among participating institutions according to their rules |
| **Payout** | Funds disbursed by the acquirer/PSP/platform to a merchant or beneficiary; payout timing need not match settlement status |
| **Authorization hold** | Temporary reservation of available funds/credit following authorization, subject to issuer/payment-method behavior |
| **Void / reversal** | Cancellation/reversal of an authorization or payment operation where supported, distinct from refund of an already completed payment |
| **Refund** | Returning funds from a prior payment; may take time to reach the payer |
| **Dispute / chargeback** | Formal contest of a card transaction that may lead to retrieval, evidence, representment, fees and liability allocation under rules |
| **Reconciliation** | Matching internal orders, payment records, provider reports, settlements and bank movements to identify missing/different entries |
| **Idempotency** | Property where repeating the same operation with the correct identity does not perform the intended business operation more than once |
| **Webhook** | Provider-to-merchant event notification, often delivered asynchronously; duplicates or delays must be handled |
| **Unknown outcome** | A transaction whose final result has not been established; not evidence of success or failure |

## Risk and authentication

| Term | Working definition |
| --- | --- |
| **EMV 3DS / 3-D Secure** | Protocol supporting cardholder authentication in e-commerce card transactions |
| **Frictionless 3DS** | Authentication completed without an interactive cardholder challenge under applicable EMV 3DS flow |
| **Challenge 3DS** | Authentication that asks the cardholder to take an additional action (e.g., OTP or bank-app confirmation) |
| **SCA (Strong Customer Authentication)** | Regulatory requirement in certain jurisdictions/use cases requiring qualifying authentication; exact applicability/exemptions vary |
| **False decline** | Legitimate payment rejected, whether by issuer or risk system; measurement requires careful validation |
| **Soft vs hard decline** | Informal/provider-specific classification of declines as potentially recoverable vs effectively final; do not assume uniform mapping or retry permissions |
| **FPAN (Funding PAN)** | Underlying card account payment credential number associated with the card; not the same as a bank deposit-account number |
| **DPAN (Device PAN)** | Network-tokenized payment credential provisioned for a device or wallet context; often has different last four digits from the FPAN |
| **Network token** | EMV payment token usable through compatible payment rails within applicable token-domain restrictions, distinct from a provider vault token |
| **Token service provider (TSP)** | Entity/system implementing the payment-token programme's token issuance, mapping and lifecycle controls |
| **Cryptogram** | Transaction-specific cryptographic data used in applicable token or EMV payment processes; not interchangeable with an FPAN or a 3DS outcome |
| **Payment Account Reference (PAR)** | Reference that can link related PAN and payment tokens for permitted use cases; not itself used as a chargeable payment credential |
| **Three-way reconciliation** | Comparison of three independent sources, often merchant ledger, PSP/acquirer settlement records and bank cash statements; participants vary by model |
| **Representment** | Formal evidence-based response contesting a card-network chargeback under applicable rules |
| **Tokenization** | Replacing sensitive payment credentials with tokens; network tokens and PSP vault tokens have different issuers and semantics |
| **PCI DSS** | Payment Card Industry Data Security Standard, covering applicable cardholder-data security controls and assessments |

## Product and economics

| Term | Working definition |
| --- | --- |
| **Authorization rate** | Approved authorization attempts divided by a specified population of eligible authorization attempts; definition must be documented |
| **Payment success by order** | Orders with a confirmed successful payment divided by orders that initiated payment (definition needs explicit window/deduplication) |
| **Checkout conversion** | Completed purchases divided by eligible checkout sessions |
| **MDR (merchant discount rate)** | Fee structure/rate charged for card acceptance, typically encompassing multiple economic components depending on agreement |
| **Interchange** | Fee component of many card transactions flowing from acquirer side toward issuer side under network economics; market rules vary |
| **Scheme/network fee** | Fee component set/charged in the card network ecosystem according to network rules |
| **Take rate** | Revenue captured by a business relative to relevant payment volume; define whether gross or net and which fees are included |
| **GMV (gross merchandise value)** | Gross value of merchandise/orders transacted; not equal to revenue, margin, or settled cash |
| **Contribution margin** | Revenue or gross margin remaining after a defined set of variable costs; finance must confirm specific methodology |

## Related reading

- [Chapter 1: What is a payment?](../book/part-1/01-what-is-a-payment.md)
- [Chapter 3: Card payment lifecycle](../book/part-1/03-card-payment-lifecycle.md)
- [Chapter 7A: FPAN, DPAN and network tokens](../book/part-2/07a-network-tokenization-fpan-dpan.md)
- [Chapter 11: 3-D Secure](../book/part-3/11-3d-secure.md)
- [Chapter 12: Authorization optimization](../book/part-3/12-authorization-optimization.md)
- [Chapter 15: Chargebacks](../book/part-4/15-chargebacks-and-disputes.md)
- [Chapter 16: Three-party reconciliation](../book/part-4/16-three-way-reconciliation.md)

## Modern platforms, treasury and AI agents (v0.5)

| Term | Working definition / PM implication |
|---|---|
| **Sub-merchant** | Seller supported within a PayFac/platform acquiring arrangement; assess underwriting and liability by actual contract |
| **Platform liable balance** | PSP/provider balance to which platform obligations, fees or shortfalls can be booked; not necessarily revenue |
| **Negative balance** | Seller/provider balance below zero due to refunds, disputes, fees or advances; requires owner and recovery policy |
| **Off-ramp** | Converts a token/digital asset into fiat through eligible providers; token receipt does not guarantee bank credit |
| **FX rate lock** | Quote validity constraint; conversion rate may expire before money is sent |
| **Offline EMV / store and forward** | Terminal-local acceptance modes during connectivity loss; final financial outcome may remain pending |
| **Dunning** | Communications and permitted collection recovery for overdue subscription invoices |
| **APP scam** | Authorized-push-payment fraud where a payer can be deceived into initiating a valid bank transfer |
| **Agentic commerce** | Agent-assisted discovery and purchasing involving commerce, customer permission and payment execution as separate layers |
| **Checkout Mandate (AP2)** | Verifiable authorization for a specific or constrained checkout under a versioned AP2 specification |
| **Payment Mandate (AP2)** | Verifiable permission for a scoped payment, tied to a checkout; distinct from issuer authorization |
| **ACP** | Agentic Commerce Protocol; commerce/checkout interoperability initiative from OpenAI and Stripe |
| **UCP** | Universal Commerce Protocol; a versioned commerce standard with capability descriptions, checkout and extensibility |
| **Scoped payment credential** | Token or reference limited to allowed merchant/amount/time or other controls as supported; not unlimited PAN authority |

See [Chapter 20](../book/part-5/20-agentic-commerce-delegated-payments.md) for the differences between agent identity, customer intent, credential issuance and payment authorization.
