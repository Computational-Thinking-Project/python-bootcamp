"""Summarize request counts and nearest-rank p95 latency by route."""

from collections import Counter, defaultdict
from math import ceil
from typing import TypedDict


class LogStats(TypedDict):
    """Per-route counts, p95 latencies and the route with the highest p95."""

    counts: dict[str, int]
    p95: dict[str, float]
    slowest: str | None


def analyse(pairs: list[tuple[str, float]]) -> LogStats:
    """Compute request counts and nearest-rank p95 latency per route.

    P95 uses the sorted value at ceil(0.95 * n) - 1. Equal p95 values select
    the route encountered first. Empty input returns empty dictionaries and
    None for slowest. The input list is not modified.
    """
    counts: Counter[str] = Counter()
    latencies: defaultdict[str, list[float]] = defaultdict(list)

    for route, latency_ms in pairs:
        counts[route] += 1
        latencies[route].append(latency_ms)

    p95: dict[str, float] = {}

    for route, values in latencies.items():
        values.sort()
        index = ceil(0.95 * len(values)) - 1
        p95[route] = values[index]

    slowest = max(p95, key=lambda route: p95[route]) if p95 else None

    return {"counts": dict(counts), "p95": p95, "slowest": slowest}
