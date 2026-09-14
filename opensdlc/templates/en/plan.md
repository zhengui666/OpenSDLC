<!-- Destination: .opensdlc/tasks/<task-id>/plan.md
Reuse the existing task ID. For a new task, read .opensdlc/config.json: zh-CN requires a Simplified Chinese name (修复登录超时); en, missing or English fallback requires an English name (fix-login-timeout). The directory, task_id and links must agree; do not rename on language changes.
Link from task.md#plan. Investigate without editing implementation first. Include only work needed to satisfy the accepted specification.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# {{task_title}} — implementation plan

<a id="basis"></a>
## Starting point

**Accepted intent and specification:** {{basis}}

**Inspected files, end-to-end flow and shared callers:** {{investigation}}

**Existing code / standard library / native features / dependencies to reuse:** {{reuse}}

<a id="steps"></a>
## Execution order

| Step | Exact paths and change | Dependency | Verification |
| --- | --- | --- | --- |
| {{step}} | {{paths_and_change}} | {{dependency}} | {{check}} |

<a id="risks"></a>
## Risks and alternatives

**Most likely breakage and highest-risk step:** {{risks}}

**Rejected alternatives and rationale:** {{alternatives}}

**Recovery / rollback when relevant:** {{recovery}}

<a id="parallel"></a>
## Independent work packages

**Only when useful: goal, input, owner, writable paths, isolation, checks and integration order:** {{work_packages}}

<a id="decision"></a>
## Engineering decision and deviations

**Actual acceptance and significant-risk consultation:** {{decision}}

**Current deviation and required specification decision:** {{deviations}}
