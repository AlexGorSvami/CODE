def specialTriplets(nums: list) -> int:
    from collections import Counter
    lt, rt = Counter(), Counter(nums)
    count = 0

    for n in nums:
        rt[n] -= 1 
        count += lt[n*2] * rt[n*2]
        count %= 10**9 + 7 
        lt[n] += 1 

    return count 
