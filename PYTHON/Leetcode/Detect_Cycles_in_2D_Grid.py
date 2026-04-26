from typing import List
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n, seen = len(grid), len(grid[0]), set()
        
        def dfs(x, y, p):
            seen.add((x, y))
            return any(0 <= nx < m and 0 <= ny < n and grid[nx][ny] == grid[x][y] and
                      ((nx, ny) != p and ((nx, ny) in seen or dfs(nx, ny, (x, y))))
                      for nx, ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)))
        
        return any(dfs(i, j, (-1,-1)) for i in range(m) for j in range(n) 
                   if (i, j) not in seen)
