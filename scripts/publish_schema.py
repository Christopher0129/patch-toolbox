#!/usr/bin/env python3
"""
Publish artifact schema and contract enforcement for patch-toolbox.

Defines the canonical schema for each publish artifact (stats.json,
categories.json, entries.json, search-index.json) and provides a
verify() function that all downstream consumers and CI gates call
to ensure the data contract is satisfied.

Usage (CLI):
    python3 scripts/publish_schema.py verify --artifacts-dir <dir>
    python3 scripts/publish_schema.py schema --artifact-type stats

Exit code: 0 if valid, 1 if contract violations found.
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional


# ── Schema definitions ──────────────────────────────────────────────────

STATS_SCHEMA = {
    "type": "object",
    "required": ["total_entries", "categories"],
    "properties": {
        "total_entries": {"type": "integer", "minimum": 0},
        "categories": {
            "type": "object",
            "required": ["network_security", "system_vulnerabilities", "system_troubleshooting"],
            "additionalProperties": {"type": "integer", "minimum": 0},
        },
    },
}

CATEGORIES_ITEM_SCHEMA = {
    "type": "object",
    "required": ["key", "label", "entry_count", "markdown_path"],
    "properties": {
        "key": {"type": "string", "pattern": r"^[a-z][a-z0-9-]*$"},
        "label": {"type": "string"},
        "entry_count": {"type": "integer", "minimum": 0},
        "markdown_path": {"type": "string"},
        "platforms": {"type": "array", "items": {"type": "string"}},
    },
}

ENTRY_ITEM_SCHEMA = {
    "type": "object",
    "required": ["slug", "title", "category", "markdown_path", "source_url"],
    "properties": {
        "slug": {"type": "string"},
        "title": {"type": "string"},
        "description": {"type": "string"},
        "category": {"type": "string"},
        "markdown_path": {"type": "string"},
        "source_url": {"type": "string"},
        "platform": {"type": "string"},
    },
}

SEARCH_INDEX_ITEM_SCHEMA = {
    "type": "object",
    "required": ["slug", "title", "category", "keywords"],
    "properties": {
        "slug": {"type": "string"},
        "title": {"type": "string"},
        "category": {"type": "string"},
        "keywords": {"type": "string"},
    },
}

# Map artifact filenames to their schemas
ARTIFACT_SCHEMAS = {
    "stats.json": {
        "type": "object",
        "schema": STATS_SCHEMA,
        "iterable": False,
    },
    "categories.json": {
        "type": "array",
        "schema": CATEGORIES_ITEM_SCHEMA,
        "iterable": True,
    },
    "entries.json": {
        "type": "array",
        "schema": ENTRY_ITEM_SCHEMA,
        "iterable": True,
    },
    "search-index.json": {
        "type": "array",
        "schema": SEARCH_INDEX_ITEM_SCHEMA,
        "iterable": True,
    },
}

REQUIRED_ARTIFACTS = list(ARTIFACT_SCHEMAS.keys())


def validate_single(payload: Any, artifact_name: str) -> List[str]:
    """Validate a single artifact payload against its schema. Returns list of violations."""
    violations: List[str] = []
    spec = ARTIFACT_SCHEMAS.get(artifact_name)
    if not spec:
        violations.append(f"Unknown artifact: {artifact_name}")
        return violations

    # Type check top-level
    if isinstance(payload, list) and not spec["iterable"]:
        violations.append(f"{artifact_name}: expected object, got list")
        return violations
    if not isinstance(payload, list) and spec["iterable"]:
        violations.append(f"{artifact_name}: expected list, got {type(payload).__name__}")
        return violations

    if spec["iterable"]:
        if not payload:
            violations.append(f"{artifact_name}: empty list")
            return violations
        for idx, item in enumerate(payload):
            violations.extend(
                _validate_item(item, spec["schema"], f"{artifact_name}[{idx}]")
            )
    else:
        violations.extend(
            _validate_item(payload, spec["schema"], artifact_name)
        )

    return violations


def _validate_item(item: Any, schema: Dict, prefix: str) -> List[str]:
    """Validate a single dict item against its JSON-ish schema. Returns list of violations."""
    violations: List[str] = []
    if not isinstance(item, dict):
        violations.append(f"{prefix}: expected dict, got {type(item).__name__}")
        return violations

    required = schema.get("required", [])
    for field in required:
        if field not in item:
            violations.append(f"{prefix}: missing required field '{field}'")

    props = schema.get("properties", {})
    for field, field_schema in props.items():
        if field not in item:
            continue
        val = item[field]
        field_type = field_schema.get("type", "")
        if field_type == "integer" and not isinstance(val, int):
            violations.append(f"{prefix}.{field}: expected int, got {type(val).__name__}")
        elif field_type == "string" and not isinstance(val, str):
            violations.append(f"{prefix}.{field}: expected string, got {type(val).__name__}")
        elif field_type == "array" and not isinstance(val, list):
            violations.append(f"{prefix}.{field}: expected list, got {type(val).__name__}")

        # Check minimum
        minimum = field_schema.get("minimum")
        if minimum is not None and isinstance(val, (int, float)) and val < minimum:
            violations.append(f"{prefix}.{field}: value {val} < minimum {minimum}")

        # Check pattern for strings
        pattern = field_schema.get("pattern")
        if pattern and isinstance(val, str):
            import re
            if not re.match(pattern, val):
                violations.append(f"{prefix}.{field}: does not match pattern '{pattern}'")

    return violations


def verify_artifacts(artifacts_dir: Path) -> Dict[str, Any]:
    """
    Verify all required publish artifacts in the given directory.

    Returns a dict with:
        - valid: bool — true if all checks pass
        - missing: list of missing artifact filenames
        - violations: list of (artifact_name, violation_string) tuples
        - counts: dict of artifact_name → item/entry count
    """
    result: Dict[str, Any] = {
        "valid": True,
        "missing": [],
        "violations": [],
        "counts": {},
    }

    # Check for missing files
    for artifact_name in REQUIRED_ARTIFACTS:
        path = artifacts_dir / artifact_name
        if not path.exists():
            result["missing"].append(artifact_name)
            result["valid"] = False

    if result["missing"]:
        return result

    # Load and validate each artifact
    for artifact_name in REQUIRED_ARTIFACTS:
        path = artifacts_dir / artifact_name
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            result["violations"].append((artifact_name, f"JSON parse error: {e}"))
            result["valid"] = False
            continue

        violations = validate_single(payload, artifact_name)
        if violations:
            result["valid"] = False
            for v in violations:
                result["violations"].append((artifact_name, v))

        # Count entries
        if isinstance(payload, list):
            result["counts"][artifact_name] = len(payload)
        elif isinstance(payload, dict):
            result["counts"][artifact_name] = payload.get("total_entries", "N/A")

    # Cross-validate: stats.total_entries == len(entries.json)
    if "entries.json" in result["counts"] and "stats.json" in result["counts"]:
        stats_total = result["counts"].get("stats.json")
        entries_len = result["counts"].get("entries.json")
        if isinstance(stats_total, int) and isinstance(entries_len, int):
            if stats_total != entries_len:
                result["violations"].append(
                    ("stats.json vs entries.json",
                     f"stats.total_entries={stats_total} != entries.json count={entries_len}")
                )
                result["valid"] = False

    # Cross-validate: categories[].entry_count sum == len(entries.json)
    if "categories.json" in (artifacts_dir / "categories.json").name if False else True:
        cat_path = artifacts_dir / "categories.json"
        if cat_path.exists():
            try:
                categories = json.loads(cat_path.read_text(encoding="utf-8"))
                cat_total = sum(c["entry_count"] for c in categories)
                if "entries.json" in result["counts"]:
                    entries_len = result["counts"].get("entries.json")
                    if isinstance(entries_len, int) and cat_total != entries_len:
                        result["violations"].append(
                            ("categories.json vs entries.json",
                             f"categories entry_count sum={cat_total} != entries.json count={entries_len}")
                        )
                        result["valid"] = False
            except (json.JSONDecodeError, KeyError):
                pass  # Already caught above

    return result


# ── CLI ─────────────────────────────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Publish artifact schema enforcement for patch-toolbox."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # verify subcommand
    verify_parser = sub.add_parser("verify", help="Verify all artifacts in a directory")
    verify_parser.add_argument("--artifacts-dir", required=True)

    # schema subcommand
    schema_parser = sub.add_parser("schema", help="Print schema for an artifact type")
    schema_parser.add_argument("--artifact-type", choices=list(ARTIFACT_SCHEMAS.keys()) + ["all"])

    args = parser.parse_args()

    if args.command == "verify":
        artifacts_dir = Path(args.artifacts_dir)
        if not artifacts_dir.exists():
            print(f"❌ Directory not found: {artifacts_dir}")
            sys.exit(1)

        result = verify_artifacts(artifacts_dir)

        if result["missing"]:
            print("❌ Missing artifacts:")
            for name in result["missing"]:
                print(f"   - {name}")

        if result["violations"]:
            print("❌ Schema violations:")
            for artifact, msg in result["violations"]:
                print(f"   [{artifact}] {msg}")

        if result["valid"]:
            print(f"✅ All artifacts valid")
            for name, count in result["counts"].items():
                print(f"   {name}: {count} entries")
        else:
            sys.exit(1)

    elif args.command == "schema":
        if args.artifact_type == "all":
            for name, spec in ARTIFACT_SCHEMAS.items():
                print(f"--- {name} ---")
                print(json.dumps(spec["schema"], indent=2))
                print()
        else:
            spec = ARTIFACT_SCHEMAS.get(args.artifact_type)
            if spec:
                print(json.dumps(spec["schema"], indent=2))
            else:
                print(f"Unknown artifact type: {args.artifact_type}")
                sys.exit(1)


if __name__ == "__main__":
    main()
