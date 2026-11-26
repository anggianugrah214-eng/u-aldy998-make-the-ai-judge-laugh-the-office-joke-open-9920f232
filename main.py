#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

A program/v1 entry for make.fun competition
u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.

The program writes a single one-line joke about office life (at most 200
characters; this line is 79) to /output/entry.txt.

It is fully deterministic: the same line is written on every run, with no
input, no network access and no randomness.
"""

import os

# One line, 79 characters. The setup is a real corporate platitude every
# office worker has heard ("bring your whole self to work"); the turn is
# the one thing nobody is supposed to bring — a resignation letter. Chosen
# over 15 other candidates after scoring them against the published judge
# brief (see candidates.md in the build workspace): genuine one-line office
# joke first, then a real surprise turn, then recognition (the quitting
# fantasy, delivered deadpan), then tight wording, then freshness — no
# printer, no Monday morning, no reply-all, no meeting-could-have-been-an-
# email. Runner-up: "The meeting ended early, which HR is now investigating
# as a possible security incident." (87 characters).
SETUP = "HR said to bring my whole self to work, "
PUNCHLINE = "so I brought my resignation letter too."


def compose_joke(setup: str, punchline: str) -> str:
    """Assemble the one-liner from its setup and punchline parts."""
    return f"{setup}{punchline}"


LINE = compose_joke(SETUP, PUNCHLINE)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
