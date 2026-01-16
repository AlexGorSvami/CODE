def maximizeSquareArea(m: int, n: int, hFences: list, vFences: list) -> int:
    side = 0 
    mod = 10 ** 9 + 7 
    dif = set()
    hFences.append(1)
    hFences.append(m)
    for i in range(len(hFences)):
        for j in range(len(hFences)):
            if i != j:
                dif.add(abs(hFences[i] - hFences[j]))

    vFences.append(1)
    vFences.append(n)
    for i in range(len(vFences)):
        for j in range(len(vFences)):
            if i != j and abs(vFences[i] - vFences[j]) in dif:
                side = max(side, abs(vFences[i] - vFences[j]))

    if side == 0:
        return -1  
    return (side ** 2) % mod 
