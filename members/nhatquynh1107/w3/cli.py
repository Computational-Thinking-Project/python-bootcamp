"""Build a study plan from the command line using the Week 2 CSV loader."""

import argparse
import sys
from datetime import date

from members.nhatquynh1107.w2.io_utils import load_tasks
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def main(argv: list[str] | None = None) -> int:
    """Print a plan and return 0, 1 for a missing file or 2 for invalid data.

    An explicit --today makes prioritisation reproducible; otherwise the
    current local date is used. Argparse exits with code 2 for malformed
    arguments and code 0 for --help.
    """
    parser = argparse.ArgumentParser(description="Study Planner CLI")
    parser.add_argument("csv_file")
    parser.add_argument("--hours", type=float, required=True)
    parser.add_argument("--today", type=date.fromisoformat, default=None)
    args = parser.parse_args(argv)

    if args.hours <= 0:
        print("Error: hours must be a positive number", file=sys.stderr)
        return 2

    try:
        tasks = load_tasks(args.csv_file)
    except FileNotFoundError:
        print(f"Error: Tasks file not found: {args.csv_file}", file=sys.stderr)
        return 1
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2

    today = args.today if args.today is not None else date.today()
    ordered_tasks = prioritise(tasks, today)
    blocks = allocate(ordered_tasks, args.hours)

    print(f"Tonight ({args.hours:.1f} h):")
    print(render(blocks))
    return 0


if __name__ == "__main__":
    sys.exit(main())
