def zigzag_arrays(n: int, l: int, r: int) -> int:
    MOD = 10**9 + 7 
    k = r - l + 1 

    if k <= 0: return 0 
    if n == 1: return k % MOD 

    def calc(size):
        dp = [1] * size 
        for _ in range(n-1):
            nxt, curr = [], 0 
            for val in dp:
                nxt.append(curr)
                curr = (curr + val) % MOD 
            dp = nxt[::-1]
        return sum(dp) % MOD 

    if k <= n + 1:
        return (2 * calc(k)) % MOD 

    pts = [calc(x) for x in range(1, n + 2)]
    answer = 0 

    pref, suff = [1] * (n + 2), [1] * (n + 2)
    for i in range(1, n + 2):
        pref[i] = (pref[i-1] * (k-i)) % MOD 
    for i in range(n, -1, -1):
        suff[i] = (suff[i+1] * (k-i-1)) % MOD 

    fact = [1] * (n + 2)
    for i in range(1, n+2):
        fact[i] = (fact[i-1] * i) % MOD 

    for i in range(1, n+2):
        num = (pref[i-1] * suff[i]) % MOD 
        den = (fact[i-1] * fact[n+1-i]) % MOD 
        if (n + 1 - i) % 2:
            den = -den 

        term = (pts[i-1] * num) % MOD * pow(den % MOD, MOD-2, MOD) % MOD 
        answer = (answer + term) % MOD 

    return (2 * answer) % MOD
