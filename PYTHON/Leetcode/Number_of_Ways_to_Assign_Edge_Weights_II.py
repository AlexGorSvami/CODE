from typing import List 
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = 18 
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)

        q = [1]
        visited = {1}
        while q:
            node = q.pop(0)
            for i in range(1, LOG):
                up[node][i] = up[up[node][i-1]][i-1]
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    depth[nei] = depth[node] + 1 
                    up[nei][0] = node 
                    q.append(nei)

        def get_dist(u, v):
            orig_u, orig_v = u, v 
            if depth[u] < depth[v]:
                u, v = v, u 
            for i in range(LOG):
                if (depth[u] - depth[v]) & (1 << i):
                    u = up[u][i]
            if u == v:
                return depth[orig_u] + depth[orig_v] - 2 * depth[u]
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u, v = up[u][i], up[v][i]
            return depth[orig_u] + depth[orig_v] - 2 * depth[up[u][0]]

        MOD = 10**9 + 7 
        return [pow(2, get_dist(u, v) - 1, MOD) if u != v else 0 for u, v in queries]


