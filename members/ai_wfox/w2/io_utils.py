"""CSV input and JSON output for tasks."""

import csv
import json
from datetime import date
from pathlib import Path

from .models import Task

FIELDS = {"title", "importance", "effort_h", "deadline"}


def load_tasks(path: str | Path) -> list[Task]:
    """O(B) time, O(n + T) space: B input chars, n tasks, T title chars."""
    tasks = []
    with Path(path).open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, strict=True)
        try:
            header = reader.fieldnames or []
            if len(header) != len(FIELDS) or set(header) != FIELDS:
                raise ValueError(
                    "line 1: expected title,importance,effort_h,deadline header"
                )
            for row in reader:
                try:
                    if None in row or None in row.values():
                        raise ValueError("expected four fields")
                    title = row["title"].strip()
                    if not title:
                        raise ValueError("title must not be empty")
                    tasks.append(
                        Task(
                            title,
                            int(row["importance"]),
                            float(row["effort_h"]),
                            date.fromisoformat(row["deadline"].strip()),
                        )
                    )
                except ValueError as exc:
                    raise ValueError(f"line {reader.line_num}: {exc}") from exc
        except csv.Error as exc:
            raise ValueError(f"line {reader.reader.line_num}: {exc}") from exc
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """O(n + T) time and space for n tasks and T title characters."""
    records = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]
    with Path(path).open("w", encoding="utf-8") as stream:
        json.dump(records, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")
