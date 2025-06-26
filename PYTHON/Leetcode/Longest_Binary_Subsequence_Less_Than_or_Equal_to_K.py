def longestSubsequence(s: str, k: int) -> int:
    res = s.count('0')
    curr = 0
    n = len(s)

    for i in range(len(s)-1, -1, -1):
        if s[i] == '1':
            curr += 1 << (n-1-i)
            if curr > k:
                break
            res += 1 

    return res 
