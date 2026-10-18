"""Task data model for Week 2 study planner."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represents a study task with title, importance, effort, and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate that importance is within the 1-5 range."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Return days remaining until deadline (0 if already due or overdue)."""
        days = (self.deadline - today).days
        return max(0, days)
