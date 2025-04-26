def countSubarrays(nums: list, minK: int, maxK: int) -> int:
    count = 0
    n = len(nums)
    right = 0
    left = 0
    min_value = float('inf')
    max_value = float('-inf')

    while right < n:
        min_value = min(min_value, nums[right])
        max_value = max(max_value, nums[right])

        if min_value == minK and max_value == maxK:
            if min_value == max_value or min_value == nums[right] or max_value == nums[right]:
                count += right - left+1
            else:
                count += 1 

        elif max_value > maxK:
            while left <= right:
                left += 1 
                max_value = float('-inf')
                min_value = float('inf')
        elif min_value < minK:
            while left <= right:
                left += 1 
                min_value = float('inf')
                max_value = float('-inf')
        right += 1 
    return count 


print(countSubarrays([1,3,5,2,7,5], 1, 5))
print(countSubarrays([1,1,1,1], 1, 1))
