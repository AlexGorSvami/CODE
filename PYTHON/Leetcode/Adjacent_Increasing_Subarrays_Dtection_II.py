def maxIncreasingSubarrays(nums: list) -> int:
    p_len, c_len = 1, 1 
    result = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            c_len += 1 
        else:
            p_len, c_len = c_len, 1 
        result = int(max(result, max(c_len/2, min(p_len, c_len))))
    return result 
