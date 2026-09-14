---
name: "{{skill_name}}"
description: "{{trigger_description}}"
---

<!-- Destination: <active-native-skill-directory>/<skill-name>/SKILL.md
Create only for repeated, real knowledge or behavior. Replace all placeholders, keep the skill name equal to its directory name, and verify positive and negative trigger examples. Do not copy this template as another OpenSDLC entry.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# {{skill_title}}

<a id="scope"></a>
## Scope and authority

**Purpose, non-goals and rule owner:** {{purpose}}

**Authoritative inputs and rules:** {{sources}}

<a id="inputs"></a>
## Required context

**What to read and verify before acting:** {{inputs}}

<a id="procedure"></a>
## Procedure

1. {{read_and_understand}}
2. {{reuse_and_execute}}
3. {{verify_and_report}}

<a id="outputs"></a>
## Outputs

**Expected result, canonical destination and smallest applicable template:** {{outputs}}

<a id="language"></a>
## Document language

Read repository `.opensdlc/config.json`: missing file or `language` defaults to `en`; `zh-CN` selects Simplified Chinese. New document prose and new task IDs MUST use the resolved language: `修复登录超时` for Chinese, `fix-login-timeout` for English. Reuse existing task IDs unchanged. Keep fixed filenames, anchors and code identifiers unchanged; preserve existing document language unless translation is requested.

<a id="boundaries"></a>
## Boundaries and failure handling

**Permissions, non-goals and behavior on missing prerequisites:** {{boundaries}}

<a id="checks"></a>
## Trigger and behavior checks

**Real requests that must trigger and must not trigger:** {{trigger_examples}}

**Runnable / observable behavior checks and accepted results:** {{checks}}
