"""Pure text formatting for study plans and optional CLI statistics."""

from shared.contract import Block


def render(blocks: list[Block]) -> str:
    """Align allocated hours while preserving titles, order and duplicates."""
    width = max((len(block.task.title) for block in blocks), default=0)
    return "\n".join(
        f"{index}. {block.task.title} {'.' * (width - len(block.task.title) + 3)} {block.hours:g} h"
        for index, block in enumerate(blocks, start=1)
    )


def render_summary(
    blocks: list[Block], total_hours: float, remaining_hours: float
) -> str:
    """Return verbose statistics; total_hours is the available time budget."""
    return (
        f"Tasks selected: {len(blocks)}\n"
        f"Available hours: {total_hours:g} h\n"
        f"Allocated hours: {sum(block.hours for block in blocks):g} h\n"
        f"Remaining hours: {remaining_hours:g} h"
    )
