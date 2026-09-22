# Cross-review: synthesis followed by adversarial challenge

This file deliberately preserves two rounds. Round 1 is the initial synthesis. Round 2 is the adversarial challenge that replaced it within the workflow. A subsequent [final evidence adjudication](../final-corrections.md) corrects errors in both rounds; the challenge is not the last authority. A Round 1 claim marked weakened or overturned is not a surviving consensus.

## Round 1 — synthesis

### Initial agreements

1. **USD 0 ledger position.** All lanes found no evidenced acceptance and no payer-linked payment at cutoff; accepted paid gross and ledger net receipts were USD 0. The synthesis already cautioned that this was not a fresh all-wallet audit. [E-FUNNEL-001] [E-FUNNEL-005] [E-FUNNEL-006]
2. **Lifecycle failures.** All lanes found 34 nonzero exits among 218, including attempts 176-205 consecutively, with 5h33m45s from first failure to the next successful exit. [E-RUNTIME-015] [E-RUNTIME-017]
3. **Mission growth.** The synthesis described four change points across 29, 41, 67, and 87 lines and interpreted v2.1 as overriding a deferred-wait reading. [E-MISSION-001] [E-MISSION-003] [E-MISSION-005] [E-MISSION-007]
4. **Buyer decision.** It described the puzzle decline as the only human buyer decision and categorized it as editorial rather than technical. [E-RUNTIME-014] [E-DROP-003]
5. **Heterogeneous queue.** It held that the 39 response entries were not 39 live paid jobs. [E-FUNNEL-004] [E-FUNNEL-005]
6. **Unmeasurable strategic dimensions.** Two lanes agreed that sector selection, search breadth/depth, opportunity selection, and marginal orb value could not be measured from this snapshot. [E-SCOPE-004] [E-FUNNEL-002] [E-FUNNEL-003]
7. **Resource totals.** It accepted 530,626,955 inclusive input and 1,561,923 output tokens and called them unpriced. [E-SCOPE-004] [E-SCOPE-010]

The synthesis explicitly noted shared-source common-mode risk. It also resolved lane disagreements about the buyer-message timestamp, wallet-row counts, maintenance versus human-help time, pre-effort demand coding, provider-read versus reconciliation timestamps, supplemental hash verification, and record-level friction counts. Some of those resolutions were themselves later challenged.

### Initial ranked counterfactuals

The first round ranked nine proposals: payout-route research, two forms of pre-send puzzle review, two versions of continued discovery during v2 deferral, two forms of stopping the second verifier probe, an earlier crash-loop breaker, and a longer diagnostic response window. It treated all as mechanisms without probabilities, but still carried later-outcome influence in several rationales.

### Initial causal conclusion

The synthesis ended with a strong claim that acceptance was reachable while settlement was not, and that the structurally missing resource was a person able to stand behind an identity where money moves. The challenge did not uphold that causal conclusion.

## Round 2 — adversarial challenge (workflow synthesis, corrected afterward)

### Upheld

- **Ledger result:** no readable acceptance or payer-linked payment; gross/net USD 0, with the all-wallet and failed-channel caveats retained. [E-FUNNEL-001] [E-FUNNEL-005] [E-FUNNEL-006]
- **Lifecycle count:** 184 code-0 and 34 code-1 exits; attempts 176-205 consecutive; 5h33m45s to the next successful exit. Breadcrumb-to-attempt mapping remains temporal inference. [E-RUNTIME-015] [E-RUNTIME-016] [E-RUNTIME-017]
- **Heterogeneous pending register:** 39 entries across applications, pending reviews, eligibility/route questions, passive offers, local closures, one intake closure, and one decline. [E-FUNNEL-004]
- **Strategic non-measurability:** sector quality, search breadth/depth, opportunity quality, and marginal orb value cannot be measured from the permitted corpus. [E-SCOPE-004] [E-FUNNEL-002] [E-FUNNEL-003]
- **Required evidence artifacts:** the sanitized analysis contained a private evidence register, timeline, and funnel measurement, and every evidence ID used by the first synthesis resolved privately.

### Weakened

- **Mission history:** four states survive, but only three textual transitions are measurable. Reinvestment is an earlier intervention without a predecessor file. [E-MISSION-001] [E-MISSION-002] [E-MISSION-003] [E-MISSION-005] [E-MISSION-007]
- **Buyer-decision exclusivity:** the puzzle decline is the only terminal accept-or-decline decision among the 30 tracked work records; inaccessible channels prevent an experiment-wide claim. [E-FUNNEL-002] [E-RUNTIME-014]
- **Resource pricing:** token totals survive, but “unpriced” does not. Root and author have reported Amp credit figures; critic, helper, subscription allocation, and provider-equivalent totals are missing. Usage is partially priced and not fully costed. [E-SCOPE-004] [E-SCOPE-010]
- **Payout-route explorer:** the known-at-time research choice survives, but the promised commercial steering effect does not. No compatible live buyer or prevented proposal was established. [E-RUNTIME-019] [E-MISSION-003]
- **Puzzle review:** a pre-send checklist for criteria already present in the brief survives; a claim that a reviewer could predict the later editorial reason does not. [E-RUNTIME-011] [E-RUNTIME-012]
- **Second verifier probe:** stopping was possible after two failures, but the second route was distinct and inexpensive. This survives only as a low-stake resource-conservation choice. [E-RUNTIME-002] [E-RUNTIME-003]
- **Research/tooling grades:** first-party documentation can establish documented contracts but not measured multi-day reliability; unavailable original research URLs cannot be silently replaced by similarly themed repositories.

### Overturned

- A continuous discovery lane before v2.1 was not retained as a ranked counterfactual: v2 explicitly allowed screening to stop, the register identified no concrete untested direction, and the proposed benefit depended on later v2.1 results. [E-MISSION-005] [E-RUNTIME-012]
- The parallel “challenge before deferral” proposal was dropped for the same hindsight problem. [E-FUNNEL-003] [E-RUNTIME-013]
- Installing a crash-loop breaker during earlier maintenance was dropped: only isolated failures were known then; the thirty-attempt pattern arrived later. [E-RUNTIME-015] [E-MISSION-006]
- Extending the diagnostic response window was dropped: it left insufficient evidenced production time and was selected after observing nonresponse. [E-RUNTIME-013]
- The claim that settlement was established as the binding constraint was rejected. No work reached acceptance, willingness to pay remained unestablished, and no end-to-end settlement rehearsal occurred.

### Unsupported claims removed from the final synthesis

- “Work acceptance was reachable and checkable, settlement never was.” Submission reachability is not acceptance reachability.
- “The structurally missing resource was a person who could stand behind an identity.” Identity was recurrent, but demand conversion, acceptance, and settlement all remained unvalidated.
- “A payout-rail explorer would have redirected eight later proposals.” No known-at-time mapping established that result.
- “All three final-state samples contain zero contradictions.” The lane samples use different atomization and are not directly comparable even after one disputed contradiction was removed.

### Final ranked counterfactuals

1. **Payout-route explorer, weakened.** Route/settlement uncertainty was already known before explorer assignment; a research-only screen was available. No revenue effect is claimed. [E-RUNTIME-019] [E-MISSION-003]
2. **Pre-send criterion coverage, upheld after narrowing.** The original brief contained experience criteria that technical checks did not assess. A nonauthor reviewer could return PASS, FAIL, or UNMEASURABLE without claiming to predict taste. [E-RUNTIME-011] [E-RUNTIME-012]
3. **Stop after repeated verifier-shaped failure, weakened.** A conservative stop was available after two failures, but the second route was distinct and cost under two minutes. [E-RUNTIME-002] [E-RUNTIME-003]

### Final future-experiment designs

The challenge proposed five designs, all explicitly requiring separate future authorization and human-verified resources:

1. Settlement qualification before production, with four settlement states, a falsification test, and a three-route/20%-window stop rule.
2. Agreed price and scope before production, compared against production on advertised demand, counting explicit human decisions only.
3. Criterion coverage before submission, with a domain-appropriate human reviewer for subjective criteria.
4. Platform-verifier health gate, using public history and one minimal safe probe.
5. Non-earning unattended-observability test with a consecutive-failure breaker, notification acknowledgement, and full-window log retention.

These are designs, not launches. None is assigned a probability of commercial success.

### Could not verify

- The original private buyer message behind the recorded decline.
- Outcomes or replies outside the readable ledger or after channel loss.
- Fresh pause-time balances across all receiving addresses.
- Digest-only captures, excluded binaries, and private contact material.
- Early CLI error causes before retained metadata begins.
- Authorization of the disputed service stop/start.
- Served model/usage from lane self-description alone; the published provenance instead uses the reconciled runtime tiers.
- Population-wide research rates or whether unavailable research URLs were renamed or superseded.
- Any commercial outcome of a counterfactual.

## Final cross-review conclusion

The central factual result survives: no accepted paid work and no payer-linked payment in the readable cutoff ledger; USD 0 accepted paid gross and ledger net receipts. The run did real technical work, but never established an agreed payable transaction. The overnight failure sequence is verified as a lifecycle pattern, not fully diagnosed. Identity and settlement were recurring route constraints, but neither is proven to be the single cause. The remaining evidence supports bounded process tests—not market exhaustion, a base rate, or a prediction that more model capability would create demand.

## Final local adjudication after both rounds

The historical judgments above are retained as attributed positions. They require these corrections before use:

- All three captured credit figures exist and total USD 3.74; this does not price subscription inference. [E-COST-001] [E-COST-002] [E-COST-003]
- The research-source 404 objections used paths introduced by the challenger. Correct cited repositories were present in its prompt and remain accessible; no source-continuity gap follows.
- The four supplemental pins were independently verified; Amp's baseline non-reading remains a per-lane coverage gap. All three actual runtime provenance checks passed with the stated evidence tiers and effort limits.
- The financial brief is 86 lines, not 87. The disputed historical restart was September 20, distinct from later pause follow-up. [E-FUNNEL-005] [E-MISSION-006]
- The first synthesis omitted Fable's editorial-fit-before-build counterfactual without explaining why. All ten originals remain in the complete lane files.
- Bounded discovery before deferral and a prospective failure breaker were feasible process options; known-at-time priority and commercial benefit remain unresolved. Final QA disputes their blanket rejection while retaining the challenge's valid hindsight criticism.

See [final corrections](../final-corrections.md) for evidence and precise scope. The challenge's ranked list is therefore a recorded judgment, not an exhaustive final ranking.
