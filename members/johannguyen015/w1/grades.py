def summary(scores: list[float]) -> dict:

    if not scores:
        raise ValueError("scores list can't be empty")
    
    sorted_scores = sorted(scores)
    n = len(scores)
    mid = n // 2
    
    if n & 1 == 0: # n is even
        median_score = (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
    else:
        median_score = sorted_scores[mid]
    median_score = round(median_score, 2)

    return {
        "min": sorted_scores[0],
        "max": sorted_scores[-1],
        "mean": round(sum(scores) / n, 2),
        "median": median_score
    }