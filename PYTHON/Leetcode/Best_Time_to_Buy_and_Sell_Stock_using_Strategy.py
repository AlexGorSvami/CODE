def maxProfit(prices: list, strategy: list, k: int) -> int:
    result, n, half = [p*s for p, s in zip(prices, strategy)], len(prices), k // 2

    sum_a, sum_p = sum(result[:k]), sum(prices[half:k])
    best_delta = sum_p - sum_a 
    for i in range(1, n-k+1):
        sum_a += result[i+k-1] - result[i-1]
        sum_p += prices[i+k-1] - prices[i+half-1]
        curr_delta = sum_p - sum_a 

        if curr_delta > best_delta:
            best_delta = curr_delta 

    if best_delta < 0:
        best_delta = 0 

    return sum(result) + best_delta 
