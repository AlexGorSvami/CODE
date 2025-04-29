def countSubarrays(nums: list, k: int) -> int:
    result = 0
    num = max(nums)
    n = len(nums)
    l = 0
    count = 0

    for i in range(n):
        if nums[i] == num:
            count += 1 

        while count == k:
            result += n-i 
            if nums[l] == num:
                count -= 1 
            l += 1 

    return result 

print(countSubarrays([1,3,2,3,3], 2))
print(countSubarrays([1,4,2,1], 3))
