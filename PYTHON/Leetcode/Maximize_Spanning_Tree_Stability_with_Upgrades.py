class UnionFind:
    def __init__(self, n: int):
        self.set = list(range(n))
        self.rank = [0] * n 

    def find_set(self, x: int) -> int:
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])
        return self.set[x]

    def union_set(self, x: int, y: int) -> bool:
        x, y = self.find_set(x), self.find_set(y)
        if x == y:
            return False 
        if self.rank[x] > self.rank[y]:
            x, y = y, x 
        self.set[x] = y 
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1 
        return True 

class Solution:
    def maxStability(self, n: int, edges: list, k: int) -> int:
        union_find = UnionFind(n)
        count = 0 
        res = float('inf')
        
        for u, v, s, m in edges:
            if not m:
                continue 
            if not union_find.union_set(u, v):
                return -1 
            count += 1 
            res = min(res, s)
            
        edges.sort(key=lambda x: -x[2])
        
        for u, v, s, m in edges:
            if m:
                continue 
            if not union_find.union_set(u, v):
                continue 
            count += 1 
            
            if count == (n - 1) - k:
                res = min(res, s)
            elif count == n - 1:
                res = min(res, 2 * s)
                
            if count == n - 1:
                break 
                
        return res if count == n - 1 else -1  
