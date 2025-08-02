def minCost(basket1: list, basket2: list) -> int:
    n1, n2 = Counter(basket1), Counter(basket2)
    n = n1 + n2 

    for i in n:
        n[i], r = divmod(n[i], 2)
        if r:
            return -1 

    min_n = min(n)
    n1 -= n 
    n2 -= n 
    arr = sorted(list(n1.elements()) + list(n2.elements()))
    return sum(min(2*min_n, arr[i]) for i in range(len(arr)//2))
