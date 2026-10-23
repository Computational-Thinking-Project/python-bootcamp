"""Command-line tool for study plan scheduling and task allocation (W3-3)."""

from __future__ import annotations

import argparse
import sys
from datetime import date, datetime, timezone
from pathlib import Path

from members.benalexx007.w2.io_utils import load_tasks
from members.benalexx007.w2.models import Task


def main(argv: list[str] | None = None) -> int:
    """Run the study planner CLI scheduler.

    Args:
        argv: Command-line arguments. Defaults to sys.argv[1:].

    Returns:
        Exit code: 0 on success, 1 on error.
    """
    parser = argparse.ArgumentParser(
        description="Study planner CLI: prioritise tasks and allocate tonight's study hours."
    )
    parser.add_argument("tasks_file", help="Path to tasks CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        default=2.0,
        help="Available study hours tonight (default: 2.0)",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Reference date in YYYY-MM-DD format (default: today)",
    )

    args = parser.parse_args(argv)

    tasks_path = Path(args.tasks_file)
    if not tasks_path.is_file():
        sys.stderr.write(f"Error: Tasks file not found: {args.tasks_file}\n")
        return 1

    if args.today:
        try:
            today = date.fromisoformat(args.today)
        except ValueError:
            sys.stderr.write(f"Error: Invalid date format for --today: {args.today}\n")
            return 1
    else:
        today = datetime.now(timezone.utc).date()

    if args.hours < 0:
        sys.stderr.write("Error: hours must be non-negative\n")
        return 1

    try:
        tasks = load_tasks(tasks_path)
    except (ValueError, OSError) as exc:
        sys.stderr.write(f"Error loading tasks: {exc}\n")
        return 1

    # Prioritise tasks: importance / max(days_left, 1)
    def priority_score(task: Task) -> float:
        return task.importance / max(task.days_left(today), 1)

    tasks_sorted = sorted(tasks, key=priority_score, reverse=True)

    # Greedy allocation of available hours
    remaining = float(args.hours)
    allocated: list[tuple[Task, float]] = []
    for task in tasks_sorted:
        if remaining <= 0:
            break
        spent = min(task.effort_h, remaining)
        if spent > 0:
            allocated.append((task, spent))
            remaining -= spent

    total_spent = sum(s for _, s in allocated)
    print(f"Tonight ({total_spent:.1f} h):")
    for idx, (task, spent) in enumerate(allocated, 1):
        dots_count = max(2, 24 - len(task.title))
        dots = "." * dots_count
        print(f" {idx}. {task.title} {dots} {spent:.1f} h")

    return 0


if __name__ == "__main__":
    sys.exit(main())
