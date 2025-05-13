def lengthAfterTransformations(s: str, t: int) -> int:
    mod = 10**9 + 7
    count = [0] * 26
    for ch in s:
        count[ord(ch) - 97] += 1 
    for _ in range(t):
        x = count[-1]
        for i in range(25, 0, -1):
            count[i] = count[i-1]
        count[1] = (count[1] + x) % mod 
        count[0] = x 
    return sum(count) % mod 
