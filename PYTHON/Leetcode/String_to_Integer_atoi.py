def myAtoi(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    sign = 1
    i = 0
    answer = 0
    if s[0] == '-':
        sign = -1
        i += 1
    elif s[0] == '+':
        i += 1
    while i < len(s) and s[i].isdigit():
        answer = answer * 10 + int(s[i])
        i += 1
    answer *= sign
    small = -2**31
    large = 2**31 - 1
    
    if answer < small:
        return small
    
    if answer > large:
        return large

    return answer 
