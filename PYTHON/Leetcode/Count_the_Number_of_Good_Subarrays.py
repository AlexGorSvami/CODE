def countGood(nums: list, k: int) -> int:
    count = {}
    goods, pairs = 0,0
    n, start = len(nums), 0
    for end in range(n):
        count[nums[end]] = count.get(nums[end], 0) + 1
        pairs += count[nums[end]] - 1
        while pairs >= k:
            count[nums[start]] -= 1
            pairs -= count[nums[start]]
            start += 1 
            goods += n-end 
    return goods 


print(countGood([1,1,1,1,1], 10))
print(countGood([3,1,4,3,2,2,4], 2))
