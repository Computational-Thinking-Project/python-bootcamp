from .models import Task


class InfeasiblePlan(Exception):
    """Report that the required study hours exceed the available hours."""

    needed_h: float
    available_h: float

    def __init__(self, needed_h: float, available_h: float) -> None:
        """Store the required and available hours for the failed plan."""
        self.needed_h = needed_h
        self.available_h = available_h

    def __str__(self) -> str:
        """Describe the required hours and the available time budget."""
        return f"Need {self.needed_h} hours, {self.available_h} hours available."


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan when completing all tasks exceeds the time budget."""
    total_effort = sum(task.effort_h for task in tasks)
    if total_effort > available_h:
        raise InfeasiblePlan(total_effort, available_h)
