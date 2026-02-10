def longestBalanced(nums: list) -> int:
    n = len(nums)
    answer = 0 
    for i in range(n):
        count = [0, 0]
        visit = set()
        for j in range(i, n):
            if nums[j] not in visit:
                count[nums[j] & 1] += 1 
                visit.add(nums[j])
            if count[0] == count[1]:
                answer = max(answer, j - i + 1)

    return answer 
