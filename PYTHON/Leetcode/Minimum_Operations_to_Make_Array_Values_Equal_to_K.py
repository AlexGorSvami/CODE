def minOperations(nums: list, k: int) -> int:
    if min(nums) < k:
        return -1

    answer = 0
    numbers = set(nums)
    for num in numbers:
        if num > k:
            answer += 1

    return answer 


print(minOperations([5,2,5,4,5], 2))
print(minOperations([2,1,2], 2))
print(minOperations([9,7,5,3], 1))
