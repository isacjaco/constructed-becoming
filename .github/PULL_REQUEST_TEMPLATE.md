## Summary

<!-- Describe the changes in this PR. What is changing and why? -->

---

## Lineage delta *(required — PR cannot be merged without this)*

Every PR must include at least one lineage delta file. This is enforced by the
`lineage-delta-required` CI check. If the check fails, the PR will be blocked
from merging.

**How to satisfy the check:**

1. Create a file under `docs/deltas/` following the naming convention:
   ```
   docs/deltas/YYYY-MM-DD_delta_<short-name>.md
   ```
   Example: `docs/deltas/2026-04-10_delta_add-ci-governance.md`

2. Use `docs/templates/identity-delta-template.md` as a starting shape
   (optional — the template is a scaffold, not a law).

3. Set the status field in your delta:
   - `⚠️ Draft` — proposed, not yet deliberated
   - `🔄 Under deliberation` — actively being discussed
   - `✅ Ratified` — accepted by the Council

- [ ] I have added a lineage delta at `docs/deltas/YYYY-MM-DD_delta_<short-name>.md`

---

## Checklist

- [ ] Changes align with the ecology's identity and governance protocols
   (see `docs/ritual-protocols.md` and `docs/law-of-perpetual-lineage.md`)
- [ ] The lineage delta names any dissent or uncertainty
- [ ] Any new agent behaviour follows `docs/agent-behaviour.md`
