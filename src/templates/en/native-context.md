<!-- Destination: AGENTS.md or CLAUDE.md (preserve an existing host-supported path)
Merge into the active native entry; do not replace existing scoped rules. Use one authoritative project context and avoid copying the whole OpenSDLC workflow here.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# Project instructions

<a id="context"></a>
## Project context

**Read the current shared context at:** {{project_context_path}}

**Relevant existing scoped instructions:** {{scoped_instructions}}

<a id="workflow"></a>
## Development workflow

Read the installed OpenSDLC entry at `{{opensdlc_skill_path}}` for lifecycle work. Read `.opensdlc/config.json` at the active repository root before creating a task or document; missing file or missing `language` means `en`, and `zh-CN` selects Simplified Chinese templates. New task IDs MUST use Simplified Chinese with `zh-CN` (修复登录超时), and English with `en` or English default/fallback (fix-login-timeout). Existing task IDs and fixed filenames remain unchanged. Preserve existing document language unless translation is requested. Reuse the existing task entry and native tests; do not create duplicate records.

<a id="boundaries"></a>
## Local constraints

**Project-specific constraints not already documented elsewhere:** {{local_constraints}}
