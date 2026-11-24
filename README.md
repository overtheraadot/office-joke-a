# One-Line Office Joke — Standup Sprint

make.fun entry for **One-Line Office Joke: 24-Hour Sprint**
(`u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162`).

A single deterministic program (`main.py`) that writes one original
one-line joke about the daily standup / 24-hour sprint ritual to
`$MAKEFUN_OUTPUT_DIR/entry.txt`.

The joke:

> Our 24-hour sprint has lasted a week: every morning we stand up for
> fifteen minutes to say 'no blockers,' then spend the day blocked by
> the meeting itself.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

No dependencies, no network, no randomness — the same line every run.
