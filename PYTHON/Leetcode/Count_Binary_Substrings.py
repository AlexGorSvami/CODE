def countBinarySubstrings(s:str) -> int:
    arrow = []
    ind, cnt = 1, 1 
    while ind < len(s):
        if s[ind] == s[ind-1]:
            cnt += 1 
        else:
            arrow.append(cnt)
            cnt = 1 
        ind += 1 
    arrow.append(cnt)
    res = 0 

    for i in range(len(arrow)-1):
        res += min(arrow[i], arrow[i+1])
    return res 
