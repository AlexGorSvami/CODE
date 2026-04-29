from typing import List
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid) + 1
        prefix = [[0] * n for _ in range(n)]
        prev_pick = [0] * n 
        prev_skip = [0] * n 

        for i in range(n-1):
            for j in range(n-1):
                prefix[i][j+1] = prefix[i][j] + grid[j][i]

        for i in range(1, n-1):
            curr_pick = [0] * n 
            curr_skip = [0] * n 

            for curr in range(n):
                for prev in range(n):
                    if curr > prev:
                        score = prefix[i-1][curr] - prefix[i-1][prev]
                        curr_pick[curr] = max(curr_pick[curr], prev_skip[prev] + score) 
                        curr_skip[curr] = max(curr_pick[curr], prev_skip[prev] + score)
                    else:
                        score = prefix[i][prev] - prefix[i][curr]
                        curr_pick[curr] = max(curr_pick[curr], prev_pick[prev] + score)
                        curr_skip[curr] = max(curr_skip[curr], prev_pick[prev])

            prev_pick = curr_pick 
            prev_skip = curr_skip 

        return max(prev_pick)
