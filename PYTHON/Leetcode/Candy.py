def candy(ratings: list) -> int:
    n = len(ratings)
    result = [1]*len(ratings)
    for i in range(n-1):
        if ratings[i+1] > ratings[i]:
            result[i+1] = result[i] + 1 
    for i in reversed(range(n-1)):
        if ratings[i] > ratings[i+1]:
            result[i] = max(result[i], result[i+1]+1)
    return sum(result)
