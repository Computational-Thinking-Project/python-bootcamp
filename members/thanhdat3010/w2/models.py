"""Task data model for Week 2 study planner."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """A study task with importance, estimated effort in hours, and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate importance range and normalize effort."""
        if not isinstance(self.importance, int) or not (1 <= self.importance <= 5):
            raise ValueError("importance must be 1-5")
        if self.effort_h < 0:
            raise ValueError("effort_h must be non-negative")
        self.effort_h = float(self.effort_h)

    def days_left(self, today: date) -> int:
        """Return days left until deadline; returns 0 if overdue."""
        return max(0, (self.deadline - today).days)
