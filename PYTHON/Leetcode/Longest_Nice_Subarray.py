def longestNiceSubarray(nums: list) -> int:
    left, right = 0, 0
    value = 0
    answer = 1
    while right < len(nums):
        while (nums[right] & value) != 0:
            value = value ^ nums[left]
            left += 1 
        value = value | nums[right]

        answer = max(answer, right - left + 1)
        right += 1

    return answer 


print(longestNiceSubarray([1,3,8,48,10]))
print(longestNiceSubarray([3,1,5,11,13]))
