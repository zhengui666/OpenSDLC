<!-- Destination: .opensdlc/evals/suite.md
Evaluate agent task performance, not just product unit tests. Reuse real tasks, existing runners and canonical reports. Do not invent sample counts or baselines.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# Agent evaluation suite

<a id="scope"></a>
## Purpose and responsibility

**Agent workflow and owner:** {{workflow_and_owner}}

**Relevant models, instructions, skills, hooks and tool configuration locations:** {{configuration}}

<a id="cases"></a>
## Representative cases

| Case / dataset location | Real source | Behavior / rule covered |
| --- | --- | --- |
| {{case_location}} | {{real_source}} | {{coverage}} |

<a id="execution"></a>
## Execution

**Exact non-interactive command, working directory and environment:** {{command}}

**Required access, isolation, budget and limits:** {{requirements}}

**Configuration-change trigger and scheduled / agreed offline cadence:** {{triggers}}

<a id="comparison"></a>
## Acceptance and comparison

**Acceptable results and runnable checks:** {{acceptance}}

**Accepted baseline and its actual configuration / report:** {{baseline}}

**Regression review and decision before configuration release:** {{regression_review}}

<a id="maintenance"></a>
## Maintenance

**Production incidents converted to permanent regression cases:** {{incident_cases}}

**Refreshing stale cases and reporting limitations:** {{maintenance}}
