def minimumDeletions(s: str) -> int:
    counts = [0] * len(s)
    counts_b = 0 
    for i, c in  enumerate(s):
        counts[i] = counts_b 
        counts_b += int(c == 'b')
    counts_a = 0 
    for i, c in reversed(tuple(enumerate(s))):
        counts[i] += counts_a 
        counts_a += int(c == 'a')

    return min(counts)
