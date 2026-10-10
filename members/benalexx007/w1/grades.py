def summary(scores: list[float]) -> dict[str, float]:
    if not scores:
        raise ValueError("scores list must not be empty")
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
    else:
        median = sorted_scores[mid]
    return {
        "min": sorted_scores[0],
        "max": sorted_scores[-1],
        "mean": round(sum(scores) / n, 2),
        "median": round(median, 2),
    }
