# lineage/deltas/

This directory holds **lineage delta files** — brief, dated records of every meaningful
change introduced through a pull request.

## Naming convention

```
YYYY-MM-DD--<short-slug>.md
```

**Examples**

```
2026-04-10--add-clerk-role.md
2026-05-01--update-ritual-protocols.md
```

## What to include

A delta file does not need to be long.  A one- or two-paragraph entry is sufficient,
covering:

- **What** is changing (the concrete change in this PR)
- **Why** it is changing (the lineage context or motivation)
- **What it supersedes or complements** (optional, but helpful for traceability)

Use `docs/templates/identity-delta-template.md` as a scaffold if helpful.

## Why this is required

Every pull request to this repository must include at least one added or modified file
here.  The `lineage-delta-required` GitHub Actions check enforces this automatically.
If your PR does not touch this directory the check will fail and the PR cannot be merged
(once branch protection is enabled — see the Contributing section of the README).
