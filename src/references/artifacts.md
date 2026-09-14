# Artifact conventions

English · [简体中文](artifacts.zh-CN.md)

Keep workflow documents at the repository root under `.opensdlc/`, with fixed locations, one authoritative
body per subject and files created only when needed. The [core workflow](../SKILL.md) defines the work;
this document defines language, templates and destinations, not a requirement to fill every file.

<a id="root"></a>
## Root and identifiers

Use the active Git worktree root, discoverable with `git rev-parse --show-toplevel`; without Git, use the
explicitly established project root. Do not use the current shell subdirectory, another worktree or the
Skill installation directory. Packages in one repository share its root `.opensdlc/`; identify affected
packages inside the task.

Reuse an existing `<task-id>` unchanged. Before naming a **new task**, resolve the repository language
as described below; the name MUST follow that language, not the conversation or template-reading language:

| Resolved language | Required new task name | Example path |
| --- | --- | --- |
| `zh-CN` | A short Simplified Chinese task name | `.opensdlc/tasks/修复登录超时/task.md` |
| `en`, including the default and English fallback | A short English task name in lowercase kebab-case | `.opensdlc/tasks/fix-login-timeout/task.md` |

An Issue number or necessary technical name may accompany the task name, but must not replace it:
use `工单-128-修复登录超时` in Chinese or `issue-128-fix-login-timeout` in English, not a bare `issue-128`.
Keep the original external identifier in the source field; do not rename the external Issue or its ID.
The directory name, `{{task_id}}` and every task link must agree. A task ID must be one valid directory
name, never contain `/` or `\`, and never be `.` or `..`. Quote paths in shell commands.
Keep the same ID across sessions, branches, PRs and language changes. Do not rename or duplicate an
existing task when its ID uses another language; translating its prose does not rename its directory.
Add a source prefix or short suffix only for a real collision; do not build a numbering service.

Release, incident, case and run IDs are outside this task-language rule. Reuse their native identifiers
where available; their filesystem names use lowercase letters, digits, hyphens, underscores and dots,
never separators or standalone `.` / `..`. Keep the original external ID in the body. Use timestamps
only when distinct runs need them.

Below, `T` means `.opensdlc/tasks/<task-id>` and `L` means the selected `en` or `zh-CN`; neither is a shell
variable. `.opensdlc/...` paths are repository-relative. Template paths are Skill-relative. Ordinary
Markdown links are relative to the document containing them, so adjust links when filling a template.

<a id="language"></a>
## Repository language

The only language setting is `.opensdlc/config.json` in the active repository root:

```json
{
  "language": "en"
}
```

For Simplified Chinese:

```json
{
  "language": "zh-CN"
}
```

| Situation | Behavior |
| --- | --- |
| File absent, or valid JSON object without `language` | English prose and English new task IDs; do not create a file merely to restate the default |
| `language` is exactly `en` | Read `templates/en/`; write new prose and name new tasks in English |
| `language` is exactly `zh-CN` | Read `templates/zh-CN/`; write new prose and name new tasks in Simplified Chinese |
| Invalid JSON, a non-object root, or an unsupported / non-string value | Report the issue, leave the file untouched and use English for new prose and new task IDs; continue unrelated work |
| Config exists but cannot be read | Report the limitation and use the English default for new prose and new task IDs, without claiming the setting was read |
| User explicitly requests a repository language change | Update only `language`, preserving other content, when writing is authorized; use the new value for new documents and new task IDs; leave existing task IDs unchanged |
| Existing document uses another language | Preserve its language during edits; translate only when explicitly requested, in place rather than creating a second canonical copy |

An empty string, `null`, `zh`, `zh-cn` and `en-US` are not supported aliases. Unknown keys are not language
settings or authority; preserve them rather than inventing behavior. There is no environment override,
per-task language file, schema service, plugin or renderer. Do not add one for this preference.

Read the setting at task start/resume and again if it changes before creating a task or document.
In read-only mode, report the intended setting/path without writing or claiming persistence. Do not infer
a language change from the conversation. The setting governs new document prose and new task IDs,
not the language of chat. There is no separate task-ID language option.

**Scope:** new task IDs, new workflow documents, PR/release prose, and new product/native Markdown documents
created by OpenSDLC. Existing repository conventions and authoritative documents retain their language and
structure; report a relevant conflict instead of silently translating or overwriting them. Fixed directory
names such as `tasks`, filenames such as `task.md` and `spec.md`, existing paths, machine keys, code
identifiers, anchors, API fields, commands and quoted evidence remain unchanged. Generated documentation
is updated at its source, not hand-translated. Switching language neither bulk-translates existing content
nor renames existing tasks.

The package itself offers English `README.md`, `SKILL.md` and references, with complete `.zh-CN.md` reading
editions. Only root `SKILL.md` is a discovery entry. Project configuration selects writing templates and
which reference edition to read; it does not change the host UI or replace the installed `SKILL.md`.
Both template libraries stay in the Skill package; generated project documents use one language each.

<a id="layout"></a>
## Layout

```text
.opensdlc/
├── config.json                       # Optional: language only
├── project.md                        # Shared context and source/native entries
├── review.md                         # Shared review rules
├── operations.md                     # Controls, delivery, observation and metrics
├── tasks/<task-id>/
│   ├── task.md                       # Default single task record
│   ├── intent.md                     # Split only when needed
│   ├── spec.md
│   ├── plan.md
│   ├── verification.md
│   ├── review.md
│   ├── handoff.md
│   └── assets/                       # Necessary references and actual screenshots
├── evals/
│   ├── suite.md
│   ├── cases/<case-id>.md
│   └── runs/<run-id>.md
├── releases/<release-id>.md
└── incidents/<incident-id>.md
```

This is an address map, not an initialization checklist. Do not precreate directories, placeholder reports,
per-step state files, `current.md`, or parallel `.en.md` / `.zh-CN.md` task records. A typical small task
uses only `T/task.md`; shared records are read or updated only as needed.

<a id="template-use"></a>
## Use a template

Read the relevant template from `templates/L/` before creating its document. The existing canonical
source or repository template takes precedence; adapt the starter to fill actual gaps rather than replace
project conventions. This is ordinary Markdown editing, not an executable template engine.

`{{snake_case}}` tokens are authoring placeholders. Set `{{task_id}}` to the exact directory name selected
under [the task naming rules](#root), never a separately translated label. Fill other tokens with verified
information in the selected language. Remove instructional HTML comments and unused placeholder rows;
omit sections not yet needed. Keep explicit `<a id="..."></a>` anchors unchanged. Unknown facts must be marked as unknown,
pending or not run in the document language; do not turn prompts into invented results. YAML keys stay
unchanged; when filling quoted YAML values, escape quotes correctly or use a valid block scalar.

Section headings and field prompts are a scaffold, not a form that every task must complete. Short
sections can be a sentence. Do not omit an applicable requirement, risk, check or responsibility just to
shorten a template. Add domain detail only where needed; do not prebuild extensibility scaffolding.

Do not copy the entire template library into `.opensdlc/`. Load one locale and the relevant templates.
For existing documents, read their actual body and follow authoritative links, keeping the established
language. For a requested translation, translate all in-scope prose, retain paths/anchors/identifiers,
preserve actual evidence and do not change decisions or approval status.

<a id="templates"></a>
## Template catalog

Each row has a complete English and Simplified Chinese starter. `review-policy.md` is the shared policy;
`task-review.md` is a task review result. `agent-skill.md` is a starter for a new native skill, not another
OpenSDLC discovery entry. Files are created at the destination, not under their template-library paths.

| Document | Fixed destination | English | Simplified Chinese |
| --- | --- | --- | --- |
| Language configuration | `.opensdlc/config.json` | [config.json](../templates/en/config.json) | [config.json](../templates/zh-CN/config.json) |
| Project context | `.opensdlc/project.md` | [project.md](../templates/en/project.md) | [project.md](../templates/zh-CN/project.md) |
| Shared review policy | `.opensdlc/review.md` | [review-policy.md](../templates/en/review-policy.md) | [review-policy.md](../templates/zh-CN/review-policy.md) |
| Shared operations | `.opensdlc/operations.md` | [operations.md](../templates/en/operations.md) | [operations.md](../templates/zh-CN/operations.md) |
| Task entry | `T/task.md` | [task.md](../templates/en/task.md) | [task.md](../templates/zh-CN/task.md) |
| Intent | `T/task.md#intent` → `T/intent.md` | [intent.md](../templates/en/intent.md) | [intent.md](../templates/zh-CN/intent.md) |
| Requirements and design | `T/task.md#spec` → `T/spec.md` | [spec.md](../templates/en/spec.md) | [spec.md](../templates/zh-CN/spec.md) |
| Implementation plan | `T/task.md#plan` → `T/plan.md` | [plan.md](../templates/en/plan.md) | [plan.md](../templates/zh-CN/plan.md) |
| Verification | `T/task.md#verification` → `T/verification.md` | [verification.md](../templates/en/verification.md) | [verification.md](../templates/zh-CN/verification.md) |
| Task review | `T/task.md#review` → `T/review.md` | [task-review.md](../templates/en/task-review.md) | [task-review.md](../templates/zh-CN/task-review.md) |
| Handoff | `T/task.md#handoff` → `T/handoff.md` | [handoff.md](../templates/en/handoff.md) | [handoff.md](../templates/zh-CN/handoff.md) |
| Evaluation suite | `.opensdlc/evals/suite.md` | [eval-suite.md](../templates/en/eval-suite.md) | [eval-suite.md](../templates/zh-CN/eval-suite.md) |
| Evaluation case | `.opensdlc/evals/cases/<case-id>.md` | [eval-case.md](../templates/en/eval-case.md) | [eval-case.md](../templates/zh-CN/eval-case.md) |
| Evaluation run | `.opensdlc/evals/runs/<run-id>.md` | [eval-run.md](../templates/en/eval-run.md) | [eval-run.md](../templates/zh-CN/eval-run.md) |
| Release and release notes | `.opensdlc/releases/<release-id>.md` | [release.md](../templates/en/release.md) | [release.md](../templates/zh-CN/release.md) |
| Incident and postmortem | `.opensdlc/incidents/<incident-id>.md` | [incident.md](../templates/en/incident.md) | [incident.md](../templates/zh-CN/incident.md) |
| Native context entry | `AGENTS.md` / `CLAUDE.md` | [native-context.md](../templates/en/native-context.md) | [native-context.md](../templates/zh-CN/native-context.md) |
| New native skill | `.claude/skills/<skill-name>/SKILL.md` / `.agents/skills/<skill-name>/SKILL.md` | [agent-skill.md](../templates/en/agent-skill.md) | [agent-skill.md](../templates/zh-CN/agent-skill.md) |
| Reusable subagent | `.claude/agents/<agent-name>.md` | [subagent.md](../templates/en/subagent.md) | [subagent.md](../templates/zh-CN/subagent.md) |
| Product README | `README.md` | [readme.md](../templates/en/readme.md) | [readme.md](../templates/zh-CN/readme.md) |
| User guide | `docs/user-guide.md` | [user-guide.md](../templates/en/user-guide.md) | [user-guide.md](../templates/zh-CN/user-guide.md) |
| API reference | `docs/api.md` | [api-reference.md](../templates/en/api-reference.md) | [api-reference.md](../templates/zh-CN/api-reference.md) |
| Architecture overview | `docs/architecture.md` | [architecture.md](../templates/en/architecture.md) | [architecture.md](../templates/zh-CN/architecture.md) |
| Canonical-source pointer | the existing fixed document path | [source-link.md](../templates/en/source-link.md) | [source-link.md](../templates/zh-CN/source-link.md) |
| PR body | native PR body | [pull-request.md](../templates/en/pull-request.md) | [pull-request.md](../templates/zh-CN/pull-request.md) |

The arrow means “inline by default; separate file only when justified,” not “write both.” Product/native
paths are defaults only when no applicable existing location exists; preserve and register actual paths
in `.opensdlc/project.md#sources` or `#native`. Do not create an alternative because a template exists.

<a id="task"></a>
## Task records and splitting

Every development task starts at `T/task.md`. State its original source and endpoint—design only,
reviewable PR, merge or release. Necessary acceptance belongs in the relevant section or a link to the
actual decision, not a second approval record.

Stable task anchors are `intent`, `spec`, `plan`, `verification`, `review`, `delivery` and `handoff`.
Use `<a id="intent"></a>` before either English or Chinese headings. Add a section when work reaches it;
by the endpoint, disclose applicable unfinished work rather than implying completion through omission.

Split only when a body is long, needs independent review or repeated reference. Move it to the specified
file, replace the original section body with a link, and retain the anchor. The entry then leads to one
body. A link is not proof that the stage was completed. For example, in `task.md`:

```markdown
<a id="spec"></a>
## Requirements and design

See [the specification](spec.md).
```

Task delivery stays at `T/task.md#delivery` using the task template's delivery section. A formal release
uses the release template; a PR-only task does not need a release record. Design research, decisions,
work packages and diagnostic notes belong in specification/plan/verification sections. Do not add default
`research.md`, ADR, work-package or subagent report files. A genuinely independent subtask may have its own
task ID, linked to its parent.

For read-only work, provide the same structure in the response, identify the intended path and say it has
not been saved. Pure questions do not create task directories.

<a id="project-docs"></a>
## Shared project documents

`project.md` contains purpose, architecture, conventions, real build/test/lint commands, healthy outputs,
common mistakes and owners. Keep it compact. `#sources` registers actual authoritative requirements,
architecture, brand/UX, security, product docs, CI and monitoring sources. `#native` lists actual context,
skill, subagent, hook and pipeline entry points and whether discovery/execution was checked.

Shared `review.md` covers defects, security, intent/specification/plan consistency, design principles,
severity, exclusions, human responsibility and review-quality tuning. Existing policy remains authoritative;
use `source-link.md` when a fixed local pointer is needed.

Shared `operations.md` has stable anchors `controls`, `delivery`, `observe` and `metrics`: action boundaries
and authorization routes; environments and real deploy/status/rollback/data recovery; monitoring baseline,
deterministic detection, response levels, actual trigger and on-call; selected measures and review cadence.
This is not an approval database or a per-task metrics report.

Product guides, API docs and architecture stay at the registered product locations. The package's own
README, Skill, references and templates remain in the Skill installation, not the target `.opensdlc/`.

<a id="eval-docs"></a>
## Evaluations, releases and incidents

Evaluation setup uses `eval-suite.md` to point to real cases, acceptance checks, commands, agent
configurations, triggers, cadence, accepted baseline and owner. Only use Markdown case/run templates when
existing executable datasets and reports do not carry the content. The suite links those native paths;
do not duplicate datasets or export full logs.

A release record includes associated tasks, exact artifact/environment, actual authorization, preparation,
execution, status checks, rollback/rehearsal, migrations, observation and user-facing release notes.
Several tasks in one release share one record. Readiness is not deployment or release approval.

One incident record covers signals, impact, timeline, facts versus hypotheses, root cause, actual response
and recovery, triage decisions, fix intent, release, postmortem and permanent regression case. Link incident,
fix task and resulting release. Existing release/incident systems can retain the body; use a local pointer.

<a id="native"></a>
## Native integration points

Host-discovered files must stay where the host reads them. Preserve active locations; register exact paths
or managed entries in `.opensdlc/project.md#native`. Do not create unused host directories.

| Capability | Native location / rule |
| --- | --- |
| Claude Code context | Preserve existing `CLAUDE.md` or `.claude/CLAUDE.md`; root `CLAUDE.md` for a needed new entry |
| AGENTS.md context | Root `AGENTS.md`; preserve scoped subdirectory instructions |
| Claude Code skill | `.claude/skills/<skill-name>/SKILL.md` |
| Codex skill | `.agents/skills/<skill-name>/SKILL.md` |
| Claude Code subagent | `.claude/agents/<agent-name>.md`; the provided subagent frontmatter targets this host |
| Claude Code team settings / hooks | `.claude/settings.json` or the active managed settings, not a replacement under `.opensdlc/` |
| GitHub Actions | `.github/workflows/<workflow-name>.yml`; retain existing `.yaml` paths |
| Other hosts, CI, deployment, test/evaluation configuration | Verify the actual native contract and register the exact path or managed entry; do not guess |

Context, native skill and subagent **Markdown documents** have templates in both languages. Hook, CI,
permissions and deployment **executable configuration** use existing native files and current official
schemas; do not fabricate a supposedly portable configuration template. The shared operations template
carries their explanatory prose. Config keys and command syntax do not change with document language.

Use supported shared distribution across hosts rather than separate rule bodies. Have the coordinator
consolidate subagent results into task sections, avoiding concurrent edits to one shared record. While a
host enforces read-only planning, keep its draft in the host-permitted location and archive the accepted
plan after document writes are authorized.

Verify real context/skill/subagent discovery at adoption. Creating a file or registering a path does not
prove the host loaded it. Consult the [Agent Skills specification](https://agentskills.io/specification),
[Claude Code skills](https://code.claude.com/docs/en/skills),
[context](https://code.claude.com/docs/en/memory),
[subagents](https://code.claude.com/docs/en/sub-agents),
[settings](https://code.claude.com/docs/en/settings) and
[Codex skills](https://developers.openai.com/codex/skills/) for host contracts.

<a id="sources"></a>
## Authority, assets and persistence

When an existing Issue, PR, design system or document owns a subject, point to it using `source-link.md`
or the relevant task section. Read the actual source before working; a stale local summary is not the
latest requirement. Use native revision/commit/run references when available, without extra fingerprints.
If a source cannot be read, report the gap rather than silently elevating a stale copy.

Version durable workflow prose normally. Git or the source platform records authorship and revisions;
no per-file development diary. Each worktree writes its own files and merges them with the corresponding
changes. Update shared project rules only when necessary.

Save necessary design references and actual screenshots as `T/assets/<descriptive-name>.<ext>` and label
their purpose; references are not execution evidence. Release/incident-specific assets use
`.opensdlc/releases/<release-id>/assets/` and `.opensdlc/incidents/<incident-id>/assets/`. Link existing
platform artifacts instead of copying caches, full logs or large binaries. Never store credentials,
sensitive personal data or unsanitized production data in these documents.

Resume by reading the original `task.md` and its authoritative links, then check current branch,
workspace, CI, review and external actions. Titles or old completion claims do not replace facts.
When moving a canonical body, update links and preserve native history; do not leave two editable authorities.
