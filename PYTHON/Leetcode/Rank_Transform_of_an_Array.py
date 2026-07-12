from typing import List 
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_map = {v: i for i, v in enumerate(sorted(set(arr)), 1)}
        return [rank_map[x] for x in arr]
