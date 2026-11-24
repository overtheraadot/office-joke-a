#!/usr/bin/env python3
"""One-Line Office Joke entry (make.fun program/v1).

Writes a single original one-line joke about the daily standup /
24-hour sprint ritual to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the line is a fixed constant; no randomness, no I/O
beyond the single output file, no network.
"""

import os
import sys

LINE = (
    "Our 24-hour sprint has lasted a week: every morning we stand up "
    "for fifteen minutes to say 'no blockers,' then spend the day "
    "blocked by the meeting itself."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
