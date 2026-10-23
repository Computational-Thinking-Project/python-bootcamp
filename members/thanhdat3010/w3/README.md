# Week 3 individual homework - Truong Thanh Dat

Issue: [#44](https://github.com/Computational-Thinking-Project/python-bootcamp/issues/44).

Run from the bootcamp repository root:

```sh
python -m members.thanhdat3010.w3.cli samples/tasks.csv --hours 2 --today 2026-10-26
python -m pytest -q tests/test_w3.py members/thanhdat3010/w3/test_w3_individual.py --member thanhdat3010
python -m ruff check members/thanhdat3010
python -m ruff format --check members/thanhdat3010
```

- W3-1: ISO dates, `tomorrow`, `in N days`, and abbreviated weekdays
  (case-insensitive). A matching weekday advances seven days.
- W3-2: Counter counts and nearest-rank p95 (`ceil(0.95 * n) - 1`).
  Empty logs return empty dictionaries and `slowest=None`; ties select the
  first route encountered.
- W3-3: Reuse my W2 CSV loader; explicitly convert personal Task objects to
  the shared Task contract, then prioritise, allocate and render. Partial
  plans are allowed. Missing files return 1 on stderr; bad arguments return 2.
- W3-4: Personal functions have annotations/docstrings and are formatted.
  The instructor harness has no BFS variant 6, so its translation test is
  excluded for earlier-week regression and BFS is tested separately.

## Python/C++ reflection - draft for Dat to review

1. Python type hints document interfaces but do not enforce types at runtime;
   C++ checks declared types during compilation.
2. `Counter` and `defaultdict` express log grouping without manually
   initialising every dictionary entry.
3. `argparse` converts arguments and reports usage errors, while pytest checks
   behaviour separately from annotations.

These are agent-written draft observations. Dat must read the implementation,
revise these lines to reflect his understanding, and include three lines in
the PR. Do not claim personal review or time spent until actually completed.
