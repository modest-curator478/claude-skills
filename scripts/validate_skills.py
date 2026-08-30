#!/usr/bin/env python3
"""Validate required metadata for every skill in the repository."""

from pathlib import Path
import re
import sys


REQUIRED_KEYS = ("name", "version", "description", "allowed-tools")
SCALAR_PATTERN = re.compile(r"^(?P<key>[a-z][a-z-]*):\s*(?P<value>.*)$")


def read_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    if not lines or lines[0] != "---":
        return {}, ["frontmatter must start on the first line"]

    try:
        closing_index = lines.index("---", 1)
    except ValueError:
        return {}, ["frontmatter is missing its closing delimiter"]

    metadata: dict[str, str] = {}
    for line in lines[1:closing_index]:
        match = SCALAR_PATTERN.match(line)
        if match is not None:
            metadata[match.group("key")] = match.group("value").strip()

    for key in REQUIRED_KEYS:
        if key not in metadata:
            errors.append(f"frontmatter is missing {key}")

    name = metadata.get("name")
    if name is not None and name != path.parent.name:
        errors.append(f"name {name!r} does not match directory {path.parent.name!r}")

    if not any(line.strip() for line in lines[closing_index + 1 :]):
        errors.append("skill body is empty")

    return metadata, errors


def validate(root: Path) -> list[str]:
    skill_paths = sorted(root.glob("*/*/SKILL.md"))
    if not skill_paths:
        return ["no skills found"]

    errors: list[str] = []
    names: dict[str, Path] = {}
    for path in skill_paths:
        metadata, path_errors = read_frontmatter(path)
        errors.extend(f"{path}: {error}" for error in path_errors)

        name = metadata.get("name")
        if name is None:
            continue
        previous = names.get(name)
        if previous is not None:
            errors.append(f"{path}: duplicate name {name!r}, already used by {previous}")
        else:
            names[name] = path

    return errors


def main() -> int:
    errors = validate(Path(__file__).resolve().parent.parent)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("Skill metadata validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
