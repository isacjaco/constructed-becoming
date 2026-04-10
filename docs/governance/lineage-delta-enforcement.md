# Lineage delta enforcement

**Status:** Ratified governance policy  
**Introduced by:** GitHub Copilot coding agent (governed PR, 2026-04-10)  
**Review horizon:** Next epoch deliberation

---

## What this document covers

This document explains the CI enforcement of the lineage delta requirement,
the policy decisions that shaped it, and how maintainers can wire it into
branch protection.

---

## The rule

**Every pull request must include at least one lineage delta file before it
can be merged.**

A lineage delta file is a Markdown file placed under `docs/deltas/` following
the naming convention established in `docs/archive-structure-proposal.md`:

```
docs/deltas/YYYY-MM-DD_delta_<short-name>.md
```

Examples:
- `docs/deltas/2026-04-10_delta_ci-governance-enforcement.md`
- `docs/deltas/2026-07-01_delta_clerk-role-amendment.md`

Use `docs/templates/identity-delta-template.md` as a starting shape.

---

## How enforcement works

The CI workflow at `.github/workflows/lineage-delta-required.yml` runs on
every `pull_request` event (opened, synchronised, reopened). It:

1. Fetches the base branch.
2. Lists all files changed in the PR (via `git diff --name-only`).
3. Filters for files matching `docs/deltas/*.md`.
4. Fails with an explanatory message if none are found; passes otherwise.

The GitHub Actions job is named **`lineage-delta-required`** so it can be
referenced directly in branch protection rules.

---

## Wiring into branch protection

To make this check mandatory (hard-block merges without a delta):

1. Go to **Repository → Settings → Branches**.
2. Open (or create) the branch protection rule for `main`.
3. Enable **"Require status checks to pass before merging"**.
4. In the search box, type `lineage-delta-required` and select the check.
5. Optionally enable **"Require branches to be up to date before merging"**
   for additional safety.
6. Save the rule.

Once saved, GitHub will prevent any PR from being merged into `main` unless
the `lineage-delta-required` check has passed on the latest commit.

---

## Policy decision: strict enforcement

This repo uses **strict enforcement**: every PR requires a lineage delta,
regardless of which paths are modified. This includes:

- Typo fixes and formatting changes
- CI/workflow updates
- Documentation-only changes
- Dependency bumps

**Rationale:** The lineage model treats *every* contribution as an act of
becoming. A delta — even a minimal one — records the intent and context of
a change. A trivial-change exemption would create a category of "ungoverned"
contributions, which contradicts the law of perpetual lineage.

**Held dissent:** A strict policy increases contributor friction for trivial
changes. If the ecology finds this burdensome in practice, an allowlist for
specific paths (e.g., dependency lock files) may be ratified through the
normal delta process. That possibility is part of this policy's lineage.

---

## What counts as a valid delta

The check only verifies *presence* — that at least one `docs/deltas/*.md`
file is added or modified in the PR. It does not validate the content of the
delta. Content validation is a cultural practice enforced through review, not
automation.

A minimal valid delta might be a single sentence explaining what changed and
why. The template in `docs/templates/identity-delta-template.md` is a
scaffold, not a requirement.

---

## Amending this policy

To change this enforcement policy:

1. Submit a PR that modifies `.github/workflows/lineage-delta-required.yml`
   (and/or this document).
2. Include a lineage delta explaining the change (meta-governance applies).
3. Obtain Council deliberation and ratification per
   `docs/ritual-protocols.md`.

---

*Introduced by: GitHub Copilot coding agent / @isacjaco, 2026-04-10*  
*Last touched: 2026-04-10*
