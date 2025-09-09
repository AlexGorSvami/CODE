def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:
    dp = [0, 1]
    share, result = 0, 0
    MOD = 10**9 + 7
    for i in range(2, n+1):
        if i - delay >= 1:
            share = (share + dp[i - delay]) % MOD 
        if i - forget >= 1:
            share = (share - dp[i - forget]) % MOD 
        dp.append(share)

    for i in range(n - forget+1, n+1):
        result = (result + dp[i]) % MOD 

    return result 
