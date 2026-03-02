def minSwaps(grid: list) -> int:
    n = len(grid)
    zero = [0] * n 
    cnt = collections.defaultdict(int)
    for i in range(n):
        count = 0 
        for j in range(n-1, -1, -1):
            if grid[i][j] == 1: break 
            count += 1 
        count = min(count,n - 1) 
        zero[i] = count 
        cnt[count] += 1 
    count = n - 1 
    for i in range(n):
        while not cnt[count]: count -= 1 
        cnt[count] -= 1 
        if n-1-i > count: return -1 

    result = 0 
    for i in range(n):
        if zero[i] >= n-1-i: continue 
        j = i + 1 
        while zero[j] < n-1-i:
            j += 1 
        result += j - i 
        while j > i:
            zero[j], zero[j-1] = zero[j-1], zero[j]
            j -= 1
    
    return result  
