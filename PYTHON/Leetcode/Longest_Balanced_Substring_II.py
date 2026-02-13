def longestBalanced(s: str) -> int:
    n = len(s)
    p = [[0, 0, 0]]
    for i in s:
        p.append(p[-1][:])
        p[-1]['abc'.index(i)] += 1 

    answer = 0 
    m = {}
    for j, (a, b, c) in enumerate(p):
        for k in [
                (-1, a-b, a-c),
                (-2, a-b, c),
                (-3, b-c, a),
                (-4, c-a, b),
                (-5, b, c),
                (-6, c, a),
                (-7, a, b),
            ]:
                if not k in m: m[k] = j
                else: answer = max(answer, j - m[k])

    return answer 
