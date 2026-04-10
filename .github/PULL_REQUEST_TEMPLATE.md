## Summary

<!-- What does this PR change, add, or remove? (1–3 sentences) -->

---

## Lineage delta ✅ (required)

Every pull request **must** include at least one lineage delta file.

### Steps

1. Create a file under `lineage/deltas/` following the naming convention:

   ```
   lineage/deltas/YYYY-MM-DD--<short-slug>.md
   ```

   Example: `lineage/deltas/2026-04-10--add-clerk-role.md`

2. Add a brief entry describing *what* is changing and *why* (one or two paragraphs is enough).  
   Use `docs/templates/identity-delta-template.md` as a scaffold if helpful.

3. Paste the path to your delta file here:

   > **Delta file:** `lineage/deltas/YYYY-MM-DD--<short-slug>.md`

The `lineage-delta-required` status check will **fail** until a file matching the path  
`lineage/deltas/**` is added or modified in this PR.

---

## Checklist

- [ ] Lineage delta file added under `lineage/deltas/YYYY-MM-DD--<short-slug>.md`
- [ ] Delta file path listed above
- [ ] Changes are consistent with the project's ritual protocols and governance philosophy
