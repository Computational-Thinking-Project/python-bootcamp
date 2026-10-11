
def word_count(text: str) -> dict[str, int]:
    text = text.lower()

    for char in ".,!?;:)":
        text = text.replace(char, " ")

    words = text.split()
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result



def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    result = []

    for word in counts:
        result.append((word, counts[word]))

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i][1] < result[j][1] or (
                result[i][1] == result[j][1]
                and result[i][0] > result[j][0]
            ):
                result[i], result[j] = result[j], result[i]
    return result[:k]
