def findMaxForm(strs: list, m: int, n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for s in strs:
        ones = zeroes = 0 
        for chr in s:
            ones += chr == '1'
            zeroes += chr == '0'

        for i in range(m, zeroes-1, -1):
            for j in range(n, ones-1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeroes][j - ones] + 1)

    return dp[-1][-1]
