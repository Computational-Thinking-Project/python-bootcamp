from collections import Counter, defaultdict
from math import ceil


def analyse(pairs: list[tuple[str, float]]) -> dict:
    if not pairs:
        return {"counts": {}, "p95": {}, "slowest": None}

    counts = Counter()
    latencies = defaultdict(list)

    for route, latency_ms in pairs:
        counts[route] += 1
        latencies[route].append(latency_ms)

    p95 = {}

    for route, values in latencies.items():
        sorted_latencies = sorted(values)
        n = len(sorted_latencies)
        index = ceil(0.95 * n) - 1
        p95[route] = sorted_latencies[index]

    slowest = max(p95, key=p95.get)

    answer = {"counts": dict(counts), "p95": p95, "slowest": slowest}
    return answer