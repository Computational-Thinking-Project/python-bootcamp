"""Log statistics analysis and latency profiling (W3-2)."""

import math
from collections import Counter, defaultdict
from typing import Any


def analyse(pairs: list[tuple[str, int | float]]) -> dict[str, Any]:
    """Compute request counts and 95th percentile latency per route.

    Args:
        pairs: List of (route_name, latency_ms) tuples.

    Returns:
        dict containing:
        - "counts": Counter of requests per route
        - "p95": dict mapping route to 95th percentile latency
        - "slowest": route name with the highest P95 latency (None if empty)
    """
    if not pairs:
        return {
            "counts": Counter(),
            "p95": {},
            "slowest": None,
        }

    counts: Counter[str] = Counter(route for route, _ in pairs)
    grouped: defaultdict[str, list[int | float]] = defaultdict(list)
    for route, latency in pairs:
        grouped[route].append(latency)

    p95: dict[str, int | float] = {}
    for route, latencies in grouped.items():
        sorted_lats = sorted(latencies)
        # Nearest-rank method for 95th percentile: ceil(0.95 * N) - 1 (0-indexed)
        idx = max(0, min(math.ceil(0.95 * len(sorted_lats)) - 1, len(sorted_lats) - 1))
        p95[route] = sorted_lats[idx]

    slowest = max(p95, key=lambda r: p95[r])

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest,
    }
