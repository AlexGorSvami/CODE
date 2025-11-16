def numSub(s: str) -> int:
    MOD = 10**9 + 7 
    result, count = 0, 0 

    for n in s:
        if n == '1':
            count += 1 
        else:
            result += count * (count + 1) // 2 
            count = 0 
    result += count * (count + 1) // 2 

    return result % MOD 
