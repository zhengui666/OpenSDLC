<!-- Destination: .opensdlc/tasks/<task-id>/task.md
Reuse the existing task ID. For a new task, read .opensdlc/config.json: zh-CN requires a Simplified Chinese name (修复登录超时); en, missing or English fallback requires an English name (fix-login-timeout). The directory, task_id and links must agree; do not rename on language changes.
The default record for a task. Add sections as work reaches them; keep short tasks short. If a section has an authoritative external source or is split out, replace its body with a link and necessary local context.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# {{task_title}}

<a id="task"></a>
## Task

**Task ID:** {{task_id}}

**Original request / Issue / incident:** {{source}}

**Agreed endpoint and merge / release scope:** {{endpoint}}

<a id="intent"></a>
## Intent

**Problem, affected users/systems and desired outcome:** {{intent}}

**Scope, constraints and non-goals:** {{scope}}

**Open questions and requirements owner decision / actual reference:** {{intent_decision}}

<a id="spec"></a>
## Requirements and design

**Expected behavior and observable acceptance:** {{acceptance}}

**Relevant interface, data, UX, permissions, errors and compatibility:** {{design}}

**Conflicts, resolutions and decision to proceed:** {{design_decision}}

<a id="plan"></a>
## Implementation plan

**Inspected flow, callers and existing reuse points:** {{reuse}}

**Ordered changes, exact paths and checks:** {{steps}}

**Risks, alternatives and engineering decision:** {{plan_decision}}

<a id="verification"></a>
## Verification

**Implementation and environment actually checked:** {{checked_scope}}

**Commands / direct observations, actual results and native report links:** {{checks}}

**Defect reproduction before and after, where applicable:** {{regression}}

**Failures, unrun checks and remaining coverage:** {{verification_gaps}}

<a id="review"></a>
## Review

**PR / reviewer and review scope:** {{review_source}}

**Findings, resolutions, re-review and current CI:** {{review_results}}

**Outstanding findings and actual human approval / pending decision:** {{review_remaining}}

<a id="delivery"></a>
## Delivery

**Actual PR / merge / deployment entry and observed state:** {{delivery_result}}

**Release record, when a release is in scope:** {{release_reference}}

**Unfinished work and next action:** {{remaining_work}}

<a id="handoff"></a>
## Handoff

**Worktree / branch / uncommitted changes:** {{workspace}}

**Key decisions and current blockers:** {{handoff_context}}

**External actions to reconcile before retrying:** {{external_state}}

**Next action, resume commands and needed access:** {{resume}}
