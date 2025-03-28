def maxPoints(grid: list, queries: list) -> list:
    from heapq import heappop, heappush
    DIRECTIONS = [(1,0), (-1, 0), (0,1), (0,-1)]

    result: list[int] = [0] * len(queries)
    rows, cols = len(grid), len(grid[0])
    min_heap = [(grid[0][0], 0, 0)]
    visited: set[tuple[int, int]] = {(0, 0)}
    count = 0

    queue = [(n,i) for i, n in enumerate(queries)]
    queue.sort()

    for limit, i in queue:
        while min_heap and min_heap[0][0] < limit:
            val, row, col = heappop(min_heap)
            count += 1

            for x, y in DIRECTIONS:
                nr, nc = row + x, col + y
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    heappush(min_heap, (grid[nr][nc], nr, nc))
                    visited.add((nr, nc))

        result[i] = count 

    return result 
