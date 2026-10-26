#!/usr/bin/env python3
"""Repair Markdown links after `openspec archive` moves a change into a dated folder.

Archiving moves openspec/changes/<name>/ to openspec/changes/archive/YYYY-MM-DD-<name>/, one level
deeper. Two kinds of links break:

1. Relative links inside the archived change that point outside it (they need one more `../`).
2. References elsewhere in the repo to `changes/<name>/` (they must point to the archive).

Usage:
    python archive_links.py <change-name> [--root PATH] [--dry-run]

Exits 1 if the archived folder cannot be found. Stdlib only.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

LINK = re.compile(r"(\]\()([^)\s]+)(\))")
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "dist", "build", "__pycache__"}
DATED = re.compile(r"^\d{4}-\d{2}-\d{2}-(.+)$")


def find_archived(root: Path, name: str) -> Path:
    archive = root / "openspec" / "changes" / "archive"
    matches = [d for d in archive.iterdir() if d.is_dir() and (m := DATED.match(d.name)) and m.group(1) == name] if archive.is_dir() else []
    if len(matches) != 1:
        raise SystemExit(f"Expected one archived folder for '{name}' under {archive}, found {len(matches)}.")
    return matches[0]


def is_relative(target: str) -> bool:
    return not re.match(r"^([a-z][a-z0-9+.-]*:|#|/)", target, re.IGNORECASE)


def markdown_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for filename in filenames:
            if filename.endswith(".md"):
                yield Path(dirpath) / filename


def fix_inside(archived: Path, old_dir: Path) -> tuple[dict[Path, str], list[str]]:
    """Rewrite links in the archived change that pointed outside the change from its old location."""
    changed: dict[Path, str] = {}
    broken: list[str] = []
    for md in archived.rglob("*.md"):
        old_file = old_dir / md.relative_to(archived)
        text = md.read_text(encoding="utf-8")

        def rewrite(match: re.Match[str]) -> str:
            target = match.group(2)
            path_part, _, anchor = target.partition("#")
            if not path_part or not is_relative(path_part):
                return match.group(0)
            if (md.parent / path_part).exists():
                return match.group(0)  # already valid from the new location
            old_target = Path(os.path.normpath(old_file.parent / path_part))
            if old_target == old_dir or old_dir in old_target.parents:
                return match.group(0)  # points inside the change: moved together
            if not old_target.exists():
                broken.append(f"{md}: {target}")
                return match.group(0)
            new_path = os.path.relpath(old_target, md.parent).replace("\\", "/")
            return f"{match.group(1)}{new_path}{'#' + anchor if anchor else ''}{match.group(3)}"

        new_text = LINK.sub(rewrite, text)
        if new_text != text:
            changed[md] = new_text
    return changed, broken


def fix_references(root: Path, name: str, archived: Path, pending: dict[Path, str]) -> dict[Path, str]:
    """Point references to changes/<name>/ anywhere in the repo at the archived folder."""
    old_ref = re.compile(r"(?<![\w-])changes/" + re.escape(name) + r"/")
    new_ref = f"changes/archive/{archived.name}/"
    changed: dict[Path, str] = {}
    for md in markdown_files(root):
        text = pending.get(md) or md.read_text(encoding="utf-8")
        new_text = old_ref.sub(new_ref, text)
        if new_text != text or md in pending:
            changed[md] = new_text
    return changed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("name", help="change name, without the date prefix")
    parser.add_argument("--root", default=".", help="repository root (default: current directory)")
    parser.add_argument("--dry-run", action="store_true", help="report without writing")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    archived = find_archived(root, args.name)
    old_dir = root / "openspec" / "changes" / args.name

    inside, broken = fix_inside(archived, old_dir)
    changed = fix_references(root, args.name, archived, inside)

    for path in sorted(changed):
        print(f"{'would fix' if args.dry_run else 'fixed'}: {path.relative_to(root).as_posix()}")
        if not args.dry_run:
            path.write_text(changed[path], encoding="utf-8", newline="\n")
    for item in broken:
        print(f"broken before archiving (left as is): {item}")
    print(f"{len(changed)} file(s) {'to fix' if args.dry_run else 'fixed'}, {len(broken)} broken link(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
