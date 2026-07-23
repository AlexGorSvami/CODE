from typing import List
import re
import bisect
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        z_spans = [m.span() for m in re.finditer(r'0+', s)]
        pref = [0] * (len(s) + 1)
        for i, c in enumerate(s):
            pref[i+1] = pref[i] + (c == '1')
            
        # Изначальное количество единиц во всей строке s
        total_ones = pref[-1]
            
        if not z_spans:
            return [total_ones] * len(queries)

        ends = [e for _, e in z_spans]
        starts = [st for st, _ in z_spans]
        Z = [e - st for st, e in z_spans]
        O = [starts[i+1] - ends[i] for i in range(len(z_spans)-1)]
        Zp = [Z[i] + Z[i+1] for i in range(len(Z)-1)]

        def build(arr, op):
            if not arr: return []
            st = [arr]
            for k in range(1, len(arr).bit_length()):
                st.append([op(st[-1][x], st[-1][x + (1 << (k - 1))]) 
                        for x in range(len(arr) - (1 << k) + 1)])
            return st

        def query(st, op, l, r):
            if l > r: return -float('inf') if op is max else float('inf')
            k = (r - l + 1).bit_length() - 1
            return op(st[k][l], st[k][r - (1 << k) + 1])

        st_z, st_o, st_zp = build(Z, max), build(O, min), build(Zp, max)
        ans = []
        
        for l, r in queries:
            i, j = bisect.bisect_right(ends, l), bisect.bisect_left(starts, r + 1) - 1
            
            # Если в подстроке меньше двух блоков нулей, 
            # нет единиц, окруженных нулями -> обмен невозможен.
            if i >= j:
                ans.append(total_ones)
                continue
                
            z_first = min(r + 1, ends[i]) - max(l, starts[i])
            z_last = min(r + 1, ends[j]) - max(l, starts[j])
            
            z_max = max(z_first, z_last, query(st_z, max, i + 1, j - 1))
            o_min = query(st_o, min, i, j - 1)
            
            p_max = z_first + z_last if j == i + 1 else max(
                z_first + Z[i+1],
                Z[j-1] + z_last,
                query(st_zp, max, i + 1, j - 2)
            )
            
            # Прибавляем чистый прирост к общему количеству единиц
            ans.append(total_ones + max(p_max, z_max - o_min))
            
        return ans
