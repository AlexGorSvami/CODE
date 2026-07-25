from itertools import combinations_with_replacement
from typing import List 
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        return len({x ^ y ^ z for x, y, z in combinations_with_replacement(nums, 3)})


              
