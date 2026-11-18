# Artifact — Payment Incident Review (PIR)

**Status:** Adaptable template and filled fictional example · Companion: [Chapter 17](../book/04-disputes-reconciliation-and-operations/17-payment-outages-incidents-and-operations.md)

## A. Blank template

**Incident ID / title / severity:**  
**Date and timezone / UTC window:**  
**IC / technical lead / Payments PM / PSP contact / finance contact / risk/compliance contact:**  
**Affected legal entity, markets, payment methods, providers and customer segments:**  
**Customer symptom versus verified payment reality:**  
**Evidence sources and freshness:**  
**Direct monetary exposure and currency (confirmed vs potential):**  
**Affected distinct orders, payment operations, auth attempts, captures and payouts:**  
**First detection, containment, restoration and financial close timestamps:**  
**What was unknown at each decision point:**  
**Risk constraints and who approved exceptional actions:**  
**Customer messaging and support recovery:**  
**Prevention actions (owner, due date, validation method):**  
**Links to immutable event trail, provider incident, reconciliation exceptions and dashboards:**

### Incident chronology

| Time + timezone | Verified observation | Decision | Decision owner | Evidence link | Residual uncertainty |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

### Recovery checklist

- [ ] Containment verified; no unauthorized retries or capture replays.
- [ ] All affected payment operations either financially resolved **or** assigned a dated exception case with owner.
- [ ] Unique orders, attempts, captures and payouts reconciled separately; monetary variance explained or escalated.
- [ ] Customer communications consistent with verified states; support queue monitored.
- [ ] Regulated or contracted incident notification decisions reviewed by compliance/legal.
- [ ] Corrective actions have an owner, date, automated test and metric to prove recurrence is prevented.

## B. Example: lost webhook acknowledgments

*All details fictional.* At 09:04 SGT, HarborCart begins to misclassify PSP-authorized payments as checkout failure after a callback consumer release. The PSP reports healthy authorization service; internal callback lag rises. Some customers click **Pay again**.

| Time (SGT) | Evidence | Decision | Owner | Unknown |
| --- | --- | --- | --- | --- |
| 09:04 | Unknown outcome queue up 4×; no corroborating issuer decline spike | Incident declared; suppress generic failure message | IC + PM | Which requests reached issuer |
| 09:09 | PSP status API confirms successful authorizations for sample operations | Prevent unsafe new attempts on unresolved orders; preserve IDs | Eng + risk | All outstanding cohorts |
| 09:20 | Captures exist for 27 orders missing merchant confirmation | Create finance exception list; safe pending communication | Finance + PM | Whether fulfilment happened |
| 09:30 | Callback consumer rollback succeeds | Reprocess only with durable deduplication and verified state constraints | Eng | Two late cases |
| 10:15 | Two cases still unresolved | Keep incident follow-up open with named owners | IC + finance | Final state for two IDs |

**What this does not mean:** 27 duplicate captures, 27 double-charged customers or a 100% recovery rate. Those would be separate findings requiring matching capture and bank records.

### Corrective actions for example

1. Add regression test for late/duplicate/out-of-order callback delivery (engineering owner).
2. Add customer-visible pending state and status-query retry safeguards (PM and engineering).
3. Alert on unknown operations older than approved threshold by value and affected distinct orders (SRE).
4. Add merchant/PSP/bank exception reconciliation on affected events (finance and data).
5. Verify all remaining exceptions and customer remediation before finance close (finance/support).

**Postmortem principle:** Describe how the system and controls failed, not merely which person clicked deploy. A green API dashboard is not proof that the payment incident is financially closed.
