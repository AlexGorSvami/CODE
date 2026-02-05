def constructTransformedArray(nums: list) -> list:
    return [nums[(i + nums[i]) % len(nums)] for i in range(len(nums))]
