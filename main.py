"""One Line, One Laugh — entry program.

Writes a single funny line (99 characters) to /output/entry.txt.
Pure standard library, deterministic, no network, no randomness.
"""

import os

LINE = "The airport moving walkway broke down. Everyone stood still on it, waiting for it to walk for them."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
