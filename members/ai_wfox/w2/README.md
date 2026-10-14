# Week 2 - AI-WFox

W2-1 to W2-5 live in this package. `tests_for_philip_kkk.py` contains nine
cross-tests for Trung Anh's W1 code, including cases absent from the instructor
suite. Reviewer for this week's contribution: nhatquynh1107.

Run from the standalone bootcamp repository root:

```sh
python -m members.ai_wfox.w2
python -m members.ai_wfox.w2 samples/tasks.csv
python -m pytest -q tests/test_w2.py members/ai_wfox/w2/test_exercises.py members/ai_wfox/w2/tests_for_philip_kkk.py --member ai_wfox
python -m ruff check members/ai_wfox/w2
```

CSV requires the four named fields title, importance, effort_h, deadline.
Titles cannot be blank; importance is 1-5; effort is finite and nonnegative;
deadline is parsed as a date. Bad records report their physical CSV line.
JSON stores dates as ISO strings. Exactly enough available hours is feasible.

For n tasks, B CSV characters, T title characters, and J output characters:

| Operation | Time | Auxiliary space |
|---|---|---|
| Task construction / days_left | O(1) | O(1) |
| load_tasks | O(B) | O(n + T) including returned tasks |
| save_json | O(n + T) | O(n + T) |
| check_feasible | O(n) | O(1) |
| Package entry point | O(B + J) | O(n + T) |

Individual Task is separate from the team's shared contract. Team render tests
are a separate contribution and do not replace the individual W2 cross-tests.

AI use: Codex drafted the exercise implementations, complexity notes, tests,
and documentation, then ran verification. Retained assistance must be recorded
in the PR and AI-use log.
