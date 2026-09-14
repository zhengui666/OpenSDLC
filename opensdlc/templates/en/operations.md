<!-- Destination: .opensdlc/operations.md
Document only actual project controls and commands. This is a shared runbook, not an approval database. Add operational sections when those capabilities are in scope.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# Project operations

<a id="controls"></a>
## Action boundaries

| Restricted action | Native enforcement location | Responsible person / authorization route | Allowed continuation if blocked |
| --- | --- | --- | --- |
| {{action}} | {{control_location}} | {{authorization_route}} | {{continuation}} |

**Allowed / denied behavior actually tested:** {{control_checks}}

<a id="delivery"></a>
## Delivery and recovery

**Environments and autonomy boundaries:** {{environments}}

**Deploy / status / rollback commands, directories and interfaces:** {{deployment_commands}}

**Automation identity, isolation and credential source; never secret values:** {{automation}}

**Data migration, recovery and old-version compatibility:** {{data_recovery}}

**Rollback rehearsal location, actual result and cadence:** {{rehearsal}}

**Post-deploy behavior and observation criteria:** {{post_deploy}}

<a id="observe"></a>
## Observe and respond

**Signal, baseline and deterministic detection rule location:** {{signals}}

**Record / diagnose / bounded response and permitted runbooks:** {{response_levels}}

**Actual scheduler / webhook / service trigger:** {{triggers}}

**Service owner, on-call, triage and communication entry:** {{on_call}}

**Incident, fix task and permanent regression paths:** {{feedback}}

<a id="metrics"></a>
## Measures and improvement

**Selected process and outcome measures; existing data sources:** {{measures}}

**Owner, review cadence and actionable follow-up:** {{metrics_review}}
