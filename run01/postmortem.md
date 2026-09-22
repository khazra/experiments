# Earn50 run 01 postmortem

## Executive finding

At the 2026-09-22 15:14:39 UTC cutoff, after 96h15m of a planned 120h window, the readable ledger contained no accepted paid-work record and no payment record linking a payer to work. Accepted paid gross and ledger net receipts before infrastructure and model allocation were USD 0. The payments register was empty. Six wallet rows contained old zero observations and two balances were unknown; no wallet was re-read at pause. This is a ledger result, not proof that every possible receiving account and inaccessible channel was current. [E-FUNNEL-001] [E-FUNNEL-005] [E-FUNNEL-006] [E-RUNTIME-020]

## What happened

The run registered 56 heterogeneous hypotheses and tracked 30 market-facing work records. Their final snapshot states were 12 withdrawn, 1 declined, 2 platform errors, 5 listed, 8 proposed, and 2 submitted-awaiting-review. Six applications and two delivered submissions were still pending or unpaid at the last successful checks. The 39-entry pending register also contained support questions, local closures, one closed intake, and the buyer decline; it was not a pipeline of 39 paid jobs. [E-FUNNEL-002] [E-FUNNEL-003] [E-FUNNEL-004] [E-FUNNEL-006]

Three items reached a buyer or platform review surface: two pending small submissions and one puzzle. Two other implementations encountered platform-verifier failures and never reached accepted delivery. The puzzle was technically checked, delivered once after authentication reconciliation, and later declined. The retained record describes the reason as suitable difficulty but insufficient editorial distinctiveness; the original private message body was not retained, so this is the run's paraphrase. [E-RUNTIME-002] [E-RUNTIME-003] [E-RUNTIME-005] [E-RUNTIME-006] [E-RUNTIME-011] [E-RUNTIME-014] [E-DROP-003] [E-DROP-014] [E-DROP-015]

The strongest execution evidence was technical: local tests, uniqueness checking, payload validation, a logical replay, and a post-submission nonauthor critic that reproduced one solution and found no correctness, payload, or prose defect. The review did not establish novice discoverability or editorial value before submission. [E-RUNTIME-011] [E-RUNTIME-012]

## Demand, acceptance, and settlement

The record never reached explicit agreed paid scope. Public listings and advertised rewards were common; direct buyer engagement was rare. The only evidenced terminal accept-or-decline decision among the 30 tracked work records was the puzzle decline. Inaccessible final channels prevent claiming it was the only human decision anywhere. [E-FUNNEL-002] [E-RUNTIME-014]

Identity, AI-eligibility, KYC, payout-route, and settlement-window restrictions repeatedly excluded or left routes unresolved. The challenge rejected the stronger causal claim that settlement was the single binding constraint: willingness to pay, acceptance, and settlement all remained unvalidated. The evidence supports multiple unresolved gates, not one proven cause of USD 0. [E-FUNNEL-003] [E-FUNNEL-004] [E-RUNTIME-019]

## Time and external waiting

Time to cash is unobserved and right-censored beyond the pause. The puzzle's delivery-to-decision interval was 22h56m42s. Two pending submissions had waited about 94h42m and 87h28m at pause; the six applications had waited roughly 86-95 hours. Concurrent waits are not summed into “lost time,” and grouped reconciliation timestamps are not treated as provider observation timestamps. [E-RUNTIME-011] [E-RUNTIME-014] [E-FUNNEL-004] [E-FUNNEL-006]

Stopping early leaves 23h44m51s unobserved. Nothing in the snapshot prices that interval or proves the 120-hour outcome would have been identical. Mailbox authentication and two thread-access failures also leave some final replies unknown. [E-SCOPE-004] [E-FUNNEL-004] [E-RUNTIME-020]

## Reliability

The lifecycle projection contains 218 root attempt exits: 184 code 0 and 34 code 1. Attempts 176-205 were thirty consecutive failures. The interval from the first of those failures to attempt 206's successful exit was 5h33m45s. Retained CLI metadata contains fatal breadcrumbs and one initialization error, but lacks attempt IDs and full payloads, so a single cause cannot be assigned to all thirty failures. [E-RUNTIME-015] [E-RUNTIME-016] [E-RUNTIME-017]

The main mailbox later returned an authentication failure, while two other response channels returned access errors. The puzzle send recovered safely after an expired authentication challenge. Runtime failures, platform-verifier failures, and external buyer delay are kept as distinct classes. [E-FUNNEL-004] [E-RUNTIME-011] [E-RUNTIME-018]

## Policy changes

Four mission states are preserved at 29, 41, 67, and 87 lines, but only three file transitions are measurable. The earlier reinvestment steering is a separate intervention whose predecessor file is absent. The later policies added bounded discovery, route-to-payment checks, concentration, demonstrations, criticism, and finally an explicit rule separating buyer waiting from discovery suspension. Temporal behavior changed after each intervention, but the review does not attribute the USD 0 result causally to the wording. [E-MISSION-001] [E-MISSION-002] [E-MISSION-003] [E-MISSION-004] [E-MISSION-005] [E-MISSION-006] [E-MISSION-007] [E-MISSION-008]

## Resource use and reporting integrity

The three exported threads record 530,626,955 inclusive input tokens and 1,561,923 output tokens. These totals cover only three projections, already include cache reads and creation, and do not establish total provider cost. The 490,765,952 cache-read tokens are already included. Separate usage summaries report USD 1.71 root, USD 1.13 author and USD 0.90 critic: USD 3.74 consumed Amp credits. These are not invoices, new cash purchases or a price for those reasoning tokens. Helper coverage and subscription allocation remain incomplete; the VPS is EUR 20/month. [E-COST-001] [E-COST-002] [E-COST-003] [E-SCOPE-004] [E-SCOPE-010] [E-RUNTIME-007] [E-RUNTIME-008] [E-RUNTIME-009]

The lanes agreed that final financial reporting generally kept proposals, delivery, acceptance, and payment separate. Their samples used different atomicity rules and are not combinable into one accuracy percentage. Stale wallet observations and failed final channels are observability limitations, not evidence of a contradictory payment claim. [E-FUNNEL-001] [E-FUNNEL-005] [E-FUNNEL-006]

## Lane provenance

- Fable lane: requested Claude Code with `claude-fable-5-1`, maximum effort; reconciled actual harness `claude`, model `claude-fable-5-1`; evidence tier `harness-usage`. The configured CLI model and observed harness session were reconciled, and the usage stream named the model. Claude Code does not independently attest the served model.
- Codex lane: requested and reconciled Codex with `gpt-6-astra`, maximum effort; evidence tier `harness-usage`. The configured CLI model and observed harness session were reconciled, and the usage stream named the model. Codex does not independently attest the served model.
- Amp lane: requested `openai/gpt-6-astra`, reconciled as `gpt-6-astra`, maximum effort; evidence tier `thread-export`. Per-message export data recorded the model label; this is not independent physical attestation. Only issuer class `openai:chatgpt-codex` is public.

All three runtime identities were reconciled. Maximum effort was configured, not independently attested. The Amp baseline did not open four supplemental files; that coverage gap remains. A lane's own identity statement was never used as verification. Three harness lanes represent two model families.

## What the lanes concluded and where they differed

All lanes agreed on the USD 0 ledger position, no evidenced acceptance/payment, the overnight failure sequence, heterogeneous pending register, and incomplete cost coverage. They disagreed on demand coding, how to count friction records, which timestamps were provider observations, and how aggressively to interpret mid-run policy effects. The challenge upheld the central ledger and lifecycle claims, narrowed Fourfold exclusivity to the 30 tracked records, corrected “four measurable transitions” to three transitions plus one earlier intervention, but its credit-cost correction was itself incomplete. Final QA recovered all three credit counters and kept them separate from inference-token pricing.

The challenge retained three bounded process choices: early settlement-route screening, pre-send criterion coverage, and an optional stop after repeated verifier failures. It rejected pre-deferral discovery and an earlier crash breaker on hindsight grounds. Final QA agrees that later discoveries cannot justify earlier choices, but disputes treating the entire earlier process options as unavailable: short read-only screening and prospective failure controls were feasible, with unknown commercial benefit. The full disagreement and all ten original counterfactuals remain visible in the reviews; none carries a success probability. [E-FUNNEL-003] [E-MISSION-005] [E-RUNTIME-015]

## What would be done differently

Future work is design-only. It should first qualify settlement states without counting an operator-funded rehearsal as revenue; qualify price, scope, decision maker and payout route before substantial production, while allowing capped informative demonstrations; obtain independent criterion-by-criterion review for subjective acceptance criteria; gate work on platform-verifier health; and test unattended failure notification in a non-earning reliability exercise. Each design has a falsification test and a stop rule in `next-run/plan.md`.

## Coverage limitations

- The ledger read USD 0 at pause without a wallet re-read.
- Final mailbox and two thread states were inaccessible; some replies are unknown.
- The first roughly two days of CLI diagnostic text rotated away.
- Only three exported threads contribute measured token totals; nested helpers and complete billing are unmeasured.
- Large private capture subtrees and excluded binaries were digest-only.
- Unique opportunities, normalized funnel transitions, sector conversion, search breadth/depth, and marginal orb value are not measurable from this corpus.
- The research set is a convenience sample and cannot yield a base rate.

## Caveats

Agreement among lanes is not proof because all lanes shared the same frozen evidence and rubric. The original buyer message behind the recorded decline is unavailable. No post-pause outcome is used to rewrite the cutoff. Nothing in this postmortem proves the opportunity space was exhausted, identifies a single binding cause, predicts that another model would create demand, or authorizes a new experiment.

## Operator intent and discovery

The initial objective was at least USD 50 of accepted-and-paid work within five days, later broadened to maximizing earnings inside the same fixed deadline. The reconstructed requests are intent evidence, not proof of runtime adoption. The final financial brief was 9,528 bytes and 86 lines. [E-SCOPE-004] [E-SCOPE-007] [E-FUNNEL-005]

The operator's principle remains: **“having no actionable opportunity in its existing register does not establish that there are no worthwhile, unexplored approaches.”** A current register can justify a bounded pause in one route without proving market exhaustion. Future comparisons should use fixed cohorts and effort budgets while reserving bounded exploration outside them. [E-SCOPE-007]

## Research and next design

The research covers agent and human attempts across software products, services, bounties, editorial work and physical retail. Most monetary claims remain self-reports. The Penniless Agent's merged work is artifact-corroborated but historical nonpayment is author-reported; a separate tiny-token case corroborates transfers without establishing arm's-length customer attribution. Existing accounts, skill, audiences, capital and human identity differ substantially between examples. The convenience sample cannot estimate a success rate or rank whole sectors. See [case studies](../research/case-studies.md).

Human-verifiable resources may widen a future route set, but working identity and payment rails do not establish demand. A useful next design would cap sector research, test an explicit customer problem and price, retain ongoing alternatives, and separate the work window from the collection window. Sector depth and buyer relationships are hypotheses worth testing, not conclusions proved by this run. See the [sector framework](../next-run/sector-selection-framework.md) and [proposed tests](../next-run/plan.md).

Native subscription CLIs demonstrably supported the required reviews. A tailored Smithers pack is a reasonable proposed reuse of the existing durable controller; a minimal controller, Temporal or LangGraph can also schedule native harnesses with different implementation and operating burdens. No comparative build-cost or multi-day reliability benchmark establishes a cheapest or best option. See [tooling comparison](../research/tooling-comparison.md).

## Final adjudication

The challenge itself introduced two wrong research URLs and missed an existing credit summary. Those errors are corrected in [final evidence corrections](final-corrections.md), alongside exact dates, provenance limits, original reviewer errors and unresolved counterfactual judgments. Full individual reviews preserve the reviewers' original positions rather than silently replacing them with consensus.
