from functools import cache

class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)
        
        @cache
        def dfs(i):
            res = 1
            # Проверяем прыжки влево (-1) и вправо (1)
            for step in (-1, 1):
                for j in range(1, d + 1):
                    nx = i + step * j
                    # Если вышли за границы или встретили препятствие — прерываем направление
                    if 0 <= nx < n and arr[nx] < arr[i]:
                        res = max(res, 1 + dfs(nx))
                    else:
                        break
            return res
            
        return max(dfs(i) for i in range(n))
