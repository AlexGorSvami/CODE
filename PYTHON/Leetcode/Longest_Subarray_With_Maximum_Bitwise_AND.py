def longestSubarray(nums: list) -> int:
    answer = 1 
    left = 0
    target = max(nums)

    for right in range(len(nums)):
        while left <= right and nums[right] != target:
            answer = max(answer, right - left)
            left += 1 
        answer = max(answer, right - left + 1)
    
    return answer 

