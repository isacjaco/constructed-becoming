name: "agent-draft"
description: "Pull request proposed by an agent or automated workflow"
labels: ["agent-draft"]
---

## Agent summary

*What did the agent do and why?*  
*Reference the session, run ID, or trigger that caused this PR.*

**Agent name / ID:**  
**Session / run reference:**  
**Trigger:**  

## Scope check

*Confirm this action falls within the agent's defined autonomous or propose-only scope.*

- [ ] This action is listed in the agent's `propose_only` scope (see `agents/<name>.md`).
- [ ] This action does **not** fall in the `autonomous` scope — human review is required.

## Lineage

*Does this PR touch identity modules (`docs/`, `agents/`)?*

- [ ] No identity modules touched — no delta required.
- [ ] Identity modules touched — delta file attached: `docs/deltas/___`

## Human reviewer checklist

*To be completed by the human reviewer before applying `human-approved` label:*

- [ ] The change is within the agent's declared scope.
- [ ] The reasoning is sound and aligns with the Law of Perpetual Lineage.
- [ ] Rollback path is documented or the change is trivially reversible.
- [ ] Lineage delta present if required.

> **Note:** This PR cannot be merged until a human reviewer applies the `human-approved` label.
