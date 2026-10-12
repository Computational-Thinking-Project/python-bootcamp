def word_count(text: str) -> dict[str, int]:
    """
    Count word frequencies in text.
    Words are converted to lower-case and punctuation (.,!?;:) is ignored.
    """
    cleaned_chars = [ch if ch not in ".,!?;:" else " " for ch in text]
    cleaned_text = "".join(cleaned_chars).lower()
    words = cleaned_text.split()

    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """
    Return top k words sorted by count descending, then alphabetically ascending.
    """
    counts = word_count(text)
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:k]
