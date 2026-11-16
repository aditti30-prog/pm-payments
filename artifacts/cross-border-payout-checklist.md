# Cross-border payout PM readiness checklist

**Use case:** Launch a cross-border payout for one corridor, one provider and one recipient type. **Status:** Educational working template (16 November 2026).

## Define the monetary contract

- [ ] Payer amount, source currency, fee model and who pays third-party charges are unambiguous.
- [ ] FX rate source, quote expiry, booking timestamp, rounding and spread are recorded.
- [ ] The promised **recipient amount** is guaranteed or explicitly estimated, not ambiguous.
- [ ] Treasury knows prefunding, partner bank/corridor limits, holiday cutoffs and liquidity exceptions.
- [ ] Finance agrees how fees, returns and FX differences are posted and reconciled.

## Define the actor, obligations and ledger

- [ ] Legal/licensed and contracted role of platform, bank, PSP, FX provider and recipient is documented per corridor.
- [ ] Screening, KYB/KYC/AML, sanctions and privacy data transfers are reviewed by responsible control owners.
- [ ] Every leg has a unique transfer reference and permissible timeout/retry behavior.
- [ ] Customer receives truthful statuses (`initiated`, `funded`, `submitted`, `credited`, `rejected`, `returned`), using rail/provider-specific semantics.
- [ ] Bank and beneficiary confirmation are not falsely inferred from gateway/API success.

## Test failure and aftercare

- [ ] Invalid beneficiary account/name, delayed compliance screening, local holiday and insufficient liquidity.
- [ ] FX quote expires before transfer execution; FX booked but payout rejects.
- [ ] Return or recall after initial acknowledgment; duplicate payout request; partial fees on return.
- [ ] Customer refund or reissue requires documented FX/fee treatment and authorizations.
- [ ] Support and finance can trace a transaction without raw credentials or guessing across providers.

## Launch metrics
Track destination-bank-confirmed credit within stated ETA, total realized cost and fee transparency, return rate by reason, unresolved funds by age, FX losses and spread, complaints, and controlled financial exceptions per 1,000 payout attempts.

**Reference:** [Chapter 9A](../book/part-2/09a-cross-border-fx-and-treasury.md); [FSB G20 targets](https://www.fsb.org/work-of-the-fsb/financial-innovation-and-structural-change/cross-border-payments/g20-targets-for-enhancing-cross-border-payments-2/).
