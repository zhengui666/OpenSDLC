<!-- Destination: .opensdlc/incidents/<incident-id>.md
Use one document for diagnosis, recovery and postmortem. Separate facts from hypotheses. Recovery is an observed result, not a command invocation.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# {{incident_title}}

<a id="impact"></a>
## Signal and impact

**Alert / report, actual trigger and baseline:** {{signal}}

**Affected users, services, duration and severity:** {{impact}}

**Service owner / on-call and response level:** {{owner}}

<a id="timeline"></a>
## Timeline

| Time and timezone | Fact / action | Evidence |
| --- | --- | --- |
| {{time}} | {{event}} | {{evidence}} |

<a id="diagnosis"></a>
## Diagnosis

**Confirmed facts and supporting signals:** {{facts}}

**Hypotheses, experiments and remaining questions:** {{hypotheses}}

**Root cause and contributing factors, or unknown:** {{root_cause}}

<a id="response"></a>
## Response and recovery

**Actual owner triage decision and authorized response:** {{decision}}

**Actions taken and current external state:** {{actions}}

**Metric recovery, user behavior and observation window:** {{recovery}}

**Communication thread and actual update:** {{communication}}

<a id="learning"></a>
## Prevention and follow-up

**Fix intent / task and resulting release:** {{fix}}

**Permanent regression case and actual check:** {{regression}}

**Monitoring / context / runbook improvement, owner and follow-up:** {{improvements}}
