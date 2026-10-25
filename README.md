# Python Bootcamp - Team 04

Weekly Python exercises for CSC10014, submitted through the team's
`assistant-team04` repository. Each member completes W1-1 through W1-5 in
their own directory and contributes their assigned Team T-W1 task.

## Repository layout

```text
python-bootcamp/
|-- README.md                 # Rules, assignment map, and test instructions
|-- PROGRESS.md               # Real issue/PR links, reviewer, tests, and hours
|-- members/
|   |-- ai_wfox/w1/           # Pham Khanh Tam; w2/ and w3/ also reserved
|   |-- htbaax/w1/            # Ha Tran Boi Anh
|   |-- nhatquynh1107/w1/     # Nguyen Nhat Quynh
|   |-- johannguyen015/w1/    # Nguyen Ba Duy
|   |-- benalexx007/w1/       # Nguyen Dinh Hung
|   |-- thanhdat3010/w1/      # Truong Thanh Dat
|   `-- philip_kkk/w1/        # Duong Trung Anh
|-- shared/study_planner/     # Shared work in later weeks
`-- tests/                   # Instructor tests and their conftest.py
```

Some files are delivered by separate team PRs. `tests/` needs the instructor's
actual test suite; a `.gitkeep` does not make the bootcamp testable. Replace
the `.gitkeep` in your own week folder when adding source files. Keep other
members' folders intact.

Folder names match GitHub usernames in lowercase with hyphens replaced by underscores.
For example, `AI-WFox` uses `ai_wfox`, `Thanhdat3010` uses `thanhdat3010`, and
`philip-kkk` uses `philip_kkk`.

## Development environment

Run commands from the **repository root**, not from `python-bootcamp/`.
Python 3.10+ is required by the project; the planned CI uses Python 3.12.

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned` in the
current terminal, then retry activation.

macOS/Linux:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Install the project's test dependency and the bootcamp linter:

```sh
python -m pip install -r requirements.txt
python -m pip install ruff
```

Use `deactivate` when finished. Never commit `.venv/`, generated caches, or
credentials.

## Week 1 individual exercises

Every member implements all five exercises under `members/<folder>/w1/`:

| Exercise | File | Required interface and behavior |
| --- | --- | --- |
| W1-1 | `grades.py` | `summary(scores)` returns min, max, mean, median; round mean/median to 2 decimals; empty input raises `ValueError` |
| W1-2 | `text_tools.py` | `word_count(text)` lowercases words and ignores `.,!?;:`; `top_k(text, k)` orders by decreasing count, then alphabetically |
| W1-3 | `rules.py` | `can_register_thesis(credits, gpa)` requires at least 120 credits and GPA 2.0; `missing(credits, gpa)` explains unmet requirements |
| W1-4 | `translate.py` | Translate your assigned C++ algorithm, preserving behavior and documenting a Python/C++ difference |
| W1-5 | `timetable.py` | `by_day(timetable)` maps each day to a sorted list of course names using a comprehension or `dict.setdefault` |

### W1-4 algorithm assignment

Algorithm numbers follow the group's supplied list, independently of T-W1
task numbers or the roster's display order.

| Algorithm number | Member | Folder | Translation |
| --- | --- | --- | --- |
| 1 | Pham Khanh Tam | `ai_wfox` | Binary search: return an index or -1 |
| 2 | Ha Tran Boi Anh | `htbaax` | Insertion sort, in place |
| 3 | Nguyen Nhat Quynh | `nhatquynh1107` | Matrix transpose |
| 4 | Nguyen Ba Duy | `johannguyen015` | Sieve of Eratosthenes: primes up to n |
| 5 | Nguyen Dinh Hung | `benalexx007` | Selection sort, in place |
| 6 | Truong Thanh Dat | `thanhdat3010` | BFS: visit order |
| 7 | Duong Trung Anh | `philip_kkk` | DFS: visit order |

The tutorial defines variants 1-4. The team's additions 5-7 need matching
interfaces and cases in the instructor-supplied test harness; confirm them
with the test owner rather than guessing function names or signatures.

## Running tests

After the instructor's `tests/test_w1.py` and `tests/conftest.py` are added,
run Tam's W1 tests from the repository root:

```sh
python -m pytest -q tests/test_w1.py --member ai_wfox --variant 1
```

Tam uses **variant 1**, because the assigned algorithm is binary search.
Tam's **T-W1 task is 2** (README), which is a separate assignment number.
Use the instructor test README as the final authority for supported options
and exact callable names.

If your own folder contains additional tests, run them separately, for example:

```sh
python -m pytest -q/members/ai_wfox/w1/test_exercises.py
```

For the complete bootcamp, once the instructor suite is installed:

```sh
python -m ruff check .
python -m pytest -q
```

The root project's pytest configuration defaults to `tests/`, so plain
`python -m pytest -q` does not by itself establish that bootcamp exercises were
tested. Pass `python-bootcamp` explicitly. A "no tests collected" result or a
missing `--member` option means setup is incomplete, not that tests passed.
The CI owner must use the instructor harness's supported discovery/options.

## Weekly contribution workflow

1. Start from the latest `main`, then create your personal branch:

   ```sh
   git switch main
   git pull --ff-only origin main
   git switch -c py/w1-<github-username>
   ```

   Tam's branch is `py/w1-AI-WFox`; their code belongs in `members/ai_wfox/w1/`.

2. Work only in your own member folder for individual exercises. Commit after
   each exercise with a meaningful message, for example
   `feat(py-w1): W1-1 grade summary`. The tutorial expects at least five
   meaningful commits per week, with actual work spread over several days.
   Do not fabricate dates or hours.
3. Run your member's tests and Ruff. Add edge cases: empty inputs, boundaries,
   ties, and absent search keys. Do not modify instructor tests to make code pass.
4. Push your branch and open one individual PR titled `py-w1: <username>`.
   Link your actual homework issue with `Closes #<issue-number>`, use the
   `python-hw` and `w1` labels and `PY-W1` milestone once configured, and
   request the reviewer assigned by the team's rotation.
5. Review the teammate assigned to you: run the tests, understand the code,
   check Pythonic style and edge cases, and leave one question, one suggestion,
   and one specific positive observation. Request changes when needed.
6. Merge only after another member's approval and passing CI. Update your own
   `PROGRESS.md` entry with real issue/PR links, reviewer, test results, and hours.

Record retained AI-generated code in the PR's AI-use section and in
`docs/ai-use-log.md`. Each student must understand and explain their own code.

## Team T-W1 ownership

Each team setup task has its own PR, separate from the individual homework PR.

| Task | Owner | Deliverable |
| --- | --- | --- |
| 1 | Nguyen Ba Duy | Bootcamp directory structure |
| 2 | Pham Khanh Tam | This `python-bootcamp/README.md` |
| 3 | Nguyen Nhat Quynh | Milestones `PY-W1`, `PY-W2`, `PY-W3` |
| 4 | Ha Tran Boi Anh | Labels `python-hw`, `w1`, `w2`, `w3`, `team-hw` |
| 5 | Duong Trung Anh | Python homework issue template |
| 6 | Truong Thanh Dat | Bootcamp CI job |
| 7 | Nguyen Dinh Hung | `PROGRESS.md` and instructor tests |

The team agrees on deadline dates and reviewer rotation. Do not infer them
from the four-person example in the tutorial.

Week 1 is complete when all **seven** individual W1 PRs are merged with review
approval, bootcamp CI passes the required tests, all seven progress rows are
accurate, and the project manager publishes the `py-w1-done` tag. A README-only
PR or passing local tests alone does not meet those completion criteria.

## Study Planner Application (Team T-W2 & T-W3)

In Weeks 2 and 3, Team 04 incrementally built the **Study Planner**, a unified tool to schedule and allocate study hours for academic tasks:

- **Team T-W2 (Core Modules):** Defined the shared `Task` and `Block` contracts, CSV parser (`parse.py`), task prioritisation (`prioritise.py`), greedy allocation (`allocate.py`), and formatted plan rendering (`render.py`).
- **Team T-W3 (CLI Application):** Built the unified CLI interface (`__main__.py`), comprehensive sample datasets (`samples/`), full-plan feasibility checks (`errors.py`), `--output` file export, `--verbose` statistics, and end-to-end automated test suites.

### Running the Study Planner CLI

Run the tool as an executable Python module from the repository root:

```bash
# Standard run (stdout)
python -m shared.study_planner samples/tasks.csv --hours 8 --today 2026-10-26

# Verbose summary with statistics
python -m shared.study_planner samples/tasks.csv --hours 8 -v

# Export rendered schedule to a UTF-8 file
python -m shared.study_planner samples/tasks.csv --hours 8 -o schedule.txt
```

For complete CLI options, exit code specifications, error handling contracts, and dataset descriptions, see the [Study Planner CLI User Guide](docs/study_planner_cli.md).

### Running the Test Suite

Run all instructor tests, module tests, and end-to-end integration tests:

```bash
python -m pytest -q tests/
python -m ruff check .
```
