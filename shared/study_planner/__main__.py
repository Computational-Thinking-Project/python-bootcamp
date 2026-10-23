"""CLI entry point and core pipeline for the study planner (Team T-W3)."""

import argparse
import sys
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def main(argv: list[str] | None = None) -> int:
    """CLI entry point. Trả về exit code (0: thành công, khác 0: lỗi)."""
    parser = argparse.ArgumentParser(description="Study planner CLI")
    parser.add_argument("csv_file", type=str, help="Path to tasks CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        default=None,
        help="Total available study hours",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Reference date for prioritisation (YYYY-MM-DD, defaults to today)",
    )

    args = parser.parse_args(argv)

    today = date.fromisoformat(args.today) if args.today else date.today()
    tasks = parse_csv(Path(args.csv_file))
    prioritised = prioritise(tasks, today=today)
    blocks = allocate(prioritised, hours=args.hours)
    output = render(blocks)
    if output:
        print(output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
