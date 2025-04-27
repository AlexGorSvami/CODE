def countSubarrays(nums: list) -> int:
    l = len(nums)
    n = 0 
    half = [nums[i]/2 for i in range(l)]
    for i in range(l-2):
        n += (nums[i] + nums[i+2] == half[i+1])
    return n 


print(countSubarrays([1,2,1,4,1]))
print(countSubarrays([1,1,1]))
