"""Text processing and word frequency tools (W1-2)."""


def word_count(text: str) -> dict[str, int]:
    """Count occurrences of each word in text ignoring specified punctuation."""
    cleaned = text.lower()

    for char in ".,!?;:)":
        cleaned = cleaned.replace(char, " ")

    words = cleaned.split()
    result: dict[str, int] = {}

    for word in words:
        result[word] = result.get(word, 0) + 1

    return result


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the top k words sorted descending by count, then alphabetically."""
    counts = word_count(text)
    items = list(counts.items())

    # Sort primarily descending by count (-count), secondarily ascending by word (alphabetical)
    sorted_items = sorted(items, key=lambda item: (-item[1], item[0]))
    return sorted_items[:k]
