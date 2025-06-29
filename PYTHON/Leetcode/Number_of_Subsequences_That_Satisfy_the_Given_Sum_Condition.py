def numSubseq(nums: list, target: int) -> int:
    m = 10**9+7
    n = len(nums)
    nums.sort()

    answer = 0
    start = 0
    end = n-1

    while start <= end:
        if nums[start] + nums[end] <= target:
            answer = (answer + pow(2, (end-start))) % m 
            start += 1 
        else:
            end -= 1

    return answer 

