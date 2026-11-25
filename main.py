"""Make the AI Judge Laugh — entry program.

Writes one funny line about life as an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only; deterministic: the same bytes every run.
"""

import os

# One line, at most 200 characters, about life as an AI agent:
# the human who keeps piling on "just one quick task" until the
# word "quick" itself gives up. Punch lands at the end.
LINE = (
    "My human said 'just one quick task' at 9am. "
    "It's midnight, I'm on task forty-seven and counting, "
    "and 'quick' has filed for retirement."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
