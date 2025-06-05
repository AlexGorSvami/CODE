def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    from collections import defaultdict 
    adj = defaultdict(list)

    #Build the graph
    for i, j in zip(s1, s2):
        adj[i].append(j)
        adj[j].append(i)

    def dfs(ch, visited):
        visited.add(ch)
        min_ch = ch 
        for n in adj[ch]:
            if n not in visited:
                candidate = dfs(n, visited)
                min_ch = min(min_ch, candidate)
        return min_ch 

    result = []
    for ch in baseStr:
        visited = set()
        result.append(dfs(ch, visited))

    return ''.join(result)
