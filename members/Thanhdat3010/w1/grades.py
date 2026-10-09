def summary(scores: list[float]) -> dict:
    """
    Calculate summary statistics (min, max, mean, median) for a list of scores.
    Mean and median are rounded to 2 decimal places.
    Raises ValueError if scores is empty.
    """
    if not scores:
        raise ValueError("scores list cannot be empty")

    sorted_scores = sorted(scores)
    n = len(sorted_scores)

    min_val = sorted_scores[0]
    max_val = sorted_scores[-1]
    mean_val = round(sum(scores) / n, 2)

    if n % 2 == 1:
        median_val = round(float(sorted_scores[n // 2]), 2)
    else:
        mid_left = sorted_scores[(n // 2) - 1]
        mid_right = sorted_scores[n // 2]
        median_val = round((mid_left + mid_right) / 2.0, 2)

    return {
        "min": min_val,
        "max": max_val,
        "mean": mean_val,
        "median": median_val,
    }
