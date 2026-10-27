# Example: Complete Release Automation Workflow

### Scenario: Releasing Version 1.2.0

1. **Check commits on `main` since last release (`v1.1.0`)**:
   ```bash
   git log v1.1.0..HEAD --oneline
   ```
   Output:
   ```text
   9f8a123 feat(search): add fuzzy search filtering
   7b4c456 fix(search): handle special regex characters in query
   3d2e789 docs(readme): update search query examples
   ```

2. **Calculate Next Version**:
   - Highest commit impact is `feat(search)` -> **MINOR** bump.
   - Previous: `v1.1.0` -> Target: `v1.2.0`.

3. **Generate Changelog**:
   ```bash
   bash ./scripts/generate-changelog.sh v1.2.0 >> CHANGELOG.md
   ```

4. **Review `CHANGELOG.md` entry**:
   ```markdown
   ## [v1.2.0] - 2026-10-27

   ### ✨ Features
   - feat(search): add fuzzy search filtering (9f8a123)

   ### 🐛 Bug Fixes
   - fix(search): handle special regex characters in query (7b4c456)

   ### 🔧 Maintenance & Documentation
   - docs(readme): update search query examples (3d2e789)
   ```

5. **Commit and Tag**:
   ```bash
   git add CHANGELOG.md package.json
   git commit -m "chore(release): v1.2.0"
   git tag -a v1.2.0 -m "Release v1.2.0: Fuzzy search & regex query fixes"
   git push origin main --tags
   ```
