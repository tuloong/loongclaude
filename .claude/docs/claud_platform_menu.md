# Primary Documentation Menu (Claude Platform + Claude Code)

This file is the primary, document-first index for this repository. Before developing or changing a module, read the relevant documentation linked here, then proceed with implementation.

## Document-first rule (mandatory)

When a task involves platform APIs, prompt optimization, model selection, token budgets, context windows, rate limits, tool use, structured outputs, sub-agents, skills, hooks, permissions, or Claude Code configuration:
- Read the relevant upstream docs first (or the local notes below if available).
- Summarize the key constraints/specs in `.claude/session_config.json` before coding.

## Sources (upstream, canonical)

- Claude Platform (API): https://platform.claude.com/docs/en/home
- Claude Code: https://code.claude.com/docs

## How to update

In Claude (chat) or Claude Code, run:

> Please visit `https://platform.claude.com/docs/en/home` and its core sub-pages (such as Prompt Engineering, Models, API Reference), extract all the core topics, and generate a Markdown format link menu document for me. The document should be categorized as 'Basic Concepts', 'Development Guidelines', and 'Performance Optimization', and retain the original URLs.

## Local docs (this repo)

- Directory index: [INDEX.md](INDEX.md)

Claude Code local notes:
- Overview: [claude_code/OVERVIEW.md](claude_code/OVERVIEW.md)
- Getting started: [claude_code/GETTING_STARTED.md](claude_code/GETTING_STARTED.md)
- Command reference: [claude_code/COMMAND_REFERENCE.md](claude_code/COMMAND_REFERENCE.md)
- Sub-agents: [claude_code/SUBAGENTS.md](claude_code/SUBAGENTS.md)
- Configuration: [claude_code/CONFIGURATION.md](claude_code/CONFIGURATION.md)
- Extensions: [claude_code/EXTENSIONS.md](claude_code/EXTENSIONS.md)
- Best practices: [claude_code/BEST_PRACTICES.md](claude_code/BEST_PRACTICES.md)

## Claude Platform — Basic Concepts

- Home: https://platform.claude.com/docs/en/home
- API overview: https://platform.claude.com/docs/en/api/overview
- Models API (reference): https://platform.claude.com/docs/en/api/models
- List models (reference): https://platform.claude.com/docs/en/api/models/list
- Get a model (reference): https://platform.claude.com/docs/en/api/models/retrieve
- Messages API (reference): https://platform.claude.com/docs/en/api/messages
- Token counting (guide): https://platform.claude.com/docs/en/build-with-claude/token-counting
- Count tokens in a message (reference): https://platform.claude.com/docs/en/api/messages/count_tokens

## Claude Platform — Development Guidelines

- Prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Long context prompting tips: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/long-context-tips
- Context windows (concepts + strategies): https://platform.claude.com/docs/en/build-with-claude/context-windows
- Extended thinking: https://platform.claude.com/docs/en/build-with-claude/extended-thinking
- Structured outputs (JSON schema): https://platform.claude.com/docs/en/build-with-claude/structured-outputs
- Tool use implementation: https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use

## Claude Platform — Performance Optimization

- Rate limits: https://platform.claude.com/docs/en/api/rate-limits
- Prompt caching: https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Batch processing: https://platform.claude.com/docs/en/build-with-claude/batch-processing
- Create a message batch (reference): https://platform.claude.com/docs/en/api/messages/batches/create

## Claude Code — Core Pages (upstream, canonical)

- Home: https://code.claude.com/docs
- Getting started (Quickstart): https://code.claude.com/docs/en/quickstart
- Command reference (CLI reference): https://code.claude.com/docs/en/cli-reference
- Sub-agents: https://code.claude.com/docs/en/sub-agents
- Agent teams: https://code.claude.com/docs/en/agent-teams
- Configuration (Settings): https://code.claude.com/docs/en/settings
- Permissions: https://code.claude.com/docs/en/permissions
- Hooks: https://code.claude.com/docs/en/hooks
- Skills: https://code.claude.com/docs/en/skills
- Best practices: https://code.claude.com/docs/en/best-practices
