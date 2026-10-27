# Cross-Model Compatibility Guide

This guide details how `AI_Skills` can be consumed across different agent environments, IDEs, and LLM architectures.

---

## 1. Google Antigravity

Antigravity natively implements the progressive disclosure skill standard.

### Installation
- **Global Installation** (available across all projects on your machine):
  ```bash
  python3 scripts/sync.py install --target antigravity-global
  # Symlinks to ~/.gemini/config/skills/<skill-name>
  ```
- **Workspace-Level Installation** (checked into your project VCS):
  ```bash
  python3 scripts/sync.py install --target antigravity-workspace
  # Symlinks to .agents/skills/<skill-name>
  ```

Antigravity will automatically index all installed skills and load their full `SKILL.md` dynamically whenever the user prompt triggers their description.

---

## 2. Anthropic Claude Code

Claude Code detects skills located in `~/.claude/skills/` or a workspace `./skills/` directory.

### Installation
- **Global**:
  ```bash
  python3 scripts/sync.py install --target claude-global
  # Symlinks to ~/.claude/skills/<skill-name>
  ```
- **Workspace**:
  ```bash
  python3 scripts/sync.py install --target claude-workspace
  # Symlinks to ./skills/<skill-name>
  ```

---

## 3. Cursor & Windsurf

Cursor uses rule files in `.cursor/rules/*.mdc`. The sync tool translates each skill into an MDC rule file with YAML frontmatter.

### Installation
```bash
python3 scripts/sync.py install --target cursor
# Generates .cursor/rules/<skill-name>.mdc
```

---

## 4. OpenAI Codex, ChatGPT, & Custom Agent Runtimes

For environments that ingest a single project instruction file (e.g. `AGENTS.md` or system prompt context):

### Consolidated Markdown Export
```bash
python3 scripts/sync.py export-md --output AGENTS.md
```
This merges all active skills and catalog summaries into a single comprehensive `AGENTS.md` file suitable for injection into system prompts or repository root guidelines.
