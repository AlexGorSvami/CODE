from typing import List 
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt = max_alt = 0 
        for g in gain:
            curr_alt += g 
            max_alt = max(max_alt, curr_alt)
        return max_alt 
