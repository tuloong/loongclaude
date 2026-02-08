# Sub-agents (Claude Code)

Upstream:
- Sub-agents: https://code.claude.com/docs/en/sub-agents
- CLI reference (agents JSON): https://code.claude.com/docs/en/cli-reference

## What sub-agents are

Sub-agents are specialized assistants that run in their own context window with their own:
- system prompt
- tool access
- permission mode

They’re useful for isolating work that would otherwise flood your main context (large code searches, test runs, log analysis) and for enforcing constraints (read-only, narrow tools, etc.).

## Built-in sub-agents

The sub-agents docs describe built-in agents such as:
- Explore (fast, read-only, good for codebase search)
- Plan (used in plan mode for research)
- general-purpose (full tools for multi-step tasks)

## Where sub-agents live (scope + precedence)

The docs describe multiple sub-agent scopes; higher priority wins when names conflict:
1) Session-scoped: `--agents` CLI flag (current session only)
2) Project-scoped: `.claude/agents/` (shared with the repo)
3) User-scoped: `~/.claude/agents/` (available across your projects)
4) Plugin-provided: plugin `agents/` directories (lowest)

## Sub-agent file format (project / user)

Sub-agents are Markdown files with YAML frontmatter + a Markdown body:

```yaml
---
name: my-agent
description: When Claude should use this agent
tools: Read, Glob, Grep
model: inherit
permissionMode: plan
---
```

The Markdown body becomes the sub-agent’s system prompt.

## Practical patterns

- Use read-only agents for investigation so your main session stays focused.
- Use specialized agents to enforce workflows (for example: review-only, test-only, refactor-only).
- Use hooks to enforce additional guardrails for a specific agent lifecycle.
