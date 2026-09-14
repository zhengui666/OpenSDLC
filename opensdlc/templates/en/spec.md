<!-- Destination: .opensdlc/tasks/<task-id>/spec.md
Reuse the existing task ID. For a new task, read .opensdlc/config.json: zh-CN requires a Simplified Chinese name (修复登录超时); en, missing or English fallback requires an English name (fix-login-timeout). The directory, task_id and links must agree; do not rename on language changes.
Link from task.md#spec. Expand only affected aspects, but make expected and failing behavior unambiguous. Keep research and design decisions here rather than creating separate logs.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# {{task_title}} — requirements and design

<a id="basis"></a>
## Intent and constraints

**Accepted intent and applicable authoritative rules:** {{basis}}

**Scope and non-goals:** {{scope}}

<a id="acceptance"></a>
## Behavior and acceptance

| Scenario | Expected observable result | Verification approach |
| --- | --- | --- |
| {{scenario}} | {{expected_result}} | {{verification_method}} |

<a id="design"></a>
## Design

**Existing flow, reuse and intended change:** {{flow}}

**Interface, input/output and data contracts:** {{contracts}}

**Permissions, privacy and trust boundaries:** {{permissions}}

**UX, accessibility and accepted visual references:** {{ux}}

**Failure, concurrency, compatibility and migration behavior:** {{failure_behavior}}

<a id="decisions"></a>
## Trade-offs and decisions

**Verified research and evidence:** {{research}}

**Alternatives and chosen approach:** {{alternatives}}

**Conflicts, responsible owners and resolution:** {{conflicts}}

**Requirements acceptance, technical consultation and decision to build:** {{acceptance_decision}}
