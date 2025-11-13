def maxOperations(s: str) -> int:
    ones, result = 0, 0 
    for i, n in enumerate(s):
        if n == '1':
            ones += 1 
        elif i > 0 and s[i - 1] == '1':
            result += ones 

    return result 
