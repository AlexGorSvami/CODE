from typing import List  
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        max_limit = n + m - 1 
        k = min(k, max_limit)

        dp = [[[-1] * (k + 1) for _ in range(m)] for _ in range(n)]

        start_cost = 1 if grid[0][0] != 0 else 0 
        start_score = grid[0][0]
        if start_cost > k:
            return -1 
        dp[0][0][start_cost] = start_score 

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue 
                cur_cost = 1 if grid[i][j] != 0 else 0 
                cur_score = grid[i][j]

                if i > 0:
                    top = dp[i-1][j]
                    for prev in range(k+1):
                        if top[prev] != -1:
                            new = prev + cur_cost 
                            if new <= k:
                                new_score = top[prev] + cur_score 
                                if new_score > dp[i][j][new]:
                                    dp[i][j][new] = new_score 

                if j > 0:
                    left = dp[i][j-1]
                    for prev in range(k+1):
                        if left[prev] != -1:
                            new = prev + cur_cost 
                            if new <= k:
                                new_score = left[prev] + cur_score 
                                if new_score > dp[i][j][new]:
                                    dp[i][j][new] = new_score

        answer = max(dp[n-1][m-1])
        return answer if answer != -1 else -1 

         
