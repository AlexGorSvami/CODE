def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    def refill(curr):
        return curr - 1 if curr > 1 else 0 

    size = 100 
    dp = [[0 for _ in range(size)] for _ in range(size)]
    dp[0][0] = poured 
    for i in range(1, size):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = refill(dp[i-1][j]) * 0.5
                continue 
            dp[i][j] = refill(dp[i-1][j]) * 0.5 + refill(dp[i-1][j-1]) * 0.5

    return dp[query_row][query_glass] if dp[query_row][query_glass] < 1 else 1
