def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError(...)
    
    minNum = min(scores)
    maxNum = max(scores)
    meanNum = sum(scores) / len(scores)
    
    sortedScore = sorted(scores)
    n = len(sortedScore)
    mid = n // 2
    
    if n % 2 == 0:
        medianNum = (sortedScore[mid - 1] + sortedScore[mid]) / 2
    else:
        medianNum = sortedScore[mid]
    
    meanNum = round(meanNum, 2)
    medianNum = round(medianNum, 2)
    
    answer = {"min": minNum, "max": maxNum, "mean": meanNum, "median": medianNum}
    return answer
    
    