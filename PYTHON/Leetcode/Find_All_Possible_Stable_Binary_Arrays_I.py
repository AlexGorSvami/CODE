def numberOfStableArrays(zero: int, one: int, limit: int) -> int:
    MOD = 10**9 + 7 

    @cache 
    def dp(rz, ro, p):
        if rz == 0 and ro == 0:
            return 1 
        else: 
            answer = 0

            for i in range(1, limit+1):
                if (p == 0 or p == -1) and ro - i >= 0:
                    answer += dp(rz, ro-i, 1)
                if (p == 1 or p == -1) and rz-i >= 0:
                    answer += dp(rz-i, ro, 0)

            return answer 

    return dp(zero, one, -1) % MOD
