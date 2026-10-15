"""CLI runner for week 2 study planner demo."""

import sys
from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Load sample CSV and print loaded tasks."""
    if len(sys.argv) > 1:
        target_path = Path(sys.argv[1])
    else:
        target_path = Path("samples/tasks.csv")
        if not target_path.exists():
            repo_root = Path(__file__).resolve().parents[3]
            target_path = repo_root / "samples" / "tasks.csv"

    tasks = load_tasks(target_path)
    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()
