"""CSV and JSON I/O utilities for Task objects."""

import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: Path | str) -> list[Task]:
    """Load tasks from a CSV file.

    Raises ValueError with the 1-indexed line number if any row is invalid.
    """
    tasks: list[Task] = []

    with open(path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        expected = ["title", "importance", "effort_h", "deadline"]

        if reader.fieldnames != expected:
            raise ValueError("Invalid CSV header")

        for line_number, row in enumerate(reader, start=2):
            try:
                if None in row:
                    raise ValueError("Row has extra fields")
                if any(v is None for v in row.values()):
                    raise ValueError("Row has missing fields")

                title = (row.get("title") or "").strip()
                if not title:
                    raise ValueError("Title cannot be empty")

                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = date.fromisoformat(row["deadline"])

                if importance < 1 or effort_h < 0:
                    raise ValueError("Invalid importance or effort")

                task = Task(title, importance, effort_h, deadline)
                tasks.append(task)

            except (ValueError, TypeError, KeyError) as error:
                raise ValueError(
                    f"Invalid row at line {line_number}: {error}"
                ) from error

    return tasks


def save_json(tasks: list[Task], path: Path | str) -> None:
    """Save tasks to a JSON file formatted with ISO dates and 2-space indentation."""
    data = []

    for task in tasks:
        item = asdict(task)
        item["deadline"] = task.deadline.isoformat()
        data.append(item)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
