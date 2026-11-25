#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Writes a single line of office comedy (at most 200 characters) to
/output/entry.txt.
"""

import os

JOKE = "Our printer got promoted to manager \u2014 ten years of jamming, blaming IT, and taking credit for everyone else's work, and HR called it management material."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
