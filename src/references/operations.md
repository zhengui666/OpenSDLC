# Engineering operations

English · [简体中文](operations.zh-CN.md)

Read this for project onboarding, automation, evaluations, releases or maintenance. The
[core workflow](../SKILL.md) defines execution; [artifact conventions](artifacts.md) define every output.
`T` denotes `.opensdlc/tasks/<task-id>`. Read repository `.opensdlc/config.json` and the matching template
before writing; name new tasks in the resolved language (Simplified Chinese for `zh-CN`, English otherwise)
and preserve existing task IDs. Use [the template catalog](artifacts.md#templates) rather than inventing another document.

<a id="artifacts"></a>
## Artifacts, acceptance and recovery

A task starts at `T/task.md`; find its existing directory at resume. Every change should explain why it
exists, what was agreed, how to implement it and what actually happened. Small tasks use the corresponding
sections of `task.md`; long content may be split at the specified paths. If an Issue, PR, requirements
system or design document is authoritative, link its body instead of duplicating it for a filename.

Read the current authoritative records during the work and write results back there. Link the task to
actual commits or PRs. Reference real acceptance decisions, never invented ones; subsequent activities
read the accepted content. A revision that changes the basis of a decision requires addressing only the
affected decision again.

Use `T/task.md#handoff` or `T/handoff.md` with the handoff template for recovery across sessions. Verify
branch, worktree, review, CI and uncertain external actions before continuing, avoiding repeated deployment
or overwriting others' changes. Keep an actionable current restart point, not round-by-round chat summaries.
Native version history retains revisions. Preserve existing document language unless translation is requested.

<a id="design-detail"></a>
## Design, implementation and observable outcomes

Expand API, data, permission, UX, compatibility and failure behavior according to the change's actual
impact. Iterate prototypes in existing design tools, store accepted references and interaction requirements
in `T/task.md#spec` or `T/spec.md`, and hand them to implementation. Necessary local assets go in `T/assets/`;
link an existing design system instead of copying it. Not every change needs a new design tool. Verify
uncertain third-party behavior in actual documentation or a minimal isolated experiment, not guessed interfaces.

Defect tests must fail for the expected cause before the fix and pass afterward. Prefer committing the
reproducer first; reference an existing test revision when it already reproduces the problem. Existing
write restrictions or independent test-diff review protect the check's effectiveness. Record observations
in `T/task.md#verification` or `T/verification.md`. If reproduction fails, state the evidence gap and
investigate rather than fabricate red/green results. When requirements require a changed test expectation,
obtain the relevant decision; the author must not change acceptance and then declare the same issue resolved.

Verify UI in the running application, data restoration when rollback involves data, and adjacent callers
when shared logic changes. A wording change need not run unrelated suites, but executable commands written
in documentation still need to be checked. Product README, user-guide, API and architecture templates are
starters for actual documentation work, not a requirement to generate a documentation site.

<a id="autonomy"></a>
## Autonomous execution and staged adoption

With an explicit accepted plan, use the host's authorized automation for routine edits and checks without
waiting after every edit. Do not expand autonomy before shared instructions, runnable checks, permissions
and review exist. “Auto” does not mean bypassing permissions. Parallel worktrees follow the same boundaries;
review and integration capacity limits their number.

First establish foundations: intent storage, project context, skills, read-only planning, feedback checks
and action boundaries. Then connect dependencies: intent plus skills supports design; context supports
parallelism, and context plus feedback supports agent evaluations. Review reads context, rules and plans
and uses a reliable review configuration. Connect pipelines after review and action boundaries; connect
observation back to intent and verify rollback. Independent foundations can be established in parallel.
Record actual integration points at `.opensdlc/project.md#native`; required missing capabilities need
concrete follow-up tasks, not silent omission.

Adopt repetition as **manual run → reusable command → event trigger**. Events may be accepted intent or
specification, PR merge, alert or schedule. Read the accepted artifact before continuing. Do not install
an event bus or orchestration service by default. Unattended work proceeds, stops or escalates based on
native deterministic checks or independent review, never the author's self-reported confidence.

<a id="controls"></a>
## Prefer native controls

**Establish real boundaries, then choose the smallest implementation.** Document the boundary and actual
enforcement entry at `.opensdlc/operations.md#controls`, using the operations template. Reuse approval
already enforced by a deployment platform and checks already run by CI. Use a host hook, tool permission
or platform permission when an action must be prevented at execution time; after-the-fact CI cannot stand
in for having blocked a production write.

Version team-maintained settings in the repository. Administrators manage non-bypassable rules in the host
or deployment platform. Where stronger isolation is actually required, use existing capabilities according
to data and authority boundaries rather than copying an entire enterprise configuration:

- Limit commands and available tools; local configuration, arguments or retries must not bypass managed restrictions.
- Use real filesystem/network isolation, including protection from shell-based credential reads; a tool read restriction alone is not process isolation.
- When needed, constrain plugin sources, MCP services and supported versions, using existing central distribution for consistency.

Test both legitimate and denied operations and show the denial reason and authorization path. Use native
logs, not a duplicate logging system. If required isolation is unavailable, do not perform the restricted
action outside it. Consult current host documentation for settings; do not hard-code illustrative versions
or platform-specific fields into a generic workflow.

**Three separate concepts:** valid checks establish behavior, necessary authorization establishes authority,
and records describe what happened. “Allowed” in a document, a nonempty environment variable or a keyword
in a command is not an identity or approval result. Trusted systems enforce security boundaries; an
agent-editable local script is not absolutely non-bypassable. Language configuration selects new prose and new task names; it grants no authority.

<a id="eval-detail"></a>
## Evaluations and review in practice

Use `eval-suite.md` for `.opensdlc/evals/suite.md`; case/run documents follow the artifact catalog. Start
from real historical work and a small discriminating set, growing as needed. Do not pad a suite with
invented cases when budget is missing. Continuous CI or an explicit offline cadence must actually run;
material agent configuration releases need relevant results. Understand and review regressions rather than
lower standards, change expectations to hide failure or mark unrun work as successful.

Shared review rules use `review-policy.md` at `.opensdlc/review.md`. A task review uses the task section
or `task-review.md` at `T/review.md`, linking actual findings and their resolution. Fixing a PR and
requesting review are different actions: read an integration's actual contract before invoking it; do not
assume one comment command both reviews and edits code. An automated author submits fixes; the code owner
approves. Automated handling of comments does not grant self-approval. Continuous self-testing,
fresh-context acceptance and PR review are not interchangeable results.

For the PR body, use the existing repository template, or the bilingual `pull-request.md` starter when
none exists. Put the result on the hosting platform and link it from the task; do not save another `pr.md`.

<a id="operations"></a>
## Release and operational feedback

Reuse existing model access, CI, isolation and deployment tools; model access can use the organization's
existing cloud arrangement without mandating a provider. Shared instructions belong at
`.opensdlc/operations.md#delivery`. Use `release.md` for `.opensdlc/releases/<release-id>.md` and link it
from task delivery. Writes go through PRs, deployment interfaces are scoped by environment, and production
authorization is separate from routine development authority. Do not wrap an existing restricted deployment
interface in another MCP service; without permission, prepare and report remaining work only.

Rehearse rollback before incidents. Account for data recovery and compatibility with older code; the
presence of a rollback command is not a rehearsal. Query actual execution status. State the observation
window covered, and do not claim long-term stability without long-term evidence.

Monitoring and response belong at `.opensdlc/operations.md#observe`. Use justified thresholds or rolling
baselines, covering spikes and gradual drift. Averages, standard deviations and graduated control bands
are options when appropriate, not a mandated distribution or fixed multiplier for every metric. Distinguish
recording, diagnosis and bounded remediation: the model explains and recommends; deterministic detection
decides whether the underlying signal crossed its boundary.

Incidents, Issues and collaboration messages enter the same flow. Small clear issues can produce compact
PRs, but intent, design, verification and review remain readable; larger problems enter formal intent
intake. The team can correct diagnostic assumptions. Reply in the original thread with actual recovery
results. Diagnosis, recovery and postmortem share `.opensdlc/incidents/<incident-id>.md` using `incident.md`,
with incident evaluations preventing recurrence. Link fix intent, task and resulting release; keep an
existing incident system authoritative and use a local source pointer as needed.

“I will monitor” in a chat is not a service. Only an actually deployed scheduler, monitoring system or
controlled service can trigger future work. When not integrated, state the gap and responsible continuation
entry rather than claiming autonomous operational feedback is complete.

<a id="metrics"></a>
## Measures and improvement

These are observation points for improving a capability, not a per-task acceptance form. Read existing
Git, Issue, PR, CI, execution/OpenTelemetry, monitoring and incident data; do not invent unavailable numbers.
Record selected measures, sources and review cadence at `.opensdlc/operations.md#metrics` rather than build
per-task reporting.

| Capability | Process observations | Outcome observations |
| --- | --- | --- |
| Intent | Time from first request to recorded intent | Acceptance ratio; intent changes after design starts |
| Requirements and design | Intent-to-specification time | Specification rework after implementation starts |
| Implementation planning | First-attempt merge ratio; plan acceptance-to-merge time | Rework count; final change alignment with plan |
| Project context | Repeated mistakes despite existing instructions | Time to a new contributor's first merge |
| Skills | Delay from rule change to skill update | Related rule violations still found in review |
| Parallel work | Sustainable parallelism without quality loss; guidance/wait time | Merge throughput together with rework rate |
| Continuous feedback | First CI success ratio | Review time and change failures |
| Agent evaluations | Evaluation performance; incident-to-regression-case time | Regressions caught in CI versus missed in production |
| PR review | Time to first review; comments resolved by the agent | Defects/vulnerabilities caught before merge versus escaped |
| Action boundaries | Actual waiting at authorization points | Unauthorized production actions |
| Pipelines | Failed-build diagnoses completed without manual intervention | Existing delivery-effectiveness / DORA measures |
| Operational feedback | Anomaly-to-intent-queue time | Diagnosis-to-merged-fix ratio; incident recurrence |

<a id="platform"></a>
## Platform integration sources

For necessary organizational configuration, consult actual host documentation for onboarding,
configuration precedence, managed settings, permissions, sandboxing, hooks, skills/plugins distribution,
managed MCP, model/network access, monitoring and activity auditing. Start at [native integration points](artifacts.md#native).
Record what the project uses and test allowed/denied actions, rather than copying sample settings without
validating the target environment. Preserve native executable configuration syntax in both prose languages.
