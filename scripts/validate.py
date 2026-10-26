#!/usr/bin/env python3
"""Validate the repo: skill frontmatter (Agent Skills spec) and relative Markdown links. Stdlib only."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK = re.compile(r"\]\(([^)\s]+)\)")
FENCE = re.compile(r"^(```|~~~)")


def frontmatter(text: str) -> dict[str, str] | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        key, sep, value = line.partition(":")
        if sep and not line.startswith((" ", "\t")):
            fields[key.strip()] = value.strip()
    return None


def check_skills() -> list[str]:
    errors = []
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skills:
        errors.append("no skills found under skills/")
    for path in skills:
        folder = path.parent.name
        meta = frontmatter(path.read_text(encoding="utf-8"))
        where = path.relative_to(ROOT).as_posix()
        if meta is None:
            errors.append(f"{where}: missing YAML frontmatter")
            continue
        name, description = meta.get("name", ""), meta.get("description", "")
        if not NAME.match(name) or len(name) > 64:
            errors.append(f"{where}: name '{name}' must be lowercase letters, digits and hyphens, at most 64 chars")
        if name != folder:
            errors.append(f"{where}: name '{name}' must equal its folder '{folder}'")
        if not 1 <= len(description) <= 1024:
            errors.append(f"{where}: description must be 1-1024 chars (has {len(description)})")
        # An unquoted YAML value breaks on ": " or " #"; quote the description if it needs them.
        if not description.startswith(("'", '"')) and (": " in description or " #" in description):
            errors.append(f"{where}: unquoted description contains ': ' or ' #', which breaks YAML")
    return errors


def relative_links(path: Path):
    """Yield (line number, target) for relative links outside fenced code blocks."""
    in_fence = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if FENCE.match(line.strip()):
            in_fence = not in_fence
        elif not in_fence:
            for target in LINK.findall(line):
                link = target.split("#", 1)[0]
                if link and not re.match(r"^([a-z][a-z0-9+.-]*:|/)", link, re.IGNORECASE):
                    yield number, target


def check_links() -> list[str]:
    errors = []
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        for number, target in relative_links(path):
            if not (path.parent / target.split("#", 1)[0]).exists():
                errors.append(f"{path.relative_to(ROOT).as_posix()}:{number}: broken link {target}")
    return errors


def check_manifests() -> list[str]:
    errors = []
    for path in sorted((ROOT / ".claude-plugin").glob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.relative_to(ROOT).as_posix()}: invalid JSON ({exc})")
    return errors


def main() -> int:
    errors = check_skills() + check_links() + check_manifests()
    for error in errors:
        print(f"error: {error}")
    count = len(list((ROOT / "skills").glob("*/SKILL.md")))
    print(f"{count} skill(s) checked, {len(errors)} error(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
