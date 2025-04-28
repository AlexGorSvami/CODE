def countSubarrays(nums: list, k: int) -> int:
    answer = 0
    curr = 0
    i = 0

    for j in range(len(nums)):
        curr += nums[j]
        while curr * (j - i+1) >= k:
            curr -= nums[i]
            i += 1 
        answer += j - i+1 
    return answer 


print(countSubarrays([2,1,4,3,5], 10))
print(countSubarrays([1,1,1], 5))
