def maxDiff(num: int) -> int:
    num_str = str(num)
    unq_digits = set(num_str)
    max_val = num 
    min_val = num 

    for digit in unq_digits:
        for n_dig in '0123456789':
            if num_str[0] == digit and n_dig == '0':
                continue
            new_n_str = num_str.replace(digit, n_dig)
            new_num = int(new_n_str)
            max_val = max(max_val, new_num)
            min_val = min(min_val, new_num)

    return max_val - min_val 
