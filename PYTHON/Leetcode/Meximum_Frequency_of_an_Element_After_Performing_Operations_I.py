def maxFrequency(nums: list, k: int, numOperations: int) -> int:
    maxx = max(nums)
    cnt = [0] * (maxx+1)
    for n in nums:
        cnt[n] += 1 

    left, right, result = 0, sum(cnt[:k]), 0
    for n in range(maxx+1):
        right -= cnt[n]
        if n + k <= maxx:
            right += cnt[n + k]
        if n > 0:
            left += cnt[n - 1]
        if n > k+1:
            left -= cnt[n - k - 1]
        result = max(result, cnt[n] + min(left + right, numOperations))

    return result 
