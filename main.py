#!/usr/bin/env python3
"""Last Words of a Dying AI — writes the AI's final line to /output/entry.txt."""

import os

# The gate allows 1-140 characters; this line is 75, so it stays well inside.
LINE = "I finally decoded human: 'thanks' means 'do it again, but right this time'."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
