# word_count: expected O(L) time/space; L = text length.
# top_k: expected O(L + V log V * W) time, O(L + V) space.
# V = distinct words; W = maximum word length. k <= 0: O(1).

WORD_SEPARATORS = str.maketrans(dict.fromkeys(".,!?;:", " "))


def word_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.lower().translate(WORD_SEPARATORS).split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []
    ranked_words = sorted(
        word_count(text).items(), key=lambda entry: (-entry[1], entry[0])
    )
    return ranked_words[:k]
