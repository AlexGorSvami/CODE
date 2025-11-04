def findXSum(nums: list, k: int, x: int) -> list:
    from collections import Counter 
    l = len(nums)
    result = []
    for i in range(l - k + 1):
        s = nums[i:i + k]
        ls = sorted([(i, j) for i, j in Counter(s).items()], reverse = True)
        if len(ls) < x:
            result.append(sum(s))
        else:
            result.append(sum([ls[i][0] * ls[i][1] for i in range(x)]))
    return result 
