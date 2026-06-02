from typing import List 
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_l = min(s + d for s, d in zip(landStartTime, landDuration))
        min_w = min(s + d for s, d in zip(waterStartTime, waterDuration))

        l_then_w = min(max(min_l, s) + d for s, d in zip(waterStartTime, waterDuration))
        w_then_l = min(max(min_w, s) + d for s, d in zip(landStartTime, landDuration))

        return min(l_then_w, w_then_l)_
