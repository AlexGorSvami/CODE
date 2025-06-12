def maxAdjacentDistance(nums: list) -> int:
    max_difference = abs(nums[-1] - nums[0])
    for i in range(len(nums)-1):
        max_difference = max(max_difference, abs(nums[i] - nums[i+1]))
    return max_difference
