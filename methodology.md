# Methodology

## Evidence boundary

The review used one frozen, redacted analysis snapshot plus four separately pinned supplemental records. The source collection was bounded and read-only. The public repository contains none of those files: it contains only derived prose, stable evidence IDs, sanitized source aliases, sha256 digests, and locators. The snapshot manifest records 627 rows and the collection record describes the capture window, readable projections, deliberate exclusions, and coverage limits. [E-SCOPE-001] [E-SCOPE-004]

The raw source collection, credential quarantine, redaction salt, pseudonym maps, private contact material, and excluded binary/archive artifacts were not opened during publication. Large private capture subtrees were available only as digests. Readable projections were used where the original database or compressed log container was excluded. [E-SCOPE-003] [E-SCOPE-005] [E-SCOPE-006]

## From collection to analysis snapshot

Collection preserved timestamps and source digests, then produced text projections for events, selected CLI metadata, thread timelines, journals, the work dashboard, the hypothesis register, and the pending-response register. Redaction replaced sensitive identifiers before review. The public evidence register deliberately removes source paths and uses stable aliases instead; the private register retains the alias-to-path relationship.

The pause is the fixed observation boundary. The run covered 96h15m of a planned 120h window. Later process-presence findings are safety follow-up, not proof of later earning activity and not a reason to move the cutoff. [E-SCOPE-008] [E-SCOPE-009] [E-RUNTIME-020]

## Independent review lanes

Three named lanes received the same frozen evidence and rubric but were required to work independently:

- `fable-claude`: Claude Code, configured for `claude-fable-5-1`, maximum effort. Runtime evidence tier: `harness-usage`; the attempt usage stream named the configured model. The observed harness session identifier is retained privately. Claude Code does not independently attest the served model.
- `astra-codex`: Codex, configured for `gpt-6-astra`, maximum effort. Runtime evidence tier: `harness-usage`; the attempt usage stream named the configured model. The observed harness session identifier is retained privately. Codex does not independently attest the served model.
- `astra-amp`: Amp, configured for `gpt-6-astra`, maximum effort. Runtime evidence tier: `thread-export`; every exported message reported `usage.model=gpt-6-astra`. Only the issuer class `openai:chatgpt-codex` is published; the subscription identifier is not.

The lane's self-description was never treated as verification. The reconciled runtime record supplied the published evidence tier. A common evidence set creates common-mode risk: lane agreement is corroboration of a shared snapshot, not independent proof of the outside world.

## Synthesis and challenge

The first synthesis compared the three finished lane outputs. A separate adversarial challenge then re-opened selected evidence and classified synthesis claims as upheld, weakened, overturned, or unverifiable. Both rounds are published separately in `run01/reviews/cross-review.md`. Final local evidence QA then corrected mistakes in both rounds; `run01/final-corrections.md` is the final adjudication. A challenged claim is not silently erased, and the challenge is not assumed infallible.

## Research method

The research lanes first read a previously validated corpus and its correction history, then performed bounded verification and gap-filling against primary sources. Grades are preserved exactly as returned: `audited`, `independent`, `self-report`, `fiction`, or `unverified`. “Audited” in the tooling report is a disclosed documentation rubric—corroboration across first-party pages or installed code—not an empirical multi-day reliability test.

The earning-attempt corpus is selected from English-language, indexed, voluntarily published material found by targeted queries. Publication bias, indexing bias, inaccessible material, and unreported failures are unavoidable. It cannot support a base rate.

## Claim and locator rules

Every experiment claim in the public files carries at least one stable evidence ID. The sanitized register resolves each ID to a source alias, sha256, and locator. Public files never reproduce private message bodies, raw telemetry rows, raw log lines, receiving addresses, account identifiers, or private filenames.

## Billing coverage

The three exported historical threads contain 530,626,955 inclusive input and 1,561,923 output tokens. Cache-read input of 490,765,952 is already included. Linked subscription inference is distinct from captured Amp credit usage: root USD 1.71, author USD 1.13, critic USD 0.90, total USD 3.74 consumed credits. These counters are not new purchases, invoices or a price for the recorded reasoning tokens. Complete helper coverage and subscription allocation remain unknown. The VPS costs EUR 20/month. [E-SCOPE-004] [E-SCOPE-010] [E-COST-001] [E-COST-002] [E-COST-003]

## Review coverage and final quality assurance

Three harness lanes represent two model families. Maximum effort was configured, not independently attested. Fable read but could not hash four supplements; Codex had successful hash-command action metadata but a failed full native trace capture; Amp did not open the supplements because it could not verify them. The deterministic freeze and final local recheck verified their pins. Amp's original gap remains disclosed; no addendum is claimed. See the complete lane blockers and final corrections.

Every original dimension finding, counterfactual, counterargument, process assessment, intent assessment, summary and blocked state is retained in the complete lane renderings. Private identifiers and paths are substituted; original factual mistakes remain visibly attributed to the reviewer and are corrected separately. The independent trace audit is limited to captured action metadata, not every possible filesystem operation.
