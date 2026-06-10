class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        res = []
        n = len(nums)
        for i in range(n):
            c_min = c_max = nums[i]
            for j in range(i, n):
                if nums[j] < c_min: c_min = nums[j]
                if nums[j] > c_max: c_max = nums[j]
                res.append(c_max - c_min)
        return sum(sorted(res, reverse=True)[:k])
