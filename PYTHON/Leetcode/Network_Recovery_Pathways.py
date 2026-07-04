from typing import List
import heapq
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        for u, v, c in edges:
            if online[u] and online[v]:
                adj[u].append((v, c))

        def check(x):
            dist = [float('inf')] * n 
            dist[0] = 0 
            pq = [(0, 0)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]: continue 
                if u == n-1: return d <= k 
                for v, c in adj[u]:
                    if c >= x and d + c < dist[v]:
                        dist[v] = d + c 
                        heapq.heappush(pq, (dist[v], v))
            return False 

        low, high, answer = 0, max([c for _, _, c in edges] + [-1]), -1 
        while low <= high:
            middle = (low + high) // 2 
            if check(middle): 
                answer, low = middle, middle + 1 
            else:
                high = middle - 1 
        return answer 


