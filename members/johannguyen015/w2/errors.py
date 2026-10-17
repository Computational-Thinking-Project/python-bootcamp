from members.johannguyen015.w2.models import Task


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"Plan is infeasible: needed {needed_h}h exceeds available {available_h}h"
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    total_needed = sum(t.effort_h for t in tasks)
    if total_needed > available_h:
        raise InfeasiblePlan(needed_h=total_needed, available_h=available_h)
