def partitionArray(nums: list, k: int) -> int:
    n = len(nums)
    record = 0
    res = 0
    nums.sort()

    while (record < n):
        record_value = nums[record]
        res += 1 
        while (((record+1) < n) and ((nums[(record+1)] - record_value) <= k)):
            record += 1 
        record += 1 

    return res 
