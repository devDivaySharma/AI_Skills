#!/usr/bin/env python3
"""
sync.py - Cross-Platform Skill Sync & Installer for AI Agents
Supports:
  - Antigravity (Global: ~/.gemini/config/skills/, Workspace: .agents/skills/)
  - Claude Code (Global: ~/.claude/skills/, Workspace: ./skills/)
  - Cursor (.cursor/rules/*.mdc)
  - Universal AGENTS.md / CLAUDE.md generator
"""

import os
import sys
import argparse
import shutil
import re
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

def parse_frontmatter(file_path):
    """Extract YAML frontmatter fields using standard regex without PyYAML dependency."""
    content = file_path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return {}, content

    yaml_block = match.group(1)
    body = content[match.end():]
    data = {}

    current_key = None
    multiline_val = []

    for line in yaml_block.splitlines():
        # Multiline string continuation (description: >-)
        if current_key and (line.startswith("  ") or line.startswith("\t")):
            multiline_val.append(line.strip())
            continue
        elif current_key and multiline_val:
            data[current_key] = " ".join(multiline_val)
            current_key = None
            multiline_val = []

        # Key-value pair
        kv_match = re.match(r"^([a-zA-Z0-9_-]+):\s*(.*)$", line)
        if kv_match:
            key, val = kv_match.group(1), kv_match.group(2).strip()
            if val in (">-", ">", "|"):
                current_key = key
                multiline_val = []
            else:
                data[key] = val.strip("'\"")

    if current_key and multiline_val:
        data[current_key] = " ".join(multiline_val)

    return data, body

def get_available_skills():
    """Scans the skills directory and loads metadata for each skill."""
    skills = {}
    if not SKILLS_DIR.exists():
        return skills

    for child in sorted(SKILLS_DIR.iterdir()):
        if child.is_dir():
            skill_md = child / "SKILL.md"
            if skill_md.exists():
                meta, body = parse_frontmatter(skill_md)
                name = meta.get("name", child.name)
                skills[name] = {
                    "dir": child,
                    "skill_md": skill_md,
                    "name": name,
                    "description": meta.get("description", "No description provided."),
                    "version": meta.get("version", "1.0.0"),
                    "category": meta.get("category", "general"),
                    "author": meta.get("author", "Unknown"),
                    "body": body,
                }
    return skills

def cmd_list(args):
    """List available skills."""
    skills = get_available_skills()
    if not skills:
        print("No skills found in skills/ directory.")
        return 0

    print("================================================================================")
    print("                     AVAILABLE AI AGENT SKILLS CATALOG                          ")
    print("================================================================================")
    print(f"{'SKILL NAME':<24} {'CATEGORY':<22} {'VERSION':<10} {'DESCRIPTION'}")
    print("-" * 80)
    for name, info in skills.items():
        desc = info['description']
        if len(desc) > 60:
            desc = desc[:57] + "..."
        print(f"{name:<24} {info['category']:<22} {info['version']:<10} {desc}")
    print("================================================================================")
    print(f"Total skills available: {len(skills)}\n")
    return 0

def cmd_validate(args):
    """Validate all skills for standard compliance."""
    skills = get_available_skills()
    errors = 0
    print("Validating skills compliance...")

    for name, info in skills.items():
        issues = []
        if not re.match(r"^[a-z0-9-]+$", name):
            issues.append(f"Invalid name '{name}': Must be lowercase alphanumeric with hyphens.")
        if not info["description"] or info["description"] == "No description provided.":
            issues.append("Missing or empty 'description' in frontmatter.")
        if not (info["dir"] / "SKILL.md").exists():
            issues.append("Missing SKILL.md")

        if issues:
            print(f"❌ {name}:")
            for iss in issues:
                print(f"   - {iss}")
            errors += 1
        else:
            print(f"✅ {name} (v{info['version']}, {info['category']}) - Valid")

    if errors > 0:
        print(f"\nValidation failed with {errors} issue(s).")
        return 1
    print("\nAll skills passed validation successfully!")
    return 0

def cmd_install(args):
    """Install or sync skills to target directory or format."""
    skills = get_available_skills()
    selected_names = args.skills if args.skills else list(skills.keys())

    # Resolve target directory based on platform option
    target_type = args.target
    dest_dir = None
    mode = "symlink" if args.symlink else "copy"

    home = Path.home()
    cwd = Path.cwd()

    if target_type == "antigravity-global":
        dest_dir = home / ".gemini" / "config" / "skills"
    elif target_type == "antigravity-workspace":
        dest_dir = cwd / ".agents" / "skills"
    elif target_type == "claude-global":
        dest_dir = home / ".claude" / "skills"
    elif target_type == "claude-workspace":
        dest_dir = cwd / "skills"
    elif target_type == "cursor":
        dest_dir = cwd / ".cursor" / "rules"
    elif target_type == "custom":
        if not args.path:
            print("Error: --path required when target is 'custom'.")
            return 1
        dest_dir = Path(args.path)

    print(f"Target Platform : {target_type}")
    print(f"Destination Path: {dest_dir}")
    print(f"Install Mode    : {mode}")
    print("-" * 60)

    dest_dir.mkdir(parents=True, exist_ok=True)

    installed_count = 0
    for name in selected_names:
        if name not in skills:
            print(f"⚠️  Skill '{name}' not found in catalog, skipping.")
            continue

        skill_info = skills[name]
        src_path = skill_info["dir"]

        if target_type == "cursor":
            # Generate .cursor/rules/<skill-name>.mdc
            rule_file = dest_dir / f"{name}.mdc"
            rule_content = f"""---
description: {skill_info['description']}
globs: *
---

{skill_info['body']}
"""
            rule_file.write_text(rule_content, encoding="utf-8")
            print(f"  + Generated Cursor rule: {rule_file.name}")
            installed_count += 1
        else:
            # Skill directory copy or symlink
            target_skill_dir = dest_dir / name
            if target_skill_dir.exists() or target_skill_dir.is_symlink():
                if target_skill_dir.is_symlink() or target_skill_dir.is_dir():
                    if target_skill_dir.is_symlink():
                        target_skill_dir.unlink()
                    else:
                        shutil.rmtree(target_skill_dir)

            if mode == "symlink":
                try:
                    target_skill_dir.symlink_to(src_path.resolve(), target_is_directory=True)
                    print(f"  + Symlinked: {name} -> {target_skill_dir}")
                    installed_count += 1
                except OSError as e:
                    print(f"  ! Symlink failed ({e}), falling back to copy.")
                    shutil.copytree(src_path, target_skill_dir)
                    print(f"  + Copied: {name} -> {target_skill_dir}")
                    installed_count += 1
            else:
                shutil.copytree(src_path, target_skill_dir)
                print(f"  + Copied: {name} -> {target_skill_dir}")
                installed_count += 1

    print("-" * 60)
    print(f"Successfully installed/synced {installed_count} skill(s) into {dest_dir}\n")
    return 0

def cmd_export_markdown(args):
    """Consolidate skills into a single AGENTS.md or CLAUDE.md file."""
    skills = get_available_skills()
    out_file = Path(args.output)
    print(f"Generating consolidated guide to {out_file}...")

    content = [
        "# Agent Skills & Operational Workflows",
        "",
        "> This document is automatically generated by AI_Skills sync tool.",
        "> It injects specialized operational runbooks directly into your agent's context.",
        "",
        "## Table of Active Skills",
        "",
        "| Skill | Category | Description |",
        "| :--- | :--- | :--- |"
    ]

    for name, info in skills.items():
        content.append(f"| **`{name}`** | `{info['category']}` | {info['description']} |")

    content.append("\n---\n")

    for name, info in skills.items():
        content.append(f"## Skill: {name} (v{info['version']})")
        content.append(f"**Description**: {info['description']}\n")
        content.append(info["body"].strip())
        content.append("\n---\n")

    out_file.write_text("\n".join(content), encoding="utf-8")
    print(f"Successfully generated {out_file} ({len(skills)} skills included).")
    return 0

def main():
    parser = argparse.ArgumentParser(description="Universal AI Agent Skills Sync & CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # list
    subparsers.add_parser("list", help="List available skills in repository")

    # validate
    subparsers.add_parser("validate", help="Validate skills for standard compliance")

    # install
    install_parser = subparsers.add_parser("install", help="Install or sync skills to a target platform")
    install_parser.add_argument(
        "--target",
        choices=[
            "antigravity-global",
            "antigravity-workspace",
            "claude-global",
            "claude-workspace",
            "cursor",
            "custom",
        ],
        default="antigravity-global",
        help="Target platform environment (default: antigravity-global)",
    )
    install_parser.add_argument("--skills", nargs="+", help="Specific skill names to install (default: all)")
    install_parser.add_argument("--path", help="Destination path if target is 'custom'")
    install_parser.add_argument("--symlink", action="store_true", default=True, help="Use symlinks (default: True)")
    install_parser.add_argument("--copy", dest="symlink", action="store_false", help="Copy files instead of symlink")

    # export-md
    export_parser = subparsers.add_parser("export-md", help="Export all skills to a consolidated markdown file")
    export_parser.add_argument("--output", default="AGENTS.md", help="Output file path (default: AGENTS.md)")

    args = parser.parse_args()

    if args.command == "list":
        return cmd_list(args)
    elif args.command == "validate":
        return cmd_validate(args)
    elif args.command == "install":
        return cmd_install(args)
    elif args.command == "export-md":
        return cmd_export_markdown(args)
    return 0

if __name__ == "__main__":
    sys.exit(main())
