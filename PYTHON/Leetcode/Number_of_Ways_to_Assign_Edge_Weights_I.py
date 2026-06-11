from typing import List 
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0 

        g = {}
        for u, v in edges:
            g.setdefault(u, []).append(v)
            g.setdefault(v, []).append(u)

        q, seen, max_d = [1], {1}, 0 
        while q:
            q = [v for u in q for v in g.get(u, []) if v not in seen and not seen.add(v)]
            if q: max_d += 1 

        return pow(2, max_d - 1, 10**9 + 7)
