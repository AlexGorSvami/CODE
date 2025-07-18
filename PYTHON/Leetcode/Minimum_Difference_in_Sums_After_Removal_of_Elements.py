def minimumDifference(nums: list) -> int:
    n = len(nums) // 3

    left = []
    sum_left = 0
    for i in range(n):
        heapq.heappush(left, -nums[i])
        sum_left += nums[i]

    sum_right = 0
    max_right, right = [], []
    for i in range(3*n-1, 2*n-1, -1):
        heapq.heappush(right, nums[i])
        sum_right += nums[i]

    max_right = [sum_right]
    for i in range(2*n-1, n-1, -1):
        heapq.heappush(right, nums[i])
        sum_right += nums[i]
        sum_right -= heapq.heappop(right)
        max_right += sum_right,
    
    max_right.reverse()

    result = sum_left - max_right[0]
    for i in range(n, 2*n):
        heapq.heappush(left, -nums[i])
        sum_left += nums[i]
        sum_left += heapq.heappop(left)
        result = min(sum_left - max_right[i-n+1], result)

    return result 
