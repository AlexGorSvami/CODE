def minOperations(s: str) -> int:
    s1, s2 = s[0:len(s):2], s[1:len(s):2]
    ch1, ch2 = s1.count('0'), s2.count('0')
    return min(len(s1) - ch1 + ch2, len(s2) - ch2 + ch1)
