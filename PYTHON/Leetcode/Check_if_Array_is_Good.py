class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums) - 1

        expected = list(range(1, n)) + [n, n]
        return nums == expected 
