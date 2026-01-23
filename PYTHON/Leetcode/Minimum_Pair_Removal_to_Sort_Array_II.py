def minimumPairRemoval(nums: list) -> int:
    from math import inf 
    from heapq import heappush, heappop, heapify 
    from itertools import pairwise 
    n = len(nums)
    nums.append(inf)
    prev, next = list(range(-1, n)), list(range(1, n+1))
    min_heap = [(a+b, i) for i, (a, b) in enumerate(pairwise(nums))]
    heapify(min_heap)
    result, bad = 0, n - sum(1 for a, b in pairwise(nums) if a <= b)
    while bad:
        summ, i = heappop(min_heap)
        r = next[i]
        if prev[r] != i or nums[i] + nums[r] != summ:
            continue 

        rr = next[r]
        bad += (nums[prev[i]] <= nums[i]) + (nums[i] <= nums[r]) + (nums[r] <= nums[rr])
        prev[rr], next[i] = i, rr 
        nums[i] = summ 
        bad -= 1 + (nums[prev[i]] <= nums[i]) + (nums[i] <= nums[rr])

        if i:
            heappush(min_heap, (nums[prev[i]] + nums[i], prev[i]))
        if rr < n:
            heappush(min_heap, (nums[i] + nums[rr], i))

        result += 1 

    return result 
