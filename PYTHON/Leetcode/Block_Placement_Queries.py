from sortedcontainers import SortedList
from typing import List

class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (2 * n)
        
    def update(self, i: int, val: int):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
            
    def query(self, l: int, r: int) -> int:
        l += self.n
        r += self.n
        res = 0
        while l < r:
            if l % 2 == 1:
                res = max(res, self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = max(res, self.tree[r])
            l //= 2
            r //= 2
        return res

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        mx = max(q[1] for q in queries) + 1
        # Увеличиваем размер дерева на 1 для корректной обработки индекса mx
        st = SegmentTree(mx + 1) 
        sl = SortedList([0, mx])
        st.update(mx, mx)
        
        res = []
        for q in queries:
            x = q[1]
            if q[0] == 1:
                sl.add(x)
                i = sl.index(x)
                prev, nxt = sl[i - 1], sl[i + 1]
                
                st.update(x, x - prev)
                st.update(nxt, nxt - x)
            else:
                sz = q[2]
                i = sl.bisect_right(x) - 1
                prev = sl[i]
                
                max_gap = max(st.query(0, prev + 1), x - prev)
                res.append(max_gap >= sz)
                
        return res
