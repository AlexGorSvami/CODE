def maxSumDivThree(nums: list) -> int:
    seen = [0, 0, 0]
    for i in nums:
        for j in seen[:]:
            seen[(j + i) % 3] = max(seen[(j + i) % 3], j + i)

    return seen[0]
