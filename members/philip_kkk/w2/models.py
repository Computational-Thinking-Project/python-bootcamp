from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Store a study task's title, importance, effort, and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Reject importance values outside the supported range of 1 to 5."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Return days until the deadline, clamping overdue tasks to zero."""
        days = (self.deadline - today).days

        return max(0, days)
