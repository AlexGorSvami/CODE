from typing import List
from collections import defaultdict, deque 
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        graph = defaultdict(list)
        for i, v in enumerate(arr):
            graph[v].append(i)

        q, visited = deque([(0, 0)]), {0}

        while q:
            i, steps = q.popleft()
            if i == len(arr) - 1:
                return steps 

            # We combine value jumps and +/- 1 steps
            for next in graph[arr[i]] + [i-1, i+1]:
                if 0 <= next < len(arr) and next not in visited:
                    visited.add(next)
                    q.append((next, steps+1))

            graph[arr[i]].clear()
