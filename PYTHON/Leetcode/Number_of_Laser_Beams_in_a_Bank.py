def numberOfBeams(bank: list) -> int:
    if len(bank) == 0 or len(bank) == 1:
        return 0 
    cur_number = 0
    total = 0 
    for i in bank:
        tmp = [int(j) for j in i]
        if sum(tmp) != 0:
            nums = tmp 
            total += cur_number * sum(nums)
            cur_number = sum(nums)
    
    return total 
