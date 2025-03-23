def countPaths(n: int, roads: list) -> int:
    from collections import defaultdict 
    from heapq import heappop, heappush 

    g = defaultdict(list)
    for i, j, t in roads:
        g[i].append((j, t))
        g[j].append((i, t))

    time = [0 if i == 0 else float('inf') for i in range(n)]
    ways = [1 if i == 0 else 0 for i in range(n)]
    stack = [(0,0)]

    while stack:
        t1, i = heappop(stack)
        if t1 > time[i]:
            continue 

        for j, t2 in g[i]:
            if time[j] > t1 + t2:
                time[j] = t1 + t2 
                ways[j] = ways[i]
                heappush(stack, (time[j], j))

            elif time[j] == t1 + t2:
                ways[j] += ways[i]
                ways[j] %= 1_000_000_007 

    return ways[n-1]
