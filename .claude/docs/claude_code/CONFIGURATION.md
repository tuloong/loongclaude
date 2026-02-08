# Configuration (Claude Code)

Upstream:
- Settings: https://code.claude.com/docs/en/settings
- Permissions: https://code.claude.com/docs/en/permissions
- Hooks: https://code.claude.com/docs/en/hooks

## Configuration scopes (where to put things)

Claude Code settings are scoped; more specific scopes take precedence:

- Managed (organization IT policy): system-level `managed-settings.json`
- User (you, across projects): `~/.claude/`
- Project (shared in repo): `.claude/`
- Local (you, this repo only, gitignored): `.claude/*.local.*`

## Files you will see most often

- `CLAUDE.md`
  - Instructions loaded at session start (project memory / rules)
- `.claude/settings.json`
  - Project-scoped settings shared with collaborators
- `.claude/settings.local.json`
  - Local overrides (not committed)
- `~/.claude/settings.json`
  - User defaults across repos

## Permissions (tools, files, domains)

Permissions are rule-based and evaluated in order: deny → ask → allow.

Key concepts from the permissions docs:
- Permission modes: `default`, `acceptEdits`, `plan`, `delegate`, `dontAsk`, `bypassPermissions`
- Permission rules use `Tool` or `Tool(specifier)` patterns
- Use deny rules to block access to secrets (like `.env`, `secrets/**`)

Docs:
- https://code.claude.com/docs/en/permissions

## Hooks (automation gates)

Hooks can run shell commands, prompt-based checks, or agent-based checks at lifecycle events.

Common events:
- `SessionStart`
- `PreToolUse`
- `PostToolUse`
- `PermissionRequest`
- `SubagentStart` / `SubagentStop`
- `PreCompact`

Docs:
- https://code.claude.com/docs/en/hooks

## Repo conventions (this project)

This repository uses project subagents and skills under:
- `.claude/agents/`
- `.claude/skills/`

See also:
- [swarm rules](../../../CLAUDE.md)
- project skill index: `/.claude/skills/workflow-index/`
