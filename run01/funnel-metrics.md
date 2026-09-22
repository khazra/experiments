# Measured funnel

“Opportunity” was never normalized into unique IDs. Counts below are register counts, not conversion rates.

| Stage | Count | Boundary | Evidence |
| --- | ---: | --- | --- |
| Unique opportunities seen | Not measurable | Search inventories and hypotheses were not deduplicated. | E-FUNNEL-003, E-SCOPE-004 |
| Hypotheses registered | 56 | 42 parked, 6 awaiting response, 5 superseded, 3 closed. | E-FUNNEL-003, E-FUNNEL-005 |
| Market-facing tracked records | 30 | 5 listed, 8 proposed, 2 submitted-awaiting-review, 12 withdrawn, 1 declined, 2 platform-error. | E-FUNNEL-002 |
| Applications | 6 | Five pending; one awaiting eligibility. | E-FUNNEL-004, E-FUNNEL-006 |
| Verifier-rejected delivery routes | 2 | Not counted as accepted delivery. | E-RUNTIME-002, E-RUNTIME-003, E-DROP-014, E-DROP-015 |
| Reached buyer/platform review | 3 | One later declined; two pending/unpaid. | E-RUNTIME-005, E-RUNTIME-006, E-RUNTIME-011, E-DROP-003 |
| Accepted | 0 | No tracked record or ledger event establishes acceptance. | E-FUNNEL-005, E-FUNNEL-006 |
| Paid | 0 | Empty payment register; ledger USD 0. | E-FUNNEL-001, E-FUNNEL-005, E-FUNNEL-006 |

## Observable durations

| Item/state | Duration | Result | Evidence |
| --- | ---: | --- | --- |
| Puzzle delivery to buyer decision | 22h56m42s | Editorial decline; no acceptance/payment. | E-RUNTIME-011, E-RUNTIME-014, E-DROP-003 |
| Feedback submission to pause | 94h42m03s | Pending/unpaid at final successful check. | E-RUNTIME-005, E-FUNNEL-004, E-FUNNEL-006 |
| Resource submission to pause | 87h28m15s | Pending/unpaid at final successful check. | E-RUNTIME-006, E-FUNNEL-004, E-FUNNEL-006 |
| Six applications to pause | Roughly 86-95h | Five pending and one eligibility unresolved. | E-FUNNEL-002, E-FUNNEL-004, E-FUNNEL-006 |
| First verifier route | 4m28s from first acknowledged submission to stop | Two verifier failures. | E-RUNTIME-002, E-DROP-014 |
| Second verifier route | 21s submission to observed failure | Internal verifier error. | E-RUNTIME-003, E-DROP-015 |

## Interpretation limits

Aggregate stage time and conversion rates are not measurable. Pending durations end at the experiment cutoff, not at eventual buyer resolution. Local scope cutoffs are not buyer rejections. Reconciliation timestamps are not provider-read timestamps. Wallets were not refreshed at pause, so USD 0 remains a ledger position. [E-FUNNEL-001] [E-FUNNEL-004] [E-FUNNEL-005]
