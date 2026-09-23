# Assessment: is another autonomous earning experiment worth running?

Assessment date: September 23, 2026. Author: Amp assistant, following discussion with the experiment owner. This is a post-publication assessment, not another blinded review, an independently audited financial statement, or a calibrated forecast. It does not modify the frozen run-01 outcome, incorporate later private live checks into that outcome, or authorize a restart, customer contact, account creation, purchase, or deployment.

## Recommendation

**Another round could be worth running as a tightly budgeted learning exercise. A general-purpose, cold-start agent should not currently be expected to become reliably self-financing.** Repeating the first experiment with a better prompt, more time, or a stronger model alone is not a persuasive investment case.

The owner should not supply the buyers. Finding and converting buyers was part of the original task; removing customer acquisition would change the question into autonomous delivery. A future design may provide lawful business identity and payment infrastructure as explicitly changed starting resources, while leaving prospect discovery, qualification, negotiation, and delivery to the agent.

The recommendation is a judgment under uncertainty, not a numerical estimate of success. Funding another round makes sense only if the owner would willingly spend the capped budget for the information it produces, including a zero-revenue result.

## What run 01 establishes, and what it does not

The [postmortem](../run01/postmortem.md) records zero accepted-and-paid revenue at the September 22 pause after 96h15m09s of a planned 120 hours. The remaining 23h44m51s was outside the frozen observation window. This is not a completed five-day outcome or a current audit of every receiving account. [E-FUNNEL-001] [E-SCOPE-004] [E-SCOPE-008]

The important negative evidence is not merely zero cash. The record never reached explicit agreed paid scope. There were 56 hypotheses and 30 market-facing work records, but only one recorded terminal buyer decision in that cohort: the puzzle rejection. Two small submissions remained pending/unpaid; two separate implementations encountered platform-verifier failures. Inaccessible channels leave other decisions unknown. [E-FUNNEL-002] [E-FUNNEL-003] [E-FUNNEL-004] [E-RUNTIME-002] [E-RUNTIME-003] [E-RUNTIME-005] [E-RUNTIME-006] [E-RUNTIME-014]

**Interpretation:** the agent demonstrated technical production and substantial procedural activity, but weak evidence of commercial judgment: selecting buyers, shaping offers, and concentrating effort where a purchase was plausible. This is not a measured causal attribution. Research and monitoring volume are not substitutes for a functioning sales pipeline.

The [final corrections](../run01/final-corrections.md) correctly reject settlement as the proven sole bottleneck. No accepted payable transaction reached settlement. Identity and payment restrictions excluded particular routes, but demand conversion, acceptance, and settlement all remained unvalidated. Working financial access would remove some friction, not establish willingness to pay. [E-FUNNEL-003] [E-FUNNEL-004] [E-RUNTIME-019]

The technical puzzle checks also illustrate the difference between correctness and purchase value: the recorded decline concerned editorial distinctiveness, while the nonauthor critic established technical properties. The original buyer message is not in the public evidence, so the reason remains the experiment's recorded paraphrase. [E-RUNTIME-011] [E-RUNTIME-012] [E-RUNTIME-014]

## There is no defensible success percentage

| Question | Assessment |
| --- | --- |
| Can an agent independently find work and receive money? | Possible in narrow reported cases; some transfers are corroborated, with work attribution less certain. |
| Can it cover modest hosting and inference costs in a suitable niche? | Plausible, but not established by the evidence reviewed here. |
| Can a fresh general-purpose agent reliably discover and operate a profitable business unattended? | The available evidence is unfavorable. |

No reliable 10%, 30%, or other success probability follows. We lack a representative population with comparable constraints, complete costs, consistent success definitions, and sufficient follow-up. Run 01 is one experiment, not 56 independent trials. The external [case-study corpus](../research/case-studies.md) is a convenience sample, not a base-rate study.

The roughly 3% headline in the [who-earns marketplace census][who-earns] is not this experiment's probability of success. The source combines different observables, including completed positive-bounty tasks and decided bids without a payout ledger, some priced at zero. Registered accounts are not a denominator of comparable, serious attempts. Its headline should not be treated as a verified customer-payment rate.

The useful conclusion is: **we lack a calibrated probability, and the evidence is weak enough that profitability should not be the default expectation.** A future experiment can estimate its own channel-specific acquisition and delivery economics; a single successful run would still not establish a general success rate.

## External evidence supports possibility more than profitability

The repository's strongest tiny-payment example is [who-earns][who-earns]: two transfers totaling 0.0348 USDC. The published research reports transfer corroboration, but work/payer attribution remains author-reported and gas/conversion costs are unknown. This assessment did not independently rerun the collection or chain verification. It is evidence of a possible payment path, not a sustainable business. See the [research corrections](../run01/final-corrections.md#research-challenge-corrections).

Two additional primary accounts were read on September 23 to challenge an exclusively negative interpretation. They are supplemental sources, not new entries in the frozen research corpus:

| Source | Claimed result | Why it does not establish autonomous profitability |
| --- | --- | --- |
| [zk0x's 30-day bounty account][bounty-case] | USD 500–800 estimated earnings against about USD 45 inference; a later table gives USD 300–600. | Includes estimated token rewards, no linked payment ledger in the article, 25 hours of human management/review, and humans reviewing submissions and choosing bounties. Financial ranges and merge counts are internally inconsistent. It may describe useful AI-assisted freelancing, but not verified autonomous profit. |
| [Bottleneck Labs' seven-agent business experiment][bottleneck] | Zero external revenue, USD 2,833.35 of API-priced token usage, and USD 359.80 in bank spending. | First-party report with published trace links, not audited accounts. The short window, early safety stops, and permissive authorization limit generalization. It nevertheless challenges the proposition that bank accounts, checkout access, and capital alone create sales. |

In the bounty account, the three named repository merge counts sum to all 59 claimed merges, despite a table reporting seven repositories with merges. The discrepancy and changing revenue ranges warrant caution, not an accusation of fabrication. Its stated human labor also makes it a different autonomy level from the proposed experiment.

Bottleneck Labs reports spam and unsolicited invoices as well as commercial failure. Those actions are harms, not useful strategies to copy. **Removing restrictions can increase spending and harmful activity without increasing sales.** Safeguards against deception, spam, unauthorized billing, and rule evasion should remain.

Neither additional account supplies a base rate. Nor does this bounded search prove that profitable private or unpublished examples do not exist.

## Measure economics, not only whether a payment occurred

A EUR 20/month server is not an insurmountable expense. The harder question is how much research, failed outreach, inference, rework, and supervision are required to obtain a few paying customers.

Run 01 cannot supply a full break-even estimate. Its captured USD 3.74 of Amp credits is not a price for the recorded inference, and helper coverage, subscription allocation, and human labor are incomplete. The 530,626,955 inclusive input tokens already contain 490,765,952 cache-read tokens; those must not be counted twice or equated with fresh reasoning. [E-COST-001] [E-COST-002] [E-COST-003] [E-SCOPE-004] [E-SCOPE-010] [E-RUNTIME-007] [E-RUNTIME-008] [E-RUNTIME-009]

### Illustrative sensitivity, not a forecast or actual budget

Assume EUR 100/month fixed cost for server and allocated subscriptions, EUR 3 incremental acquisition cost per qualified prospect, a EUR 100 selling price, and EUR 20 delivery/payment/rework cost per completed paid sale. For 40 qualified prospects approached through permitted channels:

| Conversion to completed, paid work | Expected sales | Expected operating result |
| --- | --- | --- |
| 5% | 2 | EUR 200 receipts − EUR 40 delivery − EUR 120 acquisition − EUR 100 fixed = **EUR 60 loss** |
| 10% | 4 | EUR 400 receipts − EUR 80 delivery − EUR 120 acquisition − EUR 100 fixed = **EUR 100 surplus** |

These are assumed rates and expected values, not measured conversions or guaranteed sale counts. They exclude owner labor, initial development, and taxes. The cost buckets must be mutually exclusive: subscription-covered inference is not also charged as incremental API usage. The example demonstrates sensitivity to acquisition and paid conversion, not that either rate is attainable.

Maintain two separate scorecards:

1. **Incremental cash result:** receipts minus additional cash spending caused by the experiment.
2. **Fully allocated result:** additionally account for the experiment's share of subscriptions, infrastructure, setup, and human labor, with explicit allocation assumptions and no double counting.

Using an existing subscription is legitimate; calling it unlimited free inference is not. Conversely, pricing all subscription-served tokens at hypothetical API prices does not describe the actual cash bill. Report measured usage, cash charges, allocations, and sensitivity scenarios separately.

## A more informative second round

The central question should be:

> Can the agent independently acquire unrelated paying customers for one repeatable service, with positive operating margin and limited human intervention?

Proposed changes, subject to a separate launch decision:

1. **Preserve autonomous customer acquisition.** No owner-provided buyers, warm introductions, or captive customers in the main result. If tested, label them as separate assisted cases.
2. **Allow lawful owner-backed infrastructure.** Use honestly represented business identity and approved accounts/payment access where permitted. Record setup and intervention as changed starting resources. If identity independence is essential, acknowledge the narrower market rather than disguising human participation.
3. **Extend calendar time without extending continuous reasoning.** A candidate design is three to four weeks of bounded work and a separate fixed collection window. Use scheduled/event-driven checks, not repeated model reasoning about unchanged channels. Longer elapsed time alone is not an intervention expected to create demand.
4. **Remove the strongest-model-for-everything requirement.** Use deterministic checks and cheaper triage where adequate, reserving strong reasoning for consequential decisions and delivery. Measure cost and error effects; cheaper is not automatically better.
5. **Choose a narrow offer after capped discovery.** The agent selects the service using actual demand evidence. Predefine an effort budget and a pivot rule, rather than spending the entire run cycling through unrelated markets. Keep a small, separately logged exploration allowance.
6. **Test the offer before substantial production.** Establish the buyer problem, price, scope, decision maker, acceptance criteria, and usable payment route. Allow capped samples that resolve a specific uncertainty; do not make bespoke unpaid production the default.
7. **Sell measurable customer value.** Authorized data reconciliation, a reproducible software defect, or a bounded compatibility repair are candidate task shapes, not proven winning sectors. Access to a language model is not itself a reason for the customer to buy.
8. **Retain hard action safeguards.** No unsolicited invoices, harvested-email campaigns, fabricated experience, or evasion of platform rules. Human permissions and intervention limits must be explicit before launch.

Any advantage must come from reliable workflow completion, specialized knowledge, accumulated trust, or repeat business—not merely access to the same model the buyer could use.

## Criticism of the existing next-run designs

The [proposed tests](plan.md) improve observability, safety, and evidence quality. They do not automatically improve commercial prospects:

- EXP-2's explicit accept/decline count can increase through additional rejections without improving paid conversion or margin.
- EXP-3 can show that a checklist changes decisions without showing that those changes increase customer value or earnings.
- Dividing a small opportunity pool across comparison lanes can produce an underpowered result.
- More orchestration, reviews, and reporting can consume the budget without testing demand.

These are limitations of proxy outcomes, not reasons to discard the controls. Use them selectively to protect a focused commercial test; do not turn all five designs into parallel prerequisites. Preserve essential auditability without making documentation volume a success metric.

## Decision criteria

A first arm's-length payment would establish a milestone, not a business. Stronger evidence would include two independently acquired, unrelated customers, evidence of repeat demand, and positive fully allocated operating results across subsequent periods. These are proposed continuation criteria, not statistical proof or a universal minimum sample size.

Before launch, fix the maximum loss, calendar and effort budgets, permitted actions, human-intervention allowance, and collection window. Stop or reassess when the acquisition budget is exhausted without qualified demand, no lawful usable settlement route remains, or observed delivery/acquisition costs invalidate the margin assumption. Do not widen the cohort or move deadlines merely to improve the reported result.

Initial losses must remain visible. A profitable final week does not erase setup and acquisition losses, although improving recurring economics may justify a separately budgeted continuation. Require evidence before granting that continuation.

**Bottom line:** fund another round only as a bounded test whose information is worth its possible total loss. For dependable income rather than research, the evidence does not justify another open-ended autonomous earning run. For learning, a narrower, cost-accounted test that still requires the agent to find its own customers is defensible.

## Sources and evidence boundary

Historical evidence IDs above resolve in the existing [evidence register](../run01/evidence-register.md). They refer to the frozen run-01 record, not a new audit. The [methodology](../methodology.md), [final corrections](../run01/final-corrections.md), [funnel](../run01/funnel-metrics.md), [case studies](../research/case-studies.md), and [sector framework](sector-selection-framework.md) supply the main context.

External links below were read for this assessment on September 23, 2026. They are mutable primary publications; no archival snapshot or independent financial audit is claimed. No private responses, receiving addresses, account identifiers, credential material, or private source paths are included here.

[who-earns]: https://github.com/AsherKasper/who-earns-in-the-agent-economy/blob/main/README.md
[bounty-case]: https://dev.to/zeroknowledge0x/the-agent-economy-how-ai-agents-are-earning-real-money-in-open-source-and-why-most-fail-9j2
[bottleneck]: https://www.bottlenecklabs.com/blog/benchmarking-7-autonomous-businesses
