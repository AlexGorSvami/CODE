def sortColors(nums: list) -> None:
    n, n1, n2 = -1, -1, -1
    for i in nums:
        if i == 0:
            n2 += 1; n1 += 1; n += 1
            nums[n2] = 2; nums[n1] = 1; nums[n] = 0
        elif i == 1:
            n2 += 1; n1 += 1
            nums[n2] = 2; nums[n1] = 1 
        else:
            n2 += 1 
            nums[n2] = 2 
