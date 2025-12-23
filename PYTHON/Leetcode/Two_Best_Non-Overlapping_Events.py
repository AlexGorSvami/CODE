def maxTwoEvents(events: list) -> int:
    import heapq 

    max_sum = 0
    curr_sum = 0
    pq = []
    events.sort()

    for start, end, val in events:
        while pq and pq[0][0] < start:
            curr_sum = max(curr_sum, heapq.heappop(pq)[1])

        max_sum = max(max_sum, curr_sum + val)
        heapq.heappush(pq, (end, val))

    return max_sum 
