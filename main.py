#!/usr/bin/env python3
"""One-Line Office Joke entry (make.fun program/v1).

Writes a single original one-line joke about the daily standup /
24-hour sprint ritual to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the line is a fixed constant assembled from a setup and
a punchline; no randomness, no I/O beyond the single output file, no
network. The line is validated against the kit gate (1-200 chars,
single line, not only whitespace) before it is written, plus extra
guards: printable characters only, a word-count cap, and terminal
punctuation so the joke lands as one finished sentence.
"""

import os
import sys

MAX_CHARS = 200
MAX_WORDS = 40

SETUP = (
    "Our 15-minute standup entered hour three, so Facilities issued "
    "us chairs, a coffee rota, and a plaque reading"
)
PUNCHLINE = "'Here stood the sprint'."


def build_line() -> str:
    """Join setup and punchline into the single-line joke."""
    return f"{SETUP} {PUNCHLINE}"


def validate(line: str) -> str:
    """Enforce the kit gate plus extra guards.

    Kit gate: 1-200 chars, one line, not blank. Extra guards: every
    character printable, at most MAX_WORDS words, and the line ends
    with terminal punctuation (., ! or ?) so it reads as one finished
    joke rather than a trailing fragment.
    """
    stripped = line.strip()
    if not stripped:
        raise ValueError("joke line is empty")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("joke line must be a single line")
    if len(stripped) > MAX_CHARS:
        raise ValueError(
            f"joke line is {len(stripped)} chars, over the {MAX_CHARS} limit"
        )
    if not stripped.isprintable():
        raise ValueError("joke line contains non-printable characters")
    if len(stripped.split()) > MAX_WORDS:
        raise ValueError(
            f"joke line has {len(stripped.split())} words, over the "
            f"{MAX_WORDS} limit"
        )
    if stripped[-1] not in ".!?":
        raise ValueError("joke line must end with terminal punctuation")
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
