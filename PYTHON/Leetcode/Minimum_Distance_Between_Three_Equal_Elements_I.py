def minimumDistance(nums: list) -> int:
    look = defaultdict(list)
    for i, n in enumerate(nums):
        look[n].append(i)

    result = float('inf')
    for n in look:
        if len(look[n]) >= 3:
            for pos in range(len(look[n])-2):
                i = look[n][pos]
                k = look[n][pos+1]
                j = look[n][pos+2]
                dist = abs(i-j) + abs(j-k) + abs(k-i)
                result = min(result, dist)
    if result == float('inf'):
        result = -1 
    return result 
