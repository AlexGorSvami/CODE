def countValidSelections(nums: list) -> int:
    cnt = 0 
    while 0 in nums:
        ind = nums.index(0)
        if sum(nums[:ind]) == sum(nums[ind:]):
            cnt += 2 
        elif abs(sum(nums[:ind]) - sum(nums[ind:])) == 1:
            cnt += 1 
        nums.remove(0)

    return cnt 
