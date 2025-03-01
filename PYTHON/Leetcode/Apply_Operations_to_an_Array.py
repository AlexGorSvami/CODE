def applyOperations(nums: list) -> list:
    i = 0
    count = 0
    while i < len(nums) - 1 - count:
        if nums[i] == 0:
            nums.append(nums.pop(i))
            count += 1
            i -= 1
        elif i < len(nums) - 1 and nums[i] == nums[i+1]:
            nums[i] *= 2
            nums.pop(i+1)
            nums.append(0)
            count += 1
        i += 1
    return nums 


print(applyOperations([1,2,2,1,1,0]))
print(applyOperations([0,1]))
