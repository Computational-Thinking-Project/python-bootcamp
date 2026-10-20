import argparse
import sys
from datetime import date
from math import isfinite
from pathlib import Path

from ..w2.io_utils import load_tasks


def main(argv: list[str] | None = None) -> int:
    """Load tasks and print a prioritised plan within the available hours."""
    parser = argparse.ArgumentParser(
        description="Create a study plan from a tasks CSV."
    )
    parser.add_argument("csv_file", type=Path, help="Path to the tasks CSV")
    parser.add_argument(
        "--hours", type=float, required=True, help="Available study hours"
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="Reference date (YYYY-MM-DD)",
    )
    args = parser.parse_args(argv)

    if not isfinite(args.hours) or args.hours <= 0:
        parser.error("hours must be a positive finite number")

    try:
        tasks = load_tasks(args.csv_file)
    except FileNotFoundError:
        print(f"Error: Tasks file not found: {args.csv_file}", file=sys.stderr)
        return 1
    except (OSError, ValueError) as err:
        print(f"Error: {err}", file=sys.stderr)
        return 1

    sorted_tasks = sorted(
        tasks,
        key=lambda task: task.importance / max(1, task.days_left(args.today)),
        reverse=True,
    )

    remaining_hours = args.hours
    index = 1
    print(f"Tonight ({args.hours} h):")

    for task in sorted_tasks:
        if remaining_hours <= 0:
            break

        allocated_hours = min(task.effort_h, remaining_hours)
        if allocated_hours <= 0:
            continue

        print(f"  {index}. {task.title} - {allocated_hours:g} h")
        remaining_hours -= allocated_hours
        index += 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
