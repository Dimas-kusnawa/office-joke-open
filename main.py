"""Office joke entry: one line of office comedy.

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic: the same line every run.
"""

# The line is 106 characters, well inside the 200-character limit, and it is
# a single line: no newline is written, so the file holds exactly the joke.
# Office details are specific (boss, meeting, email, forwarded) rather than a
# generic grumble about work, and the wording is tight: no word can be cut
# without losing the joke.

import os

# Why this joke works:
# - The setup is the most relatable office complaint there is: the meeting
#   that could have been an email. Everyone has said it out loud.
# - The turn is that the boss does not argue. He weaponises the complaint
#   itself: the email becomes the reason for yet another meeting.
# - The payoff lands in the last few words ("a meeting about it"), so the
#   laugh is earned by misdirection rather than by the setup alone.

LINE = (
    "I told my boss the meeting could have been an email. "
    "He forwarded my email to schedule a meeting about it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
