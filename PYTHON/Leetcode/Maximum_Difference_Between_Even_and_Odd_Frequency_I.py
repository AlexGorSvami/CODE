def maxDifference(s: str) -> int:
    from collections import Counter

    freq = Counter(s)
    max_odd = float('-inf')
    min_even = float('-inf')

    for cnt in freq.values():
        if cnt % 2 == 1:
            max_odd = max(max_odd, cnt)
        else:
            min_even = min(min_even, cnt)

    return max_odd - min_even 
