def minMaxDifference(num: int) -> int:
    s = str(num)
    for i in range(len(s)):
        if s[i] != '9':
            smax = s.replace(s[i], '9')
            break
    else:
        smax = s 
    smin - s.replace(s[0], '0')
    return int(smax) - int(smin)
