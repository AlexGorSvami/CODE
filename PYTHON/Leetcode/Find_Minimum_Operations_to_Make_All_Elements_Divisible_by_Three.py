def minimumOperations(nums: list) -> int:
    return sum([min(nums[i] % 3, 3 - (nums[i] % 3)) for i in range(len(nums))])
