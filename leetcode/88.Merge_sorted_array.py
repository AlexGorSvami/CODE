class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(m,n+m):
            nums1[i] = nums2[i-m]
        nums1.sort() 
