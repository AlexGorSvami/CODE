def maximumAmount(coins: list) -> int:
    row = len(coins)
    col = len(coins[0])
    dp = [[[-float('inf')] * 3 for _ in range(col+1)] for _ in range(row+1)]
    dp[row][col-1] = [0,0,0]
    dp[row-1][col] = [0,0,0]

    for i in range(row-1, -1, -1):
        for j in range(col-1, -1, -1):
            for k in range(3):
                if k > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j][k-1])
                    dp[i][j][k] = max(dp[i][j][k], dp[i+1][j][k-1], dp[i][j+1][k-1])
                dp[i][j][k] = max(dp[i][j][k], coins[i][j] + max(dp[i+1][j][k], dp[i][j+1][k]))

    return dp[0][0][2]
