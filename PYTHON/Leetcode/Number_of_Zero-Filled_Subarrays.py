def zeroFilledSubarray(nums: list) -> int:
    cnt, store, l = 0, 0, len(nums)
    for i in range(l):
        if nums[i] == 0:
            cnt += 1 
            store += cnt 
        else:
            cnt = 0 
    return store 
