---
name: "{{agent_name}}"
description: "{{trigger_description}}"
tools: "{{native_tool_list}}"
---

<!-- Destination: .claude/agents/<agent-name>.md (adapt only to a verified native host contract)
This frontmatter targets Claude Code. Choose only the tools actually needed, using the host's supported names. Other hosts require their own verified configuration; do not assume this file enables an agent there.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# {{agent_title}}

<a id="role"></a>
## Role and boundaries

**One useful repeatable responsibility:** {{responsibility}}

**What this agent must not do:** {{non_goals}}

<a id="input"></a>
## Task input

**Accepted plan / work package, exact input and scope:** {{input}}

**Allowed paths, isolation and tool limits:** {{limits}}

<a id="procedure"></a>
## Procedure

1. Read the supplied plan and actual code or evidence.
2. {{perform_bounded_task}}
3. Verify the result using {{verification_method}}.
4. Return findings and evidence to the coordinator; do not write a second report or modify shared records concurrently.

<a id="output"></a>
## Return format

**Result, evidence, gaps and next action:** {{return_format}}

**Parent task destination for coordinator consolidation:** {{parent_destination}}

<a id="verification-role"></a>
## Verifier separation

When acting as a verifier, inspect and report; the author fixes the implementation. Read repository `.opensdlc/config.json` for document language and new task naming: `zh-CN` requires a Simplified Chinese task name; `en` or English default/fallback requires English. Reuse the assigned task ID; do not rename it on language changes. Do not grant permissions or claim approval from prose.
