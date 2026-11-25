#!/usr/bin/env python3
"""Writes the Moon's final answer to /output/entry.txt.

One line, stdlib only, no network, no reads outside this repo.
No trailing newline: the file is exactly the entry line.
"""

import os

ENTRY = "Four billion years of howling, wishing, and 2 a.m. promises. I'm a rock, not your therapist. Go to bed."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
