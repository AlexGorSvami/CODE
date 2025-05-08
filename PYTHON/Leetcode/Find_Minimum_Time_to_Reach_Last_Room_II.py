def minTimeToReach(moveTime: list) -> int:
  import heapq
  minheap = []
  ROW = len(moveTime)
  COL = len(moveTime[0])
  heapq.heappush(minheap, (0, 0, 0, 0)) # delta + 1 
  seen = set([(0, 0)])
  while minheap:
        time, row, col, t_delta = heapq.heappop(minheap)
        if row == ROW-1 and col == COL-1:
            return time
        for r_d, c_d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_r, next_c = row + r_d, col + c_d
            if 0 <= next_r < ROW and 0 <= next_c < COL and (next_r, next_c) not in seen:
                next_t = max(time, moveTime[next_r][next_c]) + t_delta + 1
                next_t_delta = t_delta ^ 1
                heapq.heappush(minheap, (next_t, next_r, next_c, next_t_delta))
                seen.add((next_r, next_c))
