"""Chat log analysis and latency percentiles profiling (W3-2)."""

import math
from collections import Counter, defaultdict
from typing import TypedDict


class LogAnalysis(TypedDict):
    """Structured report schema for chat log latency statistics."""

    counts: Counter[str]
    p95: dict[str, int | float]
    slowest: str | None


def analyse(pairs: list[tuple[str, int | float]]) -> LogAnalysis:
    """Analyse chat log records to compute request counts and p95 latencies per route.

    Args:
        pairs: A list of (route, latency_ms) tuples.

    Returns:
        LogAnalysis dict containing:
        - "counts": Counter mapping each route to its invocation count.
        - "p95": dict mapping each route to its 95th percentile latency (nearest-rank).
        - "slowest": Name of the route with the highest p95 latency, or None if empty.
    """
    if not pairs:
        return {
            "counts": Counter(),
            "p95": {},
            "slowest": None,
        }

    counts: Counter[str] = Counter()
    latencies_by_route: defaultdict[str, list[int | float]] = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        latencies_by_route[route].append(latency)

    p95: dict[str, int | float] = {}
    for route, latencies in latencies_by_route.items():
        sorted_latencies = sorted(latencies)
        n = len(sorted_latencies)
        # Nearest-rank method: index = ceil(0.95 * N) - 1
        rank_idx = max(0, min(math.ceil(0.95 * n) - 1, n - 1))
        p95[route] = sorted_latencies[rank_idx]

    slowest_route = max(p95, key=lambda route: p95[route])

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest_route,
    }
