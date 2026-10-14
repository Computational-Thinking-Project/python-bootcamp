"""CLI: O(B + output size) time and O(n + T) space."""

import sys
from pathlib import Path

from .io_utils import load_tasks


def main() -> int:
    if len(sys.argv) > 2:
        print("Usage: python -m members.ai_wfox.w2 [CSV path]", file=sys.stderr)
        return 2
    path = (
        Path(sys.argv[1])
        if len(sys.argv) == 2
        else Path(__file__).resolve().parents[3] / "samples/tasks.csv"
    )
    try:
        tasks = load_tasks(path)
    except (OSError, ValueError) as exc:
        print(f"Cannot load tasks: {exc}", file=sys.stderr)
        return 1
    for task in tasks:
        print(
            f"{task.title}: importance {task.importance}, "
            f"effort {task.effort_h:g} h, deadline {task.deadline.isoformat()}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
