def minPairSum(nums: list) -> int:
    n = len(nums)
    nums.sort()
    result = 0
    for num in range(int(n/2)):
        result = max(result, nums[num] + nums[n - 1 - num])
    return result 
