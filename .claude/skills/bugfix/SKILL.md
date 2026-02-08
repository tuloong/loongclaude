---
name: bugfix
description: Bugfix workflow (triage → reproduce → fix → review → verify) using project subagents.
disable-model-invocation: true
---

Run a bugfix workflow in Claude Code using subagents.

## Steps

1) Triage (swarm-incident-triage or swarm-router)
- If you have logs/symptoms, use `swarm-incident-triage` to summarize impact, evidence, hypotheses, and mitigations.
- Otherwise, use `swarm-router` to define repro steps and a plan.

2) Reproduce + fix (swarm-debugger)
- Delegate to `swarm-debugger`.
- Require: minimal repro, root cause with evidence, smallest safe fix, verification commands and results.

3) Review (swarm-reviewer)
- Delegate to `swarm-reviewer`.
- If not LGTM, hand back to `swarm-debugger` or `swarm-coder` with a prioritized fix list.

4) Verify (swarm-tester)
- Delegate to `swarm-tester` to run `python -m pytest` (or repo-equivalent).
- If failing, hand off to `swarm-debugger`.

## Handoff envelope (required)
```json
{
  "type": "handoff",
  "next_role": "Router|Coder|Reviewer|Tester",
  "summary": "Progress summary (done/todo/risks)",
  "next_instructions": "Actionable tasks for the next agent"
}
```
