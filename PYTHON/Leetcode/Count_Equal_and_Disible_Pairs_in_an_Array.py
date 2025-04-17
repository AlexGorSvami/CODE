def countPairs(nums: list, k: int) -> int:
    n_pairs = 0
    pairs = {}
    for i, num in enumerate(nums):
        if num in pairs:
            pairs[num].append(i)
        else:
            pairs[num] = [i]

    for ind in pairs.values():
        for i in range(len(ind)):
            for j in range(i+1, len(ind)):
                if (ind[i] * ind[j]) % k == 0:
                    n_pairs += 1 
    return n_pairs 


print(countPairs([3,1,2,2,2,1,3], 2))
print(countPairs([1,2,3,4], 1))
