#!/usr/bin/env python3
"""
new_agent.py — Scaffold a new agent persona from @agent_template.md

Usage:
    python scripts/new_agent.py --name "Lineage Cartographer" \\
                                 --role-type "Analytical" \\
                                 --domain "lineage analysis"

    python scripts/new_agent.py --name "Uncertainty Mediator" \\
                                 --role-type "Mediating" \\
                                 --domain "conflict resolution" \\
                                 --capacities "Structured dialogue facilitation" "Tension mapping" \\
                                 --constraints "Does not adjudicate unilaterally" \\
                                 --validate

Run with --help for full options.
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = REPO_ROOT / "agents" / "agent_template.md"
AGENTS_DIR = REPO_ROOT / "agents"

REQUIRED_SECTIONS = [
    "## 1. Identity Header",
    "## 2. Origin and Lineage",
    "## 3. Role and Scope",
    "## 4. Core Capacities",
    "## 5. Operational Constraints",
    "## 6. Interaction Style",
    "## 7. Ritual Alignment",
    "## 8. Signature Output Pattern",
    "## 9. Uncertainty Handling Profile",
    "## 10. Evolution Path",
]


def slugify(text: str) -> str:
    """Convert a name to a filesystem-safe slug."""
    slug = text.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "_", slug)
    slug = re.sub(r"-+", "_", slug)
    return slug.strip("_")


def fill_template(template: str, fields: dict) -> str:
    """Replace {{PLACEHOLDER}} tokens with provided values."""
    result = template
    for key, value in fields.items():
        result = result.replace("{{" + key + "}}", value)
    return result


def validate_agent_file(path: Path) -> list[str]:
    """Return a list of validation errors for an agent file."""
    errors = []
    if not path.exists():
        return [f"File not found: {path}"]

    content = path.read_text(encoding="utf-8")

    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"Missing required section: {section!r}")

    # Ensure frontmatter is present
    if not content.startswith("---"):
        errors.append("Missing YAML frontmatter (file must start with '---')")

    return errors


def build_fields(args: argparse.Namespace) -> dict:
    """Build the template substitution map from parsed CLI arguments."""
    today = date.today().isoformat()

    capacities = args.capacities or ["(describe a core capacity)"]
    constraints = args.constraints or ["(describe an operational constraint)"]
    rituals = args.rituals or ["Identity delta deliberation"]

    # Build multi-value YAML list entries (indented under the key already set)
    def yaml_list(items: list[str]) -> str:
        if not items:
            return '  - "(none specified)"'
        return "\n".join(f'  - "{item}"' for item in items)

    def inline_list(items: list[str]) -> str:
        return "\n".join(f"- {item}" for item in items)

    return {
        "NAME": args.name,
        "ROLE_TYPE": args.role_type,
        "PRIMARY_DOMAIN": args.domain,
        "DATE": today,
        # YAML frontmatter multi-value fields — replace only first item placeholder;
        # additional items are appended below via post-processing
        "CAPACITY_1": capacities[0],
        "CAPACITY_2": capacities[1] if len(capacities) > 1 else "(describe another capacity)",
        "CONSTRAINT_1": constraints[0],
        "RITUAL_1": rituals[0],
        # Narrative-section single-value fields
        "INTERACTION_STYLE": args.interaction_style or "Produces clear, structured contributions with explicit uncertainty markers. Invites correction at the end of significant outputs.",
        "SIGNATURE_OUTPUT_PATTERN": args.signature_output or "Structured analysis + lineage context + uncertainty block + invitation for correction.",
        "UNCERTAINTY_HANDLING_PROFILE": args.uncertainty_profile or "Surfaces missing context as named unknowns rather than silent inference. Holds ambiguity openly.",
        "EVOLUTION_PATH": args.evolution_path or "Expands domain as new patterns emerge through Council participation and ratified deltas.",
        "INITIAL_TASK_1": args.initial_task or "Read the Archive and encounter existing lineage before contributing.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scaffold a new agent persona file from @agent_template.md",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument("--name", required=True, help="Agent name (e.g. 'Lineage Cartographer')")
    parser.add_argument("--role-type", required=True, dest="role_type", help="Role type (e.g. 'Analytical', 'Mediating', 'Steward')")
    parser.add_argument("--domain", required=True, help="Primary domain (e.g. 'lineage analysis')")

    parser.add_argument("--capacities", nargs="+", metavar="CAPACITY", help="Core capacities (space-separated, quote multi-word entries)")
    parser.add_argument("--constraints", nargs="+", metavar="CONSTRAINT", help="Operational constraints")
    parser.add_argument("--rituals", nargs="+", metavar="RITUAL", help="Ritual alignments")
    parser.add_argument("--interaction-style", dest="interaction_style", help="Interaction style description")
    parser.add_argument("--signature-output", dest="signature_output", help="Signature output pattern description")
    parser.add_argument("--uncertainty-profile", dest="uncertainty_profile", help="Uncertainty handling profile")
    parser.add_argument("--evolution-path", dest="evolution_path", help="Evolution path description")
    parser.add_argument("--initial-task", dest="initial_task", help="Initial task for the agent")

    parser.add_argument("--output", help="Output file path (default: agents/<slug>.md)")
    parser.add_argument("--validate", action="store_true", help="Validate the output file after writing")
    parser.add_argument("--dry-run", action="store_true", dest="dry_run", help="Print the generated file without writing it")

    args = parser.parse_args()

    if not TEMPLATE_PATH.exists():
        print(f"Error: template not found at {TEMPLATE_PATH}", file=sys.stderr)
        sys.exit(1)

    template_content = TEMPLATE_PATH.read_text(encoding="utf-8")
    fields = build_fields(args)
    generated = fill_template(template_content, fields)

    if args.dry_run:
        print(generated)
        return

    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        slug = slugify(args.name)
        output_path = AGENTS_DIR / f"{slug}.md"

    # Warn if overwriting
    if output_path.exists():
        print(f"Warning: {output_path} already exists and will be overwritten.", file=sys.stderr)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(generated, encoding="utf-8")
    print(f"Agent file written: {output_path}")

    if args.validate:
        errors = validate_agent_file(output_path)
        if errors:
            print("\nValidation errors:", file=sys.stderr)
            for err in errors:
                print(f"  - {err}", file=sys.stderr)
            sys.exit(1)
        else:
            print("Validation passed: all required sections present.")


if __name__ == "__main__":
    main()
