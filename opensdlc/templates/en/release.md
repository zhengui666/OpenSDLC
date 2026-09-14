<!-- Destination: .opensdlc/releases/<release-id>.md
Preparation is not execution or authorization. Use one record for a release spanning several tasks. Link a canonical release system instead when it already holds this content.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# {{release_title}}

<a id="scope"></a>
## Release scope

**Related tasks / PRs and target environment:** {{scope}}

**Exact artifact / build / revision and current deployed target:** {{artifact}}

**Release owner and real authorization / pending authorization:** {{authorization}}

<a id="preparation"></a>
## Preparation

**Checks and reviews already completed; outstanding requirements:** {{readiness}}

**Deploy / status / rollback entry and shared runbook:** {{commands}}

**Migration risks, compatibility and recovery procedure:** {{migration}}

**Actual rehearsal and observation criteria:** {{rehearsal}}

<a id="execution"></a>
## Execution and observed state

**Actual action, actor, time and platform result:** {{execution}}

**Deployed version, behavior checks and current state:** {{state}}

**Observation window covered and remaining uncertainty:** {{observation}}

**Rollback or recovery performed, if any:** {{recovery}}

<a id="notes"></a>
## Release notes

**User-visible changes, fixes and breaking changes:** {{changes}}

**Required user action and known limitations:** {{user_action}}

<a id="follow-up"></a>
## Follow-up

**Unfinished items, owners and incident / task links:** {{follow_up}}
