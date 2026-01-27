def minCost(n: int, edges: list) -> int:
    dic = defaultdict(list)
    for a, b, w in edges:
        dic[a].append((b,w))
        dic[b].append((a,w*2))

    distance = [0] + [inf] * (n-1)
    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        w, node = heapq.heappop(heap)
        for ni, nw in dic[node]:
            if w + nw < distance[ni]:
                distance[ni] = w + nw 
                heapq.heappush(heap, (w + nw, ni))

    return distance[n-1] if distance[n-1] != inf else -1
