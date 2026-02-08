---
name: review
description: Structured code review workflow using swarm-reviewer (and optionally swarm-security-reviewer).
disable-model-invocation: true
---

Run a structured review.

## Steps

1) Primary review (swarm-reviewer)
- Delegate to `swarm-reviewer`.
- Require prioritized findings (Critical / High / Medium / Low) and concrete fixes.

2) Optional security pass (swarm-security-reviewer)
- If the change touches auth, permissions, input handling, file paths, network calls, or secrets, also delegate to `swarm-security-reviewer`.

3) Close the loop
- If changes are required, hand off to `swarm-coder` (or `swarm-debugger`) with an actionable fix list.
- If acceptable, require `LGTM` from `swarm-reviewer` and hand off to `swarm-tester` for verification.
