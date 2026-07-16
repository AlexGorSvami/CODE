from typing import List 
from math import gcd 
class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        mx = 0 
        p = sorted(gcd(x, mx := max(mx, x)) for x in nums)
        return sum(gcd(p[i], p[~i]) for i in range(len(p) // 2))
