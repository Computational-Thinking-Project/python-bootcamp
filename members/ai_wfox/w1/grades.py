# Time: O(n log n); space: O(n), n = number of scores.


def summary(scores: list[float]) -> dict[str, float]:
    if not scores:
        raise ValueError("scores must not be empty")

    sorted_scores = sorted(scores)
    score_count = len(sorted_scores)
    middle_index = score_count // 2
    median = sorted_scores[middle_index]
    if score_count % 2 == 0:
        median = (sorted_scores[middle_index - 1] + median) / 2

    return {
        "min": sorted_scores[0],
        "max": sorted_scores[-1],
        "mean": round(sum(scores) / score_count, 2),
        "median": round(median, 2),
    }
