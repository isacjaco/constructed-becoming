# Governance playbook

**Status:** Ratified  
**Steward:** Governance Clerk (human)  
**Effective from:** 2026-04-10  
**Review horizon:** End of next epoch or after 12 weeks of operation — whichever comes first

---

## Purpose

This playbook translates the **Law of Perpetual Lineage** into operational rules. It sets out who may change what, under which conditions, and how every change is recorded so that lineage is never silently broken. It is a living document: amendments follow the identity-delta process described below.

---

## I. Core commitments

| Commitment | Meaning in practice |
|---|---|
| **No silent change** | Every merge touching identity modules must include a lineage delta file and a narrative summary. |
| **No unreviewed agent PR** | Agent-authored pull requests must carry the `human-approved` label before merge. CI enforces this. |
| **Reversibility by default** | Every change must document a rollback path. If no rollback path exists, the change is escalated before merge. |
| **Dissent as lineage** | Disagreements are recorded, not collapsed. A rejected proposal is archived, not deleted. |

---

## II. Decision flows

### 2.1 Human-authored change

```
Author opens PR
  │
  ├─ Touches identity modules (docs/*, agents/*)? ──Yes──▶ Attach lineage delta
  │                                                          (docs/deltas/YYYY-MM-DD_delta_<slug>.md)
  │
  ├─ Conceptual or philosophical content? ──Yes──▶ Attach conceptual PR checklist sign-off
  │
  └─ Standard content change ──────────────────▶ Normal review; one human approval required
```

All human PRs require at least **one human reviewer** approval before merge.

### 2.2 Agent-authored change

```
Agent opens PR (label: agent-draft applied automatically by CI)
  │
  ├─ CI checks:
  │   ├─ agent-draft label present? (fail-safe: block if absent)
  │   ├─ Touches identity modules? ──Yes──▶ Lineage delta present? ──No──▶ BLOCK
  │   └─ YAML frontmatter valid (agents/*.md)? ──No──▶ BLOCK
  │
  ├─ Human reviewer adds human-approved label
  │
  └─ CI re-checks label ──▶ allow merge
```

Agents **may not** self-merge. The `human-approved` label may only be applied by a human reviewer (branch-protection rules enforce this).

### 2.3 Emergency rollback

When a merged change causes a critical regression:

1. **Identify the lineage delta** for the change — it contains the documented rollback steps.
2. The Governance Clerk or any Council reviewer opens a revert PR referencing the original delta.
3. Revert PR bypasses the lineage-delta requirement but must include a short narrative note in the PR body explaining the emergency.
4. After the revert merges, a post-mortem delta is opened within 48 hours.

---

## III. Agent scope matrix

Agents operate within defined scopes. Anything outside the **autonomous** column requires a human-reviewed PR.

| Action | Autonomous (no review needed) | Propose only (PR + human review) |
|---|---|---|
| Generate a draft chronicle | ✅ | |
| Generate a draft identity delta | ✅ | |
| Amend a chronicle (non-governance) | ✅ | |
| Create a new `agents/*.md` file | | ✅ |
| Modify `docs/law-of-perpetual-lineage.md` | | ✅ |
| Modify `docs/governance-playbook.md` | | ✅ |
| Modify any file in `docs/` (governance corpus) | | ✅ |
| Create or amend a GitHub Actions workflow | | ✅ |
| Merge any PR | | ✅ (human only) |

---

## IV. Labelling conventions

| Label | Applied by | Meaning |
|---|---|---|
| `agent-draft` | CI (automatic) | PR was opened by an agent or automated workflow |
| `human-approved` | Human reviewer | A human has reviewed and approved the agent-authored PR |
| `lineage-required` | CI (automatic) | PR touches identity modules; a delta file is required |
| `conceptual` | Author | PR contains philosophical or diagrammatic content; checklist required |
| `governance` | Author or Clerk | PR amends governance documents; Clerk sign-off required |
| `emergency-rollback` | Any Council reviewer | Revert PR; waives delta requirement; post-mortem required |

---

## V. Lineage delta requirement

Any PR that modifies files matching these paths **must** include a corresponding `docs/deltas/YYYY-MM-DD_delta_<slug>.md` file:

- `docs/law-of-perpetual-lineage.md`
- `docs/governance-playbook.md`
- `docs/architecture.md`
- `docs/ritual-protocols.md`
- `docs/system-prompt.md`
- `agents/**`

Use `docs/templates/identity-delta-template.md` as the starting scaffold.

---

## VI. Conceptual PR checklist

PRs labelled `conceptual` require a reviewer to confirm the following before approving:

- [ ] The proposal is connected to an existing principle or lineage entry (link provided).
- [ ] The conceptual claim has at least one testable or observable implication stated.
- [ ] No existing governance norms are implicitly overridden without a corresponding delta.
- [ ] Philosophical alignment with the Law of Perpetual Lineage is affirmed or a tension is explicitly named.

---

## VII. Amending this playbook

This playbook is itself subject to the Law of Perpetual Lineage. To amend it:

1. Open an identity delta (use the template in `docs/templates/identity-delta-template.md`).
2. Reference this playbook in the delta's **Related chronicle / event** field.
3. Open a PR labelled `governance`; the Governance Clerk must approve.
4. After merge, record the amendment in `docs/chronicles/` as a brief threshold entry.

---

*Effective from: 2026-04-10*  
*Steward: Governance Clerk (human)*  
*Last touched: 2026-04-10*
