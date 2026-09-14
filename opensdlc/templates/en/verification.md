<!-- Destination: .opensdlc/tasks/<task-id>/verification.md
Reuse the existing task ID. For a new task, read .opensdlc/config.json: zh-CN requires a Simplified Chinese name (修复登录超时); en, missing or English fallback requires an English name (fix-login-timeout). The directory, task_id and links must agree; do not rename on language changes.
Link from task.md#verification. Record observations, not desired results. Zero tests, queued jobs, timeouts and unrun checks are not passes; link full reports instead of copying logs.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# {{task_title}} — verification

<a id="scope"></a>
## Checked implementation

**Commit / branch / relevant uncommitted changes or native build reference:** {{implementation}}

**Environment, configuration and time / run:** {{environment}}

**Acceptance covered:** {{acceptance}}

<a id="checks"></a>
## Actual checks

| Command or direct check | Result and relevant output | Report / evidence |
| --- | --- | --- |
| {{check}} | {{actual_result}} | {{evidence}} |

<a id="regression"></a>
## Regression and behavior

**Defect reproduced before the fix and expected failure cause:** {{before_fix}}

**Behavior after the fix and adjacent callers / flows:** {{after_fix}}

**Actual UI observations compared with accepted references:** {{visual_checks}}

**Reason for any changed test expectation and review:** {{test_changes}}

<a id="independent"></a>
## Independent verification

**Verifier, independent context, scope and actual result when required:** {{independent_result}}

<a id="gaps"></a>
## Remaining gaps

**Existing failures versus introduced regressions:** {{failures}}

**Unrun checks, limitations and next action:** {{gaps}}
