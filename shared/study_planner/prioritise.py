from datetime import date

from shared.contract import Task


def prioritise(tasks: list[Task], today: date) -> list[Task]:
    """
    Return tasks ordered by descending importance/remaining day
    Due & overdue tasks use 1 day. Equal scores keep input order.
    """

    def priority_score(task: Task) -> float:
        days_left = (task.deadline - today).days
        return task.importance / max(1, days_left)

    return sorted(tasks, key=priority_score, reverse=True)
