def maxAscendingSum(nums: list) -> int:
    current_sum = max_sum = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_sum += nums[i]
        else:
            current_sum = nums[i]
        max_sum = max(max_sum, current_sum )
    return max_sum


print(maxAscendingSum([10,20,30,5,10,50]))
print(maxAscendingSum([10,20,30,40,50]))
print(maxAscendingSum([12,17,15,13,10,11,12]))
