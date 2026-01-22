def minimumPairRemoval(nums: list) -> int:
    op, n = 0, len(nums)
    while not all(nums[i] <= nums[i+1] for i in range(n-1)):
        start = 0 
        for i in range(1, n-1):
            if nums[start] + nums[start+1] > nums[i] + nums[i+1]:
                start = i 
        nums[start] += nums.pop(start+1)
        op += 1 
        n -= 1 

    return op 
