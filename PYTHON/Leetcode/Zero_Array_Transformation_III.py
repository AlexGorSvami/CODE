def maxRemoval(nums: list, queries: list) -> int:
    import heapq 

    n, m = len(nums), len(queries)
    start_queries = [[] for _ in range(n)]
    for i, (j, k) in enumerate(queries):
        start_queries[j].append((k, i))

    availible = []
    active = []
    used = 0

    for pos in range(n):
        for end, query_ind in start_queries[pos]:
            heapq.heappush(availible, (-end, query_ind))

        while active and active[0][0] < pos:
            heapq.heappop(active)

        current = len(active)
        need_more = nums[pos] - current 

        if need_more > 0:
            for _ in range(need_more):
                found = False 
                temp_remove = []

                while availible:
                    neg_end, query_ind = heappop(availible)
                    end = -neg_end 

                    if end >= pos:
                        heapq.heappush(active, (end, query_ind))
                        used += 1 
                        found = True 
                        break
                    else:
                        temp_remove.append((neg_end, query_ind))

                for item in temp_remove:
                    heapq.heappush(availible, item)

                if not found:
                    return -1 

    return m - used 
