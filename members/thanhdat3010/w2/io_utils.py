"""CSV loading and JSON serialization utilities for tasks."""

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

        # Validate expected header columns
        expected_cols = ["title", "importance", "effort_h", "deadline"]
        normalized_header = [c.strip().lower() for c in header]
        if normalized_header != expected_cols:
            raise ValueError(f"Invalid header at line 1: expected {expected_cols}")

        for line_no, row in enumerate(reader, start=2):
            if not row or not any(field.strip() for field in row):
                continue

            if len(row) != 4:
                raise ValueError(
                    f"Invalid column count at line {line_no}: expected 4 fields, got {len(row)}"
                )

            try:
                title = row[0].strip()
                if not title:
                    raise ValueError("title cannot be empty")
                importance = int(row[1].strip())
                effort_h = float(row[2].strip())
                deadline = date.fromisoformat(row[3].strip())
                task = Task(title, importance, effort_h, deadline)
            except Exception as exc:
                raise ValueError(f"Invalid task data at line {line_no}: {exc}") from exc

            tasks.append(task)

    return tasks


def save_json(tasks: list[Task], path: Path | str) -> None:
    """Save a list of Task objects to a JSON file."""
    out_path = Path(path)
    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]
    out_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
