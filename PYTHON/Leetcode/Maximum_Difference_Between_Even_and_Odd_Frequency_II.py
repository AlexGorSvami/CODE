def maxDifference(s: str, k: int) -> int:
    from collections import defaultdict
    import math

    answer = -math.inf
    for i in '01234':
        for j in '01234':
            if i != j:
                seen = defaultdict(lambda: math.inf)
                pi = [0]
                pj = [0]
                ii = 0 
                for l, ch in enumerate(s):
                    pi.append(pi[-1])
                    pj.append(pj[-1])
                    if ch == i:
                        pi[-1] += 1  
                    elif ch == j:
                        pj[-1] += 1 

                    while ii <= l - k + 1 and pi[ii] < pi[-1] and pj[ii] < pj[-1]:
                        key = (pi[ii] % 2, pj[ii] % 2)
                        diff = pi[ii] - pj[ii]
                        seen[key] = min(seen[key], diff)
                        ii += 1
                    key = (1 - pi[-1] % 2, pj[-1] % 2)
                    diff = pi[-1] - pj[-1]
                    answer = max(answer, diff - seen[key])
    return answer 
