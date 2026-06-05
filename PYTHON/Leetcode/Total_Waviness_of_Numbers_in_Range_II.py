class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n: int) -> int:
            if n < 100: 
                return 0
            
            s = str(n)
            
            @cache
            def dp(i, tight, lead, p1, p2):
                if i == len(s): 
                    return 1, 0  # (количество валидных комбинаций, сумма волнистости)
                
                c, w = 0, 0
                limit = int(s[i]) if tight else 9
                
                for d in range(limit + 1):
                    nl = lead and d == 0
                    is_w = p2 >= 0 and (p2 < p1 > d or p2 > p1 < d)
                    
                    sc, sw = dp(i + 1, tight and d == limit, nl, -1 if nl else d, -1 if nl else p1)
                    
                    c += sc
                    w += sw + sc * is_w
                    
                return c, w
                
            return dp(0, True, True, -1, -1)[1]
            
        return solve(num2) - solve(num1 - 1)
