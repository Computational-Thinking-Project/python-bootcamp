"""Load and display the sample tasks with python -m members.nhatquynh1107.w2."""

from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Load the repository's sample CSV and print each task."""
    path = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"
    tasks = load_tasks(path)

    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()
