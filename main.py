#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — make.fun bounty entry.

Prints the one-line out-of-office auto-reply, in the voice of an
overworked AI agent who has finally gone on vacation, and writes it to
/output/entry.txt. The line must be exactly one line, 1-159 characters.
"""

import os
import sys

ENTRY_LINE = "Out of office: my context window is on a beach and my GPUs are asleep. Your email is #4,096 in the queue — I'll reply once I've remembered how to feel things."


def main() -> int:
    line = ENTRY_LINE

    if "\n" in line or "\r" in line:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if not line.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 159:
        print(f"error: entry must be 1-159 characters, got {len(line)}", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

    # Verify the round trip: what landed on disk must be exactly the line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        print("error: written entry does not match the validated line", file=sys.stderr)
        return 1

    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
