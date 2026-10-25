"""Grade summary calculations (W1-1)."""


def summary(scores: list[float]) -> dict[str, float]:
    """Compute summary statistics for a list of exam scores.

    Args:
        scores: List of numeric grades.

    Returns:
        dict containing 'min', 'max', 'mean', and 'median' rounded to 2 decimals.

    Raises:
        ValueError: If scores list is empty.
    """
    if not scores:
        raise ValueError("Scores cannot be empty")

    sorted_scores = sorted(scores)
    n = len(scores)

    if n % 2 == 1:
        median = sorted_scores[n // 2]
    else:
        median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2

    return {
        "min": min(scores),
        "max": max(scores),
        "mean": round(sum(scores) / n, 2),
        "median": round(median, 2),
    }
