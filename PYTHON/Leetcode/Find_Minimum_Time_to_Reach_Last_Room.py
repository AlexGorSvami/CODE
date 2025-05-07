def minTimeToReach(moveTime: list) -> int:
    import heapq 
    
    n, m = len(moveTime), len(moveTime[0])
    has: set[tuple[int, int]] = set()
    que = [(0,0,0)]
    heapq.heapify(que)
    while que:
        t, x, y = heapq.heappop(que)
        if (x, y) in has:
            continue
        has.add((x, y))
        if x == n-1 and y == m-1:
            return t
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                heapq.heappush(que, (max(t + 1,  moveTime[nx][ny] + 1), nx, ny)) 


print(minTimeToReach([[0,4], [4,4]]))
print(minTimeToReach([[0,0,0],[0,0,0]]))
