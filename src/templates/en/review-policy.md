<!-- Destination: .opensdlc/review.md
Use shared rules across tasks. If a policy already exists, use the source-link template at this path instead of duplicating it.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# Project review policy

<a id="scope"></a>
## Scope and basis

**Code owner, technical owner and authoritative standards:** {{owners_and_sources}}

**Included code and explicitly excluded generated / already-checked content:** {{scope}}

<a id="focus"></a>
## Review focus

**Correctness, failure handling and regression risks:** {{correctness}}

**Security, privacy and permissions:** {{security}}

**Intent / specification / plan consistency; reuse and design principles:** {{design}}

**Test diff validity and documentation accuracy:** {{tests_and_docs}}

<a id="severity"></a>
## Severity and response

| Severity | Concrete definition | Required response / native enforcement |
| --- | --- | --- |
| {{severity}} | {{definition}} | {{response}} |

<a id="approval"></a>
## Review and approval

**Human review threshold and actual branch / platform settings:** {{human_threshold}}

**Fix, verify and request re-review procedure:** {{review_loop}}

<a id="quality"></a>
## Finding quality

**Quality owner, review cadence and noise controls:** {{quality_review}}

**Recurring issues to add to project context:** {{context_feedback}}
