def countHillValley(nums: list) -> int:
    hills = 0
    i = 1

    while i < len(nums)-1:
        j = i + 1 
        while j < len(nums)-1 and nums[j] == nums[i]:
            j += 1
        if (nums[i-1] > nums[i] and nums[j] > nums[i]):
            hills += 1 
        if (nums[i-1] < nums[i] and nums[j] < nums[i]):
            hills += 1 
        i = j 
    return hills 
