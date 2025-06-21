from collections import Counter
def minimumDeletions(word: str, k: int) -> int:
    cnt = Counter(word)
    freqs = list(cnt.items())
    min_deletions = (float('inf'))

    for i in range(len(freqs)):
        _, x = freqs[i]
        total = 0
        for j in range(len(freqs)):
            if i == j:
                continue
            _, y = freqs[j]
            if y < x:
                total += y
            elif y > x + k:
                total += y - x-k
        min_deletions = min(min_deletions, total)
    return min_deletions
