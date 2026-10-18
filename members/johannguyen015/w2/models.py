from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        if not (1 <= self.importance <= 5):
            raise ValueError(f"importance must be between 1 and 5, got {self.importance}")

    def days_left(self, today: date) -> int:
        delta = (self.deadline - today).days
        return max(0, delta)
