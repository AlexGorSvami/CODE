class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = {}

        for i, num in enumerate(nums):
            example = target - num

            if example in nums_dict:
                return [nums_dict[example], i]

            nums_dict[num] = i

        return []

