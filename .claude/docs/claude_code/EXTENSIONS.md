# Extending Claude Code (Skills, Hooks, Plugins)

Upstream:
- Skills: https://code.claude.com/docs/en/skills
- Hooks: https://code.claude.com/docs/en/hooks
- Settings (scope + configuration): https://code.claude.com/docs/en/settings

## Skills

Skills are reusable prompts/workflows stored as:
- Project: `.claude/skills/<skill-name>/SKILL.md`
- User: `~/.claude/skills/<skill-name>/SKILL.md`

Skills can be:
- reference content (knowledge Claude applies inline)
- task content (step-by-step workflow; often `disable-model-invocation: true`)

Docs: https://code.claude.com/docs/en/skills

## Hooks

Hooks are deterministic automation steps that run at lifecycle events (tool calls, session start/end, etc.) and can:
- block risky actions (PreToolUse)
- enforce checks (TaskCompleted, Stop, TeammateIdle)
- inject context (SessionStart)

Docs: https://code.claude.com/docs/en/hooks

## Plugins

Claude Code supports plugins that can bundle skills, agents, hooks, and MCP servers.

Start from settings documentation for plugin configuration:
- https://code.claude.com/docs/en/settings
