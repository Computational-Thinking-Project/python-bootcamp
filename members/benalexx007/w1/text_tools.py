import heapq
from collections import Counter

_PUNCT_TABLE = str.maketrans(".,!?;:", "      ")


def word_count(text: str) -> dict[str, int]:
    cleaned = text.lower().translate(_PUNCT_TABLE)
    return dict(Counter(cleaned.split()))


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []
    counts = word_count(text)
    if k >= len(counts):
        return sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return heapq.nsmallest(k, counts.items(), key=lambda item: (-item[1], item[0]))
