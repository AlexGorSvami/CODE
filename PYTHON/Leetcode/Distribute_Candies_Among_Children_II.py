def distributeCandies(n: int, limit: int) -> int:
    out = 0
    m = min(n, limit)
    for i in range(m + 1):
        out += max(0, m - abs(n - i - m)+1)
    return out
