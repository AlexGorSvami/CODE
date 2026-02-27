def minOperations(s: str, k: int) -> int:
    def ceil(x, y):
        return (x + y - 1) // y 
    
    n = len(s)
    zeroes = s.count('0')
    if n == k:
        if zeroes == 0:
            return 0 
        elif zeroes == n:
            return 1 
        else: 
            return -1 

    inf = float('inf')
    answer = inf 
    if zeroes % 2 == 0:
        m = max(ceil(zeroes, k), ceil(zeroes, n - k))
        m += m & 1 
        answer = min(answer, m)

    if zeroes % 2 == k % 2:
        m = max(ceil(zeroes, k), ceil(n - zeroes, n - k))
        m += (m & 1) == 0 
        answer = min(answer, m)

    return answer if answer < inf else -1
