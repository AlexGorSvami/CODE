def check(nums: list) -> bool:
    has_break = False
    breaks = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            has_break = True
            breaks += 1
            if breaks > 1:
                return False
    return not breaks or nums[0] >= nums[-1]


print(check([3,4,5,1,2]))
print(check([2,1,3,4]))
print(check([1,2,3]))
