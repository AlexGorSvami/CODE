def maximumCount(nums: list) -> int:
    pos = len([i for i in nums if i > 0])
    neg = len([i for i in nums if i < 0])
    return max(pos, neg)


print(maximumCount([-2,-1,-1,1,2,3]))
print(maximumCount([-3,-2,-1,0,0,1,2]))
print(maximumCount([5,20,66,1314]))
