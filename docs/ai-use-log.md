# AI assistance log

## 2026-10-23 - Thanhdat3010 - Week 3 individual exercises

Contributor: Truong Thanh Dat. Tool: Codex, Antigravity.

Codex assisted in generating the initial implementation of date parsing, Counter-based
nearest-rank p95 analysis, and the personal CLI reusing Dat's W2 loader (Issue #44).
Dat reviewed the implementation, fixed the local calendar date timezone logic in `cli.py`
using `datetime.now().astimezone().date()`, refined type hints and docstrings, and finalized
the three-line Python/C++ reflection in `README.md`.
Verification: 77 tests passed locally, personal formatting and Ruff clean, CI passing.

## 2026-10-07 - AI-WFox - Week 1 Python bootcamp

Contributor: Pham Khanh Tam. Tool: Codex.

### Individual exercises

Pham Khanh Tam wrote the exercise code and complexity analysis.
Codex added comments/docstrings and supplementary tests.

### Team T-W1 documentation

Codex helped draft `python-bootcamp/README.md`.

## 2026-10-14 - AI-WFox - Week 2 individual exercises

Pham Khanh Tam revised the code and tests. Codex provided initial code/test
drafts and supported documentation, CI, and verification.

## 2026-10-17 - AI-WFox - Team T-W2 render tests

Codex drafted and verified the render tests against the team's implementation.

## 2026-10-20 - philip-kkk - Week 3 individual exercises

Contributor: Duong Trung Anh. Tool: Codex.

Trung Anh wrote `dates.py`; Codex reviewed it and explained relevant Python
syntax.

For W3-4, Codex added missing type hints and docstrings and formatted only
`members/philip_kkk/`, preserving the existing algorithms and outputs.
Verification uses the instructor's applicable W1/W2/W3 tests, the existing
cross-member tests, separate DFS checks, Ruff, and manual CLI checks.

## 2026-10-20 - AI-WFox - Week 3 individual exercises

Contributor: Pham Khanh Tam. Tool: Antigravity (Gemini).

### Individual exercises (W3-1 to W3-4)

Gemini generated baseline test fixtures and verified boundary logic for nearest-rank P95 and weekday offset calculations. Pham Khanh Tam reviewed, refactored, and verified all implementations locally with pytest and Ruff.
