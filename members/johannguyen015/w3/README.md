# Week 3 Individual Homework — Johan Nguyen (`johannguyen015`)

This directory contains the individual assignments for Week 3 of the Python Bootcamp.

## Modules Summary

- **W3-1 (`dates.py`)**: `parse_due(text, today)` converts natural language expressions (`"today"`, `"tomorrow"`, `"in 3 days"`, `"Fri"`) and ISO dates (`"YYYY-MM-DD"`) to `datetime.date` objects.
- **W3-2 (`log_stats.py`)**: `analyse(pairs)` computes request frequency per route with `collections.Counter`, extracts 95th percentile (P95) latency using nearest rank calculation, and identifies the slowest route.
- **W3-3 (`cli.py`)**: A command-line interface powered by `argparse` that loads task definitions from CSV (reusing W2 models and I/O), prioritises by `importance / max(days_left, 1)`, and greedily schedules tasks into tonight's available hours.
- **W3-4 (`README.md` & code quality)**: Strict type hints, complete docstrings, 100% clean `ruff check`, and comparative reflection.

## W3-4 Reflection: Python vs C++

1. **Standard Library Abstractions**: Python's standard library provides high-level components (`argparse`, `datetime`, `collections.Counter`) that replace verbose custom parsers and hash map boilerplate required in C++.
2. **Dynamic Typing with Optional Typing**: Dynamic types and comprehensions enable rapid prototyping and concise data pipelines, while modern type hints (`typing`, `list[T]`) restore type safety and IDE support without template complexity.
3. **Reference Semantics & Memory Safety**: Objects in Python are managed automatically via reference counting and garbage collection, removing memory leaks and pointer manipulation hazards present in C++.
