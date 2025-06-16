def maximumDifference(nums: list) -> int:
    n = nums[::-1]
    if n == nums:
        return -1
    n_max = max(nums)
    n_min = min(nums)
    if nums.index(n_max) > nums.index(n_min):
        return n_max - n_min 
    l = len(nums)
    i = 0
    j = 1 
    n_max = -1 
    while j < l-1:
        if nums[j] > nums[i]:
            n_max = max(n_max, nums[j]-nums[i])
            j += 1 
        else:
            i += 1 
            j = i+1 
    return n_max
