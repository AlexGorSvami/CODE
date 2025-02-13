def minOperations(nums: list, k: int) -> int:
    import heapq

    result = 0
    heapq.heapify(nums)
    while nums:
        if nums[0] >= k:
            break
        min1 = heapq.heappop(nums)
        min2 = heapq.heappop(nums)
        heapq.heappush(nums, 2*min1+min2)
        result += 1 

    return result 




print(minOperations([2,11,10,1,3], 10))
print(minOperations([1,1,2,4,9], 20))
