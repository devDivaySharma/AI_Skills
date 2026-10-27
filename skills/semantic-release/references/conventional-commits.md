# Conventional Commits Reference Specification

The Conventional Commits specification is a lightweight convention on top of commit messages, providing an easy set of rules for creating an explicit commit history.

## Structure

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Commit Types

| Type | Purpose | SemVer Impact |
| :--- | :--- | :--- |
| **`feat`** | Introduces a new user-facing or API feature | `MINOR` |
| **`fix`** | Patches a bug in codebase | `PATCH` |
| **`perf`** | Improves performance | `PATCH` (or non-bumping) |
| **`refactor`** | Code change that neither fixes a bug nor adds a feature | Non-bumping |
| **`docs`** | Documentation only changes | Non-bumping |
| **`test`** | Adding or correcting existing tests | Non-bumping |
| **`chore`** | Changes to the build process, tooling, or libraries | Non-bumping |
| **`ci`** | Changes to CI configuration files and scripts | Non-bumping |

## Breaking Changes
Any commit that breaks backward compatibility must communicate this:
1. Append `!` after the type/scope: `feat(auth)!: replace token endpoint format`
2. Include a `BREAKING CHANGE:` footer:
   ```text
   feat: replace XML parser with JSON parser

   BREAKING CHANGE: payload format must now be valid JSON; XML is no longer accepted.
   ```
   Both trigger a `MAJOR` SemVer bump.
