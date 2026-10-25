# Study Planner CLI User Guide (Team T-W3)

`shared.study_planner` is a unified command-line application developed by Team 04 (Week 3, CSC10014) to parse study task datasets, evaluate plan feasibility, prioritise deadlines, greedily allocate available study hours, and render human-readable schedules.

---

## 1. Architecture & Execution Pipeline

The CLI integrates the modular components developed across Team T-W2 and Team T-W3 into a sequential, deterministic pipeline:

```text
       +-----------------------+
       |   Input CSV Dataset   |
       +-----------+-----------+
                   |
                   v
     [ parse_csv(csv_path) ]       --> Parses headers and task fields
                   |
                   v
     [ CLI finite-effort check ]   --> Validates that all effort_h are finite
                   |
                   v
  [ check_feasible(tasks, hours) ] --> Ensures sum(effort_h) <= available hours
                   |
                   v
   [ prioritise(tasks, today) ]    --> Orders by importance / max(1, days_left)
                   |
                   v
    [ allocate(tasks, hours) ]     --> Greedily allocates study blocks
                   |
                   v
        [ render(blocks) ]         --> Formats dot-leader schedule lines
                   |
                   +---> (Optional: render_summary if --verbose)
                   |
                   v
         stdout OR --output file
```

### Component Ownership & Integration
- **`shared/study_planner/parse.py`**: Reads CSV files, normalises header names, and instantiates mutable `Task` objects.
- **`shared/study_planner/errors.py`**: Defines `InfeasiblePlan` and `check_feasible()` to ensure available study hours cover the required workload.
- **`shared/study_planner/prioritise.py`**: Ranks tasks in descending order of urgency score computed as `importance / max(1, days_left)` without effort-based ranking. Due and overdue tasks use 1 day; equal scores maintain input order.
- **`shared/study_planner/allocate.py`**: Greedily allocates study hours into `Block` segments matching available time.
- **`shared/study_planner/render.py`**: Formats study blocks into structured numbered lines with dot leaders (`1. Assignment ... 1.5 h`), and formats verbose allocation statistics.
- **`shared/study_planner/__main__.py`**: CLI entry point with `argparse`, finite-effort validation, input sanitation, and clean error exit code management.

---

## 2. Command-Line Interface Specification

### Syntax

```bash
python -m shared.study_planner <csv_file> --hours <hours> [options]
```

### Positional Arguments

| Argument | Type | Description |
|---|---|---|
| `csv_file` | `str` | Relative or absolute path to the task dataset CSV file. |

### Options & Flags

| Flag | Short | Type | Required | Default | Description |
|---|---|---|---|---|---|
| `--hours` | | `float` | **Yes** | *None* | Total study hours available. Must be a finite, positive number. |
| `--today` | | `str` | No | System date | Reference date in ISO format (`YYYY-MM-DD`) for urgency calculation. Recommended for reproducible ordering. |
| `--output` | `-o` | `Path` | No | *None* | File path to write the formatted plan (UTF-8). Must differ from `csv_file`. |
| `--verbose`| `-v` | flag | No | `False` | Display allocation statistics (`Tasks selected`, `Available hours`, `Allocated hours`, `Remaining hours`). |
| `--help` | `-h` | flag | No | | Print CLI argument help message and exit with code `0`. |

---

## 3. Exit Codes & Error Handling Contract

The CLI conforms to a strict exit code contract. Handled errors output clear messages directly to `sys.stderr` without exposing Python tracebacks.

| Exit Code | Classification | Trigger Condition | Example `stderr` Message |
|:---:|---|---|---|
| **`0`** | **Success** | Input valid, plan feasible, output successfully written to stdout or file. | *(None)* |
| **`1`** | **File / Budget Error** | File not found at specified path. | `Error: Tasks file not found: missing.csv` |
| | | Unreadable file due to OS/permission error. | `Error: Could not read tasks file: Permission denied` |
| | | CSV file contains 0 tasks (empty file). | `Error: File is empty: samples/tasks_empty.csv` |
| | | Target `--output` is identical to input `csv_file`. | `Error: Output file must differ from the tasks CSV` |
| | | Output file cannot be written (permission/disk). | `Error: Cannot write output file: Permission denied` |
| | | **Infeasible plan**: required effort > available hours. | `Error: InfeasiblePlan: 7.5 hours needed exceeds 2 hours available` |
| **`2`** | **Syntax / Format Error** | Missing required `--hours` argument. | `usage: ... error: the following arguments are required: --hours` |
| | | Non-numeric or non-positive `--hours` (`<= 0`, `inf`, `nan`). | `Error: hours must be a positive number` |
| | | Invalid `--today` format (not `YYYY-MM-DD`). | `Error: today must be a valid date in YYYY-MM-DD format` |
| | | Corrupted/malformed CSV header or data types. | `Error: Invalid CSV format: ...` |
| | | Non-finite task `effort_h` value in CSV. | `Error: Invalid CSV format: effort_h must be a finite number` |

---

## 4. Sample Datasets Catalog (`samples/`)

Team 04 maintains standardized test datasets under `samples/` for end-to-end verification:

| Dataset File | Tasks Count | Total Effort (h) | Purpose / Target Test Scenario |
|---|:---:|:---:|---|
| `samples/tasks.csv` | **2** | **7.5 h** | Default benchmark dataset with 2 core tasks (`Assignment` 1.5h, `DS exam` 6h). Feasible when `--hours >= 7.5`. |
| `samples/tasks_expanded.csv` | **7** | **21.0 h** | Extended realistic student workload with 7 diverse tasks across varying priorities and deadlines. |
| `samples/tasks_infeasible.csv` | **3** | **250.0 h** | Extreme workload checking designed to verify `InfeasiblePlan` handling (Exit code 1). |
| `samples/tasks_empty.csv` | **0** | **0.0 h** | 0-byte file designed to test empty dataset detection (Exit code 1). |
| `samples/tasks_corrupted.csv` | **2** | *N/A* | Malformed headers and invalid numeric types designed to test CSV validation (Exit code 2). |

---

## 5. Usage Examples

### 5.1. Standard Plan Execution (Stdout)

Generate a schedule using the default benchmark dataset with an 8-hour budget on reference date `2026-10-26`:

```bash
python -m shared.study_planner samples/tasks.csv --hours 8 --today 2026-10-26
```

**Output:**
```text
1. Assignment ... 1.5 h
2. DS exam ...... 6 h
```

---

### 5.2. Verbose Output with Statistics

Inspect task allocation breakdown and remaining study hours with `--verbose` / `-v` (specifying `--today` for reproducible task ordering):

```bash
python -m shared.study_planner samples/tasks.csv --hours 9 --today 2026-10-26 -v
```

**Output:**
```text
1. Assignment ... 1.5 h
2. DS exam ...... 6 h

Tasks selected: 2
Available hours: 9 h
Allocated hours: 7.5 h
Remaining hours: 1.5 h
```

---

### 5.3. Saving to File (`--output`)

Export the formatted plan to a UTF-8 text file, specifying `--today` for reproducible output:

```bash
python -m shared.study_planner samples/tasks.csv --hours 8 --today 2026-10-26 -o schedule.txt
```

When `-o` is supplied without `-v`, the CLI runs silently and writes the complete plan to `schedule.txt`. When combined with `-v`, the summary statistics are displayed on `stdout` while the full plan is preserved in the file.

---

### 5.4. Error Handling Examples

#### Insufficient Study Budget (Exit Code 1)
```bash
python -m shared.study_planner samples/tasks.csv --hours 2 --today 2026-10-26
```
*Stderr Output:*
```text
Error: InfeasiblePlan: 7.5 hours needed exceeds 2 hours available
```

#### Missing Input File (Exit Code 1)
```bash
python -m shared.study_planner nonexistent.csv --hours 8
```
*Stderr Output:*
```text
Error: Tasks file not found: nonexistent.csv
```

#### Invalid Arguments (Exit Code 2)
```bash
python -m shared.study_planner samples/tasks.csv --hours -5
```
*Stderr Output:*
```text
Error: hours must be a positive number
```

---

## 6. Programmatic Invocation

The CLI entry point `main()` can be invoked directly in Python scripts or automated test harnesses using pytest's `capsys`:

```python
from shared.study_planner.__main__ import main

# Execute with explicit argument vector
exit_code = main(["samples/tasks.csv", "--hours", "8", "--today", "2026-10-26"])
assert exit_code == 0
```
