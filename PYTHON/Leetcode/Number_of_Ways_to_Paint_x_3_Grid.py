def numOfWays(n: int) -> int:
    MOD = 10**9 + 7 
    a = b = 6 

    for _ in range(2, n + 1):
        a, b = (2*a + 2*b) % MOD, (2*a + 3*b) % MOD 

    return (a + b) % MOD 
