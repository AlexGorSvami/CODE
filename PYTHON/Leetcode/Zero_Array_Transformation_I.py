def isZeroArray(nums: list, queries: list) -> bool:
    n = len(nums)
    count = [0] * (n+1)
    for i, j in queries:
        count[i] += 1
        count[j+1] -= 1

    current_count = 0 
    for k in range(n):
        current_count += count[k]
        if current_count < nums[k]:
            return False
    return True

print(isZeroArray([1,0,1], [[0,2]]))
