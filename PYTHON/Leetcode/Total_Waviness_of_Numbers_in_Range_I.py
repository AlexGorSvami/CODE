from functools import cache 
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n: int) -> int:
            s = str(n)

            @cache 
            def dp(i, d1, d2, is_limit, is_lz):
                if i == len(s):
                    return 1, 0 
                total_cnt = total_wave = 0 
                limit = int(s[i]) if is_limit else 9 

                for d in range(limit + 1):
                    next_lz = is_lz and d == 0
                    nd1, nd2 = (-1, -1) if next_lz else (d, d1 if not is_lz else -1)

                    cnt, wave = dp(i + 1, nd1, nd2, is_limit and d == limit, next_lz)
                    total_cnt += cnt 
                    total_wave += wave 

                    if d2 != -1 and ((d1 > d2 and d1 > d) or (d1 < d2 and d1 < d)):
                        total_wave += cnt 

                return total_cnt, total_wave 
            
            return dp(0, -1, -1, True, True)[1]

        return solve(num2) - solve(num1 - 1)
