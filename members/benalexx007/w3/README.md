# Week 3 Individual Homework — Nguyen Dinh Hung (`benalexx007`)

This directory contains individual homework assignments for Week 3 of the Python Bootcamp.

## Modules Summary

- **W3-1 (`dates.py`)**: `parse_due(text, today)` converts natural language expressions (`"today"`, `"tomorrow"`, `"in 3 days"`, `"Fri"`, etc.) and ISO dates (`"YYYY-MM-DD"`) into `datetime.date` objects. Handles week wraparounds (jumping to the next occurrence in the future) and raises `ValueError` for unparseable strings.
- **W3-2 (`log_stats.py`)**: `analyse(pairs)` computes request counts per route using `collections.Counter`, calculates the 95th percentile (P95) latency using nearest-rank index math (`ceil(0.95 * N) - 1`), and identifies the slowest route.
- **W3-3 (`cli.py`)**: A command-line scheduling tool using `argparse` that loads tasks from CSV (reusing `Task` models and I/O from Week 2), calculates urgency/importance scores (`importance / max(days_left, 1)`), and greedily allocates study time into tonight's budget with dot-padded formatting.
- **W3-4 (`README.md` & code quality)**: Strict type hints (`from __future__ import annotations`), comprehensive docstrings, 100% clean `ruff check`, and comparative reflection.

## W3-4 Reflection: Python vs C++ in Software Engineering

1. **Standard Library Expressiveness vs Manual Boilerplate**:
   - In Python, tasks like CLI argument parsing (`argparse`), date arithmetic (`datetime.timedelta`), and histogram/frequency counting (`collections.Counter`) are part of the standard library, requiring just a few lines of clean, readable code.
   - In C++, accomplishing the same requires heavy third-party libraries (e.g., CLI11 or Boost.Program_options), manual chrono manipulations with `std::chrono::year_month_day`, and boilerplate with `std::unordered_map`.

2. **Dynamic Typing with Gradual Type Annotations**:
   - Python combines fast exploratory iteration with static type safety via type annotations (`list[tuple[str, int | float]]`, `date | None`) validated by linters like Ruff and mypy.
   - In C++, type safety is enforced strictly at compile-time via static typing and template metaprogramming, which catches errors earlier but significantly increases code verbosity and compilation times.

3. **Memory Safety & Lifetime Management**:
   - Python uses reference counting with cyclic garbage collection, eliminating common memory bugs such as use-after-free, dangling pointers, and double-free.
   - In C++, developers must explicitly manage object lifecycles using RAII, `std::unique_ptr`, and `std::shared_ptr`. While modern smart pointers reduce errors, improper reference handling or pointer arithmetic can still lead to memory corruption or crashes.

4. **Productivity vs Raw Compute Performance**:
   - Python optimizes for **developer velocity**: high-level data structures, list comprehensions, and clean exception handling allow developers to build maintainable microservices and tools in hours rather than days.
   - C++ optimizes for **runtime execution efficiency and hardware predictability**: it remains the standard for performance-critical systems (e.g., game engines, embedded systems, high-frequency trading), but at the cost of higher engineering effort and maintenance overhead.
