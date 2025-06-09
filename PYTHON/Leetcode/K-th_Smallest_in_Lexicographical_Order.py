def findKthNumber(n: int, k: int) -> int:
    res = 1 
    k -= 1
    while k > 0:
        cnt = 0
        interval = [res, res+1]
        while interval[0] <= n:
            cnt += (min(n+1, interval[1]) - interval[0])
            interval = [10*interval[0], 10*interval[1]]

        if k >= cnt:
            res += 1 
            k -= cnt 
        else:
            res *= 10
            k -= 1 

    return res 
