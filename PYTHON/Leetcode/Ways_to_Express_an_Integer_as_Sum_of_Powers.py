def numberOfWays(n: int, x: int) -> int:
    powers = []
    mod = 10 ** 9 + 7
    i = 1

    while i ** x <= n:
        powers.append(i ** x)
        i += 1 

    dp = [0] * (n + 1)
    dp[0] = 1 

    for j in powers:
        for k in range(n, j-1, -1):
            dp[k] = (dp[k] + dp[k - j]) % mod 

    return dp[n]
