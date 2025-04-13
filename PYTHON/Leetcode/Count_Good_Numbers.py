def countGoodNumbers(n: int) -> int:
    MOD = 10**9 + 7
    return (pow(5, (n + 1) // 2, MOD) * pow(4, n // 2, MOD)) % MOD


print(countGoodNumbers(1))
print(countGoodNumbers(4))
print(countGoodNumbers(50))
