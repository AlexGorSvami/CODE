def trapRainWater(heightMap: list) -> int:
    import heapq
    min_heap = []
    rows, cols = len(heightMap), len(heightMap[0])
    visit = [[False]*cols for _ in range(rows)]

    for first_ind in range(rows):
        for second_ind in range(cols):
            if first_ind in (0, rows-1) or second_ind in (0, cols - 1):
                heapq.heappush(min_heap, (heightMap[first_ind][second_ind], first_ind, second_ind))
                visit[first_ind][second_ind] = True

    result = 0
    min_boundary_height = 0
    while min_heap:
        height, first_ind, second_ind = heapq.heappop(min_heap)
        min_boundary_height = max(min_boundary_height, height)
        for x,y in ((1,0), (-1,0), (0,1), (0,-1)):
            right, center = first_ind + x, second_ind + y
            if 0 <= right < rows and 0 <= center < cols and not visit[right][center]:
                visit[right][center] = True 
                heapq.heappush(min_heap, (heightMap[right][center], right, center))
                if heightMap[right][center] < min_boundary_height:
                    result += min_boundary_height - heightMap[right][center]

    return result 

print(trapRainWater([[1,4,3,1,3,2], [3,2,1,3,2,4], [2,3,3,2,3,1]]))
print(trapRainWater([[3,3,3,3,3], [3,2,2,2,3], [3,2,1,2,3], [3,2,2,2,3], [3,3,3,3,3]]))
