# Universal Agent Skill Specification (UASS)

Version: 1.0.0  
Status: Standard

## 1. Overview
The **Universal Agent Skill Specification (UASS)** establishes a portable, deterministic format for packaging domain knowledge, runbooks, executable scripts, and references for AI coding agents and autonomous LLM systems.

---

## 2. Directory Layout

Every skill must be packaged inside its own directory within `skills/<skill-name>/`:

```text
skills/<skill-name>/
├── SKILL.md              # Mandatory: Core entry point with frontmatter & steps
├── scripts/              # Optional: Executable helpers (bash, python, node)
│   └── helper.sh
├── references/           # Optional: Deep architectural docs & cheatsheets
│   └── guide.md
└── examples/             # Optional: Concrete input/output samples and walkthroughs
    └── walkthrough.md
```

---

## 3. The `SKILL.md` File

### 3.1 YAML Frontmatter (Mandatory)
Every `SKILL.md` MUST begin with a valid YAML frontmatter block enclosed by `---`:

```yaml
---
name: my-specialized-skill
description: >-
  Use this skill when the user asks to perform X, debug Y, or automate Z.
  State trigger conditions clearly and concisely in third-person.
version: 1.0.0
author: Author Name
category: developer-workflows
compatibility:
  antigravity: ">=1.0"
  claude-code: ">=1.0"
  cursor: ">=0.40"
  openai-agents: "universal"
tags:
  - tag1
  - tag2
---
```

#### Field Requirements:
- **`name`** *(string, required)*: Lowercase letters, digits, and hyphens (`[a-z0-9-]+`). Must match the parent directory name.
- **`description`** *(string, required)*: The summary injected into the agent's index. The agent reads this to decide whether to activate the skill. Must clearly state **what** the skill does and **when** it should be triggered.
- **`category`** *(string, recommended)*: Category grouping (e.g. `developer-workflows`, `ai-tooling`, `cloud-infra`).
- **`version`** *(string, recommended)*: SemVer version string (e.g. `1.0.0`).

### 3.2 Body Structure
The Markdown body should be organized logically:
1. **Overview**: Concise explanation of the capability.
2. **When to Activate**: Clear bullet points of positive triggers and out-of-scope boundaries.
3. **Core Principles / Decision Framework**: High-level heuristics the agent must follow.
4. **Step-by-Step Instructions**: Sequential, unambiguous workflow steps.
5. **Helper Scripts & Links**: Relative Markdown links to `./scripts/`, `./references/`, and `./examples/`.

---

## 4. Progressive Disclosure & Token Efficiency

To prevent blowing out the agent's context window:
1. **Compact Indexing**: The agent only ingests the `name` and `description` until the skill is triggered.
2. **On-Demand Reference**: Heavy tables, cheatsheets, and voluminous examples must live in `references/` or `examples/`, linked relatively. The agent only reads them if needed.
3. **Executable Scripts**: Pack complex terminal commands into self-contained scripts in `scripts/` instead of cluttering the prompt with fragile, copy-pasted multi-line shell snippets.
