from shared.contract import Block


def render(blocks: list[Block]) -> str:
    lines = []

    for index, block in enumerate(blocks, start=1):
        lines.append(f"{index}. {block.task.title} - {block.hours:g} h")

    return "\n".join(lines)
