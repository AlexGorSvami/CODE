def countGoodArrays(n: int, m: int, k: int) -> int:
    MOD = 10**9 + 7
    max_n = n 
    fact = [1] * (max_n)
    inv_fact = [1] * (max_n)

    for i in range(1, max_n):
        fact[i] = (fact[i-1]*i) % MOD

    inv_fact[max_n-1] = pow(fact[max_n-1], MOD-2, MOD)
    for i in range(max_n-2, -1, -1):
        inv_fact[i] = (inv_fact[i+1] * (i + 1)) % MOD 

    def comb(n, r):
        if r < 0 or r > n:
            return 0 
        return (fact[n] * inv_fact[r] % MOD) * inv_fact[n - r] % MOD 

    t = n-1-k
    if t < 0:
        return 0 

    res = comb(n-1, t)
    res = res * m % MOD 
    res = res * pow(m-1, t, MOD) % MOD 

    return res
