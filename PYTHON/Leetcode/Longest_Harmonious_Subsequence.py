def findLHS(nums: list) -> int:
    answer = 0
    cnt = collections.Counter(nums)
    for n in nums:
        if n + 1 in cnt:
            answer =  max(answer, cnt[n] + cnt[n+1])
    return answer 
