from pathlib import Path
from .io_utils import load_tasks


def main():
    path = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"
    tasks = load_tasks(path)

    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()
