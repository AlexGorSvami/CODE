def canPartition(nums: list) -> bool:
    if sum(nums) & 1 == 0:
        target = sum(nums) >> 1
        cur = {0}
        for i in nums:
            cur |= {i + x for x in cur}
            if target in cur:
                return True 
    return False


print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
