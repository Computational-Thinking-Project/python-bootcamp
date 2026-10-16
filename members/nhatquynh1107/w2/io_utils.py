import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    tasks = []

    with open(path, encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            line_number = reader.line_num

            try:
                if None in row or any(value is None for value in row.values()):
                    raise ValueError()

                task = Task(
                    title=row["title"], importance=int(row["importance"]), effort_h=float(row["effort_h"]), deadline=date.fromisoformat(row["deadline"])
                    )
                tasks.append(task)

            except (ValueError, TypeError, KeyError) as error:
                raise ValueError(
                    f"Invalid data at line {line_number}: {error}"
                ) from error

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    data = []

    for task in tasks:
        data.append({
            "title": task.title, "importance": task.importance, "effort_h": task.effort_h, "deadline": task.deadline.isoformat()
            })

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
