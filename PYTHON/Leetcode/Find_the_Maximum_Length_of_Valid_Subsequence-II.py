def maximumLength(nums: list, k: int) -> int:
    dp = [[0 for _ in range(k)] for _ in range(k)]
    answer = 0

    for num in nums:
        x = num % k
        for i in range(k):
            dp[x][i] = 1 + dp[i][x]
            answer = max(answer, dp[x][i])
    return answer
