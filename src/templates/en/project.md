<!-- Destination: .opensdlc/project.md
Keep the core context about one page. Link detailed sources instead of copying them. Record verified commands, not guesses.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# {{project_name}} — project context

<a id="purpose"></a>
## Purpose and architecture

**Purpose and users:** {{project_purpose}}

**Main components and real request/data flow:** {{architecture_summary}}

**Relevant packages and owners:** {{packages_and_owners}}

<a id="commands"></a>
## Working commands

| Purpose | Exact command and working directory | Healthy result |
| --- | --- | --- |
| {{command_purpose}} | {{command_and_directory}} | {{healthy_result}} |

<a id="conventions"></a>
## Conventions and recurring mistakes

**Reuse points and repository conventions:** {{repository_conventions}}

**Known pitfalls and corrections:** {{pitfalls}}

<a id="owners"></a>
## Responsibilities

**Requirements / engineering / code / release / service owners:** {{responsible_people}}

<a id="sources"></a>
## Authoritative sources

| Subject | Canonical path or URL | Owner |
| --- | --- | --- |
| {{source_subject}} | {{source_location}} | {{source_owner}} |

<a id="native"></a>
## Native integration points

| Capability | Actual path or managed entry | Discovery / execution check |
| --- | --- | --- |
| {{native_capability}} | {{native_location}} | {{native_check}} |

Document only active integrations; put missing required capabilities in a concrete follow-up task.
