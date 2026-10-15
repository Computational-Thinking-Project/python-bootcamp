"""CSV parsing for study tasks (Team T-W2)."""

import csv
from datetime import date
from pathlib import Path

from shared.contract import Task


def parse_csv(path: Path | str) -> list[Task]:
    """Parse a CSV file containing study tasks and return a list of Task objects.

    Args:
        path: Path to the CSV file.

    Returns:
        A list of Task objects parsed from the CSV.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If header is invalid, row format is malformed, or data validation fails.
    """
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"Tasks file not found: {file_path}")

    tasks: list[Task] = []

    with file_path.open(encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        if header is None:
            return []

        expected_cols = ["title", "importance", "effort_h", "deadline"]
        normalized_header = [c.strip().lower() for c in header]
        if normalized_header != expected_cols:
            raise ValueError(f"Invalid CSV header at line 1: expected {expected_cols}, got {header}")

        for line_no, row in enumerate(reader, start=2):
            if not row or not any(field.strip() for field in row):
                continue

            if len(row) != 4:
                raise ValueError(
                    f"Invalid column count at line {line_no}: expected 4 fields, got {len(row)}"
                )

            title = row[0].strip()
            if not title:
                raise ValueError(f"Empty title at line {line_no}")

            try:
                importance = int(row[1].strip())
            except ValueError as exc:
                raise ValueError(f"Invalid importance at line {line_no}: must be an integer") from exc

            if not 1 <= importance <= 5:
                raise ValueError(
                    f"Invalid importance at line {line_no}: must be between 1 and 5, got {importance}"
                )

            try:
                effort_h = float(row[2].strip())
            except ValueError as exc:
                raise ValueError(f"Invalid effort_h at line {line_no}: must be a float") from exc

            if effort_h < 0:
                raise ValueError(
                    f"Invalid effort_h at line {line_no}: must be non-negative, got {effort_h}"
                )

            try:
                deadline = date.fromisoformat(row[3].strip())
            except ValueError as exc:
                raise ValueError(
                    f"Invalid deadline date format at line {line_no} (expected YYYY-MM-DD): {row[3]}"
                ) from exc

            tasks.append(
                Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
            )

    return tasks
