from pathlib import Path

from members.johannguyen015.w2.io_utils import load_tasks


def main() -> None:
    sample_csv = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"
    tasks = load_tasks(sample_csv)
    print(f"Loaded {len(tasks)} tasks from {sample_csv.name}:")
    for t in tasks:
        print(f"- {t.title} (Importance: {t.importance}, Effort: {t.effort_h}h, Deadline: {t.deadline})")


if __name__ == "__main__":
    main()
