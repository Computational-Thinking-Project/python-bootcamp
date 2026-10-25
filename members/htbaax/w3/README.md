# Week 3 — Standard Library and Tooling (`htbaax`)

This package contains the Week 3 individual exercises implementing date arithmetic, log latency analysis, a CLI study scheduling tool, and clean code practices.

## Module Structure

- `dates.py`: Implements `parse_due(text: str, today: date) -> date` supporting ISO formats, relative expressions ("tomorrow", "in N days"), and forward weekday jumping (e.g., "Fri", "Tue").
- `log_stats.py`: Implements `analyse(pairs: list[tuple[str, int | float]]) -> LogAnalysis` calculating request volume with `collections.Counter`, nearest-rank P95 latency per route, and identifying the slowest route.
- `cli.py`: Study planner command-line interface with `argparse`, reusing Week 2 `load_tasks`, prioritizing tasks by urgency, greedily allocating available hours, and formatting output with dot leaders.
- `test_w3_individual.py`: Unit test suite testing all individual functions against edge cases.

## Reflection: Python vs. C++

1. **Memory Model & Object References:** Unlike C++ where variables directly represent memory cells or require explicit pointer/reference semantics (`&`, `*`, `std::unique_ptr`), Python binds names to shared heap-allocated objects; copying a variable merely copies the reference rather than performing deep memory duplication.
2. **First-Class High-Level Collections:** Python's standard library provides expressive high-level abstractions like `collections.Counter`, `defaultdict`, and list comprehensions with slicing out of the box, avoiding verbose template boilerplate such as `std::map<std::string, int>` or manual iterator loops in C++.
3. **Dynamic Typing with Gradual Type Annotations:** In contrast to C++'s rigid compile-time type verification, Python type hints serve purely as executable documentation and static analysis guidance without affecting runtime speed, making interface boundaries testable and refactorable with rapid iteration.
