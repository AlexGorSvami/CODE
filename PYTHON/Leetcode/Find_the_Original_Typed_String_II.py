from itertools import accumulate
def possibleStringCount(word: str, k: int) -> int:
    MOD = 10**9 + 7

    group = [1]
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            group[-1] += 1 
        else:
            group.append(1)

    n = len(group)
    total = 1 
    for size in group:
        total *= size 
        total %= MOD 

    if n >= k:
        return total 

    target = k - n

    dp = [[0] * target for _ in range(n)]
    group = [i-1 for i in group]

    for i in range(min(target, group[0] + 1)):
        dp[0][i] = 1 
    for index in range(1, n):
        psa = [0] + list(accumulate(dp[index-1], func=lambda x, y: x + y % MOD))
        query = lambda l, r: (psa[r+1] - psa[l] % MOD)

        for cur_s in range(target):
            dp[index][cur_s] = (dp[index][cur_s] + query(max(0, cur_s - group[index]), cur_s)) % MOD 
    less_k = sum(dp[-1])
    return (total - less_k) % MOD 


