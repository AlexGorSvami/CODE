def maximumEnergy(energy: list, k: int) -> int:
    n = len(energy)
    dp = [0 for _ in range(n)]
    for i in range(n-k, n):
        dp[i] = energy[i]

    for i in range(n-k-1, -1, -1):
        dp[i] = energy[i] + dp[i+k]
    return max(dp)
