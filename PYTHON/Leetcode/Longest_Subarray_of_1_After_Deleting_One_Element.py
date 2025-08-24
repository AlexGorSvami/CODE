def longestSubarray(nums: list) -> int:
    i = j = cnt = max_1 = 0
    l1 = len(nums)
    while i < l1:
        if nums[i] == 0:
            cnt += 1 
        while j < l1 and cnt > 1:
            if nums[j] == 0:
                cnt -= 1 
            j += 1 
        max_1 = max(i-j, max_1)
        i += 1 
    return max_1  
