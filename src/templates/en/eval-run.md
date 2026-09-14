<!-- Destination: .opensdlc/evals/runs/<run-id>.md
Use only when no complete canonical report exists. Link native run/configuration identifiers; do not build a separate fingerprint or log system.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# {{run_title}}

<a id="run"></a>
## Run scope

**Actual run ID / time and runner:** {{run}}

**Candidate configuration and accepted baseline references:** {{configurations}}

**Included cases, actual command and environment:** {{scope}}

<a id="results"></a>
## Actual results

| Case | Baseline result | Candidate result | Evidence / failure cause |
| --- | --- | --- | --- |
| {{case}} | {{baseline_result}} | {{candidate_result}} | {{evidence}} |

<a id="decision"></a>
## Comparison and review

**Regressions, improvements and noise:** {{comparison}}

**Reviewer and actual decision / pending decision:** {{decision}}

**Unrun cases, limits and next action:** {{limitations}}
