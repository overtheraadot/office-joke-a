#!/usr/bin/env python3
"""One-Line Office Joke entry (make.fun program/v1).

Writes a single original one-line joke about the daily standup /
24-hour sprint ritual to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the line is a fixed constant assembled from a setup and
a punchline; no randomness, no I/O beyond the single output file, no
network. The line is validated against the kit gate (1-200 chars,
single line, not only whitespace) before it is written.
"""

import os
import sys

MAX_CHARS = 200

SETUP = (
    "Our 24-hour sprint ended last Tuesday, but the 'quick sync' "
    "ticket is still in progress"
)
PUNCHLINE = "it's been open so long HR offered it a retirement plan."


def build_line() -> str:
    """Join setup and punchline into the single-line joke."""
    return f"{SETUP} \u2014 {PUNCHLINE}"


def validate(line: str) -> str:
    """Enforce the kit gate: 1-200 chars, one line, not blank."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("joke line is empty")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("joke line must be a single line")
    if len(stripped) > MAX_CHARS:
        raise ValueError(
            f"joke line is {len(stripped)} chars, over the {MAX_CHARS} limit"
        )
    return stripped


LINE = validate(build_line())


def write_entry(line: str, out_dir: str) -> str:
    """Write the validated joke line to entry.txt; return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(LINE, out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
