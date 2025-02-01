def isArraySpecial(nums: list) -> bool:
    return all(i % 2 != j % 2 for i, j in zip(nums, nums[1:]))

print(isArraySpecial([1]))
print(isArraySpecial([2,1,4]))
print(isArraySpecial([4,3,1,6]))

