def maximumProfit(prices: list, k: int) -> int:
    INF = float('-inf')
    dp = [[INF] * 3 for _ in range(k + 1)]
    dp[0][0] = 0 

    for price in prices:
        new_dp = [row[:] for row in dp]

        for t in range(k + 1):
            if dp[t][0] != INF:
                new_dp[t][1] = max(new_dp[t][1], dp[t][0] - price)
                new_dp[t][2] = max(new_dp[t][2], dp[t][0] + price)

            if t < k and dp[t][1] != INF:
                new_dp[t + 1][0] = max(new_dp[t + 1][0], dp[t][1] + price)

            if t < k and dp[t][2] != INF:
                new_dp[t + 1][0] = max(new_dp[t + 1][0], dp[t][2] - price)

        dp = new_dp 
    
    return max(dp[t][0] for t in range(k + 1))

