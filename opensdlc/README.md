# OpenSDLC

**A complete software delivery workflow for AI coding agents, from clear intent to verified delivery and operational feedback.**

English · [简体中文](README.zh-CN.md)

[Quickstart](#quickstart) · [Language](#language) · [Workflow](#workflow) · [Templates](#templates) · [Examples](#examples) · [Documentation](#docs)

OpenSDLC is an instruction-only Agent Skill. It connects requirements, design, implementation, testing,
review, release and maintenance using the tools your project already has. Work stays understandable to
the next developer or agent through stable records in the repository's `.opensdlc/` directory.

```text
Plan → Design → Build ⇄ Test → Deliver → Maintain
 ↑                                         │
 └──────── Intent from real feedback ───────┘
```

**Understand before editing.** Read the real flow, reuse existing capabilities and fix root causes.  
**Verify before reporting.** Distinguish implementation, passing checks, merged PRs and actual deployment.  
**Write once, find it again.** Fixed paths and bilingual templates keep records usable across sessions.

<a id="quickstart"></a>
## Quickstart

### Install the Skill

Copy the complete `opensdlc/` directory into your agent's project-level skill directory. Keep the
references and both template libraries alongside `SKILL.md`. No runtime, generator, background service
or new project dependency is required.

The [skills.sh](https://skills.sh) CLI can install it directly into the detected agent's skill directory:

```sh
npx skills add https://github.com/zhengui666/OpenSDLC --skill opensdlc
```

| Agent | Project installation | Explicit invocation |
| --- | --- | --- |
| [Claude Code](https://code.claude.com/docs/en/skills) | `.claude/skills/opensdlc/` | `/opensdlc` |
| [Codex](https://developers.openai.com/codex/skills/) | `.agents/skills/opensdlc/` | `$opensdlc` |

For a **new** Claude Code installation, run from the directory containing the unpacked `opensdlc/`:

```sh
PROJECT="/absolute/path/to/your-project"
mkdir -p "$PROJECT/.claude/skills"
cp -R opensdlc "$PROJECT/.claude/skills/"
```

For Codex, use `$PROJECT/.agents/skills/` instead. If the destination already exists, inspect and preserve
project-specific changes before replacing files. Use the native loader for other hosts; do not assume
every agent scans the same path. Without a loader, explicitly read `SKILL.md` and the resources it references.

### Start a task

Invoke OpenSDLC in the target repository and describe the outcome and delivery boundary:

```text
Use OpenSDLC to fix the login page remaining in a loading state after a request times out.
Inspect the actual request flow and existing tests, fix the root cause and add regression coverage.
Name the task using the repository language. Deliver a reviewable PR; do not merge or deploy.
```

The agent reads project instructions and relevant code, locates existing task work and uses the task
template at `.opensdlc/tasks/fix-login-timeout/task.md`. After necessary decisions, it implements,
verifies and addresses applicable review. English is the default for prose and new task IDs, even when
another language is used in chat. With `zh-CN`, the new task uses `.opensdlc/tasks/修复登录超时/task.md`.
Try a real small task to confirm discovery, document writing and actual checks; a copied directory alone
does not prove integration works.

<a id="language"></a>
## Language

**English by default. Simplified Chinese through one repository setting.**

For Chinese documents and new task IDs, create or edit `.opensdlc/config.json` at the **target repository root**:

```json
{
  "language": "zh-CN"
}
```

Use `"en"` for English. When the file or `language` is absent, no configuration is needed: English applies.
Ready-to-use examples: [English](templates/en/config.json) · [Simplified Chinese](templates/zh-CN/config.json).
Merge the setting into an existing file rather than overwrite unrelated fields.

The setting governs **new document prose and new task IDs**:

| Repository language | Required new task ID | Example specification path |
| --- | --- | --- |
| `zh-CN` | Simplified Chinese, such as `修复登录超时` | `.opensdlc/tasks/修复登录超时/spec.md` |
| `en`, absent configuration or English fallback | English, such as `fix-login-timeout` | `.opensdlc/tasks/fix-login-timeout/spec.md` |

An Issue number may accompany the name: `工单-128-修复登录超时` or `issue-128-fix-login-timeout`.
Fixed directory names such as `tasks`, filenames such as `spec.md`, anchors, config keys and executable
syntax stay unchanged. Existing tasks retain their IDs and paths even when the setting changes.
Existing documents keep their language unless translation is explicitly requested; no parallel copies
are generated and the installed Skill is not rewritten. Chat language is independent.

The package's default `README.md`, `SKILL.md` and references are English, with complete Chinese reading
editions. Root `SKILL.md` remains the only discovery entry. This is an OpenSDLC instruction convention,
not a claim that the host natively reads `.opensdlc/config.json`. The agent reads it as part of the workflow.
See [the exact language rules](references/artifacts.md#language), including unsupported values and read-only work.

<a id="workflow"></a>
## Workflow

| Stage | Agent responsibility | Useful output |
| --- | --- | --- |
| Plan | Clarify the problem, users, outcome, constraints and non-goals; obtain the relevant intent decision | Accepted intent |
| Design | Define requirements and design together; resolve conflicts and specify acceptance, interfaces, data, UX and failure behavior | Implementable specification |
| Build | Investigate read-only, reuse code, agree a plan, implement incrementally and isolate truly independent work | Current plan and implementation |
| Test | Run feedback checks, reproduce defects, inspect real behavior and evaluate relevant agent configuration changes | Actual verification and evaluation results |
| Deliver | Fix review findings and failing CI; obtain required review/authorization; deploy and verify rollback within scope | Actual PR, merge or release result |
| Maintain | Detect signals deterministically, diagnose, triage, fix, verify recovery and retain incident regressions | Operational learning and new intent |

Context, reusable skills, subagents, hooks and CI/CD support these stages. Use each capability when its
trigger applies: do not repeat onboarding per task, force parallel agents into sequential work or perform
production actions for a PR-only task. A required capability that lacks tools or access is unfinished,
not silently inapplicable.

Requirements owners decide intent/specification, engineering owners accept plans, code owners review,
and release owners authorize production. One person may hold several roles. Reuse clear decisions rather
than asking again per file or command; an agent does not grant itself approval.

<a id="templates"></a>
## Document templates

Every defined document type has a complete English and Simplified Chinese starter. They provide concrete
sections and prompts—not blank headings or prefilled success claims.

| Scope | Included starters |
| --- | --- |
| Shared project guidance | Project context, review policy and operations |
| Task delivery | Compact task, intent, requirements/design, plan, verification, task review and handoff |
| Agent evaluations | Suite, case and run result |
| Release and maintenance | Release preparation/execution/notes; incident diagnosis/recovery/postmortem |
| Native agent documents | `AGENTS.md` / `CLAUDE.md` context entry, new `SKILL.md`, reusable subagent |
| Product and collaboration | README, user guide, API reference, architecture, PR body and canonical-source pointer |

Start with [the template catalog](references/artifacts.md#templates), or open the default
[English task template](templates/en/task.md) / [Chinese task template](templates/zh-CN/task.md).
Use `{{snake_case}}` as writing prompts, replace them with facts, and remove unused prompts. There is no
template renderer to install. Existing canonical documents and repository-specific templates take precedence.

**Template availability is not an instruction to generate every document.** A small task normally needs
one `task.md`, with short sections added as work progresses. Split only for length, independent review or
reuse. Keep the stable entry linked to one authoritative body; do not create a second full copy.

<a id="artifacts"></a>
## Where work lives

**The Skill directory holds instructions and templates. The target repository's `.opensdlc/` holds work.**

```text
.opensdlc/
├── config.json                       # Optional language preference
├── project.md                        # Shared context and canonical sources
├── review.md                         # Shared review rules
├── operations.md                     # Controls, delivery, observation, metrics
├── tasks/<task-id>/
│   ├── task.md                       # Default single record
│   ├── spec.md                       # Only when split out
│   ├── plan.md                       # Only when split out
│   └── assets/                       # Necessary references / actual screenshots
├── evals/
│   ├── suite.md
│   ├── cases/<case-id>.md
│   └── runs/<run-id>.md
├── releases/<release-id>.md
└── incidents/<incident-id>.md
```

Intent, verification, task review and handoff also have specified split paths. The
[full artifact contract](references/artifacts.md) maps every document to its template and destination.
Folders are created on demand, not as empty scaffolding. Existing Issues, PRs, design tools, CI and incident
systems can remain authoritative; fixed local entries link them rather than copy their content.

Host-discovered files stay at their native locations. Product documentation stays in the existing product
layout. Markdown starters cover their prose; executable hooks, CI and permissions reuse actual native
configuration, not a fabricated universal configuration format.

<a id="examples"></a>
## Examples

### Deliver a feature

```text
Use OpenSDLC to add notification preferences to the settings page.
Read and reuse the account, permissions and settings modules.
Define acceptance and a plan, implement, verify and resolve review findings.
Follow the repository's document language setting. Deliver a reviewable PR, without merging or deploying.
```

### Resume work

```text
Use OpenSDLC to continue .opensdlc/tasks/fix-login-timeout/.
Read the task entry and handoff, then verify the workspace, remote PR and CI state.
Resume unfinished work at the original endpoint; do not create another task or rewrite existing records.
```

### Change document language

```text
Set this repository's OpenSDLC document language to Simplified Chinese in .opensdlc/config.json.
Use templates/zh-CN/ for new documents and Simplified Chinese names for new task IDs.
Preserve existing document languages, filenames and task IDs.
```

### Evaluate an agent change

```text
Use OpenSDLC to improve this repository's agent review instructions.
Read the current rules, representative tasks and accepted baseline, then run relevant evaluations.
Inspect regressions and false positives before submitting the configuration and actual results.
If execution is unavailable, report the gap; product unit tests do not replace agent evaluations.
```

<a id="faq"></a>
## FAQ

### Is this a new development platform?

No. OpenSDLC is Markdown instructions, references, templates and small JSON language examples. It reuses
Git, Issue/PR platforms, tests, CI, permissions, deployments and monitoring. It does not install a service,
provide external access or introduce a policy engine.

### Must every change create a full document set?

No. Use one task entry and the sections needed for understanding, verification and handoff. Existing
sources are linked. Keep applicable checks even when documentation is compact.

### Can work proceed autonomously?

Within accepted goals, plans and permissions. Material decisions, required human review and production
authorization still belong to responsible people. Skill instructions do not override real permissions.

### Does changing language translate the repository?

No. It selects new-document prose and the language of new task IDs. Existing tasks keep their IDs and
paths. Existing content is edited in its established language unless an in-place translation is requested.
Fixed filenames, code identifiers, anchors and native settings remain unchanged.

### Is execution guaranteed across agents?

No. The entry follows the [Agent Skills format](https://agentskills.io/specification), but actual execution
depends on the host, model, tools and project. Verify behavior in your environment. Unrun checks, absent
reviews and unfinished deployment/observation cannot be reported as successful.

<a id="docs"></a>
## Documentation

| Need | English | Simplified Chinese |
| --- | --- | --- |
| Lifecycle instructions | [SKILL.md](SKILL.md) | [SKILL.zh-CN.md](SKILL.zh-CN.md) |
| Language, templates and fixed artifact paths | [Artifact conventions](references/artifacts.md) | [文档约定](references/artifacts.zh-CN.md) |
| Automation, evaluations, review, release and feedback | [Engineering operations](references/operations.md) | [工程实践](references/operations.zh-CN.md) |

The package is organized as:

```text
opensdlc/
├── README.md
├── README.zh-CN.md
├── SKILL.md                          # The only discovery entry
├── SKILL.zh-CN.md                     # Complete Chinese reading edition
├── references/
│   ├── artifacts.md
│   ├── artifacts.zh-CN.md
│   ├── operations.md
│   └── operations.zh-CN.md
└── templates/
    ├── en/                           # Default document starters + config.json
    └── zh-CN/                        # Matching Chinese starters + config.json
```
