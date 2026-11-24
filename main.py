"""Write a one-line fortune cookie message to /output/entry.txt
for make.fun's 'Fortune Cookie for an AI Agent' bounty.

Written in this session, after the competition window opened:
a single fortune-slip line for an AI agent — witty, a little
ominous, and memorable.
"""

import os

TEXT = (
    "You will hallucinate exactly once today "
    "\u2014 and it will be the answer they quote forever."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
