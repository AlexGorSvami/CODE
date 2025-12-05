def countPartitions(nums: list) -> int:
    output, left, right = 0, 0, sum(nums)
    for num in nums:
        left += num 
        right -= num 
        if not right:
            break 
        if not(abs(right - left) & 1):
            output += 1 
    return output 
