def nextBeautifulNumber(n: int) -> int:
    from collections import Counter
    beautiful = True
    while beautiful:
        n += 1 
        cnt = Counter(str(n))
        flag = False 
        for num, count in cnt.items():
            if int(num) != count:
                flag = True 
                break 
            if not flag:
                beautiful = False 
    return n 
