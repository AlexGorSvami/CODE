def countSubarrays(nums: list, minK: int, maxK: int) -> int:
    p_min = p_max = bad = -1
    answer = 0

    for i, num in enumerate(nums):
        if num == minK:
            p_min = i 

        if num == maxK:
            p_max = i 

        if num < minK or num > maxK:
            bad = i 

        if p_min != -1 and p_max != -1:
            answer += max(0, min(p_min, p_max) - bad) 

    return answer 


print(countSubarrays([1,3,5,2,7,5], 1, 5))
print(countSubarrays([1,1,1,1], 1, 1))
