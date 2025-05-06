def buildArray(nums: list) -> list:
    return [nums[nums[i]] for i in range(len(nums))]


print(buildArray([0,2,1,5,3,4]))
print(buildArray([5,0,1,2,3,4]))
