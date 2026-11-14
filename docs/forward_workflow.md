# Forward Workflow for Constructed-Becoming

*Lineage-aware, agent-coauthored, governance-aligned*

**Status:** Draft — pending Council deliberation. Nothing here is ratified policy until the Council affirms it per [`ritual-protocols.md`](ritual-protocols.md). See [Open questions for deliberation](#open-questions-for-deliberation).

This workflow turns the repository into a **self-governing, multi-agent ecosystem** where every change is intentional, narrativized, and lineage-preserving. It integrates:

- The **Lineage Chronicle**
- The **GitHub Actions agent runs**
- The **Copilot agent session history**
- The **Agent Factory templating system**
- The **current repository identity**

---

## 1. Intake Phase — A Change Enters the Lineage

**Purpose:** Every change begins as a story, not a diff.

**Sources of new intent:**
- Human steward proposes a change
- Copilot cloud agents generate a draft PR
- Narrative continuation agents propose lineage deltas
- Governance templating agents propose structural updates

**Required artifacts:**
- **Intent Note** — short narrative of why this change exists
- **Lineage Position** — ancestor modules affected, expected descendants
- **Uncertainty Markers** — what the agent is unsure about

This ensures every change begins with **context**, not code.

---

## 2. Drafting Phase — Agents Produce the First Shape

**Actors:** Copilot cloud agents, templating agents, lineage-aware assistants.

**Actions:**
- Generate draft PRs
- Apply agent templates to ensure structure
- Produce:
  - Proposed module
  - Narrative explanation
  - Lineage implications
  - Uncertainty fields
  - Ritual alignment (which governance rituals apply)

**Outcome:** A Draft PR with:
- Structured agent template
- Narrative body
- Initial implementation
- Auto-generated lineage delta

Agents create drafts; humans refine.

---

## 3. Governance Review — The Council Convenes

**Actors:**
- Human Steward (final authority)
- Rotating Council Reviewers
- Automated Governance Agents

**Inputs:**
- Draft PR
- Lineage delta
- Identity kernel constraints
- Governance playbook rules

**Checks performed:**
- Does the change preserve lineage continuity?
- Does it violate identity kernel commitments?
- Are uncertainty markers surfaced, not hidden?
- Does the agent template conform to schema?
- Does the narrative match the Becoming Engine's expectations?

**Automated checks (proposed — not yet implemented):**
- Onboarding workflow validation
- Agentic workflow framework checks
- Narrative reporting checks
- Repository observer agent feedback

The checked-in GitHub Actions workflows currently only generate onboarding PRs and deploy Pages; none of the checks above exist yet. Until they do, the **interim manual review** applies: the reviewer confirms each question under "Checks performed" by hand and records the result in the PR discussion.

**Outcome:** A Reviewed PR with:
- Council comments
- Steward decision
- Updated lineage delta

---

## 4. Refinement Phase — Agents Respond to the Council

**Actors:**
- Copilot cloud agents
- Specialized agents (e.g., lineage cartographer, repository observer)

**Actions:**
- Address council comments
- Regenerate sections using agent templates
- Update lineage delta
- Produce a **narrative continuation** describing how the change evolved
- Re-run automated workflows

---

## 5. Merge Ritual — The Change Joins the Lineage

**Conditions for merge:**
- Steward approval
- Council deliberation recorded (or the Council decision referenced) for governance changes
- Manual governance review completed (automated checks are proposed; see Phase 3)
- Lineage delta present and reviewed by hand
- Narrative continuity confirmed by a reviewer
- Agent template conformance confirmed by a reviewer

**Merge actions:**
- Commit includes: final code, final narrative, final lineage delta
- Chronicle updated
- Agents notified of new lineage state

This is where the repository "becomes" again.

---

## 6. Chronicle Update — The Story Remembers

After merge, the system updates:

- **Lineage Chronicle**
- **Identity Kernel** if needed
- **Becoming Engine** logs
- **Agent registry**
- **Narrative continuation threads**

This ensures the repository remains a **living organism**, not a static codebase.

---

## 7. Continuous Agentic Evolution — The Lineage Breathes

Agents continue to run (onboarding PR generation exists today; the remainder are proposed):

- Onboarding workflows
- Agentic workflow framework *(proposed)*
- Narrative reporting *(proposed)*
- Repository observation *(proposed)*
- Automated PR generation
- Identity kernel maintenance *(proposed)*
- Governance templating *(proposed)*

This creates a **self-maintaining, self-narrating ecosystem**.

---

## Summary

Every change enters as a story, is shaped by agents, judged by governance, refined through lineage, merged through ritual, and remembered by the chronicle.

---

## Open questions for deliberation

1. Which proposed automated checks should be implemented first, and who owns them?
2. Is the interim manual review in Phases 3 and 5 sufficient until automation exists?
3. Should a maturity vocabulary (Draft, Proposed, Ratified, Active, Superseded, Archived) be adopted for governance artifacts?
4. Should governance decisions get a lightweight decision-record format alongside deltas?
5. Should the Stewardship section define who may approve, ratify, and supersede governance documents, including emergency overrides?

---

*Seed document of the Ritual Library — first catalogued 2026-04-11*  
*Part of the [Curated Ritual Library](../GOVERNANCE.md#governance-artifacts)*
