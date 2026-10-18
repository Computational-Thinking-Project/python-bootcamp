from shared.contract import Block, Task


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    """Allocate available study hours greedily to prioritised tasks.

    Args:
        tasks: Prioritised list of tasks to allocate study time to.
        hours: Total available study hours.

    Returns:
        List of Block instances representing allocated study time per task.

    Raises:
        ValueError: If hours is negative.
    """
    if hours < 0:
        raise ValueError("hours must be non-negative")
    if not tasks or hours == 0:
        return []

    blocks: list[Block] = []
    remaining = float(hours)

    for task in tasks:
        if remaining <= 0:
            break
        alloc = min(task.effort_h, remaining)
        if alloc > 0:
            blocks.append(Block(task=task, hours=alloc))
            remaining -= alloc

    return blocks
