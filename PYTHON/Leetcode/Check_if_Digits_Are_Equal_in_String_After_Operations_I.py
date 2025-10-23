def hasSameDigits(s: str) -> bool:
    while len(s) > 2:
        new_str = ''
        for i in range(len(s)-1):
            new_str += str((int(s[i]) + int(s[i+1])) % 10)
        s = new_str 
    return s[0] == s[1]
