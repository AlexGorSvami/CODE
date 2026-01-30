def minimumCost(source: str, target: str, original: list, changed: list, cost: list) -> int:
    look = {i: {} for i in set(original)}

    def dfs(n):
        heap = [(0, n)]
        visited = set()
        while heap:
            curr_cost, a = heappop(heap)
            if a in visited:
                continue 
            visited.add(a)
            look[n][a] = curr_cost 
            for b in graph[a]:
                heappush(heap, (curr_cost + graph[a][b], b))

    graph = defaultdict(dict)
    for x, y, z in zip(original, changed, cost):
        if y not in graph[x]:
            graph[x][y] = z 
        else:
            graph[x][y] = min(graph[x][y], z)

    for n in set(original):
        dfs(n)

    n = len(source)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n+1):
        if source[i-1] == target[i-1]:
            dp[i] = dp[i-1]

        for l in set(len(s) for s in original):
            if i >= l and (s := source[i-l:i]) in look and (t := target[i-l:i]) in look[s]:
                dp[i] = min(dp[i], dp[i-l] + look[s][t])

    return dp[-1] if dp[-1] < float('inf') else -1

