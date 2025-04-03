def maximumTripletValue(nums: list) -> int:
    n = len(nums)
    left_max = [0] * n 
    right_max = [0] * n 

    for i in range(1, n):
        left_max[i] = max(left_max[i-1], nums[i-1])
        right_max[n-1-i] = max(right_max[n-i], nums[n-i])

    max_value = 0

    for j in range(1, n-1):
        max_value = max(max_value, (left_max[j] - nums[j]) * right_max[j])
    
    return max_value

print(maximumTripletValue([1,2,3]))


