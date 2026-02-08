# Command Reference (Claude Code)

Upstream:
- CLI reference: https://code.claude.com/docs/en/cli-reference

## Core CLI commands (high-level)

These are the core workflows highlighted in the CLI reference:
- `claude` — start interactive mode
- `claude -p "query"` — print mode (one-off), then exit
- `claude -c` — continue the most recent conversation in the current directory
- `claude -r "<session>" "query"` — resume by session/name
- `claude update` — update Claude Code

## Common flags (selected)

The CLI reference includes many flags; these are the ones most relevant to automation and workflow control:
- `--permission-mode <mode>` — start in a specific permission mode
- `--tools "..."` — restrict which built-in tools are available
- `--allowedTools "..."` / `--disallowedTools "..."` — allowlist/denylist tool patterns
- `--output-format <text|json|stream-json>` — choose output encoding for print mode
- `--json-schema <schema>` — validated JSON output (print mode)
- `--model <alias-or-full-model-id>` — select a model
- `--agents <json>` — define custom subagents dynamically for a session
- `--mcp-config <path-or-json>` — load MCP server configuration
- `--plugin-dir <dir>` — load plugins from a directory for this session

Always refer to the upstream CLI reference for the complete, up-to-date list:
- https://code.claude.com/docs/en/cli-reference

## Notes for automation

- Print mode (`-p`) is designed for headless scripting.
- `--output-format json` can make it easier to parse responses programmatically.
- `--agents` can be used to provide one-off, session-scoped subagents for automation.
