def word_count(text: str) -> dict[str, int]:
    if not text:
        return {}
    
    punctuations = ' .,!?;:'
    for p in text:
        if p in punctuations:
            text = text.replace(p, ' ')
    
    text = text.lower()
    words = text.split()
    wordFreq = {}
    
    for word in words:
        if word in wordFreq:
            wordFreq[word] += 1
        else:
            wordFreq[word] = 1
    
    return wordFreq
    
def top_k(text: str, k: int) -> list[tuple[str, int]]:
    if not text or k <= 0:
        return []
    
    wordFreq = word_count(text)
    sortedWords = sorted(wordFreq.items(), key=lambda x: (-x[1], x[0]))
    
    return sortedWords[:k]