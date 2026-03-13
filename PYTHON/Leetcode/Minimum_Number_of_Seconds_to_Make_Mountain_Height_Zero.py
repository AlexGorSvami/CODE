def minNumberOfSeconds(mountainHeight: int, workerTimes: list) -> int:
    hours = mountainHeight 
    work_times = workerTimes 
    result = 0 
    pq = sorted(map(lambda x: (x, x, 1), work_times))
    while hours:
        result, step, m = heappop(pq)
        hours -= 1 
        heappush(pq, (result + (m + 1) * step, step, m + 1))
    return result
