def totalMoney(n: int) -> int:
    i, total, deposit = 1, 0, 1
    while n:
        total += deposit 
        if not i % 7 or not i % n:
            deposit -= 5
            n -= i 
            i = 1
        else:
            deposit += 1 
            i += 1 
    return total

