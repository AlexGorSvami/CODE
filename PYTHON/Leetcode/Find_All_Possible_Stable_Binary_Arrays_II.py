def numberOfStableArrays(zero: int, one: int, limit: int) -> int:
    MOD = 10**9 +7

    dp1 = [[0]*(one+1) for _ in range(zero+1)]
    dp2 = [[0]*(one+1) for _ in range(zero+1)]

    for i in range(1, min(limit, zero) + 1):
        dp1[i][0] = 1 
    for j in range(1, min(limit, one) + 1):
        dp2[0][j] = 1 

    for k in range(1, zero+1):
        for l in range(1, one+1):
            dp1[k][l] = dp1[k-1][l] + dp2[k-1][l]
            if k > limit:
                dp1[k][l] -= dp2[k-limit-1][l]

            dp2[k][l] = dp2[k][l-1] + dp1[k][l-1]
            if l > limit:
                dp2[k][l] -= dp1[k][l-limit-1]

    return (dp1[zero][one] + dp2[zero][one]) % MOD

