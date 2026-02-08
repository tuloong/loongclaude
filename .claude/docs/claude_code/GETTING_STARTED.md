# Getting Started (Claude Code)

Upstream:
- Quickstart: https://code.claude.com/docs/en/quickstart
- Overview: https://code.claude.com/docs

## Prerequisites

- A Claude subscription (Pro/Max/Teams/Enterprise) or a Claude Console account
- A code project directory to run Claude Code in

## Install

Follow the official quickstart for the latest install methods:
- https://code.claude.com/docs/en/quickstart

Common install options (examples from the docs):

- macOS / Linux / WSL:
  - `curl -fsSL https://claude.ai/install.sh | bash`
- Windows PowerShell:
  - `irm https://claude.ai/install.ps1 | iex`
- Windows WinGet:
  - `winget install Anthropic.ClaudeCode`
- Homebrew:
  - `brew install --cask claude-code`

## First login

Start Claude Code, then log in:
- Run `claude`
- In the interactive session: `/login`

## Start a session

From your project root:
- `claude`

Then ask onboarding-style questions:
- “what does this project do?”
- “where is the main entry point?”
- “explain the folder structure”

## Make a first change safely

- Describe a small task: “add a hello world function to the main file”
- Review diffs and approve edits when prompted

## Essential commands

The quickstart highlights these as common entry points:
- `claude` (interactive)
- `claude "task"` (start interactive with a prompt)
- `claude -p "query"` (one-off, then exit)
- `claude -c` (continue most recent conversation in this directory)
- `claude -r` (resume a previous conversation)

For the full list: https://code.claude.com/docs/en/cli-reference
