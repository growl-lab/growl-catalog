#!/usr/bin/env python3
"""Validate every simulations/<id>/metadata.yaml against schema/metadata.schema.json.

Usage:
    python scripts/validate_metadata.py            # check all entries
    python scripts/validate_metadata.py <id> ...   # check specific entries

Exit code is non-zero if any entry fails, so this runs as a CI check.
"""
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
SIM_DIR = ROOT / "simulations"
SCHEMA = json.loads((ROOT / "schema" / "metadata.schema.json").read_text())
VALIDATOR = Draft202012Validator(SCHEMA)


def check(folder: Path) -> list[str]:
    errors = []
    meta = folder / "metadata.yaml"
    if not meta.exists():
        return [f"{folder.name}: missing metadata.yaml"]
    try:
        data = yaml.safe_load(meta.read_text())
    except yaml.YAMLError as exc:
        return [f"{folder.name}: YAML could not be parsed: {exc}"]
    if not isinstance(data, dict):
        return [f"{folder.name}: metadata.yaml is empty or not a mapping"]

    for err in sorted(VALIDATOR.iter_errors(data), key=lambda e: list(e.path)):
        where = ".".join(str(p) for p in err.path) or "(top level)"
        msg = err.message
        if err.validator == "anyOf" and where == "paper":
            msg = "give at least a doi or an arxiv id"
        errors.append(f"{folder.name}: {where}: {msg}")

    if data.get("id") != folder.name:
        errors.append(f"{folder.name}: id '{data.get('id')}' must match the folder name")
    if not (folder / "README.md").exists():
        errors.append(f"{folder.name}: missing README.md")
    return errors


def main(argv: list[str]) -> int:
    if argv:
        folders = [SIM_DIR / name for name in argv]
    else:
        folders = sorted(p for p in SIM_DIR.iterdir() if p.is_dir() and not p.name.startswith("_"))

    all_errors = []
    for folder in folders:
        errs = check(folder)
        all_errors.extend(errs)
        print(f"{'FAIL' if errs else 'ok  '}  {folder.name}")

    if all_errors:
        print("\nProblems found:")
        for e in all_errors:
            print(f"  - {e}")
        return 1
    print(f"\nAll {len(folders)} entries valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
