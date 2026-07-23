from typing import List 
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        flat = [v for row in grid for v in row]
        k %= m * n 
        flat = flat[-k:] + flat[:-k] if k else flat 
        return [flat[i:i+n] for i in range(0, m*n, n)]

