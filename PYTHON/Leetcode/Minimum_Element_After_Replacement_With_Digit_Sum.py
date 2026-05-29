from typing import List 
class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            n = 0
            for j in str(i):
                n += int(j) 
            arr.append(n)
            n = 0

        return min(arr)

