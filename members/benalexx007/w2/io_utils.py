"""CSV loading and JSON serialization utilities for tasks (W2-2)."""

from __future__ import annotations

import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: Path | str) -> list[Task]:
    """Load study tasks from a CSV file.

    Raises ValueError with the line number if any row has invalid fields.
    """
    file_path = Path(path)
    tasks: list[Task] = []

    with file_path.open(encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        if header is None:
            return []

        expected_cols = ["title", "importance", "effort_h", "deadline"]
        normalized_header = [c.strip().lower() for c in header]
        if normalized_header != expected_cols:
            raise ValueError(
                f"Invalid header at line 1: expected {expected_cols}, got {header}"
            )

        for line_no, row in enumerate(reader, start=2):
            if not row or not any(field.strip() for field in row):
                continue

            if len(row) != 4:
                raise ValueError(f"Invalid column count at line {line_no}: expected 4")

            title = row[0].strip()
            if not title:
                raise ValueError(f"Empty title at line {line_no}")

            try:
                importance = int(row[1].strip())
            except ValueError as exc:
                raise ValueError(
                    f"Invalid importance at line {line_no}: must be an integer"
                ) from exc

            try:
                effort_h = float(row[2].strip())
            except ValueError as exc:
                raise ValueError(
                    f"Invalid effort_h at line {line_no}: must be a float"
                ) from exc

            try:
                deadline = date.fromisoformat(row[3].strip())
            except ValueError as exc:
                raise ValueError(
                    f"Invalid deadline date format at line {line_no}: expected YYYY-MM-DD"
                ) from exc

            try:
                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
            except ValueError as exc:
                raise ValueError(f"Invalid task data at line {line_no}: {exc}") from exc

            tasks.append(task)

    return tasks


def save_json(tasks: list[Task], path: Path | str) -> None:
    """Serialize list of Task objects to a JSON file."""
    file_path = Path(path)
    data = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]
    file_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
