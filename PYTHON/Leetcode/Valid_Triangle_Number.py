def triangleNumber(nums: list) -> int:
    n = len(nums)
    nums.sort()
    result = 0 
    for i in range(2, n):
        j = i - 1
        k = 0
        while k < j:
            if nums[k] + nums[j] > nums[i]:
                result += j - k 
                j -= 1 
            else:
                k += 1 
    return result 
