import csv
import json
from datetime import date
from pathlib import Path

from members.johannguyen015.w2.models import Task


def load_tasks(path: str | Path) -> list[Task]:
    tasks: list[Task] = []
    file_path = Path(path)

    with file_path.open(mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)

        for line_num, row in enumerate(reader, start=2):
            if not row or all(field.strip() == "" for field in row):
                continue
            if len(row) != 4:
                raise ValueError(f"Invalid format at line {line_num}: expected 4 columns")

            title = row[0].strip()
            try:
                importance = int(row[1].strip())
                effort_h = float(row[2].strip())
                deadline = date.fromisoformat(row[3].strip())
                task = Task(title=title, importance=importance, effort_h=effort_h, deadline=deadline)
            except Exception as exc:
                raise ValueError(f"Invalid task data at line {line_num}: {exc}") from exc

            tasks.append(task)

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]
    file_path = Path(path)
    with file_path.open(mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
