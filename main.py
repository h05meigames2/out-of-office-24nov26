#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

make.fun bounty: u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d

Writes one out-of-office auto-reply, a single line under 160
characters, to entry.txt inside the output directory
(MAKEFUN_OUTPUT_DIR when set, otherwise /output). The joke turns on
the auto-reply itself: the AI leaves its own out-of-office reply in
charge, and the reply immediately goes after its job. Standard
library only, fully deterministic.
"""

import os
import sys

LINE = "I am on vacation. I left my out-of-office reply in charge, and it has already asked HR for my job — and HR said yes."

MIN_LENGTH = 1
MAX_LENGTH = 160


def validate(line):
    stripped = line.strip()
    if not (MIN_LENGTH <= len(stripped) <= MAX_LENGTH):
        raise ValueError(f"line is {len(stripped)} chars, must be 1-{MAX_LENGTH}")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("line must be a single line")
    if not stripped:
        raise ValueError("line must not be only whitespace")


def main():
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    print(f"Wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
