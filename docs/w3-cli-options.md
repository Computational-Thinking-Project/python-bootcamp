# T-W3 CLI options - Truong Thanh Dat

Issue: [#45](https://github.com/Computational-Thinking-Project/python-bootcamp/issues/45).
Reviewer: `nhatquynh1107`, per Team-T-w3.md.

Run from the bootcamp repository root:

```sh
python -m shared.study_planner samples/tasks.csv --hours 2 --today 2026-10-26
python -m shared.study_planner samples/tasks.csv --hours 2 -o out.txt -v
python -m pytest -q tests/test_render.py tests/test_cli_options.py
```

- `--output PATH` / `-o PATH`: write the rendered plan as UTF-8, replacing
  that output file. Reject the source CSV as output. Report write failures on
  stderr and return 1. Parent directories must already exist.
- `--verbose` / `-v`: include selected-task count, available hours,
  allocated hours and remaining hours. `render_summary` returns text without
  I/O; `main` prints or saves it.
- Combined `-o -v`: save plan plus statistics and display statistics on
  stdout. `-o` alone is silent on stdout; no flags preserve ordinary output.
- Formatting preserves titles, task order and allocated hours. Dot leaders
  separate titles from the hours column.

Integration note for Quynh: this PR preserves greedy allocation. Rejecting
every total effort greater than the budget would break the existing sample
(7.5 hours of tasks, 2-hour partial plan). Agree on the intended scope of
`InfeasiblePlan` before merging that change. General input-error handling
remains a separate assigned task.
