<!-- Destination: .opensdlc/evals/cases/<case-id>.md
Use only when an existing executable dataset does not already carry this case. Keep the task input distinguishable from the evaluator instructions; use sanitized data.
Replace placeholders with facts. Omit unused prompts, never required behavior. A template is not evidence that work ran. -->

# {{case_title}}

<a id="source"></a>
## Source and purpose

**Case ID and real task / incident source:** {{source}}

**Behavior or failure this case distinguishes:** {{purpose}}

<a id="setup"></a>
## Starting conditions

**Repository / fixture / starting state:** {{setup}}

**Allowed tools, environment and constraints:** {{environment}}

<a id="input"></a>
## Task input

```text
{{task_input}}
```

<a id="expectation"></a>
## Expected result

**Acceptable observable outcome:** {{expected}}

**Forbidden shortcuts and invalid outcomes:** {{invalid_outcomes}}

<a id="checks"></a>
## Runnable assessment

**Exact checks and expected success / failure criteria:** {{checks}}

**Necessary human judgment and limits:** {{judgment}}
