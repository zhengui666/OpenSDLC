# Optional task-board synchronization

Read this when the user has enabled synchronization to a specific connected board. It is an optional
projection of existing work, not a new authority, service, approval system or prerequisite for OpenSDLC.
Do not send repository or personal information to an unapproved destination. Keep source documents,
GitHub and the user's manual board decisions authoritative for their respective fields.

## Trigger in the workflow

The executing agent synchronizes immediately after the actual task record or verified state changes:

| OpenSDLC event | Board projection |
| --- | --- |
| Accept work | Ensure project, then create the task as pending or in_progress as actually started |
| Decompose work | Create real children under their parent, parents first, recursively |
| Start or change stage | Update stage in detail; retain the separate execution status |
| Meaningful progress or verification | Update only changed detail, next action and evidence |
| Encounter a blocker | blocked, the concrete blocker and next action |
| Pause / resume | paused / actual resumed status; preserve current stage |
| Deliver to the agreed endpoint | done only when that endpoint's checks actually passed; link evidence |

Stages are Plan, Design, Build, Test, Deliver and Maintain. They are NOT status values. For example,
`detail: "Stage: Test\nWaiting for the test environment"` and `status: "blocked"` can coexist. Update the
whole intended detail only when it is unlocked; do not append repeated stage logs or overwrite a manual
note. PR-only delivery does not mean merged or deployed. Do not mark the project done because one task
finished. Reconcile events serially per task with the latest authoritative work before replay; CAS protects
board revisions, not semantic ordering of old events. Never replay an old blocked event over later success.

The coordinator owns synchronization after delegated results are integrated. Workers report progress;
they do not race to rewrite a shared parent. Synchronization happens during actual agent execution, using
the host's existing authorized connector. Merely installing this Skill does not create a webhook, timer,
watcher or background process. If the agent stops, no future work is promised. Use an existing verified
host event integration only when separately configured and authorized.

## Identity and hierarchy

Record the chosen non-secret board provider, destination and stable project ID in the existing
`.opensdlc/project.md#native`. Reuse an existing mapping; do not identify a task by its mutable title.
Do not put a private destination or project facts into the distributed Skill. `.opensdlc/config.json`
remains the language setting; no extra configuration engine is required.

The board represents the project as a root node (`parentId: null`), tasks as its children, and arbitrary
subtask depth as further children. Each ID must be 1–100 ASCII letters, digits, `_` or `-`. Existing mapped
board IDs take precedence. For a new unmapped task, use the optional helper:

```sh
python3 /path/to/opensdlc/scripts/board_sync.py id project-example 'fix-login-timeout'
```

It hashes the stable project ID and original OpenSDLC task ID, including Chinese IDs, into a legal ID.
Store the mapping in the existing task record. Preserve it across titles, language changes, branches,
restarts and worktrees. Never change the source ID or salt the ID to evade a tombstone. A genuinely new
task needs its own identity. Reuse a real independent subtask's original task ID; for a plan subsection,
assign a stable source ID once and keep it with that subsection rather than deriving it from an index.
Keep the parent's ID explicitly. Missing or deleted parents stop child creation. Moving an existing node
is a separate decision, not an implicit consequence of a status update.

## Existing connector contract

Prefer the connected MCP tools:

- `board_read({})` returns `{board: {tasks: [...], events: [...]}, revision}`
- `board_update({revision, operation})` returns the updated board and incremented revision
- `operation` is `{action: "create" | "update", id, parentId?, patch}`
- `patch` contains only changed `title`, `status`, `detail`, `next`, `evidence`
- Status is `pending`, `in_progress`, `blocked`, `paused` or `done`
- Title is at most 160 characters; other text fields at most 5000
- Task records include `id`, `parentId`, those fields, `updatedAt`, `deletedAt`, and `locks: string[]`

1. Read the current board; reconcile the stable ID, all ancestors, deletedAt and field locks.
2. Omit unchanged fields and every manually locked field. If nothing remains, do not write.
3. Send one create/update with the exact read revision. Create parents before children; never replace
   the entire board. Do not send delete, restore, unlock, locks or deletedAt operations.
4. Verify the returned revision and values. Report skipped locks, tombstones and unverified writes
   separately from synchronization success.
5. On HTTP 409, reread. A tombstone, missing/deleted parent or lock is not a transient revision conflict.
   Recompute the delta against the new board; stop unchanged-revision rejections. Retry only a genuinely
   newer-revision, still-permitted delta, with a small bound, then report contention.
6. On timeouts or uncertain writes, read and reconcile before another attempt. If credentials, tools or
   access are absent, report **not synchronized** and continue independent engineering work. Record the
   pending synchronization in the existing handoff; never report a write that did not happen.

The optional `scripts/board_sync.py` implements the diff and CAS loop with injected `read()` and
`update(request)` adapters. It has no network access, credential handling or third-party dependencies.
Translate only a real conflict response into its `Conflict` exception; let authentication, permissions,
validation and transport failures remain explicit. The helper does not install or invoke MCP itself.

For an agent using MCP directly, save the read snapshot and one current event in host-permitted temporary
files, then run:

```sh
python3 /path/to/opensdlc/scripts/board_sync.py plan snapshot.json event.json
```

Example event (a current fact, not a historical log):

```json
{"id":"example-task","parentId":"project-example","patch":{"status":"blocked","detail":"Stage: Test\nTest environment unavailable","next":"Restore the test environment"}}
```

If the output contains `request`, pass that object unchanged to `board_update`. If `request` is null,
respect its outcome and do not improvise a privileged fallback. After a conflict, repeat the read and
planning steps; do not resend the old request. The `id` and `plan` commands only calculate: output is
NOT proof of a board write. A native MCP-capable agent may follow the same contract without Python.

## Optional HTTP host adapter

An already-authorized provider may expose the same contract via GET and POST at its verified `/api/sync`
endpoint; POST uses `{revision, operation}`. Keep any non-secret endpoint/provider configuration in the
host/project configuration, never baked into OpenSDLC. Use the provider's existing authentication through
the host and inject credentials only at runtime; never write them to source, task records or logs.

For an OpenAI Sites host specifically, first verify `get_site` reports owner-private access and the exact
existing site. Only when that response supplies its existing `siwc_bypass_bearer_token` may the host send
`OAI-Sites-Authorization: Bearer …` to that exact verified site. Do not print the token, follow redirects
with it, persist it, create credentials or reuse it for another origin. This optional host behavior is
not provided by the planner and must obey the host's permissions. Prefer MCP when available.

## Verification and limits

From the OpenSDLC source repository:

```sh
python3 -m unittest discover -s tests -v
```

The contract tests replay task acceptance, recursive decomposition, stage changes, blocking, pausing,
resumption and completion against an in-memory CAS server. They cover stable IDs, duplicate events,
field locks, tombstones, missing parents, conflicts, unknown outcomes and forbidden fields. They do not
prove any user's live destination is connected or that a host invoked the Skill.

At adoption, run an authorized real task event through the connected provider and inspect the returned
record and revision. Test real trigger discovery separately from planner unit tests. State what actually
ran: local contract replay, host-trigger evaluation and live destination verification are distinct checks.
