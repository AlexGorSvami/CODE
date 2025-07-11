def mostBooked(n: int, meetings: list) -> int:
    pq = []
    avalible_rooms = [i for i in range(n)]
    count = [0 for i in range(n)]
    for start, end in sorted(meetings):
        while pq and pq[0][0] <= start:
            _, room = heapq.heappop(pq)
            heapq.heappush(avalible_rooms, room)

        if avalible_rooms:
            room = heapq.heappop(avalible_rooms)
            heapq.heappush(pq, [end, room])
        else:
            next_end, room = heapq.heappop(pq)
            heapq.heappush(pq, [next_end + (end - start), room])
        count[room] += 1 
    return count.index(max(count))
