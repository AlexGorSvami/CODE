def subsetXORSum(nums: list) -> int:
    summ = 0

    for i in nums:
        summ |= i 

    return summ * 2**(len(nums)-1)

print(subsetXORSum([1,3]))
print(subsetXORSum([5,1,6]))
print(subsetXORSum([3,4,5,6,7,8]))
