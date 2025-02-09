def countBadPairs(nums: list) -> int:
    from collections import Counter
    count = Counter()
    result = 0
    for i, val in enumerate(nums):
        result += i - count[i - val]
        count[i - val] += 1
    return result 


print(countBadPairs([4,1,3,3]))
print(countBadPairs([1,2,3,4,5]))
