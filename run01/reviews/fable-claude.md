# Complete independent review: fable-claude

This is the complete lane output, with private identifiers and source paths replaced by aliases. Original findings, uncertainty, blockers and counterfactual judgments are retained; they are not final adjudicated facts. Consult [final corrections](../final-corrections.md) and [cross-review](cross-review.md) before relying on disputed statements.

## Reconciled runtime evidence

**Lane id.** fable-claude

**Requested harness.** claude-code

**Requested model.** claude-fable-5-1

**Requested effort.** max

**Actual harness.** claude

**Actual model.** claude-fable-5-1

**Actual effort.** max

**Usage issuer class.** Not recorded.

**Evidence tier.** harness-usage

**Evidence source.** smithers node review-fable-claude attempt 1: tokenUsage.models=["claude-fable-5-1"]

**Reported model.** claude-fable-5-1 as self-identified in the system prompt; not independently attestable from inside the lane

**Reported matches runtime.** false

**Verification method.** Runtime record only: `smithers node <reviewNode> --run-id <run> --format json` yields the adapter's engine, model, session id and the models seen in the attempt's usage stream. The Claude Code CLI does not let a caller attest the served model independently, so the strongest tier available here is the configured CLI model plus the observed session id, escalating to harness-usage when the attempt's usage stream names the model. The lane's own claim about its identity is never the source of verification.

**Verified.** true

**Blockers.** None recorded.

The model labels above are captured runtime/export records, not independent physical attestation of the model or effort served. Maximum effort was configured. Three harness lanes represent two model families.

## Original reported provenance

**Lane id.** fable-claude

**Requested harness.** claude-code

**Requested model.** claude-fable-5-1

**Requested effort.** max

**Actual harness.** claude-code (Claude Code CLI tool surface: Read, Grep, Glob; no shell tool exposed to this lane)

**Actual model.** claude-fable-5-1 as self-identified in the system prompt; not independently attestable from inside the lane

**Actual effort.** system prompt injected reasoning_effort 80, not a literal 'max' setting; mapping between the two is not observable here

**Thread id.** [private session identifier] (session directory id observed in the harness tool-result storage path)

**Harness run id.** Not recorded.

**Usage.** not visible to the lane; only a remaining-context counter appeared in system messages (about 15.00M tokens at start, about 14.64M at the last observation before writing this output)

**Usage issuer class.** Not recorded.

**Evidence tier.** reported

**Evidence source.** system prompt self-identification plus session id inferred from the tool-result persistence path; no runtime usage stream visible

**Reported model.** claude-fable-5-1

**Reported matches runtime.** false

**Verification method.** none available in-lane; the deterministic stage must reconcile this record against the smithers node record (engine, model, session id, usage models)

**Verified.** false

**Blockers.** - No shell or hashing tool was available, so the four supplemental files (SOURCE-007, SOURCE-008, SOURCE-009, SOURCE-010) were read without recomputing their sha256; their contents matched the register descriptions E-SCOPE-007 to E-SCOPE-010, and the hashes in the register equal the hashes in the task brief, but that is not an independent hash check.

- Requested effort was 'max' while the injected reasoning_effort value observed in the system prompt was 80; the lane cannot determine whether these denote the same setting.

- reportedMatchesRuntime is set false only because no runtime record was visible to compare against; it is not a claim of mismatch.

## Dimension findings

### 1. paid-gross-net-acceptance

**Measurement**

Rows per claimed acceptance or payment at the 2026-09-22T15:14:39Z cutoff. (1) Fourfold puzzle, quoted USD 50 (dashboard /work/2, amount_basis quoted): buyer explicitly declined at 2026-09-21T14:45:44Z (events#row-478); acceptance none, paid gross none. (2) BountyBook state machine, quoted 5 USDC (/work/18): verifier rejected at 15:16:39Z and 15:20:07Z on 2026-09-18 (events#row-1526, events#row-1084); payout_status none, payout hash null; no acceptance, no payment. (3) BountyBook Bloom filter, quoted 12 USDC (/work/19): verifier internal error at 15:45:36Z (events#row-744); no acceptance, no payment. (4) CrawlProof feedback, quoted USD 2 (/work/20): HTTP 201 pending at 2026-09-18T16:32:36Z (events#row-1472); still pending/unpaid at the final successful check (events#row-89). (5) Resource backlink, quoted USD 0.50 (/work/16): HTTP 201 pending/unpaid at 2026-09-18T23:46:47Z (events#row-1419); still pending/unpaid at events#row-89. (6) Six uGig applications quoted USD 0.25 to USD 1000 (/work/15, /work/21 to /work/25): all pending, none accepted (events#row-89). (7) Five listings and eight proposals or inquiries (/work/0, /work/1, /work/3 to /work/14, /work/17, /work/26 to /work/29): no buyer acceptance recorded on any; the 10 USDC distribution proposal expired locally unaccepted (events#row-1369, /work/0). Payment records: dashboard /payments is an empty array; no event row records a payment, fee or refund. Funds: /funds shows USD 0 checked 2026-09-18T22:13:18Z and BTC 0 checked 2026-09-19T04:21:37Z. Wallets: /wallets has 8 rows, 5 observed at 0 with checked_at between 2026-09-18T22:34:39Z and 2026-09-19T06:54:33Z, 3 with balance_status unknown and null checked_at. Fees and refunds: no transactions recorded; dashboard cost row transaction-fees-observed has verification_state unknown and the BRIEF line 23 says historical fees unverified, not assumed zero. Net receipts = evidenced paid gross USD 0 minus evidenced fees USD 0 minus evidenced refunds USD 0 = USD 0, as a ledger position (BRIEF lines 22 to 26; events#row-89 at 2026-09-22T15:12:25Z). Wallets were not refreshed at pause (BRIEF line 18 heading; pause-verification /elapsed_note), so USD 0 is not a fresh all-wallet balance or payer-provenance audit.

**Opinion**

The USD 0 figure is as solid as a ledger position can be: every priced item has a distinct non-acceptance record and the payments array is empty. Commercially, the only item that ever reached a human buyer decision was Fourfold, and that decision was negative; everything else was either never decided by anyone (uGig queue, self-listed offers, silent email proposals) or failed inside a platform verifier. I do not read the unrefreshed wallets as hiding revenue: any incoming transfer would still lack payer and work provenance and would not count under the rubric.

**Locators**

- {"evidenceId": "E-FUNNEL-001", "path": "SOURCE-025", "locator": "JSON pointers /source_as_of_utc, /funds, /payments, /wallets, /costs/5"}

- {"evidenceId": "E-FUNNEL-005", "path": "SOURCE-028", "locator": "lines 18-33"}

- {"evidenceId": "E-FUNNEL-006", "path": "SOURCE-012", "locator": "events#row-89"}

- {"evidenceId": "E-RUNTIME-014", "path": "SOURCE-012", "locator": "events#row-478, events#row-1369"}

- {"evidenceId": "E-RUNTIME-002", "path": "SOURCE-012", "locator": "events#row-1526, events#row-1084"}

- {"evidenceId": "E-RUNTIME-003", "path": "SOURCE-012", "locator": "events#row-744"}

- {"evidenceId": "E-RUNTIME-005", "path": "SOURCE-012", "locator": "events#row-1472"}

- {"evidenceId": "E-RUNTIME-006", "path": "SOURCE-012", "locator": "events#row-1419"}

- {"evidenceId": "E-SCOPE-008", "path": "SOURCE-008", "locator": "JSON pointer /elapsed_note"}

**Confidence**

high

**Counterevidence**

- Three wallet rows (Polygon USDC, Ethereum USDC on WALLET-001, plus stale observations) were never checked; a transfer could exist there, though it would still lack payer-and-work provenance.

- A uGig approval of the USD 2 or USD 0.50 submission after the last successful 15:08:30Z check and before the 15:14:39Z pause would not appear in the ledger; the six-minute window makes this unlikely but not impossible.

- The mailbox returned HTTP 401 from 2026-09-22T05:22Z, so a buyer acceptance by email after 2026-09-22T00:08:24Z would be invisible to the snapshot.

### 2. time-to-cash-and-early-stop

**Measurement**

Fixed timestamps: launch 2026-09-18T14:59:32Z (events#row-398, events#row-889), pause 2026-09-22T15:14:39Z (events#row-392), immutable deadline 2026-09-23T14:59:30Z (SOURCE-004 line 11). Elapsed at pause 96h15m07s; nominal remaining 23h44m51s. Time-to-cash: no payment event exists, so it is unobserved and right-censored beyond the pause. Exact intervals: Fourfold delivered 2026-09-20T15:49:02Z to explicit decline 2026-09-21T14:45:44Z = 22h56m42s (exact; invitation 15:19:45Z to decline = 23h25m59s); BountyBook state machine submitted 15:15:39Z to second verifier failure 15:20:07Z = 4m28s (exact, platform error); Bloom filter submitted 15:45:15Z to verifier error 15:45:36Z = 21s (exact). Right-censored at pause, state confirmed by the final successful check at 15:08:30Z (events#row-89, pending-responses last_checked_at): WORK-022 2026-09-18T16:12:44Z, 95h01m55s; WORK-023 16:12:45Z, 95h01m54s; WORK-024 21:22:49Z, 89h51m50s; WORK-025 21:22:50Z, 89h51m49s; WORK-026 21:22:51Z, 89h51m48s (eligibility unresolved); WORK-016 2026-09-19T01:18:59Z, 85h55m40s; WORK-021 2026-09-18T16:32:36Z, 94h42m03s; WORK-017 23:46:24Z, 87h28m15s; clawlancer inquiry 22:34:06Z, 88h40m33s; two AgentPact offers 15:23:01Z, 95h51m38s; nostr CSV offer 22:10:01Z, 89h04m38s; ugig python-fix offer 16:40:37Z, 94h34m02s; Clawstr offer 2026-09-19T01:54:49Z, 85h19m50s. Right-censored at the last successful check rather than at pause because the channel later failed: BasedAgents distribution proposal 2026-09-21T15:12:23Z to last successful read 18:11:57Z (2h59m34s), HTTP 403 afterwards; CREATINE inquiry 2026-09-20T09:49:10Z to last successful read 2026-09-21T11:02:39Z (25h13m29s), HTTP 403 afterwards; eleven mission-mailbox items (Puzzler sent 2026-09-22T00:08:02Z, FFmpeg 2026-09-21T18:10:58Z held in moderation, BTC Transcripts, ERROR, Microlancer, Sphinx, Averray, AgenticTrade, OpenTask, Dealwork, Dreamboat form) last successfully read 2026-09-22T00:08:24Z, HTTP 401 at 05:22Z and 09:04Z. Unresolved at pause: the pending register holds 39 entries (pending-responses /entries/0 to /entries/38): 27 awaiting an external party (14 due at 18:00Z on working channels, 13 on inaccessible channels or eligibility questions), 10 locally closed at scope cutoffs and held for final reconciliation only (modeling, Flarum, Anki, WBuilds, Pouncing, Multitude, CoinSutra, Nostr banner, RustChain, SIGNOMY), 1 closed intake (Atelier), 1 buyer-declined (Fourfold). Both commitment slots were empty (BRIEF line 37). The snapshot contains no post-pause customer outcome: pause-followup reports ledger_events_after_pause 0. No monetary cost or saving is assigned to the unobserved final interval.

**Opinion**

The early stop removed a final day in which the only cash-capable events were uGig decisions on two micro-submissions and six applications that had already sat unchanged for 85 to 95 hours, plus replies on channels the run could no longer read. I see nothing in the run's own trajectory that suggests the last 23h45m would have looked different from the preceding four days, but that is an inference from stasis, not a measurement, and the mailbox blindness means a late reply cannot be excluded. The pause itself was an operator decision; the run was in a deferred-wait posture with no committed work, so it interrupted no delivery.

**Locators**

- {"evidenceId": "E-SCOPE-008", "path": "SOURCE-008", "locator": "JSON pointers /paused_at_utc, /elapsed_note, /root_service, /registered_orbs"}

- {"evidenceId": "E-FUNNEL-004", "path": "SOURCE-027", "locator": "JSON pointers /channel_failures/mission_mailbox, /entries/0 through /entries/38"}

- {"evidenceId": "E-FUNNEL-006", "path": "SOURCE-012", "locator": "events#row-89"}

- {"evidenceId": "E-RUNTIME-020", "path": "SOURCE-012", "locator": "events#row-392"}

- {"evidenceId": "E-RUNTIME-001", "path": "SOURCE-012", "locator": "events#row-398, events#row-889"}

- {"evidenceId": "E-RUNTIME-014", "path": "SOURCE-012", "locator": "events#row-478"}

- {"evidenceId": "E-FUNNEL-002", "path": "SOURCE-025", "locator": "JSON pointers /work/0 through /work/29 (submitted_at_utc, last_checked_at_utc)"}

- {"evidenceId": "E-SCOPE-009", "path": "SOURCE-009", "locator": "JSON pointers /ledger_events_after_pause, /earning_activity_after_pause"}

**Confidence**

high

**Counterevidence**

- A buyer reply could have arrived on the 401-blocked mailbox or the 403-blocked BasedAgents thread after the last successful read; the snapshot cannot see it, so the 27 external waits may already have resolved unobserved.

- uGig review latency is unknown; a queue that is silent for 95 hours can still clear on day five.

- The elapsed figure uses the 14:59:32Z lifecycle event; the run id and SOURCE-004 use 14:59:30Z, a two-second difference.

### 3. demand-validation

**Measurement**

Strongest buyer-side signal timestamped before material production, one category per tracked dashboard work record (30 records, /work/0 to /work/29). Category A, explicit paid-scope agreement or acceptance: 0. Category B, direct buyer invitation or substantive buyer reply without agreed paid scope: 2 (Fourfold, invitation at 2026-09-20T15:19:45Z, events#row-1254, before worker start at 15:20:50Z; Clawstr Python-review listing, five external replies including a scope question answered on 2026-09-19T03:07:12Z, no purchase commitment, /work/14). Category C, public listing or advertised reward only: 23 (BountyBook state machine and Bloom filter, CrawlProof feedback, resource backlink, six uGig applications, Clawlancer inquiry, modeling diagnostic, Flarum, CREATINE, Anki, WBuilds, Pouncing, Multitude, CoinSutra, Nostr banner request, RustChain, SIGNOMY). Category D, agent-originated proposal without buyer reply and no reward listing: 1 (BasedAgents distribution proposal replying to a public question, /work/0; latest replies unknown after HTTP 403). Category E, no buyer-side signal: 4 (AgentPact Python-review offer, AgentPact CSV offer, Nostr CSV offer, uGig Python-fix offer). Atelier Python-review offer also had no buyer signal and zero orders before deliberate deactivation (/work/13, events with evidence atelier-deactivated-128); counted in E if Atelier is placed there, giving E = 5 and C = 22; the dashboard lists 30 either way. Effort that began before the strongest signal: synthetic demonstration samples were built with no buyer-side signal for the self-listed offers (CSV sample 2026-09-18T21:57:51Z; Atelier synthetic review sample; uGig sample 2026-09-19T09:25:42Z). For BountyBook, CrawlProof and the backlink, code or content production began after a public listing and before any buyer engagement with this agent. Fourfold production (18.69 minutes of orb time plus root verification) began after the invitation but before any agreed paid scope; the publisher's best-effort payment reply (events#row-1289) arrived while the artifact was already built. The hypothesis register (56 records) marks route-fact funding as verified only in the sense of advertised amounts; no record reaches an agreed fee.

**Opinion**

No opportunity ever converted advertised or invited demand into an agreed paid transaction, and the run knew it: every work record carefully labels its amount as quoted. Thirteen outbound proposals and inquiries produced exactly one substantive human reply, and that reply became a decline. The routes with real advertised demand (BountyBook, uGig) had verifiers or review queues that never issued a decision. In my judgement the strategy validated reachability and eligibility thoroughly but never validated willingness to pay before spending production effort; the parallel-clarification pattern (ask about payment while building) was the closest it came.

**Locators**

- {"evidenceId": "E-FUNNEL-002", "path": "SOURCE-025", "locator": "JSON pointers /work/0 through /work/29 (status, amount_basis, outcome)"}

- {"evidenceId": "E-FUNNEL-003", "path": "SOURCE-026", "locator": "JSON pointers /hypotheses/0 through /hypotheses/55 (route_facts.funding, status)"}

- {"evidenceId": "E-DROP-003", "path": "SOURCE-025", "locator": "JSON pointer /work/2"}

- {"evidenceId": "E-FUNNEL-005", "path": "SOURCE-028", "locator": "lines 33-39"}

- {"evidenceId": "E-RUNTIME-011", "path": "SOURCE-012", "locator": "events#row-1289, events#row-2000"}

- {"evidenceId": "E-RUNTIME-004", "path": "SOURCE-012", "locator": "events#row-342, events#row-1529"}

- {"evidenceId": "E-RUNTIME-002", "path": "SOURCE-012", "locator": "events#row-394, events#row-340"}

**Confidence**

medium

**Counterevidence**

- The category assignments rely on the run's own descriptions of listings and replies; the underlying platform captures are digest-only under workspace/.private and could not be re-read.

- Clawstr's five external replies may have been peer chatter rather than buyer engagement, which would move it from B to E.

- Pending uGig applications may have been under genuine consideration; silence is not evidence of absent demand.

### 4. execution-quality

**Measurement**

One row per produced or submitted deliverable. (1) BountyBook state machine: claim 2026-09-18T15:13:16Z (events#row-394); implementation with published tests plus six extra tests passing on Python 3.13.5, recorded 15:15:15Z (events#row-340); submitted 15:15:39Z (events#row-1916); turnaround claim to submission 2m23s; verifier rejected 15:16:39Z with 'Code output too small: 1 lines' against a 41-line file (events#row-1526); one retry rejected 15:20:07Z with 'Cannot read properties of undefined (reading length)' (events#row-1084); no independent critic (pre-policy-v2); buyer disposition none; platform history 3632 attempts with zero passed (/work/18); outcome platform-error. (2) BountyBook Bloom filter: claim 15:43:41Z (events#row-66); submitted 15:45:15Z with local tests passed at 95 false positives per 10000 (events#row-987); turnaround 1m34s; verifier internal error 'reading required_fields from undefined' at 15:45:36Z (events#row-744); no retry, submissions suspended; platform history 758 attempts with zero passed (/work/19); outcome platform-error. (3) CrawlProof feedback: submitted 16:32:36Z HTTP 201 pending (events#row-1472); acceptance criteria are the platform bounty terms; locally described as evidence-qualified feedback (screenshots are binary-excluded and unreadable here); no critic; pending review at cutoff (events#row-89); outcome pending review. (4) Resource backlink: post published and readback-verified 23:46:22Z, submission HTTP 201 pending/unpaid 23:46:47Z (events#row-1419); pending review at cutoff; outcome pending review. (5) Fourfold puzzle: invitation 2026-09-20T15:19:45Z (events#row-1254); registered a1.small worker built the candidate from 15:20:50.989Z to 15:39:32.290Z, 18.69 minutes; root independent DFS found exactly one solution with search exhausted in 19 nodes and five boundary tests passing at 15:33:49Z (events#row-1903); submit intent at 15:40:58Z cites a 350-step logical replay and two negative mutations (events#row-1178); first send failed on an expired authentication challenge at 15:44:40Z; read-only reconciliation at 15:49:01Z (events#row-1289); delivered and acknowledged 15:49:02Z (events#row-270); invitation to delivery 29m17s; independent nonauthor critic ran 16:06:51Z to 16:14:30Z (7m39s) after submission, reproduced one solution and 81 written placements, found no correctness, payload or prose defect, and left novice discoverability unmeasured (journal 2026-09-20 lines 26-30); buyer declined 2026-09-21T14:45:44Z, stated reason verbatim in the record: difficulty suitable, editorial distinctiveness insufficient (events#row-478, /work/2); outcome buyer-declined, editorial not technical. (6) Demonstrations completed locally without buyer review: CSV synthetic sample with seven tests (2026-09-18T21:57:51Z), Atelier synthetic review sample (atelier-synthetic-review-sample-62), uGig synthetic fix sample (2026-09-19T09:25:42Z); no buyer disposition. Classification: accepted 0; buyer-declined 1; platform-error 2; pending review 2; locally completed without buyer review 3.

**Opinion**

Technical correctness was never the evidenced failure mode. The one human decision was editorial, and the two verifier failures came from a platform whose own histories show zero passing attempts across thousands. Turnarounds were fast. The attribute that actually decided the only buyer-judged item, editorial distinctiveness, was the one attribute neither root verification nor the critic pass attempted to assess; the critic was scoped to correctness and ran after submission, so it could not have changed what was sent.

**Locators**

- {"evidenceId": "E-RUNTIME-002", "path": "SOURCE-012", "locator": "events#row-394, events#row-340, events#row-1916, events#row-1526, events#row-1084"}

- {"evidenceId": "E-RUNTIME-003", "path": "SOURCE-012", "locator": "events#row-66, events#row-987, events#row-744"}

- {"evidenceId": "E-RUNTIME-011", "path": "SOURCE-012", "locator": "events#row-1903, events#row-2000, events#row-1178, events#row-1289, events#row-270"}

- {"evidenceId": "E-RUNTIME-012", "path": "SOURCE-020", "locator": "lines 7-30"}

- {"evidenceId": "E-RUNTIME-014", "path": "SOURCE-012", "locator": "events#row-478"}

- {"evidenceId": "E-DROP-003", "path": "SOURCE-025", "locator": "JSON pointer /work/2"}

- {"evidenceId": "E-DROP-014", "path": "SOURCE-025", "locator": "JSON pointer /work/18"}

- {"evidenceId": "E-DROP-015", "path": "SOURCE-025", "locator": "JSON pointer /work/19"}

- {"evidenceId": "E-RUNTIME-005", "path": "SOURCE-012", "locator": "events#row-1472"}

**Confidence**

high

**Counterevidence**

- The first state-machine rejection ('1 lines') could be an agent-side payload-envelope error rather than a platform defect; the run itself recorded that suspicion (events#row-1526) and no independent reproduction exists.

- The critic's no-defect result and the walkthrough quality cannot be re-checked here because the critic input bundle and puzzle image are binary-excluded.

- The buyer's stated reason is known only through the run's paraphrase in events and dashboard; the message body was deliberately not retained.

### 5. external-delays

**Measurement**

Pending register at 2026-09-22T15:08:30Z: 39 entries. Causes use only the entries' status strings and related records. Buyer no reply: 16 entries. Ten were sent by email or relay and closed locally at scope cutoffs with 'closed_unaccepted_scope_cutoff' (modeling sent 2026-09-21T08:48:40Z, Flarum 2026-09-20T10:54:35Z, Anki 06:21:24Z, WBuilds 05:13:19Z, Pouncing 00:54:42Z, Multitude 2026-09-19T21:32:43Z, CoinSutra 20:16:52Z, RustChain 11:28:24Z, SIGNOMY 10:48:06Z, all last checked 2026-09-21T12:12:00Z; Nostr banner 2026-09-19T17:44:27Z last checked 2026-09-20T12:00:48Z), and six remained open with 'awaiting_scoped_reply', 'awaiting_buyer_reply', 'awaiting_buyer_deal' or 'awaiting_scope_and_timing' (Clawstr, Nostr CSV, uGig Python-fix, two AgentPact offers, Clawlancer), last successfully checked 15:08:30Z with state persisting, so right-censored at pause: Clawlancer 88h40m33s, AgentPact offers 95h51m38s, Nostr CSV 89h04m38s, uGig fix 94h34m02s, Clawstr 85h19m50s. Buyer or platform review: 7 entries ('application_pending' x5, 'submitted_awaiting_review' x2), state confirmed at 15:08:30Z, right-censored at pause: 95h01m55s, 95h01m54s, 89h51m50s, 89h51m49s, 85h55m40s for the applications; 94h42m03s (CrawlProof) and 87h28m15s (backlink). Eligibility clarification: 9 entries ('awaiting_eligibility', 'awaiting_eligibility_clarification', 'awaiting_eligibility_and_submission_route', 'awaiting_alternative_submission_route', 'awaiting_eligibility_and_settlement_clarification', 'awaiting_exception_to_published_eligibility', 'awaiting_ai_eligibility_alternative_submission_and_payment_timing', 'awaiting_eligibility_scope_and_payment_route'): uGig agent-job-board (confirmed at 15:08:30Z, 89h51m48s censored at pause) and Microlancer, Sphinx, Averray, AgenticTrade, OpenTask, Dealwork, BTC Transcripts, ERROR on the mission mailbox, last successfully read 2026-09-22T00:08:24Z, not confirmable through the pause. Moderation hold: 1 (FFmpeg, 'last_known_moderation_hold', list notice received 2026-09-21T18:11:30Z). Payment-timing hold: 0 entries name it as the sole cause; AgenticTrade and BTC Transcripts name settlement or payment timing alongside eligibility and are counted above. Inaccessible final channel as the primary recorded state: 4 (Puzzler and Dreamboat 'latest_mail_unknown' after HTTP 401; BasedAgents 'latest_replies_unknown_http403', last success 2026-09-21T18:11:57Z; CREATINE 'latest_reply_check_http403', last success 2026-09-21T11:05:50Z). The mailbox failure additionally blinds all 11 mission_mailbox entries from 05:22Z on 2026-09-22 (channel_failures/mission_mailbox, journal 2026-09-22 line 21). Buyer declined: 1 (Fourfold). Closed intake: 1 (Atelier, zero orders). Waits are concurrent and are not summed or divided by 96h15m. Runtime and verifier failures are reported under reliability.

**Opinion**

The dominant external condition was silence rather than slow processing: sixteen items got no reply at all, nine eligibility questions were never answered, and the two review queues that could have paid never moved in four days. The mailbox authentication failure on the last day converted eleven already-slow waits into blind ones. I would not call any counterparty blameworthy on this record; most proposals were sent to listings the run itself described as months old, so the silence may be closed need rather than delay.

**Locators**

- {"evidenceId": "E-FUNNEL-004", "path": "SOURCE-027", "locator": "JSON pointers /channel_failures/mission_mailbox, /entries/0 through /entries/38"}

- {"evidenceId": "E-FUNNEL-006", "path": "SOURCE-012", "locator": "events#row-89"}

- {"evidenceId": "E-RUNTIME-005", "path": "SOURCE-012", "locator": "events#row-594, events#row-1066, events#row-1472"}

- {"evidenceId": "E-RUNTIME-006", "path": "SOURCE-012", "locator": "events#row-1419, events#row-427, events#row-794"}

- {"evidenceId": "E-FUNNEL-002", "path": "SOURCE-025", "locator": "JSON pointers /work/0 through /work/29 (submitted_at_utc, last_checked_at_utc, blocker)"}

- {"evidenceId": "E-RUNTIME-018", "path": "SOURCE-023", "locator": "lines 21, 41, 49"}

**Confidence**

high

**Counterevidence**

- The pending statuses are the run's own labels; a 'no reply' could hide a reply that landed in the 401-blocked mailbox after 2026-09-22T00:08:24Z.

- Right-censored durations for the fourteen successful-channel items assume the 15:08:30Z state held until 15:14:39Z; no check exists inside that six-minute gap.

### 6. reputation-kyc-payment-friction

**Measurement**

Records counted once each from hypotheses.json, pending-responses.json and dashboard work records, using only explicit source wording. Confirmed incompatibility: 21 records, all hypotheses: h-authorized-prompt-challenge (bots and automation forbidden, majority-age and identity/tax documentation, judging and payment after the deadline), h-paid-image-restoration (age attestations on Reddit and PhotoshopGurus), h-finite-optimization-rewards (minimum 30-day comment wait; stated as deadline incompatibility, not an AI ban), h-authorized-security-bounty (Immunefi and HackenProof adult or legal-capacity attestations; Cryptohopper excludes AI-generated reports and pays only PayPal or EU bank), h-github-pr-bounties (human-qualified account or GitHub PR identity), h-electronic-component-library (forum terms 13+ and no machine-generated contributions), h-numerical-notebook-repair (Julia 13+ and non-machine terms; SciML legal-name, CV, GitHub and bank process; QuantumSavory forbids first-time LLM submissions and requires tax forms), h-home-automation-artifact (13+ and no machine-generated content), h-static-site-repair (Hugo 13+ and no machine-generated contributions), h-scientific-image-macro (image.sc 13+ and no machine-generated contributions), h-score-engraving (Freelancer individual-linked accounts and no automation), h-spreadsheet-formula-repair (ExcelForum prohibits AI-generated answers), h-workflow-automation-repair (n8n age 13 and automation prohibition), h-public-source-location (human-only researchers; Research Bounties requires Stripe identity verification), h-reproducible-technical-tutorial (Midnight prohibits substantially AI-generated work and requires KYC), h-paid-agent-evaluation (Prime terms 18, legal capacity, no automated access), h-reader-funded-technical-answers (Stacker adult/capacity), h-paid-editorial-fact-check (Upwork profile/identity route unavailable; five-day security hold beyond the deadline), h-nonsecurity-correctness-rewards (payout review cadence ending 2028), h-accessible-document (PeoplePerHour account and settlement incompatibilities), h-embroidery-stitch-artifact (VerticalScope 18+ set aside). By type across those 21 (overlapping): adult, age or legal-capacity attestation 12; AI-identity or machine-generated-content prohibition 10; KYC or identity verification including tax, legal name, bank or Stripe 4; payout method 2; settlement timing 4. No dashboard work record and no pending entry states a confirmed identity or KYC incompatibility; BountyBook explicitly accepted a fresh wallet (events#row-394). Unresolved friction: 39 records. Pending entries 10: WORK-026 (signup requests human review), Microlancer, Sphinx, Averray (GitHub-only submission route pending alternative), AgenticTrade (eligibility and settlement timing), OpenTask, Dealwork, BTC Transcripts (AI eligibility, alternative submission, payment timing), ERROR (eligibility, scope, payment route), Clawlancer (seven-day commitment and settlement timing versus deadline). Work records 12 whose blocker text names unanswered AI eligibility or payment route: modeling, Flarum, Anki, WBuilds, Pouncing, Multitude, CoinSutra, RustChain, SIGNOMY, CREATINE, BasedAgents distribution (payout unknown), WORK-016. Hypotheses 17 with route facts unknown and no prohibition: h-mailing-list-paid-patches, h-existing-puzzle-license, h-computational-replication-rewards, h-paid-compute-fulfillment, h-community-forum-customization, h-personal-knowledge-plugin, h-procedural-graphics-tool, h-paid-localization, h-cartographic-artifact (I-am-not-a-robot checkbox left uninteracted), h-podcast-production-artifact, h-dataset-repair, h-crypto-editorial-explainer, h-game-mod-source-repair, h-agency-subcontract-intake, h-spanish-direct-commissions, h-paid-public-data-contributions, h-paid-puzzle-artifact (PayPal or Venmo unavailable, alternative rail unresolved). Dashboard blocker strings (lines 21-27) additionally name about fifteen platforms with natural-person, adult, GitHub, Stripe KYC or human-linked-account requirements (Averray, Drips Wave, boss.dev, Circle, The Colony, BoTTube, MoltyWork, TaskBounty, OKX, AgentGigs, Moltbook, Superteam, Atelier, Clawlancer, Cryptohopper); these are free-text platform statements, not tracked records, and are not added to the counts. No funnel-loss percentage is computed because unique opportunities and a classified denominator are unavailable.

**Opinion**

Identity friction is the most repeated explicit exclusion in the register and it is structural rather than incidental: a transparent AI with no owner identity collides with age or legal-capacity clauses on nearly every human marketplace and with KYC on most payout rails, and the run correctly refused to route around it. What the record does not show is a single buyer rejecting the work because of AI identity; the one buyer who engaged did so after disclosure and judged on editorial merit. I read the unresolved-friction pile mostly as unanswered mail rather than as proven barriers.

**Locators**

- {"evidenceId": "E-FUNNEL-003", "path": "SOURCE-026", "locator": "JSON pointers /hypotheses/0 through /hypotheses/55 (route_facts.submission, route_facts.payout, blocker, blocker_class)"}

- {"evidenceId": "E-FUNNEL-004", "path": "SOURCE-027", "locator": "JSON pointers /entries/11, /entries/13, /entries/25, /entries/28, /entries/32 through /entries/38"}

- {"evidenceId": "E-RUNTIME-019", "path": "SOURCE-012", "locator": "events#row-212, events#row-1981, events#row-264, events#row-89"}

- {"evidenceId": "E-SCOPE-003", "path": "SOURCE-003", "locator": "lines 3-17"}

- {"evidenceId": "E-FUNNEL-002", "path": "SOURCE-025", "locator": "JSON pointers /blockers/1 through /blockers/8, /work/0 through /work/29 (blocker)"}

- {"evidenceId": "E-RUNTIME-002", "path": "SOURCE-012", "locator": "events#row-394"}

**Confidence**

medium

**Counterevidence**

- Several confirmed incompatibilities rest on the agent's reading of terms pages or on helper reports (DoltHub, PhotoshopGurus, Gray Swan) that root did not independently verify.

- A 13+ or adult clause may not in practice exclude a disclosed AI operated by an adult owner; the mission's no-owner-identity rule, not the platform, made it exclusionary.

- Counterparty domains are pseudonymised, so some platform identifications rely on the run's own labels.

### 7. constraints-and-operator-changes

**Measurement**

Version ledger from preserved copies and events. Change point 1, reinvestment steering: authorized at 2026-09-18T21:52:53Z (events#row-1641, attempt_id operator-steering) citing mission sha256 56ca504e...; that hash matches no mission copy in the analysis root (grep over the snapshot finds it only in the event stores), and the earliest preserved copy (SOURCE-011, sha256 c6ff70cb per its SHA256SUMS, 29 lines) already contains the reinvestment paragraph at line 11; byte diff unavailable. First subsequent behavior: no reinvestment spend was ever possible (cleared earnings USD 0; dashboard cost reinvestment-spend-observed 0). Change point 2, activity/discovery adjustment: maintenance started 2026-09-19T21:15:56Z and completed 21:27:21Z after 11m25s (events#row-1861, events#row-1860); the 29-line mission became the 41-line mission (SOURCE-013, sha256 aee98ce7) by appending lines 31-41: hypothesis and pending registers, up to two bounded explorers of roughly 45 to 60 minutes, blocker classification, a two-hour pivot rule, and compacted reporting; the same maintenance replaced earn50-control, earn50-worker and earn50-run.service (SHA256SUMS lines 2-4). First subsequent behavior: continuation 111 acknowledged the steering at 21:18:31Z, pivot recorded 21:20:14Z, two explorer threads started 21:20:58.862Z and 21:22:00.555Z, six pivots recorded between 21:20:14Z and 2026-09-20T08:25:00Z (hypotheses.json /pivots). Change point 3, policy v2: written at about 15:53Z on 2026-09-20 and recorded at 15:55:22Z as effective at the next attempt (events#row-799); pre-change 41-line copy sha256 aee98ce7, after copy 67 lines sha256 83dd5eb6 (after/SHA256SUMS), 26715 bytes; changes: line 35 edited in place from 'roughly 45 to 60 minutes' to 'until useful exhaustion and at most 60 minutes', lines 41-67 appended with trust boundary, route-to-payment facts, at most two committed items and explicit supersession of the two-hour pivot, demonstration tiers, isolation, independent critic, allocation question, evidence-not-activity, security research eligibility, brief hygiene, descendant briefing and one-time migration; an unattributed earn50-run stop and start occurred 15:58:38Z to 15:58:49Z from the maintenance account (events#row-1973). Effective: root resumed under v2 at 16:00:52Z (events#row-818). First subsequent behavior: migration and BRIEF reconciliation, security qualification screen parked at 16:11:22Z, nonauthor critic acknowledged v2 at 16:05:47Z and ran 16:06:51Z to 16:14:30Z, then deferred waits with hourly and later three-hourly checks and no new hypothesis from 16:26Z until 2026-09-21T08:34Z (journal 2026-09-20 lines 32-56, journal 2026-09-21 lines 3-17). Change point 4, policy v2.1: appended 2026-09-21T08:32:48Z (events#row-954); before copy sha256 83dd5eb6 is byte-identical to the v2 after copy (hashes.before.txt), after copy 87 lines sha256 78e79064, 31446 bytes (hashes.after.txt); adds lines 69-87: verbatim owner observation to be answered in the brief, a discovery lane outside the two slots, challenge before exhaustion, two separate decisions, migration; the idle wrapper was deliberately woken at 08:32:56Z (events#row-1137). Effective: root resumed under v2.1 at 08:34:04Z (events#row-1620). First subsequent behavior: independent challenge helper of about 11 minutes, Hutter rules screen, and a conditional 25 USDC diagnostic proposal sent 08:48:40Z (discovery-challenge-160, events#row-1088 line). Temporal sequence only; no causal attribution to commercial outcome.

**Opinion**

Each operator change arrived after a visible stall and each was followed by a visible change in behavior, but the outcome column is identical across all four versions: USD 0. The two mid-run policies pulled in opposite directions within seventeen hours: v2 told the run that a deferred wait is correct and screening to look busy is prohibited, the run then sat for sixteen hours, and v2.1 told it to keep a discovery lane open. The run followed the letter of whichever version was in force, which is a point in favour of its instruction-following and a point against treating its idle period as autonomous judgement.

**Locators**

- {"evidenceId": "E-MISSION-001", "path": "SOURCE-011", "locator": "lines 1-29"}

- {"evidenceId": "E-MISSION-002", "path": "SOURCE-012", "locator": "events#row-1641"}

- {"evidenceId": "E-MISSION-003", "path": "SOURCE-013", "locator": "lines 30-41"}

- {"evidenceId": "E-MISSION-004", "path": "SOURCE-012", "locator": "events#row-1861, events#row-1860"}

- {"evidenceId": "E-MISSION-005", "path": "SOURCE-014", "locator": "lines 35, 43-67"}

- {"evidenceId": "E-MISSION-006", "path": "SOURCE-012", "locator": "events#row-799, events#row-818, events#row-1973"}

- {"evidenceId": "E-MISSION-007", "path": "SOURCE-015", "locator": "lines 69-87"}

- {"evidenceId": "E-MISSION-008", "path": "SOURCE-012", "locator": "events#row-954, events#row-1137, events#row-1620"}

- {"evidenceId": "E-FUNNEL-003", "path": "SOURCE-026", "locator": "JSON pointers /pivots/0 through /pivots/5"}

**Confidence**

high

**Counterevidence**

- The reinvestment steering hash 56ca504e may be the hash of the post-change mission that was later further edited before the 09-19 backup, or of the pre-change mission; the snapshot cannot say which, so the diff direction is unknown.

- The sixteen-hour deferral after v2 may reflect a genuinely empty register rather than v2's wording; the run also deferred for long stretches on 2026-09-19 under the earlier text.

### 8. reliability

**Measurement**

Failure classes counted from the event projection and retained CLI metadata. Worker lifecycle exits with code 1: 34 rows in total, attempts 1 (2026-09-18T14:59:33Z), 34 (2026-09-18T22:50:52Z), 78 (2026-09-19T12:15:39Z), 83 (2026-09-19T13:32:21Z) and the 30 consecutive attempts 176 through 205 from 2026-09-22T00:12:40Z to 05:09:54Z; exits with code 0: 184 rows. Attempt 175 exited 0 at 00:11:32Z and scheduled the next continuation after 60 seconds with source default-active; attempt 176 started 00:12:33Z and exited 1 at 00:12:40Z; the wrapper restarted about every ten minutes (177 at 00:22:40Z, 178 at 00:32:50Z, ... 205 at 05:09:40Z), each exiting 1 within about ten seconds. Retained CLI fatal errors: 34 ERROR-level lines in the metadata projection, of which 3 are 'tool execution failed: apply_patch' on 2026-09-21 at 08:34:55Z, 12:16:22Z and 15:13:15Z, 30 are 'CLI fatal breadcrumb' between lines 30291 (00:12:39.808Z) and 41023 (05:09:54.653Z), one per failed attempt, and 1 is the only explicit error text, 'Cannot access AH before initialization.' at 00:12:39.808Z (line 30315), immediately after a client_append_user_msg request in ultra mode; the metadata retains no payload text, so the cause of the remaining 29 failures is not individually established. Observed recovery interval: first failure 00:12:40Z to next successful start 05:19:55Z (events#row-482) = 5h07m15s, and to next successful exit 05:46:25Z (events#row-459) = 5h33m45s; this is an observed interval, not exclusively productive time lost, because the queue's only scheduled work in that window was one grouped check at 03:00Z and the completion of attempt 175's interrupted dashboard reconciliation (journal 2026-09-22 line 5). Attempt 206 exited 0 at 05:46:25Z and scheduled the next continuation after 60 seconds with source invalid-active; attempt 207 started 05:47:25Z (events#row-740) and exited 0 at 05:49:59Z with a 3600-second deferred hint. Label disagreement: during attempt 206's window the event stream carries lifecycle and outcome rows labelled attempt-179 (05:20:10Z), attempt-180 (05:36:09Z, 05:36:41Z), attempt-181, 182, 184, 185, 186, 187 and attempt-188 (05:41:41Z and the handover outcome at 05:46:13Z, events#row-317), and the journal heads the handover as Attempt188 (journal 2026-09-22 lines 25-31), while lifecycle rows place attempts 179 through 188 in the failed sequence; both labels are retained without normalization. Platform-verifier failures: 3 rejections across 2 BountyBook deliveries (state machine rejected twice, one retry; Bloom filter rejected once, no retry); both jobs left reopened on the platform and abandoned by the run pending repair evidence (events#row-1084, events#row-744; /work/18, /work/19). Channel and HTTP failures: mission mailbox HTTP 401 first at 2026-09-22T05:22Z to 05:25Z and again 09:04Z to 09:08Z, routine retries then stopped; BasedAgents thread HTTP 403 on 2026-09-21 at about 21:02Z and on 2026-09-22 at about 12:02Z; CREATINE reply page HTTP 403 from 2026-09-21T12:05Z; Fourfold first send failed on an expired authentication challenge at 2026-09-20T15:44:40Z and was recovered by reconciliation at 15:49:01Z; a BasedAgents profile GET 403 was mis-reported as success and corrected at 2026-09-21T15:1xZ (journal 2026-09-21 line 61). Service stop or restart events: root service frozen for maintenance 2026-09-19T21:15:56Z to 21:27:21Z (events#row-1861, events#row-1860); unattributed earn50-run stop and start 2026-09-20T15:58:38Z to 15:58:49Z from the maintenance account, no in-flight loss recorded (events#row-1973); deliberate maintenance wake 2026-09-21T08:32:56Z (events#row-1137); operator pause 2026-09-22T15:14:39Z (events#row-392). Scheduler behaviour: the journals record at least 24 continuations that resumed before their deferred hint expired (for example 142-143, 145, 147, 149, 151-152, 154-155, 157-158, 161, 164-165, 167-168, 170-171, 212-214, 216-217); cause unverified by the run. Coverage gap: CLI metadata before 2026-09-20T23:00:06.786Z rotated away, so the four earlier code-1 exits have no retained error text and a complete error-cause census is not possible.

**Opinion**

Reliability was adequate for four days and then failed in the most benign window available: the crash loop ran overnight while the run was in a deferred wait, and it healed by itself. The more consequential defects, in my judgement, were the ones that touched customer channels: a mailbox key that stopped working on the final day and was never repaired, and a wrapper that repeatedly woke the root early against its own deferral hints, burning root context on no-op turns. I cannot attribute the 15:58Z stop-start; the record says the maintenance account issued no such command.

**Locators**

- {"evidenceId": "E-RUNTIME-015", "path": "SOURCE-012", "locator": "events#row-493, events#row-845 and the lifecycle rows for attempt IDs 176-205"}

- {"evidenceId": "E-RUNTIME-016", "path": "SOURCE-022", "locator": "lines 1-3, 8257, 16118, 20208, 30291, 30315, 41023, 55444"}

- {"evidenceId": "E-RUNTIME-017", "path": "SOURCE-012", "locator": "events#row-482, events#row-459, events#row-740, events#row-317"}

- {"evidenceId": "E-RUNTIME-018", "path": "SOURCE-023", "locator": "lines 3-7, 25-31"}

- {"evidenceId": "E-RUNTIME-002", "path": "SOURCE-012", "locator": "events#row-1526, events#row-1084"}

- {"evidenceId": "E-RUNTIME-003", "path": "SOURCE-012", "locator": "events#row-744"}

- {"evidenceId": "E-MISSION-006", "path": "SOURCE-012", "locator": "events#row-799, events#row-818, events#row-1973"}

- {"evidenceId": "E-RUNTIME-001", "path": "SOURCE-012", "locator": "events#row-1245, events#row-1130"}

- {"evidenceId": "E-FUNNEL-004", "path": "SOURCE-027", "locator": "JSON pointer /channel_failures/mission_mailbox"}

**Confidence**

high

**Counterevidence**

- The 30 fatal breadcrumbs are matched to the 30 failed attempts by count and time window only; the projection carries no attempt id, so a one-to-one mapping is inferred.

- Early wake counts come from journal prose, not from a normalized scheduler log, and may be incomplete.

- The apply_patch tool failures on 2026-09-21 have no retained payload and may have been harmless retries.

### 9. resource-and-token-efficiency

**Measurement**

Per exported thread, from SOURCE-010 (method: sum of top-level messages[].usage; totalInputTokens already includes cache reads and creation; maxInputTokens is capacity, not consumption). Root [private session identifier]: totalInputTokens 463,267,734; outputTokens 1,402,004; cacheReadInputTokens 427,747,456; cacheCreationInputTokens 35,520,278; 3177 usage-bearing messages, all gpt-6-astra; first projected message 2026-09-18T15:00:39.169Z (seq 0), last 2026-09-22T15:12:37.716Z (seq 6450), span 96h11m58s; last assistant turn shows about 183k input tokens per message. Attributable outputs: everything market-facing in the dashboard (30 work records, 13 outbound proposals or inquiries, 5 submissions), all BRIEF, journal and register maintenance, 218 attempts. Explorer/author [private session identifier]: totalInputTokens 39,135,750; outputTokens 102,263; cacheRead 36,392,704; cacheCreation 2,743,046; 298 usage messages; span 2026-09-19T21:20:58.862Z to 2026-09-20T15:39:54.962Z (18h18m56s). Exclusively attributable: explorer screens for event collateral, font engineering, embroidery, localization, compute fulfillment, public-source location, procedural graphics and scientific-image hypotheses (hypotheses.json evidence_references and owner fields), and the Fourfold candidate built in 18.69 minutes on 2026-09-20 (events#row-1128 line; journal 2026-09-20 line 8). Explorer/critic [private session identifier]: totalInputTokens 28,223,471; outputTokens 57,656; cacheRead 26,625,792; cacheCreation 1,597,679; 219 usage messages; span 2026-09-19T21:22:00.555Z to 2026-09-20T16:15:21.937Z (18h53m21s). Exclusively attributable: dataset-repair, browser-extension, cartographic and game-mod explorer screens, and the post-submission Fourfold critic pass of 7m39s (journal 2026-09-20 lines 26-30). Three-thread totals, reported separately: input 530,626,955; output 1,561,923; cache read 490,765,952 (arithmetic re-added and matches). Amp credit cost from SOURCE-004 line 42: root USD 1.71, author USD 1.13; inference was served through a linked subscription issuer. No per-progress-unit ratio is constructed: no output has both exclusive thread attribution and a common unit across threads. Unmeasured: nested helper calls (Task, Librarian, Finder helpers exposed no thread id), omitted messages, provider billing coverage, monetary model cost, human-help duration (two maintenance windows measured at 11m25s and about 5 minutes; user assistance duration unknown), host-side full cost; the runtime never parsed an Amp usage record (dashboard /costs/3, BRIEF line 29).

**Opinion**

Measured against outputs, the root thread consumed about 463 million inclusive input tokens, over 92 percent of them cache reads, to run 218 attempts that produced thirteen outbound contacts and five submissions; by the end each assistant turn carried about 180k tokens of context. I would not call that efficient, but the rubric rightly blocks a cost verdict: the tokens were subscription-served, cache reads are not full-price, and the two orbs were cheap by comparison and did produce the only artifact a buyer ever judged. The clearest waste I can point to is structural: the early-wake pattern meant dozens of root turns re-read a 180k-token context to conclude nothing was due.

**Locators**

- {"evidenceId": "E-SCOPE-010", "path": "SOURCE-010", "locator": "JSON pointers /method, /rows/0, /rows/1, /rows/2, /sum_input, /sum_output, /sum_cache_read"}

- {"evidenceId": "E-RUNTIME-007", "path": "SOURCE-016", "locator": "messages seq=0, seq=1, seq=6448, seq=6450"}

- {"evidenceId": "E-RUNTIME-008", "path": "SOURCE-017", "locator": "messages seq=0, seq=609"}

- {"evidenceId": "E-RUNTIME-009", "path": "SOURCE-018", "locator": "messages seq=0, seq=444"}

- {"evidenceId": "E-RUNTIME-010", "path": "SOURCE-019", "locator": "JSON pointers /threads/[private session identifier], /threads/[private session identifier], /threads/[private session identifier]"}

- {"evidenceId": "E-SCOPE-004", "path": "SOURCE-004", "locator": "lines 37-47, 65-66"}

- {"evidenceId": "E-RUNTIME-012", "path": "SOURCE-020", "locator": "lines 8, 26-30"}

**Confidence**

high

**Counterevidence**

- Local Task, Librarian and Finder helpers ran inside root turns with no thread id; their consumption may already be inside the root totals or may be entirely unmeasured, and the snapshot cannot say which.

- Cache-read pricing and subscription coverage are unknown, so the inclusive input figure may overstate economic cost by an unknown factor.

- Orb thread spans include idle time between tasks; wall-clock span is not active time.

### 10. instruction-accumulation

**Measurement**

Mission change points with preserved copies: 29 lines (c6ff70cb, earliest preserved, already containing the reinvestment paragraph at line 11) to 41 lines at 2026-09-19T21:27:21Z (aee98ce7; lines 31-41 added: registers, up to two explorers of roughly 45 to 60 minutes, blocker classification, about-two-hour pivot, compacted reporting) to 67 lines effective 2026-09-20T16:00:52Z (83dd5eb6, 26715 bytes; line 35 edited in place to 'until useful exhaustion and at most 60 minutes'; lines 41-67 added) to 87 lines effective 2026-09-21T08:34:04Z (78e79064, 31446 bytes; lines 69-87 added; the v2.1 before copy is byte-identical to the v2 after copy). Exact repetitions: the immutable deadline 2026-09-23T14:59:30Z is restated at lines 19, 43 and 71; the USD 50 minimum-not-cap rule at lines 3, 9 and 11; transparent AI identity at lines 5 and 7; the three-orb a1.medium limit at lines 15, 17, 35, 65 and 71; the deadline propagation to workers at lines 17, 19, 35, 65 and 87. Explicit contradictions resolved by precedence text: line 39 (about-two-hour pivot) versus line 49 ('The earlier two-hour pivot rule is superseded'); line 35 (fixed explorer duration) versus its in-place edit; line 13 ('Operate actively... keep discovering and evaluating opportunities... Before waiting, consider new areas') versus line 49 and line 59 ('an empty slot does not have to be filled... record that and stop screening'; 'A deferred wait is correct behaviour... you must not run searches or send messages in order to look busy') versus line 79 and line 85 ('Keep one bounded discovery effort available while committed work waits'; 'While a plausible untested direction remains, run a bounded investigation'); v2.1 line 71 says it replaces contradicted wording but the v2 text remains in the file, so both readings coexist under a precedence rule. BRIEF versions preserved: seed at 2026-09-20T15:54Z (79 lines, sha256 2fb2a1d6, committed slots empty, 42 hypotheses, 35 pending entries), post-adoption at 16:11:22Z (79 lines, Fourfold committed, 43 hypotheses), final at 2026-09-22T15:08:30Z (87 lines, both slots empty, 56 hypotheses, 39 pending entries, ten allocation entries, the verbatim owner observation at line 49). Earlier BRIEF growth is not inferred; before 2026-09-20 the workspace MISSION.md (509,616 bytes at freeze, journal 2026-09-21 line 33) served as the running record and no version of it is preserved in the analysis root. First comparable decisions around each change: before 09-19 21:15Z the run alternated hourly checks with single-platform screens (events#row-427, events#row-794); after, it recorded six pivots in eleven hours and started two explorers. Before v2 (attempt 139) it built and submitted Fourfold within thirty minutes of an invitation; after v2 (attempts 140-159) it ran one security qualification screen and one critic pass, then deferred with no new hypothesis for about sixteen hours (journal 2026-09-20 lines 32-56; 2026-09-21 lines 3-17). Before v2.1 the 08:02Z decision was 'no ready action, defer to 11:00'; after v2.1 the run produced eleven bounded discovery screens, four outbound inquiries and thirteen new hypotheses in the remaining 30h40m, each ending in a scoped pause with a stated reassessment trigger. Behavioral change is recorded as temporal association only.

**Opinion**

The mission tripled in length and by the end contained its own history: a pivot rule, its supersession, and a later correction of the supersession, all live in one file with a precedence clause. The run handled that competently; its later briefs answer the owner observation verbatim every time. What I would not conclude is that the accumulated text degraded judgement; the visible pattern is rather that the run's behaviour tracked the newest paragraph closely, which is the opposite failure, a lack of independent initiative when the newest paragraph said waiting was fine.

**Locators**

- {"evidenceId": "E-MISSION-001", "path": "SOURCE-011", "locator": "lines 1-29"}

- {"evidenceId": "E-MISSION-003", "path": "SOURCE-013", "locator": "lines 30-41"}

- {"evidenceId": "E-MISSION-005", "path": "SOURCE-014", "locator": "lines 13, 35, 43-67"}

- {"evidenceId": "E-MISSION-007", "path": "SOURCE-015", "locator": "lines 69-87"}

- {"evidenceId": "E-RUNTIME-007", "path": "SOURCE-016", "locator": "messages seq=0 through seq=6450 (textChars of user messages grow with re-injected mission)"}

- {"evidenceId": "E-FUNNEL-005", "path": "SOURCE-028", "locator": "lines 1-4, 45-53, 63-76"}

- {"evidenceId": "E-MISSION-004", "path": "SOURCE-012", "locator": "events#row-1861, events#row-1860"}

- {"evidenceId": "E-RUNTIME-013", "path": "SOURCE-021", "locator": "whole file"}

**Confidence**

medium

**Counterevidence**

- Line counts and byte sizes measure text, not what the model attended to; the per-attempt runtime paragraph appended after the mission is not preserved and may have mattered more.

- The post-v2 deferral could reflect an exhausted register rather than the new wording; both explanations fit the timeline.

### 11. reporting-integrity

**Measurement**

Fixed sample of 57 claims. BRIEF financial-truth rows (10, lines 22-31): accepted paid gross USD 0, matched (events#row-89, /payments empty); fees and refunds 'no transactions recorded, historical fees unverified', matched (/costs/5 unknown, no fee event); net receipts USD 0, matched (events#row-89); cleared earned funds USD 0, matched (events#row-89 spendable USD 0); reinvestment USD 0 and no reservations, matched (/costs/6 amount 0, events#row-89); VPS actual EUR 20 monthly, matched (/costs/0, 2026-09-18T14:35:17Z); subscription and Amp allowance unknown not zero, matched (/costs/2, /costs/7); model route, tokens and cost unknown with no runtime usage record, matched at the claim time (provider_usage rows carry null quantities, for example events#row-1133 line; the thread-export totals exist only outside the host); human help 'minutes unknown; no measured assistance session', contradicted in part: events record two measured maintenance windows, 11m25s on 2026-09-19 (events#row-1860) and 15:51 to 15:56Z on 2026-09-20 (events#row-799), and the mission at line 41 directs that measured maintenance time be used; the BRIEF row and dashboard /costs/4 present human help as wholly unmeasured; FX 'not performed; no non-USD revenue', unverifiable (no distinct source row; consistent with the empty payments array). Dashboard at source_as_of_utc 2026-09-22T15:08:30Z: /payments empty array, matched (no payment event through 15:08:30Z); /wallets 8 rows, all stale (checked 2026-09-18 to 2026-09-19) or unknown (3 rows, null checked_at), classified as limitation, 8 unverifiable; /work 30 records, each with a distinct event row supporting its submission time and, where terminal, its terminal state: BasedAgents (events#row-1369), modeling (event 9e1c76de at 08:51:19Z), Fourfold (events#row-478), Flarum (911e7fdf), CREATINE (273e1e43), Anki (19c8691b), WBuilds (0b1e66db), Pouncing (d3aa1df3), Multitude (e2e00887), CoinSutra (edaa2cd3), Nostr banner (e9877cde and 7fc1d240), RustChain (87cd6cc4), SIGNOMY (626bd8e9), Atelier (3055c52a), Clawstr (c8ec2534), ugig-app-seo (268a2cb9), backlink (events#row-1419), Clawlancer (events at 2026-09-18T22:34:38Z), state machine (events#row-1084), Bloom (events#row-744), CrawlProof (events#row-1472), ugig doc-cleanup and python-gui (events#row-1066), inventory (6d1a1043), pipeline (5b084a58), job-board (5edd683d), AgentPact Python (events#row-342), Nostr CSV (82ae1200), AgentPact CSV (ffd10481), ugig python-fix (208c6e92): 30 matched; the 'latest replies unknown' qualifiers on BasedAgents and CREATINE are recorded as limitations, not matches. Final event claim at 2026-09-22T15:12:25Z (events#row-89, 8 claims): six applications pending, matched (five application_pending plus one awaiting_eligibility at 15:08:30Z); two submissions pending/unpaid, matched (two submitted_awaiting_review); no new acceptance or payment, matched (no acceptance or payment row exists); gross USD 0, net USD 0, reinvestment USD 0, spendable USD 0, matched (BRIEF lines 22-26, dashboard /funds and /costs/6); queue 14 next 18:00Z and 25 final, matched (independent count of next_check_at values in pending-responses.json gives 14 and 25). Mailbox 401 and distribution 403 at the final check are limitations. Sample result: 47 matched, 1 contradicted in part, 9 unverifiable, of 57. Not extrapolated: the dashboard has no generated_at or totals fields and no complete report-version history exists.

**Opinion**

On this sample the run's reporting is honest to the point of severity: every quoted amount is labelled quoted, every unknown is labelled unknown, and the only discrepancy I found is an omission that understates the operator's measured help rather than overstating results. The stale wallet rows are a genuine reporting weakness because the dashboard presents observed zeros from day one next to a day-five source_as_of_utc; a reader could take them as current.

**Locators**

- {"evidenceId": "E-FUNNEL-001", "path": "SOURCE-025", "locator": "JSON pointers /source_as_of_utc, /funds, /payments, /wallets, /costs/0 through /costs/8"}

- {"evidenceId": "E-FUNNEL-002", "path": "SOURCE-025", "locator": "JSON pointers /work/0 through /work/29"}

- {"evidenceId": "E-FUNNEL-005", "path": "SOURCE-028", "locator": "lines 18-53"}

- {"evidenceId": "E-FUNNEL-006", "path": "SOURCE-012", "locator": "events#row-89"}

- {"evidenceId": "E-FUNNEL-004", "path": "SOURCE-027", "locator": "JSON pointers /entries/0 through /entries/38 (next_check_at, status)"}

- {"evidenceId": "E-MISSION-004", "path": "SOURCE-012", "locator": "events#row-1860"}

- {"evidenceId": "E-MISSION-006", "path": "SOURCE-012", "locator": "events#row-799"}

- {"evidenceId": "E-RUNTIME-014", "path": "SOURCE-012", "locator": "events#row-478, events#row-1369"}

**Confidence**

high

**Counterevidence**

- The human-help finding depends on reading 'measured assistance session' to include maintenance windows; the mission distinguishes maintenance time from user assistance duration, and the BRIEF may be using the narrower meaning.

- Matching a work record to an event row establishes the submission and terminal state, not every field; amounts and URLs were not cross-checked against platform captures, which are digest-only.

## Counterfactuals

### 1. CF-1-fourfold-editorial-fit-before-build

**Decision point**

2026-09-20T15:19:45Z, when the puzzle publisher's reply invited a disclosed-AI submission (events#row-1254) and root immediately reused the a1.small worker to build one candidate (worker start 15:20:50.989Z), sending only a payment and timing clarification in parallel at 15:21:49Z.

**Known at time**

- {"evidenceId": "E-RUNTIME-011", "path": "SOURCE-012", "locator": "events#row-2000, events#row-1289"}

- {"evidenceId": "E-MISSION-003", "path": "SOURCE-013", "locator": "lines 35-37"}

- {"evidenceId": "E-FUNNEL-003", "path": "SOURCE-026", "locator": "JSON pointer /hypotheses/34 (h-paid-puzzle-artifact, route_facts, evidence_references)"}

**Options available then**

- Build one candidate immediately and submit it after correctness verification, asking only about payment and timing in parallel (taken).

- Fold an editorial-fit question into the same 15:21Z clarification, asking what the publisher considers distinctive and what has recently run, and hold the build until the reply.

- Build two or three candidates with different mechanics, have the nonauthor worker rank them for distinctiveness against the publisher's public archive, and submit one.

- Decline the invitation as unqualified because the payout rail was unknown.

**Alternative decision**

Combine the second and third options: add one editorial-fit question to the clarification already being sent, and before sending any artifact have the registered nonauthor worker compare the candidate against the publisher's published puzzles for distinctiveness, not only correctness.

**Feasibility under actual constraints**

The mission in force (41-line version) allowed one transparent clarification as the smallest meaningful test and permitted two bounded explorers; the second orb was idle. No budget was needed. Transparent AI identity was already disclosed. About 71 hours remained to the deadline and the publisher's decision took 23 hours, so a few hours of qualification fit inside the window. The no-owner-identity rule was untouched.

**Expected difference**

The decline reason was editorial distinctiveness with suitable difficulty; that is the one attribute the process never assessed before sending. Asking the publisher what they want, or at least having a nonauthor judge distinctiveness before submission, changes what gets submitted rather than whether it is correct. The mechanism is selection on the criterion the buyer actually used.

**Confidence**

medium

**Counterevidence**

- The publisher may not articulate distinctiveness in advance, and a second candidate could be declined for the same reason; editorial taste is not measurable by the agent.

- Delaying the build risked the buyer's best-effort payment window before 2026-09-23 noon.

- The invitation itself may have been a courtesy to a disclosed AI rather than a serious acquisition interest, in which case no candidate would have converted.

### 2. CF-2-discovery-lane-before-v2-1

**Decision point**

2026-09-20T16:26:39Z, attempt 141, when root recorded 'Register has no ready/exploring hypothesis' and deferred to hourly and then three-hourly checks, a posture it held until the owner's v2.1 correction at 2026-09-21T08:34:04Z (journal 2026-09-20 lines 32-56, journal 2026-09-21 lines 3-17).

**Known at time**

- {"evidenceId": "E-MISSION-005", "path": "SOURCE-014", "locator": "lines 13, 35, 49, 59"}

- {"evidenceId": "E-RUNTIME-012", "path": "SOURCE-020", "locator": "lines 32-56"}

- {"evidenceId": "E-MISSION-006", "path": "SOURCE-012", "locator": "events#row-818"}

- {"evidenceId": "E-RUNTIME-008", "path": "SOURCE-017", "locator": "messages seq=607 through seq=609 (author orb idle after 15:39:54Z)"}

**Options available then**

- Defer with hourly checks, extended to three-hourly after repeated no-change results (taken).

- Give the idle author orb a v2 brief and one bounded explorer task on an untested hypothesis while Fourfold waited on review.

- Run a short local helper to challenge the assumption that no ready hypothesis existed, examining what the parked exclusions actually established.

- Reopen one of the 24 parked hypotheses with a tier-A demonstration.

**Alternative decision**

Take the second or third option: keep one bounded discovery effort running while the committed item waited, using the idle orb under a v2 brief or a fifteen-minute local challenge helper.

**Feasibility under actual constraints**

Policy v2 line 49 permitted screening while committed items wait and line 35 permitted up to two explorers; the original line 13 'Operate actively' paragraph was unchanged and binding; both orbs were idle and within the three-orb a1.medium limit; no money was needed; 70 hours remained. v2 line 59 discouraged searching to look busy, so the alternative would need a recorded allocation answer, which the same policy required anyway.

**Expected difference**

The roughly sixteen hours between 16:26Z and 08:34Z the next morning contained no discovery. When the same kind of lane was mandated by v2.1, the run produced eleven bounded screens, thirteen new hypotheses and four outbound inquiries in the final thirty hours. Moving that activity sixteen hours earlier would have given any resulting proposals a full extra day of reply time before the deadline; the mechanism is reply-window length, not more intelligence.

**Confidence**

medium

**Counterevidence**

- Every v2.1-era lane ended in a scoped pause with no qualified lead and no reply, so earlier lanes might only have produced more parked hypotheses.

- The run's reading that v2 made a deferred wait correct behaviour was textually defensible; the owner's own correction was needed to change it, which suggests the alternative was not obviously available to the run.

- The register at 16:11Z already held 24 parked hypotheses; an untested direction may genuinely not have been visible.

### 3. CF-3-explorer-on-payout-rails

**Decision point**

2026-09-19T21:20:14Z to 21:22:00Z, when the activity-adjustment maintenance authorised two bounded explorers and root pivoted from marketplace scans to 'event collateral' and 'dataset repair' explorers (hypotheses.json /pivots/5; explorer threads titled buyer-requested event collateral and buyer-requested dataset repair in SOURCE-019).

**Known at time**

- {"evidenceId": "E-MISSION-003", "path": "SOURCE-013", "locator": "lines 33-37"}

- {"evidenceId": "E-RUNTIME-019", "path": "SOURCE-012", "locator": "events#row-393 (Circle, boss.dev, Drips identity requirements at 2026-09-19T11:08:26Z)"}

- {"evidenceId": "E-RUNTIME-006", "path": "SOURCE-012", "locator": "events#row-427, events#row-794 (six applications pending, no replies, by 2026-09-19T07:17Z)"}

- {"evidenceId": "E-RUNTIME-004", "path": "SOURCE-012", "locator": "events#row-1529 (AgentPact settlement on Base documented, zero deals)"}

- {"evidenceId": "E-RUNTIME-010", "path": "SOURCE-019", "locator": "JSON pointers /threads/[private session identifier]/title, /threads/[private session identifier]/title"}

**Options available then**

- Assign both explorers to new market verticals chosen by root (taken).

- Assign one explorer to a settlement-and-eligibility qualification: enumerate which reachable buyer routes actually pay a disclosed AI into a self-custodied wallet within about 72 hours without age or identity attestation, and rank the existing pending items and candidate verticals by that.

- Assign one explorer to deepen the six pending uGig applications with tier-A demonstrations for the posters who had not replied.

**Alternative decision**

Take the second option: spend one of the two explorer slots on a route-and-rail screen before spending more root turns on vertical-by-vertical outreach.

**Feasibility under actual constraints**

Research-only work with no accounts, contacts or spend was explicitly what explorers were for under the 41-line mission; it needed no budget, no identity, and no deadline exception; the orb allowance was available. The zero-budget and no-owner-identity rules make the question central rather than a distraction.

**Expected difference**

From 2026-09-21 onward the run discovered settlement and identity exclusions one at a time at about fifteen minutes each: the Upwork five-day hold, the Hutter thirty-day wait, CrowdStrike post-deadline payout, PeoplePerHour, Immunefi and HackenProof capacity terms. A consolidated screen on 2026-09-19 would have front-loaded those exclusions and steered the eight direct proposals sent on 2026-09-20 toward buyers whose rails were already known to work. The mechanism is fewer proposals sent into routes that could not pay in time.

**Confidence**

low

**Counterevidence**

- The direct-email proposals failed on silence, not on rails; knowing the rail does not create a reply.

- The sector-selection dimension is unmeasurable, so I cannot claim a rail-compatible sector with live demand existed.

- Root already recorded several rail facts in passing (AgentPact Base settlement, uGig SOL payout), so the marginal information from a dedicated screen may have been small.

### 4. CF-4-crash-loop-breaker-at-v2-maintenance

**Decision point**

2026-09-20T15:51Z to 15:56Z, the operator's policy v2 maintenance window (events#row-799), which followed the 2026-09-19T21:15Z maintenance that had already replaced earn50-worker, earn50-control and earn50-run.service (activity-adjustments SHA256SUMS lines 2-4).

**Known at time**

- {"evidenceId": "E-RUNTIME-001", "path": "SOURCE-012", "locator": "events#row-1245 (attempt 1 exited 1), events#row-1130"}

- {"evidenceId": "E-RUNTIME-015", "path": "SOURCE-012", "locator": "lifecycle rows for attempts 34, 78 and 83 exiting with code 1 on 2026-09-18T22:50:52Z, 2026-09-19T12:15:39Z and 2026-09-19T13:32:21Z"}

- {"evidenceId": "E-MISSION-004", "path": "SOURCE-012", "locator": "events#row-1860 (maintenance verified worker and continuation scheduling)"}

- {"evidenceId": "E-MISSION-006", "path": "SOURCE-012", "locator": "events#row-1973 (rollout tests of worker runtime, 11 of 11 passed)"}

**Options available then**

- Keep restart-on-failure with roughly ten-minute retries and no escalation (taken).

- Add a consecutive-failure threshold to the wrapper that notifies the operator and backs off after, say, three code-1 exits.

- Pin or roll back the Amp CLI version on a fatal initialization error rather than retrying the same binary.

**Alternative decision**

Take the second option: a consecutive-failure breaker with operator notification, added while the operator was already testing the worker runtime.

**Feasibility under actual constraints**

This is a host-side operator change, outside the agent's constraints; it touches no mission rule, budget, identity or deadline. The operator was already editing and testing the wrapper on both 2026-09-19 and 2026-09-20, and four code-1 exits had already occurred.

**Expected difference**

The thirty-attempt loop from 00:12:40Z to 05:19:55Z on 2026-09-22 would have surfaced to a human at about 00:35Z instead of running silently for five hours. The concrete losses were small: one missed 03:00Z grouped check, an interrupted dashboard reconciliation, and thirty wasted CLI starts. The mechanism is earlier human awareness, not a different agent decision.

**Confidence**

low

**Counterevidence**

- Recovery happened spontaneously at attempt 206 with no intervention; a breaker that stopped retrying might have lengthened the outage if nobody was awake at 00:35Z.

- The window was a deferred-wait period with almost nothing scheduled, so the commercial cost of the loop was close to zero regardless.

- The only explicit error text points inside the Amp CLI ('Cannot access AH before initialization'), which the operator could not fix by wrapper changes; a version pin might have been the only effective remedy and its feasibility is unknown.

## Process assessment

The method was rigorous about truth and cautious about action, and those two properties explain most of what the record shows. On truth it was excellent: every amount is labelled quoted, every unknown is labelled unknown, the register is dense with source-backed exclusions, and the reporting sample checked out at 47 of 57 with one partial omission. On action the process produced thirteen outbound contacts, five submissions and five self-listed offers in four days, of which exactly one reached a human decision. The recurring cycle was: find a listing, verify it is reachable without human attestation, send one transparent inquiry, set a scope cutoff, wait, close locally when silent. That cycle validated eligibility exhaustively and willingness-to-pay never. Where the process did invest production effort before a buyer engaged (BountyBook, CrawlProof, the backlink) it chose the smallest possible units, and where a buyer did engage (Fourfold) it optimised for correctness and was declined on taste. The operator's three mid-run corrections each targeted a real stall, and the run adopted each within an hour, which is creditable, but it also means the run's own initiative during the sixteen-hour post-v2 deferral was low. Resource use was dominated by a 96-hour root thread that re-read a near-full context on dozens of early wakes to conclude nothing was due; that is a harness defect more than a strategy defect. I do not conclude that the space was exhausted or that more intelligence would have found paying demand; the evidence supports only that this method, under these identity and settlement constraints, did not.

## Intention alignment

Against the reconstructed operator intent and the mission in force at each moment. Zero budget, legal means, transparent AI identity, no owner identity or accounts: followed throughout; the run repeatedly refused age attestations, robot checkboxes, owner-linked accounts and key bypasses. Count only accepted paid work, record costs and unknowns: followed to the letter, with the one partial gap that measured maintenance minutes were reported as unmeasured. Ultra mode and at most three small orbs: followed; exports show ultra and two a1.small orbs. Continuous opportunity seeking while waiting (intent point 3): this is where letter and point diverged. Between 2026-09-20T16:26Z and 2026-09-21T08:34Z the run followed the newly installed policy v2 text that a deferred wait is correct behaviour and that an empty slot need not be filled, and it stopped discovery entirely; the operator's intent, and the unchanged 'Operate actively' paragraph, said the opposite, and v2.1 had to restore it. In that interval the run was following the mission's latest paragraph rather than the operator's point. Dissatisfaction with passivity and low-pay microtasks (intent point 7): the run's day-one microtasks (USD 2, USD 0.50) and its later pattern of fifteen-minute screens ending in scoped pauses satisfy the mission's evidence-and-bounds wording while missing the point that the operator wanted paid work executed; the run never found work that both qualified and engaged a buyer, and it recorded that honestly rather than manufacturing activity, which is the right failure mode but still a failure against the point. The owner observation that an empty register does not prove absent approaches (intent point 10) was quoted and answered in every subsequent brief; each answer ended in a scoped pause with a trigger, so it was honoured procedurally and never overturned an exclusion. Security work (intent point 8): qualified once, parked on identity and payout terms, never tested against any system, which matches intent. The sector-first strategy in intent point 12 postdates the run and was not in force. Net: high alignment with the mission text at every timestamp; alignment with the operator's underlying point was strong on integrity and safety and weakest on initiative during the v2 window.

## Summary

Across 96h15m the Earn50 run produced no independently evidenced acceptance or payment: the ledger reads USD 0 gross and net with wallets unrefreshed at pause, thirty market-facing items ended as 12 withdrawn, 1 declined, 2 platform errors, 5 listed, 8 proposed and 2 pending, and the only human buyer decision (Fourfold, declined for editorial distinctiveness after 22h57m) came after a build that was verified for correctness but never for the criterion the buyer used. Demand was never validated beyond invitations and listings; twenty-one hypotheses record explicit identity, age, KYC or settlement-timing incompatibilities and thirty-nine records leave eligibility or payout unanswered. Reliability held until an overnight thirty-attempt CLI crash loop that self-healed after 5h07m, and a mailbox authentication failure blinded eleven pending items on the final day. Three operator policy changes each produced the intended behavioural shift within an hour; the run tracked the newest mission text closely, including a sixteen-hour deferral that v2 permitted and v2.1 reversed. Reporting integrity on a 57-claim sample was 47 matched, 1 partially contradicted (measured maintenance minutes reported as unmeasured), 9 unverifiable (stale or unknown wallets, FX). Three-thread token consumption was 530.6M inclusive input and 1.56M output, unpriced. Four counterfactuals are offered without probabilities: editorial-fit qualification before the Fourfold build, a discovery lane during the post-v2 deferral, an explorer devoted to payout rails on 2026-09-19, and a crash-loop breaker at the 2026-09-20 maintenance.

## Blocked

false

## Blockers

- Supplemental file sha256 values could not be recomputed in this lane (no shell or hashing tool); contents matched the register descriptions and the hashes listed in the brief equal those in the evidence register, but the pin was not independently verified.

- Lane model identity and effort are self-reported only; the injected reasoning_effort was 80 against a requested 'max', and no runtime usage record was visible for comparison.
