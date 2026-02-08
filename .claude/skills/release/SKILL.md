---
name: release
description: Release prep workflow (notes, checklist, version bump guidance) using swarm-release-manager.
disable-model-invocation: true
---

Prepare a release without publishing.

## Steps

1) Draft release notes (swarm-release-manager)
- Delegate to `swarm-release-manager`.
- Require: version bump suggestion, release notes, and a checklist.

2) Update docs/changelog if needed (swarm-docs-writer)
- If documentation or changelog needs changes, delegate to `swarm-docs-writer`.

3) Final review (swarm-reviewer)
- Delegate to `swarm-reviewer` to ensure release notes and docs match the actual changes.
