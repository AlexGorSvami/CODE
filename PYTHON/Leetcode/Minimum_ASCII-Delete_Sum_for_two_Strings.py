def minimumDeleteSum(s1: str, s2: str) -> int:
    n1, n2 = len(s1), len(s2)
    total = sum([ord(i) for i in s1]) + sum([ord(i) for i in s2])

    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(n1):
        for j in range(n2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + ord(s1[i])
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    return total - 2 * dp[-1][-1]
