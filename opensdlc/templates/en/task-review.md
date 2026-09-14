<!-- Destination: .opensdlc/tasks/<task-id>/review.md
Reuse the existing task ID. For a new task, read .opensdlc/config.json: zh-CN requires a Simplified Chinese name (修复登录超时); en, missing or English fallback requires an English name (fix-login-timeout). The directory, task_id and links must agree; do not rename on language changes.
Link from task.md#review. The PR platform remains authoritative for comments, approval and CI. An author's self-review is not independent review or human approval.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# {{task_title}} — review

<a id="scope"></a>
## Review basis

**PR and actual candidate revision:** {{candidate}}

**Reviewer / review type and applicable rules:** {{reviewer}}

**Intent, specification and plan references:** {{basis}}

<a id="findings"></a>
## Findings and resolution

| Finding / severity | Location and impact | Resolution / actual re-review |
| --- | --- | --- |
| {{finding}} | {{location_and_impact}} | {{resolution}} |

<a id="outcome"></a>
## Current outcome

**Latest checks and re-review references:** {{checks}}

**Unresolved findings:** {{unresolved}}

**Actual human approval or pending decision:** {{approval}}

**Recurring issues or stale context to correct:** {{learning}}
