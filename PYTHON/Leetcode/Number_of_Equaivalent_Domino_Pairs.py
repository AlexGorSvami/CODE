def numEquivDominoPairs(dominoes: list) -> int:
    hash = {}

    for a,b in dominoes:
        if a > b:
            a,b = b,a
        if (a,b) in hash:
            hash[(a,b)] += 1 
        else:
            hash[(a,b)] = 1 
    pairs = 0
    for _, cnt in hash.items():
        if cnt > 1:
            pairs += cnt * (cnt - 1) / 2 
    return int(pairs) 


print(numEquivDominoPairs([[1,2], [2,1], [3,4], [5,6]]))
