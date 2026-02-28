def concatenatedBinary(n: int) -> int:
    answer = 0
    MOD = 10**9+7
    for i in range (1, n+1):
        l = i.bit_length()
        answer = ((answer << l) + i) % MOD
    
    return answer 
