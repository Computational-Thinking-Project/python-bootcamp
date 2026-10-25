"""CLI entry point and core pipeline for the study planner (Team T-W3)."""

import argparse
import sys
from csv import Error as CSVError
from datetime import date
from math import isfinite
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.errors import InfeasiblePlan, check_feasible
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def main(argv: list[str] | None = None) -> int:
    """Validate input and print a complete study plan.

    Return 0 on success, 1 for file or budget errors, and 2 for invalid data.
    Expected input errors are reported on stderr without a traceback.
    Argparse exits with code 2 for missing arguments and 0 for --help.
    """
    parser = argparse.ArgumentParser(description="Study planner CLI")
    parser.add_argument("csv_file", type=str, help="Path to tasks CSV file")
    parser.add_argument(
        "--hours",
        required=True,
        help="Positive, finite study hours available to complete all tasks",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Reference date for prioritisation (YYYY-MM-DD, defaults to today)",
    )

    args = parser.parse_args(argv)

    try:
        hours = float(args.hours)
    except ValueError:
        print("Error: hours must be a positive number", file=sys.stderr)
        return 2
    if not isfinite(hours) or hours <= 0:
        print("Error: hours must be a positive number", file=sys.stderr)
        return 2

    try:
        today = (
            date.fromisoformat(args.today) if args.today is not None else date.today()
        )
    except ValueError:
        print("Error: today must be a valid date in YYYY-MM-DD format", file=sys.stderr)
        return 2

    try:
        tasks = parse_csv(Path(args.csv_file))
        if any(not isfinite(task.effort_h) for task in tasks):
            raise ValueError("effort_h must be a finite number")
    except FileNotFoundError:
        print(f"Error: Tasks file not found: {args.csv_file}", file=sys.stderr)
        return 1
    except (ValueError, CSVError) as error:
        print(f"Error: Invalid CSV format: {error}", file=sys.stderr)
        return 2
    except OSError as error:
        print(f"Error: Could not read tasks file: {error}", file=sys.stderr)
        return 1

    if not tasks:
        print(f"Error: File is empty: {args.csv_file}", file=sys.stderr)
        return 1

    try:
        check_feasible(tasks, hours)
    except InfeasiblePlan as error:
        print(
            f"Error: InfeasiblePlan: {error.needed_h:g} hours needed exceeds "
            f"{error.available_h:g} hours available",
            file=sys.stderr,
        )
        return 1

    prioritised = prioritise(tasks, today=today)
    blocks = allocate(prioritised, hours=hours)
    output = render(blocks)
    if output:
        print(output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
