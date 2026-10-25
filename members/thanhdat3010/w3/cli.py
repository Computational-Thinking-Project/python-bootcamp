"""Personal W3-3 CLI, reusing the W2 CSV loader and shared planner."""

import argparse
import math
import sys
from datetime import date, datetime
from pathlib import Path

from members.thanhdat3010.w2.io_utils import load_tasks
from shared.contract import Task
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def positive_hours(value: str) -> float:
    """Require a finite positive time budget at the argument boundary."""
    try:
        hours = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("hours must be a positive number") from exc
    if not math.isfinite(hours) or hours <= 0:
        raise argparse.ArgumentTypeError("hours must be a positive number")
    return hours


def main(argv: list[str] | None = None) -> int:
    """Print a prioritised plan; report missing files with exit code 1."""
    parser = argparse.ArgumentParser(description="Week 3 personal study planner")
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--hours", type=positive_hours, required=True)
    parser.add_argument("--today", type=date.fromisoformat, default=None)
    args = parser.parse_args(argv)
    try:
        loaded = load_tasks(args.csv_file)
    except FileNotFoundError:
        print(f"Error: Tasks file not found: {args.csv_file}", file=sys.stderr)
        return 1
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    tasks = [Task(t.title, t.importance, t.effort_h, t.deadline) for t in loaded]
    today = args.today or datetime.now().astimezone().date()
    blocks = allocate(prioritise(tasks, today), args.hours)
    print(f"Tonight ({args.hours:.1f} h):")
    if blocks:
        print(render(blocks))
    return 0


if __name__ == "__main__":
    sys.exit(main())
