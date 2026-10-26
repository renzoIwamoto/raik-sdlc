#!/usr/bin/env python3
"""Check WCAG 2.x contrast ratios between color pairs. Stdlib only.

Colors are hex (#rgb or #rrggbb) or token names read from a CSS file with --tokens
(custom properties such as `--color-ink: #1f2421;`, matched as `ink` or `color-ink`).

Usage:
    python contrast.py [--tokens index.css] [--min 4.5] FG BG [FG BG ...]

Exit code 1 if any pair is below --min (4.5 for normal text, 3 for large text and UI parts).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

TOKEN = re.compile(r"--([\w-]+)\s*:\s*(#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?)\s*;")


def load_tokens(path: str | None) -> dict[str, str]:
    if not path:
        return {}
    return {name: value for name, value in TOKEN.findall(Path(path).read_text(encoding="utf-8"))}


def resolve(color: str, tokens: dict[str, str]) -> str:
    if color.startswith("#"):
        return color
    for name in (color, f"color-{color}"):
        if name in tokens:
            return tokens[name]
    raise SystemExit(f"Unknown color '{color}'. Use #hex or a token defined as a hex value in --tokens.")


def luminance(hex_color: str) -> float:
    digits = hex_color.lstrip("#")
    if len(digits) == 3:
        digits = "".join(c * 2 for c in digits)
    if len(digits) != 6 or not re.fullmatch(r"[0-9a-fA-F]{6}", digits):
        raise SystemExit(f"Not a #rgb or #rrggbb color: {hex_color}")

    def channel(i: int) -> float:
        c = int(digits[i : i + 2], 16) / 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = channel(0), channel(2), channel(4)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg: str, bg: str) -> float:
    lighter, darker = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("colors", nargs="+", help="pairs: FG BG [FG BG ...]")
    parser.add_argument("--tokens", help="CSS file with color custom properties")
    parser.add_argument("--min", type=float, default=4.5, help="minimum ratio (default 4.5)")
    args = parser.parse_args(argv)
    if len(args.colors) % 2:
        parser.error("colors must come in FG BG pairs")

    tokens = load_tokens(args.tokens)
    failures = 0
    for fg, bg in zip(args.colors[::2], args.colors[1::2]):
        value = ratio(resolve(fg, tokens), resolve(bg, tokens))
        ok = value >= args.min
        failures += not ok
        print(f"{'pass' if ok else 'FAIL'}  {value:5.2f}:1  {fg} on {bg}")
    print(f"{failures} pair(s) below {args.min}:1")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
