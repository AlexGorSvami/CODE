def maxDistinctElements(nums: list, k: int) -> int:
    n = len(nums)
    max_val = float('-inf')
    result = 0
    nums.sort()
    for i in range(n):
        if (nums[i] + k) <= max_val:
            continue
        result += 1 
        max_val = max(max_val + 1, nums[i] - k)
    return result 
