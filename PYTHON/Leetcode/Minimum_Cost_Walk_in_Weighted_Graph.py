def minimumCost(n: int, edges: list, query: list):
    parent = list(range(n))
    rank = [1]*n
    weight = [-1]*n

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int, z: int) -> None:
        xrep = find(x)
        yrep = find(y)

        if xrep == yrep:
            weight[xrep] &= z
            
            return 
        if rank[xrep] > rank[yrep]:
            parent[yrep] = xrep 
            rank[xrep] += rank[yrep]
            weight[xrep] &= weight[yrep] & z 
        else:
            parent[xrep] = yrep 
            rank[yrep] += rank[xrep]
            weight[yrep] &= weight[xrep] & z

    answer =[]

    for x,y,z in edges:
        union(x, y, z)

    for x, y in query:
        px, py = find(x), find(y)
        answer.append(weight[px] if px == py else -1)

    return answer

print(minimumCost(5, [[0,1,7], [1,3,7], [1,2,1]], [[0,3], [3,4]]))
