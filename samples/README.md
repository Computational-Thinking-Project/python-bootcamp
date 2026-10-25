# Study Planner Sample Datasets (Team T-W3)

This directory contains standardized sample task datasets in CSV format for running, demonstrating, and automating tests for the `study_planner` application.

## Schema Specification

Each valid CSV file must follow the standard comma-separated format with a header row:

| Column | Type | Constraints / Description | Example |
|---|---|---|---|
| `title` | `str` | Name or title of the task (non-empty) | `Assignment` |
| `importance` | `int` | Priority score from `1` (lowest) to `5` (highest) | `4` |
| `effort_h` | `float` | Estimated effort in hours (> 0.0) | `1.5` |
| `deadline` | `date` | Due date in ISO 8601 format (`YYYY-MM-DD`) | `2026-10-27` |

---

## Dataset Catalog

| Filename | Tasks Count | Total Effort (h) | Primary Target / Purpose | Expected CLI Behavior |
|---|:---:|:---:|---|---|
| [`tasks.csv`](tasks.csv) | 2 | 7.5 h | Standard textbook reference dataset; instructor W2 test compatibility | Success (`returncode == 0`), allocates Assignment & DS exam |
| [`tasks_expanded.csv`](tasks_expanded.csv) | 7 | 21.0 h | Extended dataset with 7 realistic student tasks for comprehensive CLI testing | Success (`returncode == 0`), full priority scheduling |
| [`tasks_empty.csv`](tasks_empty.csv) | 0 | 0.0 h | Empty input validation | Error (`returncode == 1`), "Empty tasks file" |
| [`tasks_infeasible.csv`](tasks_infeasible.csv) | 3 | 250.0 h | Extreme workload checking | Error (`returncode == 1`), `InfeasiblePlan` |
| [`tasks_corrupted.csv`](tasks_corrupted.csv) | 2 | N/A | Malformed headers and invalid types | Parsing error (`returncode == 2`), usage error |
| [`tasks_bad.csv`](tasks_bad.csv) | 2 | N/A | Legacy malformed rows | Format validation error |

---

## Usage Examples

### 1. Standard Reference Planning
Allocate 2 study hours on date `2026-10-26`:
```bash
python -m shared.study_planner samples/tasks.csv --hours 2 --today 2026-10-26
```
Expected output:
```text
1. Assignment - 1.5 h
2. DS exam - 0.5 h
```

### 2. Extended Multi-Task Planning
```bash
python -m shared.study_planner samples/tasks_expanded.csv --hours 4 --today 2026-10-26
```

### 3. Empty File Error
```bash
python -m shared.study_planner samples/tasks_empty.csv --hours 2
# Exit code: 1, stderr describes empty file
```

### 4. Infeasible Plan Detection
```bash
python -m shared.study_planner samples/tasks_infeasible.csv --hours 2
# Exit code: 1, stderr indicates InfeasiblePlan
```

### 5. Malformed / Corrupted CSV Handling
```bash
python -m shared.study_planner samples/tasks_corrupted.csv --hours 2
# Exit code: 2, parsing failure report
```
