def findSmallestInteger(nums: list, value: int) -> int:
    from collections import Counter
    cnt = Counter([n % value for n in nums])
    for i in range(len(nums)):
        if cnt[i % value] == 0:
            return i 
        cnt[i % value] -= 1 
    return len(nums)
