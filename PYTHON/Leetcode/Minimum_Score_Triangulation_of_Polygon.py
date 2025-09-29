def minScoreTriangulation(values: list) -> int:
    n = len(values)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for i in range(0, n - length):
            j = i + length 
            best = float('inf')
            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j] 
                if cost < best:
                    best = cost 
            dp[i][j] = best 
    return dp[0][n-1]
