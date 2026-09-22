# Subscription-compatible harnesses and workflow engines

## Method and grading

The research read the validated tooling corpus and its correction history, then opened first-party documentation for the claims reported here and inspected one locally installed package read-only. The research lane did not run candidates. Separately, this postmortem successfully exercised the three required native review harnesses and reconciled their runtime model records; that is local feasibility evidence, not a multi-day reliability comparison. This is a convenience sample of tools named by the brief or surfaced while reading them.

Grades are preserved exactly. In this report, `audited` means a first-party documentation claim corroborated by a second official artifact or installed code; it does not mean empirical multi-day testing. `self-report` means a single first-party vendor source. `unverified` means an ambiguous mechanism or an unbuilt design.

## Candidates

### Claude Code CLI on a Claude subscription

- Primary sources: [authentication](https://code.claude.com/docs/en/authentication), [headless mode](https://code.claude.com/docs/en/headless), [legal and compliance](https://code.claude.com/docs/en/legal-and-compliance)
- Verification grade: `audited`
- Grade reason: three official pages were opened and cross-corroborated.
- Outcome: subscription OAuth is explicitly documented; a one-year token supports CI/scripts on eligible paid plans. Resume, structured output, retry events, and permission controls exist. Subscription-funded headless execution cannot use bare mode, so project hooks and local MCP configuration remain a trust concern. Credential precedence can silently select a paid API key if one is present.
- Near-zero exclusions: paid Claude plan; recommended bare scripting mode is API-key mode; vendor language says advertised plan limits assume ordinary individual usage.
- Relevance: the reference sanctioned subprocess boundary: unmodified vendor binary, account-holder sign-in.

### Anthropic authentication boundary

- Primary source: [legal and compliance](https://code.claude.com/docs/en/legal-and-compliance)
- Verification grade: `self-report`
- Grade reason: one first-party legal page, authoritative only for Anthropic's policy.
- Outcome: intermediating Claude.ai credentials/session tokens is prohibited; end-user sign-in to an unmodified Claude Code binary is expressly allowed. Hosting in agent infrastructure carries Commercial Terms conditions.
- Near-zero exclusions: the rule applies to Anthropic only.
- Relevance: constrains architecture by keeping subscription inference inside the vendor CLI process.

### Claude Code GitHub Actions with subscription OAuth

- Primary sources: [GitHub Actions](https://code.claude.com/docs/en/github-actions), [authentication](https://code.claude.com/docs/en/authentication)
- Verification grade: `audited`
- Grade reason: official action documentation corroborated by the authentication page.
- Outcome: cron-triggered automation can use a subscription OAuth token rather than API billing. State must live in repository/issue artifacts; observability is workflow logs and comments. Actor permissions and repository administration gate use.
- Near-zero exclusions: paid Claude plan; GitHub Actions minutes; token tied to the subscriber; repository/GitHub App administration.
- Relevance: no-server scheduler with weak cross-run state.

### Codex CLI on a ChatGPT plan

- Primary sources: [CLI](https://learn.chatgpt.com/docs/codex/cli), [pricing](https://learn.chatgpt.com/docs/pricing), [authentication](https://learn.chatgpt.com/codex/auth), [command reference](https://learn.chatgpt.com/codex/developer-commands?surface=cli)
- Verification grade: `audited`
- Grade reason: four official pages cross-corroborate plan inclusion, authentication, resume, and command flags.
- Outcome: ChatGPT sign-in and session refresh are documented. Noninteractive mode supports JSONL events, schema output and resume. API-key authentication is recommended for automation, but the vendor also documents an advanced ChatGPT-managed path for trusted private CI. That credential-seeding workflow explicitly excludes public/open-source repositories and is not deployed or published here. [Noninteractive mode](https://learn.chatgpt.com/docs/non-interactive-mode), [authentication](https://learn.chatgpt.com/docs/auth).
- Near-zero exclusions: additional credits are a paid purchase; API-key usage is billed; weekly caps are unpublished.
- Relevance: a native subscription subprocess was demonstrated in this review. Documentation of an advanced automation path does not establish unlimited capacity or permission for every use pattern.

### Amp with a linked ChatGPT subscription

- Primary sources: [pricing](https://ampcode.com/docs/pricing), [model routing](https://ampcode.com/docs/customize/model-routing), [plugins](https://ampcode.com/docs/customize/plugins), [execute mode](https://ampcode.com/docs/cli/execute-mode)
- Verification grade: `audited`
- Grade reason: official pages cross-corroborate subscription connections, routing, plugins, and noninteractive credentials.
- Outcome: linked subscriptions consume plan limits; covered models carry no Amp token fee. Uncovered models fall back to Amp credits, non-model tools can consume credits, and orbs have a separate allowance. For scripts/CI using `AMP_API_KEY`, execute-mode documentation calls for a long-lived Settings token; a short login token cannot refresh in that environment variable. This does not establish that every stored-login execute path fails. The actual required Amp review succeeded on the existing linked subscription. Plugin agent modes can continue turns but model pinning still needs provenance.
- Near-zero exclusions: uncovered routes and paid tools/orbs can consume credits; the linked subscription is an endowment. Hobby documents all product features, linked subscriptions and own runners; Enterprise inherits lower-tier features. No newly paid Amp plan was required for the observed review.
- Relevance: cost boundary is a live routing invariant, not a one-time authentication fact.

### Smithers as shipped

- Primary sources: [docs index](https://smithers.sh/llms.txt), [durable execution](https://smithers.sh/docs/concepts/durable-execution/), [agent policies](https://smithers.sh/docs/guides/agent-policies/), [model seats](https://smithers.sh/docs/guides/model-seats/)
- Verification grade: `audited`
- Grade reason: four official pages plus read-only inspection of the installed agent package.
- Outcome: durable steps, approvals, resource budgets, quota parking, observability, and multi-agent adapters are available while vendor CLIs remain inference subprocesses. Completed actions replay from storage; unfinished side effects can repeat, so application idempotency remains required. Code intentionally removes a paid Anthropic key unless explicitly supplied so Claude Code can use subscription auth.
- Near-zero exclusions: another system to operate and keep current; public pricing wording can imply key-based spend; a distinct OpenAI-session route needs separate compliance review.
- Relevance: the existing controller provides documented quota parking and resource pools. Their presence does not prove alternatives cannot implement comparable controls.

### Smithers OpenAI seat using a Codex session store

- Primary sources: [model seats](https://smithers.sh/docs/guides/model-seats/), [Anthropic boundary used only as structural comparison](https://code.claude.com/docs/en/legal-and-compliance)
- Verification grade: `unverified`
- Grade reason: the mechanism is documented; its standing under OpenAI policy was not established.
- Outcome: Smithers documents reading a Codex session and calling a ChatGPT backend directly rather than spawning `codex exec`. This is structurally different from the sanctioned subprocess boundary. No claim is made that OpenAI forbids it.
- Near-zero exclusions: permission for this alternative authentication route was not assessed. This task used native CLI seats; the alternative is unnecessary to the recommendation.
- Relevance: configuration choice that should not be inherited silently.

### Tailored Smithers pack

- Primary sources: [durable execution](https://smithers.sh/docs/concepts/durable-execution/), [agent policies](https://smithers.sh/docs/guides/agent-policies/), [model seats](https://smithers.sh/docs/guides/model-seats/), [docs index](https://smithers.sh/llms.txt)
- Verification grade: `unverified`
- Grade reason: the constituent primitives are documented; the proposed composition does not exist.
- Outcome: proposed lanes with declared seats, budgets, quota parking, human gates, idempotency keys, and OTLP. It must still add business qualification/CRM and served-model checks for Amp.
- Near-zero exclusions: authoring/maintenance labor and all exclusions of the chosen CLI.
- Relevance: reuse of durable primitives without claiming revenue benefit.

### Purpose-built minimal harness

- Primary sources: [Claude headless](https://code.claude.com/docs/en/headless), [Claude authentication](https://code.claude.com/docs/en/authentication), [Codex commands](https://learn.chatgpt.com/codex/developer-commands?surface=cli)
- Verification grade: `unverified`
- Grade reason: the CLI primitives are documented; the harness is only a design.
- Outcome: a small loop could use structured output, resume, denial policy, retry events, and subscription inference. Honest build cost includes journal, idempotency, quota parking, approvals, and dashboard.
- Near-zero exclusions: project hooks/MCP settings require review; human build and maintenance are unmeasured; side-effect safety must be implemented.
- Relevance: fewer components may simplify a bounded run, but journal, recovery, quota, alerts and side-effect handling still require implementation. Build hours, maintenance effort and comparative cost were not measured.

### Temporal as pure scheduler

- Primary source: [Activities](https://docs.temporal.io/activities)
- Verification grade: `self-report`
- Grade reason: one first-party page; the exact phrase “at-least-once” was not present on the cited page.
- Outcome: Activities retry and should be idempotent; heartbeat state can resume work. Subscription auth, quota, model provenance, and inference remain in a subprocess harness. Operational cost is server plus workers.
- Near-zero exclusions: infrastructure and human operations; no consumer-plan integration.
- Relevance: durable timers and explicit retry semantics, not exactly-once effects.

### LangGraph as pure scheduler

- Primary source: [functional API](https://docs.langchain.com/oss/python/langgraph/functional-api)
- Verification grade: `self-report`
- Grade reason: one first-party vendor page.
- Outcome: unfinished tasks may run again after resume, so side effects must be idempotent. Checkpoint replay restores completed task results. It is a library rather than a server, but subscription auth/quota/provenance stay in the subprocess harness.
- Near-zero exclusions: native integrations naturally favor paid provider APIs; no subscription controls of its own.
- Relevance: a library deployment has different operating and recovery contracts from a Temporal service. Both require attention to idempotent external effects; that common obligation does not make the contracts identical.

### OpenCode subscription authentication

- Primary source: [providers](https://opencode.ai/docs/providers/)
- Verification grade: `unverified`
- Grade reason: the same page offers consumer-plan sign-in and warns that a plugin form of Claude subscription use is prohibited; the exact path could not be resolved.
- Outcome: consumer subscription options are documented for Claude and ChatGPT, but the Claude route is ambiguous enough that durability and orchestration were not evaluated.
- Near-zero exclusions: cannot be treated as a compliant zero-cost Claude path while documentation remains internally ambiguous.
- Relevance: example of subscription support that is neither safely assumed nor safely rejected without further primary-source work.

## Corrected claims

- Counting repeated card wording is not a restriction: Amp Hobby includes all product features and Enterprise inherits the other tiers. Linked-subscription inference has no generic Amp token markup; optional paid tools and orbs remain separate.
- Amp's model-routing page moved rather than disappearing; it documents subscription connections and billable fallback.
- Amp's long-lived-token instruction is specific to the scripts/CI environment-variable path. The successful existing-account Amp review is stronger evidence of this task's feasibility than a blanket blocker inferred from that instruction.
- A prior Codex quotation omitted the image-generation scope of one sentence; paid API usage remains established by a different pricing sentence.
- Codex plan/allowance claims belong to the pricing page; command flags now come from official command documentation, and the documented bypass flag differs from a prior local-help flag.
- Temporal recommends idempotency and retries failed Activities, but “at-least-once” is an inference here, not a quotation from the cited page.
- Smithers diagnostics do read a credential file/keychain to test token presence/expiry; no token replay was found.
- Smithers subscription support is documented outside the compact index; the separate direct ChatGPT-session route remains compliance-unverified.
- Smithers, Temporal, and LangGraph all require application idempotency for remote side effects; engine choice rests on operational and recovery contracts, not exactly-once effects.

## Open gaps

- Per-plan capacity is unpublished for the multi-day horizon.
- New-account provisioning and every billing fallback were not audited; no new paid-plan requirement is inferred from that gap.
- Amp does not document which models a linked ChatGPT connection serves, so the credit-fallback boundary is unknown.
- The documented trusted-private automation path does not settle every multi-day usage pattern; no account-wide permission or capacity guarantee is claimed.
- The permissibility of Smithers' direct Codex-session reuse route is unestablished.
- OpenCode's Claude consumer-auth path remains ambiguous.
- Multi-seat Claude registration in Smithers lacks a public guide page.
- Temporal's exact “at-least-once” wording remains unsourced in this report.
- No candidate has measured multi-day reliability data.
- Several other installed or public harnesses were not evaluated.
- The research comparison did not benchmark candidates. Required review lanes succeeded separately; comparative multi-day reliability and operating costs remain unmeasured.

## Summary

The clearest low-spend boundary is the unmodified vendor CLI signed in by the account holder. Durable engines can schedule that subprocess but do not remove plan limits, idempotency obligations, or business qualification. Smithers documents quota parking and a resource pool; a minimal harness can reduce components while leaving those controls to its author. A tailored pack reuses this task's existing controller, but is a proposed design, not an established best or cheapest choice. Nothing in this comparison establishes revenue impact.

## Final interpretation of vendor policy and evidence

Official policy pages are authoritative for the vendor's published terms; two pages from one vendor are not an independent audit. Retain the original grade labels as research metadata, and distinguish documented policy/capability, local observations, unmeasured comparisons and proposed designs. Anthropic's product-hosting commercial conditions do not by themselves establish that this account holder's personal local controller requires a new commercial agreement; nor do they establish another vendor's policy. No account action or credential change follows from this comparison.

| Choice | What it contributes | Work still required | Evidence limit |
| --- | --- | --- | --- |
| Native subscription CLI | Model interaction through existing account and native harness | State, budgets, alerts, side-effect controls | Required lanes worked; no multi-day guarantee |
| Tailored Smithers | Existing durable state, UI, approvals and quota mechanisms | Business qualification, scoped action rules, recovery tests | Proposed composition; no revenue advantage proved |
| Minimal controller | Small bounded control loop | Journal, safe replay, limits, notifications and maintenance | No measured cheapest/lowest-overhead result |
| Temporal + CLI | Durable activities, timers and retry machinery | Service operations and subscription subprocess integration | Different recovery contract; external effects still need safe retry |
| LangGraph + CLI | Checkpoints and resumable graph execution | Hosting, durable storage, limits and subscription subprocess integration | Different recovery contract; no comparative reliability benchmark |
