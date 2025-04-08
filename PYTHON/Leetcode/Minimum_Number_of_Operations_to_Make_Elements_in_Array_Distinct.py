def minimumOperations(nums: list) -> int:
    answer = 0

    while len(nums) > len(set(nums)):
        nums = nums[3:]
        answer += 1

    return answer 

print(minimumOperations([1,2,3,4,2,3,3,5,7]))
print(minimumOperations([4,5,6,4,4]))
print(minimumOperations([6,7,8,9]))
