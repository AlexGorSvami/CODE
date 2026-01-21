def minBitwiseArray(nums: list) -> list:
    for i in range(len(nums)):
        result = -1
        d = 1 

        while (nums[i] & d) != 0:
            result = nums[i] - d 
            d <<= 1 
        nums[i] = result 

    return nums 
