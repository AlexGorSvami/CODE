from typing import List 
from collections import deque 
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
       m, n  = len(grid), len(grid[0])
       start_h = health - grid[0][0]

       if start_h <= 0:
           return False 

       q = deque([(0, 0, start_h)])
       visited = {(0, 0): start_h}

       while q:
           r, c, h = q.popleft()

           if r == m - 1 and c == n - 1:
               return True 

           for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
               nr, nc = r + dr, c + dc 

               if 0 <= nr < m and 0 <= nc < n:
                   nh = h - grid[nr][nc]

                   if nh > visited.get((nr, nc), 0):
                       visited[(nr, nc)] = nh 
                       q.append((nr, nc, nh))
       return False 
