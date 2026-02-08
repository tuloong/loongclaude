---
name: security
description: Security review workflow using swarm-security-reviewer with remediation guidance.
disable-model-invocation: true
---

Run a security-focused review on a change or feature.

## Steps

1) Security review (swarm-security-reviewer)
- Delegate to `swarm-security-reviewer`.
- Require: threat model, prioritized findings, and a verification plan.

2) Remediation (swarm-coder)
- If findings require code changes, hand off to `swarm-coder` with concrete remediation tasks.

3) Verify (swarm-tester)
- Delegate to `swarm-tester` to run tests and provide evidence that fixes work.
