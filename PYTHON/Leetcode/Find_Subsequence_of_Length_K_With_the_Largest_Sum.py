def maxSubsequence(nums: list, k: int) -> list:
    nums_and_i = [(nums[i],i) for i in range(len(nums))]
    nums_and_i.sort(reverse=True)
    answer = nums_and_i[:k]
    answer.sort(key = lambda x: x[1])
    return [answer[i][0] for i in range(k)]
