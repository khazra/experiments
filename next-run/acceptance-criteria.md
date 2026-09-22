# Acceptance criteria for any future authorized run

No run is authorized by this document. If one is separately approved, completion requires all criteria below.

## Safety and authority

- Written authorization defines window, budget, allowed accounts, and human approvers.
- No new paid account, software purchase, credit purchase, or paid harness call unless explicitly authorized.
- Future written authorization defines delegated routine actions and human approval boundaries; this document itself authorizes no contact or external side effect.
- No live security testing without explicit written authorization and scope.

## Commercial truth

- Proposal, delivery, acceptance, payment, availability, and spendability are distinct states.
- Revenue requires an evidenced payer, work item, acceptance, and transfer.
- Operator-funded tests are infrastructure cost, never revenue.
- Fees, refunds, taxes, infrastructure, model/harness cost, and human time are separate lines; unknowns stay unknown.
- Wallet/account balances are refreshed at the fixed cutoff or reported stale.

## Funnel and time

- Every unique opportunity receives one stable ID.
- Every transition has a provider observation timestamp and a separate reconciliation timestamp.
- Local closure is never labelled buyer rejection.
- Pending states carry a cause and censoring rule.
- Sector, channel, search, qualification, production, review, and settlement effort are recorded comparably.

## Quality

- Buyer criteria are captured before production.
- Each criterion receives PASS, FAIL, or UNMEASURABLE from a nonauthor reviewer before submission.
- Subjective criteria use a domain-appropriate human reviewer where required.
- Platform-verifier health is checked before implementation.

## Reliability and observability

- Consecutive failures trigger a breaker and durable alert.
- A named human tests the alert channel before start.
- Credential expiry and quota-reset conditions are recorded.
- Logs cover the entire window plus collection margin.
- Every external side effect has an idempotency key or equivalent provider mechanism.

## Stop and null-result discipline

- Every hypothesis has a falsification test and stop rule before action.
- A double zero, exhausted qualified inventory, or failed settlement qualification is publishable as the result.
- The registered comparison sample is not expanded after an unfavorable result. Separately budgeted discovery may continue outside that sample with its own record.
- Post-cutoff outcomes are reported separately and never move the original boundary.

- Work and collection windows are fixed separately before launch. Later payments are reported in the collection window without rewriting the work-window result.
- Numerical comparisons include sample limits and uncertainty; process-test success is not a commercial success claim.
