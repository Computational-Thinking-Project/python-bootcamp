import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Read tasks from CSV, reporting invalid rows with their line number."""
    tasks = []

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for line_num, row in enumerate(reader, start=2):
            if None in row:
                raise ValueError(f"Invalid data in line {line_num}: extra fields")

            try:
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = date.fromisoformat(row["deadline"])
                current_task = Task(row["title"], importance, effort_h, deadline)
            except (ValueError, TypeError, KeyError) as exc:
                raise ValueError(f"Invalid data in line {line_num}: {exc}") from exc
            tasks.append(current_task)

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save tasks to JSON, converting deadline dates to strings."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump([task.__dict__ for task in tasks], file, indent=2, default=str)
