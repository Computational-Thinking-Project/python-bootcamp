"""Per-route request counts and nearest-rank p95 latency for W3-2."""

from collections import Counter, defaultdict
from collections.abc import Iterable
from math import ceil
from typing import TypedDict


class LogStats(TypedDict):
    """Analysis result; empty input has no slowest route."""

    counts: dict[str, int]
    p95: dict[str, float]
    slowest: str | None


def analyse(pairs: Iterable[tuple[str, float]]) -> LogStats:
    """Compute p95 using sorted[ceil(0.95 * n) - 1] for each route.

    Equal p95 values select the first route encountered in the input.
    """
    counts: Counter[str] = Counter()
    latencies: defaultdict[str, list[float]] = defaultdict(list)
    for route, latency in pairs:
        counts[route] += 1
        latencies[route].append(latency)
    p95 = {
        route: sorted(values)[ceil(0.95 * len(values)) - 1]
        for route, values in latencies.items()
    }
    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": max(p95, key=p95.get) if p95 else None,
    }
