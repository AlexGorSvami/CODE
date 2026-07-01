from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        q = deque()
        dist = [[-1] * n for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    dist[r][c] = 0
                    
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
                    
        pq = [(-dist[0][0], 0, 0)]
        dist[0][0] = -1 
        
        while pq:
            d, r, c = heapq.heappop(pq)
            d = -d
            
            if r == n - 1 and c == n - 1:
                return d
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] != -1:
                    heapq.heappush(pq, (-min(d, dist[nr][nc]), nr, nc))
                    dist[nr][nc] = -1
                    
        return 0
