def mininmumCost(nums: list) -> int:
    n = sorted(nums)[:3]
    if nums[0] in n:
        return sum(n)
    return nums[0] + n[0] + n[1]
