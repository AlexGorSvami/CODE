def minRemoval(nums: list, k: int) -> int:
    n = len(nums)
    nums.sort()
    j = 0 
    answer = 0 

    for i in range(n):
        while nums[i] > k * nums[j]:
            j += 1 
        answer = max(answer, i-j+1)

    return n - answer 
