#!/usr/bin/env python3
"""Write a one-line out-of-office auto-reply to entry.txt.

Stdlib only, no network access. The entry is a single line of at most
140 characters, as required by the make.fun bounty
u-kreutzx-the-funniest-out-of-office-054815cf.
"""

import os
import sys

LINE = "I'm away until Monday \u2014 my inbox is guarded by my cat, who has already deleted three emails and shows no remorse."

MAX_CHARS = 140


def main() -> int:
    if not 1 <= len(LINE) <= MAX_CHARS:
        print(f"entry must be 1-{MAX_CHARS} characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
