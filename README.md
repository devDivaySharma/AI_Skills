# AI_Skills 🚀

> **Curated Collection of Universal Agent Skills for Antigravity, Claude Code, Cursor, and Modern AI Coding Agents.**

[![Antigravity Compatible](https://img.shields.io/badge/Antigravity-Ready-4285F4?style=flat-square&logo=google)](https://github.com/devDivaySharma/AI_Skills)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-D97706?style=flat-square)](https://github.com/devDivaySharma/AI_Skills)
[![Cursor](https://img.shields.io/badge/Cursor-Rules%20Supported-000000?style=flat-square)](https://github.com/devDivaySharma/AI_Skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

`AI_Skills` is an open catalog of battle-tested, modular skills that supercharge AI coding assistants. Built upon the **Universal Agent Skill Specification (UASS)**, each skill utilizes **progressive disclosure** (injecting lightweight triggers first and loading detailed runbooks only on demand) to minimize token consumption while maximizing agent reliability.

---

## 📦 Skills Catalog

| Skill | Category | Version | Triggers / Purpose | Runbook |
| :--- | :--- | :---: | :--- | :--- |
| **[`git-workflow`](./skills/git-workflow/)** | `developer-workflows` | `v1.0.0` | Interactive rebase, merge conflicts, worktrees, atomic commits, reflog recovery. | [SKILL.md](./skills/git-workflow/SKILL.md) |
| **[`pr-reviewer`](./skills/pr-reviewer/)** | `developer-workflows` | `v1.0.0` | 5-pillar diff audit (correctness, security, performance, tests, architecture) with prioritized blocker/warning tags. | [SKILL.md](./skills/pr-reviewer/SKILL.md) |
| **[`automated-testing`](./skills/automated-testing/)** | `developer-workflows` | `v1.0.0` | Test suite design, TDD workflows, runner auto-detection (Vitest/Jest/Pytest/Go), edge case matrices, and clean mocking. | [SKILL.md](./skills/automated-testing/SKILL.md) |
| **[`semantic-release`](./skills/semantic-release/)** | `developer-workflows` | `v1.0.0` | Conventional Commits validation, SemVer calculation, automated CHANGELOG compilation, and release tagging. | [SKILL.md](./skills/semantic-release/SKILL.md) |

---

## ⚡ Quick Start & Installation

The repository includes a zero-dependency CLI (`scripts/sync.py`) and bash installer (`scripts/install.sh`) to install skills into your preferred agent runtime in seconds.

### 1. Install to Antigravity (Global)
Installs into `~/.gemini/config/skills/`, making skills available across **all** your local projects:
```bash
./scripts/install.sh antigravity-global
```

### 2. Install to Antigravity (Current Workspace)
Symlinks skills into `./.agents/skills/` for team sharing via git:
```bash
./scripts/install.sh antigravity-workspace
```

### 3. Install to Anthropic Claude Code
```bash
# Global installation (~/.claude/skills/)
python3 scripts/sync.py install --target claude-global

# Workspace installation (./skills/)
python3 scripts/sync.py install --target claude-workspace
```

### 4. Export to Cursor Rules (`.cursor/rules/*.mdc`)
Converts skills into Cursor MDC rules with globs and frontmatter descriptions:
```bash
python3 scripts/sync.py install --target cursor
```

### 5. Consolidated Markdown Export (`AGENTS.md`)
Generates a single consolidated document for OpenAI Codex, ChatGPT, or custom agent contexts:
```bash
python3 scripts/sync.py export-md --output AGENTS.md
```

---

## 🛠️ CLI Reference (`scripts/sync.py`)

```bash
# List all skills with descriptions
python3 scripts/sync.py list

# Validate all skills against the specification
python3 scripts/sync.py validate

# Install specific skills only
python3 scripts/sync.py install --target antigravity-global --skills git-workflow pr-reviewer

# Copy files instead of symlinking (useful for standalone deployments)
python3 scripts/sync.py install --target antigravity-workspace --copy
```

---

## 📂 Repository Architecture

```text
AI_Skills/
├── AGENTS.md                   # Consolidated skills guide for agents
├── README.md                   # Repository guide and catalog
├── docs/
│   ├── SPECIFICATION.md        # Universal Agent Skill Specification (UASS)
│   └── CROSS_MODEL_GUIDE.md    # Multi-model integration reference
├── scripts/
│   ├── install.sh              # Quick installation shell script
│   └── sync.py                 # Cross-platform CLI (list, validate, install, export)
├── templates/
│   └── skill-template/         # Canonical starting template for new skills
│       └── SKILL.md
└── skills/
    ├── git-workflow/           # Advanced git operations & conflict resolution
    ├── pr-reviewer/            # Multi-pillar pull request review & security audit
    ├── automated-testing/      # Test harnesses, TDD, runner detection, mocking
    └── semantic-release/       # Conventional commits, SemVer & changelog generation
```

---

## ✍️ Creating New Skills

To contribute or create a new skill:

1. Duplicate the template directory:
   ```bash
   cp -r templates/skill-template skills/my-new-skill
   ```
2. Edit `skills/my-new-skill/SKILL.md`:
   - Set unique lowercase `name` (e.g. `docker-optimization`).
   - Write a clear `description` in third-person stating triggers.
   - Outline step-by-step procedures and boundary conditions.
3. Add helper scripts to `skills/my-new-skill/scripts/` (if applicable).
4. Add reference docs to `skills/my-new-skill/references/` for token-efficient deep reading.
5. Validate your skill:
   ```bash
   python3 scripts/sync.py validate
   ```

See the [Universal Agent Skill Specification](./docs/SPECIFICATION.md) for full design standards.

---

## 🤝 Contributing & License

Contributions, new skills, and platform integrations are welcome! Please ensure all PRs pass `python3 scripts/sync.py validate`.

Distributed under the [MIT License](LICENSE).