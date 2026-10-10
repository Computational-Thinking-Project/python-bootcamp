def word_count(text: str) -> dict[str, int]:
    text = text.lower()

    if not text:
        return {}
    
    for punctuation in ".,!?;:":
        text = text.replace(punctuation, " ")

    words = text.split()
    wordCounts = {}

    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1

    return wordCounts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    wordCounts = word_count(text)

    if not text or k <= 0:
        return []

    sortedWords = sorted(wordCounts.items(), key=lambda item: (-item[1], item[0]))

    return sortedWords[:k]
