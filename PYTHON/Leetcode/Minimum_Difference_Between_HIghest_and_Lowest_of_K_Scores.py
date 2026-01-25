def minimumDifference(nums: list, k: int) -> int:
    nums.sort()
    lowest = float('inf')
    n = len(nums)

    if n == 1:
        return 0 

    for i in range(n+1-k):
        num = nums[i+k-1] - nums[i]
        if num < lowest:
            lowest = num 

    return lowest 
