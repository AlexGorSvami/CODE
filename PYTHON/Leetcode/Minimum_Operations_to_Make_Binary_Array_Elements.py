def minOperations(nums: list) -> int:
    answer = 0
    for i, el in enumerate(nums):
        if el == 0:
            if i + 2 >= len(nums):
                return -1 
            nums[i + 1] ^= 1 
            nums[i + 2] ^= 1 
            answer += 1
    
    return answer 



print(minOperations([0,1,1,1,0,0]))
print(minOperations([0,1,1,1]))
