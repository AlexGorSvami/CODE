def maxSubarraySum(nums: list, k: int) -> int:
    n = len(nums)
    prefix_sum = list()
    for ind in range(n):
        if not ind:
            prefix_sum.append(nums[ind])
        else:
            prefix_sum.append(nums[ind] + prefix_sum[-1])
    min_prefix_sum = [float('inf')] * k 
    min_prefix_sum[-1] = 0 
    max_sum = float('-inf')
    for ind in range(n):
        max_sum = max(max_sum, prefix_sum[ind] - min_prefix_sum[ind % k])
        min_prefix_sum[ind % k] = min(min_prefix_sum[ind % k], prefix_sum[ind])
    return max_sum 
