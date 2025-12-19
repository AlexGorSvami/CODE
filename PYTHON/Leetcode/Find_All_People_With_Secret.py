def findAllPeople(n: int, meetings: list, firstPerson: int) -> list:
    graph = collections.defaultdict(list)
    for x, y, t in meetings:
        graph[x].append((y, t))
        graph[y].append((x, t))

    min_heap = []
    heapq.heappush(min_heap, (0,0))
    heapq.heappush(min_heap, (0, firstPerson))
    knows = set()

    while min_heap:
        time, person = heapq.heappop(min_heap)
        if person in knows:
            continue 
        knows.add(person)
        for p, t in graph[person]:
            if p not in knows and t >= time:
                heapq.heappush(min_heap, (t, p))
    return list(knows)
