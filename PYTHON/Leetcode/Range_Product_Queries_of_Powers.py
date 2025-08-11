def productQueries(n: int, queries: list) -> list:
    mod, powers, i = 10**9+7, [], 0 

    while n > 0:
        if n & 1:
            powers.append(1 << i)
        n >>= 1 
        i += 1
    answer = []
    for left, right in queries:
        product = 1 
        for i in range(left, right+1):
            product = (product * powers[i]) % mod 
        answer.append(product)
    return answer 
