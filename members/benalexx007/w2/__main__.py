"""CLI runner for Week 2 tasks (W2-5)."""

from __future__ import annotations

from datetime import date
from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Load and print study tasks from sample CSV."""
    samples_dir = Path(__file__).resolve().parents[3] / "samples"
    csv_path = samples_dir / "tasks.csv"

    if not csv_path.is_file():
        print(f"Sample file not found: {csv_path}")
        return

    tasks = load_tasks(csv_path)
    today = date(2026, 10, 26)

    print(f"Loaded {len(tasks)} tasks from {csv_path.name} (as of {today}):")
    print("-" * 65)
    print(f"{'Task Title':<20} {'Importance':<12} {'Effort (h)':<12} {'Days Left'}")
    print("-" * 65)
    for task in tasks:
        print(
            f"{task.title:<20} {task.importance:<12} {task.effort_h:<12.1f} {task.days_left(today)}"
        )
    print("-" * 65)


if __name__ == "__main__":
    main()
