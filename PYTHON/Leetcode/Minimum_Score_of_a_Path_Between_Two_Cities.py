from typing import List 
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        q, seen, min_score = [1], {1}, float('inf')
        for node in q:
            for neighbor, weight in graph[node]:
                min_score = min(min_score, weight)
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append(neighbor)

        return min_score 
