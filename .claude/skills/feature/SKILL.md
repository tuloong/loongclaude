---
name: feature
description: End-to-end feature workflow (requirements → design → implement → review → test) using project subagents.
disable-model-invocation: true
---

Run a full feature workflow in Claude Code using this repository’s subagents and the handoff envelope.

## Steps

1) Requirements (swarm-product)
- Use the `swarm-product` subagent to clarify scope and acceptance criteria.
- Capture the acceptance checklist in your main thread.

2) Design (swarm-architect)
- Use the `swarm-architect` subagent to propose a design, interfaces, and a migration plan.
- Choose a design and capture key decisions.

3) Routing (swarm-router)
- Use the `swarm-router` subagent to turn requirements + design into an execution plan.
- Router must output a handoff JSON pointing to the next role.

4) Implementation (swarm-coder)
- Delegate to `swarm-coder` to implement changes and update/add tests.
- Coder must output a handoff JSON to `Reviewer`.

5) Review (swarm-reviewer)
- Delegate to `swarm-reviewer` for security/correctness/maintainability review.
- If not LGTM, hand off back to `Coder` with a fix list.

6) Verification (swarm-tester)
- Delegate to `swarm-tester` to run tests and provide repro steps for any failures.
- If failing, hand off to `Coder`. If passing, hand off to `Reviewer` for final LGTM.

## Handoff envelope (required)
```json
{
  "type": "handoff",
  "next_role": "Router|Coder|Reviewer|Tester",
  "summary": "Progress summary (done/todo/risks)",
  "next_instructions": "Actionable tasks for the next agent"
}
```
