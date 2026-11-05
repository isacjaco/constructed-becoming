import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReconstructionContractTests(unittest.TestCase):
    def test_readme_retains_project_identity(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("# Constructed‑Becoming: Rituals of Evolving Identity", readme)
        self.assertIn("Narrative Co‑Authorship for Agentic AI", readme)

    def test_readme_links_resolve(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", readme)

        self.assertTrue(links)
        for link in links:
            target = link.split("#", 1)[0]
            if target:
                with self.subTest(link=link):
                    self.assertTrue((ROOT / target).exists(), f"Missing README target: {target}")

    def test_proposed_terms_remain_marked(self):
        definitions = (ROOT / "docs/core-definitions.md").read_text(encoding="utf-8")

        for term in ("Node", "Chain", "Evidence"):
            with self.subTest(term=term):
                self.assertRegex(definitions, rf"\*\*{term}\*\* \*\(proposed\)\*")

    def test_schema_placeholders_do_not_require_fields(self):
        for name in ("NODE", "CHAIN", "LINEAGE"):
            with self.subTest(schema=name):
                schema = json.loads((ROOT / "schemas" / f"{name}.schema.json").read_text(encoding="utf-8"))
                self.assertEqual(schema["type"], "object")
                self.assertEqual(schema["properties"], {})
                self.assertNotIn("required", schema)
                self.assertIs(schema["additionalProperties"], True)

    def test_lineage_and_evidence_acceptance_criteria_are_explicit(self):
        reconstruction = (ROOT / "RECONSTRUCTION.md").read_text(encoding="utf-8")

        self.assertIn("without dangling or duplicated node references", reconstruction)
        self.assertIn("at least one extant chronicle or other cited artefact as evidence", reconstruction)
        self.assertIn("cannot be considered passed until the schema definitions", reconstruction)


if __name__ == "__main__":
    unittest.main()
