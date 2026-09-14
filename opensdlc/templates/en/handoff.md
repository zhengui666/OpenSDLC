<!-- Destination: .opensdlc/tasks/<task-id>/handoff.md
Reuse the existing task ID. For a new task, read .opensdlc/config.json: zh-CN requires a Simplified Chinese name (修复登录超时); en, missing or English fallback requires an English name (fix-login-timeout). The directory, task_id and links must agree; do not rename on language changes.
Link from task.md#handoff. Keep a current restart point, not a transcript. The receiving agent must verify the real workspace and remote state before continuing.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# {{task_title}} — handoff

<a id="goal"></a>
## Goal and decisions

**Task entry and agreed endpoint:** {{task_and_endpoint}}

**Accepted decisions and important constraints:** {{decisions}}

<a id="workspace"></a>
## Workspace

**Repository / worktree / branch and relevant changes:** {{workspace}}

**Other work to preserve:** {{preserve}}

<a id="progress"></a>
## Actual progress

**Completed work and verification references:** {{completed}}

**Remaining work, blockers and owners:** {{remaining}}

<a id="external"></a>
## External state

**PR / CI / review / deployment state to recheck:** {{remote_state}}

**Timed-out or uncertain writes; query before retry:** {{uncertain_actions}}

<a id="resume"></a>
## Resume

**First next action and exact commands / working directory:** {{resume_steps}}

**Required access and where to request it:** {{access}}
