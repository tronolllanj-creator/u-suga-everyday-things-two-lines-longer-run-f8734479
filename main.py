"""
# Entry validated: output is 1-400 chars, exactly two lines, one sentence each.
Entrypoint for the grader.

Writes the exact required text to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
from pathlib import Path

TEXT = """An escalator is a metal zipper of stairs that pulls people upward between floors.
This maps the interlocking steps to a zipper, but it leaves out that zippers are pulled by hand while the escalator is driven by electric motors."""


def main() -> None:
    # Validate TEXT according to the strict rules
    lines = TEXT.split("\n")
    valid = (
        1 <= len(TEXT) <= 400
        and bool(TEXT.strip())
        and len(lines) == 2
        and all(
            bool(line.strip())
            and line.strip().endswith(".")
            and line.strip().count(".") == 1
            for line in lines
        )
    )
    if not valid:
        raise ValueError("TEXT fails validation rules.")

    # Determine output directory and path
    out_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    out_dir = Path(out_dir_env)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"

    # Write TEXT with no trailing newline
    out_path.write_text(TEXT, encoding="utf-8")

    # Print output path and character count
    print(f"{out_path}\n{len(TEXT)}")


if __name__ == "__main__":
    main()