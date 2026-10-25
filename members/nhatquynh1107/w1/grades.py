"""Calculate descriptive statistics for a list of grades."""


def summary(scores: list[float]) -> dict[str, float]:
    """Return min, max, mean and median; reject an empty list.

    Mean and median are rounded to two decimal places.
    """
    if not scores:
        raise ValueError()

    minScores = min(scores)
    maxScores = max(scores)
    mean = sum(scores) / len(scores)

    sortedScores = sorted(scores)
    n = len(scores)
    mid = n // 2

    if n % 2 == 1:
        med = sortedScores[mid]
    else:
        med = (sortedScores[mid - 1] + sortedScores[mid]) / 2

    med = round(med, 2)
    mean = round(mean, 2)

    return {"min": minScores, "max": maxScores, "mean": mean, "median": med}
