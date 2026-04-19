from typing import List 
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        answer = 0 
        n, m = len(nums1), len(nums2)
        for i in range(n):
            if i >= m-1:
                break 
            l, h = i + 1, m - 1 
            while l < h:
                midd = l + (h-l+1) // 2 
                if nums1[i] <= nums2[midd]:
                    l = midd 
                else:
                    h = midd - 1 
            answer = max(answer, h - i if nums2[h] >= nums1[i] else 0)
        return answer 

