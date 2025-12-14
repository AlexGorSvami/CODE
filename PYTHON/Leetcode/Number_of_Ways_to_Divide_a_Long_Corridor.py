def numberOfWays(corridor: str) -> int:
    MOD = 10**9 + 7 
    result = 1 
    prev_seat, num_seat = 0, 0 

    for i, c in enumerate(corridor):
        if c == 'S':
            num_seat += 1 
            if num_seat > 2 and num_seat % 2 == 1:
                result *= i - prev_seat 
            prev_seat = i 

    return result % MOD if num_seat > 1 and num_seat % 2 == 0 else 0
