"""Report when a complete study plan exceeds the available time budget."""

from shared.contract import Task


class InfeasiblePlan(Exception):
    """Carry the required and available hours for an infeasible plan."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        """Store the total required effort and the available study hours."""
        self.needed_h = needed_h
        self.available_h = available_h

    def __str__(self) -> str:
        """Describe the required effort and the available time budget."""
        return f"Need {self.needed_h} hours but {self.available_h} hours available."


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan if completing all tasks exceeds available_h.

    An empty list requires zero hours. The task list is not modified.
    """
    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
