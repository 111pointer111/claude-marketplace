# AGENTS.md

## What this is

A Markdown-only Claude Code plugin marketplace. No build tools, no tests, no package manager, no runtime code. All content is `.md` files and `.json` metadata.

## Structure

Two parallel content types:

- **Plugins** — live at repo root (e.g. `socratic-teach/`). Each has `.claude-plugin/plugin.json` + `skills/<name>/SKILL.md`. The root `marketplace.json` is the index; add entries there when adding plugins.
- **Skills** — live under `skills/`. Each has `SKILL.md` (with YAML frontmatter) + `README.md`.

There is no `plugins/` directory despite what CLAUDE.md says. Plugins sit at the repo root.

## Adding a new Skill

1. Create `skills/<name>/SKILL.md` with this frontmatter:
   ```yaml
   ---
   name: <skill-name>
   description: <description>
   type: skill
   user-invocable: true
   argument-hint: '[<hint>]'
   ---
   ```
2. Create `skills/<name>/README.md`
3. If it needs API keys, add vars to `skills/.env.example`
4. SKILL.md must begin with env-check logic reading from `skills/.env`

## Adding a new Plugin

1. Create `<name>/.claude-plugin/plugin.json` (see `socratic-teach/.claude-plugin/plugin.json` for schema)
2. Create `<name>/skills/<skill>/SKILL.md`
3. Add entry to `marketplace.json` under `"plugins"`

## Env / API Keys

All keys centralized in `skills/.env` (gitignored). Template: `skills/.env.example`. Never commit `.env` files.

## Two Skill formats coexist

- **Standard** (`skills/*/SKILL.md`) — YAML frontmatter, env-check preamble, markdown logic
- **Manifest-based** (`skills/flutter-ios-code-review/`) — `manifest.json` + lowercase `skill.md`, no frontmatter

When creating new skills, use the standard SKILL.md format with frontmatter.

## Historical persona distiller output

`skills/historical-persona-distiller/output/` contains ~90+ auto-generated persona SKILL.md files. These are pipeline outputs, not hand-written. Don't manually edit them; fix the distiller skill instead.

## Conventions

- Primary language is Chinese (Simplified) for all content and docs
- `CLAUDE.md` is the authoritative project doc (in Chinese)
- No lint, typecheck, or test commands exist — content-only repo
- `.claude/settings.local.json` has MCP permissions (MiniMax tools)
- `minimax_model_skill` uses `mmx` CLI (`npm install -g mmx-cli`), not MCP
