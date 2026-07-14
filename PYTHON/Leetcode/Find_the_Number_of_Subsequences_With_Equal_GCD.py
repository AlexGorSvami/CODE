from typing import List
from math import gcd 
from functools import cache 
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        @cache 
        def dp(i, g1, g2):
            if i == len(nums):
                return int(g1 == g2 > 0)
            return (dp(i+1, g1, g2) +
                    dp(i+1, gcd(g1, nums[i]) if g1 else nums[i], g2) + 
                    dp(i+1, g1, gcd(g2, nums[i]) if g2 else nums[i])) % 1000000007
        return dp(0, 0, 0)
