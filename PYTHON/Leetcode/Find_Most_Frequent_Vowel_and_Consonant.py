def maxFreqSum(s: str) -> int:
    vow, cons = 0, 0
    for i in set(s):
        cnt = s.count(i)

        if i in 'aeiou':
            vow = max(vow, cnt)
        else:
            cons = max(cons, cnt)
    return vow + cons 
