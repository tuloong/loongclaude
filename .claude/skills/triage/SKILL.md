---
name: triage
description: Incident and bug triage workflow using swarm-incident-triage and swarm-debugger.
disable-model-invocation: true
---

Triage an incident or production issue.

## Steps

1) Triage (swarm-incident-triage)
- Delegate to `swarm-incident-triage`.
- Provide logs, timestamps, symptoms, and recent changes if available.

2) Decide path (swarm-router)
- Use `swarm-router` to decide whether to focus on mitigation, rollback, or a fix.

3) Fix/verify (swarm-debugger → swarm-reviewer → swarm-tester)
- Debugger produces minimal repro and a fix.
- Reviewer provides LGTM or fix requests.
- Tester verifies with tests and repro steps.
