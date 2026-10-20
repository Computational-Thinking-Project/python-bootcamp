"""Chat log analysis module for computing route request counts and latencies."""

import math
from collections import Counter, defaultdict
from typing import Any


def analyse(pairs: list[tuple[str, int | float]]) -> dict[str, Any]:
    """Analyse route and latency pairs to compute request counts and p95 latency.

    Args:
        pairs: List of (route, latency_ms) tuples.

    Returns:
        Dictionary containing:
            - "counts": collections.Counter of requests per route.
            - "p95": Dictionary mapping each route to its 95th percentile latency.
            - "slowest": Route with the highest p95 latency, or None if pairs is empty.
    """
    if not pairs:
        return {"counts": Counter(), "p95": {}, "slowest": None}

    counts: Counter[str] = Counter(route for route, _ in pairs)
    grouped: defaultdict[str, list[int | float]] = defaultdict(list)
    for route, latency in pairs:
        grouped[route].append(latency)

    p95: dict[str, int | float] = {}
    for route, latencies in grouped.items():
        sorted_lats = sorted(latencies)
        # Nearest rank method for 95th percentile: ceil(0.95 * N) - 1 (0-indexed)
        idx = max(0, min(math.ceil(0.95 * len(sorted_lats)) - 1, len(sorted_lats) - 1))
        p95[route] = sorted_lats[idx]

    slowest = max(p95, key=lambda r: p95[r])

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest,
    }
