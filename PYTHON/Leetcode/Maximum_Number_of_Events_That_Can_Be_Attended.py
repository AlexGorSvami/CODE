import collections, heapq
def maxEvents(events: list) -> int:
    if len(events) == 0:
        return 0


    start_to_end = collections.defaultdict(list)
    for start, end in events:
        start_to_end[start].append(end)

    result = 0
    query = []
    for i in range(min(events, key=lambda x: x[0])[0], max(events, key=lambda x: x[1])[1]+1):
        for num in start_to_end[i]:
            heapq.heappush(query, num)

        while len(query) != 0 and query[0] < i:
            heapq.heappop(query)

        if len(query) != 0 and query[0] >= i:
            heapq.heappop(query)
            result += 1 

    return result 
