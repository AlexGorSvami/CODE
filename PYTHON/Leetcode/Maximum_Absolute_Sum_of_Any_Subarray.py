def maxAbsoluteSum(nums: list) -> int:
    n = len(nums)
    array = [num for num in nums]

    answer = abs(nums[0])
    for i in range(1, n):
        array[i] += max(0, array[i-1])
        answer = max(answer, array[i])
    
    array = [-num for num in nums]

    for i in range(1, n):
        array[i] += max(0, array[i-1])
        answer = max(answer, array[i])

    return answer 



print(maxAbsoluteSum([1, -3, 2, 3, -4]))
print(maxAbsoluteSum([2, -5, 1, -4, 3, -2]))
