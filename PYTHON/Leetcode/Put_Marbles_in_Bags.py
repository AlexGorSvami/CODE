def putMarbles(weights: list, k: int) -> int:
    n = len(weights)
    possible_cuts = []
    for i in range(n-1):
        sum_pair = weights[i] + weights[i+1]
        possible_cuts.append(sum_pair)

    possible_cuts.sort()

    minimum, maximum = 0, 0

    for i in range(k - 1):
        minimum += possible_cuts[i]
        maximum += possible_cuts[n - 2 - i]
    
    return maximum - minimum 


print(putMarbles([1,3,5,1], 2))
print(putMarbles([1,3], 2))
