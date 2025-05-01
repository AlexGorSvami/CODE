def maxTaskAssign(tasks: list, workers: list, pills: int, strength: int) -> int:
    n = len(tasks)
    tasks.sort()
    workers.sort()
    m = len(workers)

    def check(num):
        deq = deque()
        index = 0
        power = pills 
        for i in range(m - num, m):
            while index < num and workers[i] + strength >= tasks[index]:
                deq.append(tasks[index])
                index += 1 
            if not deq:
                return False 
            if deq[0] <= workers[i]:
                deq.popleft()
            else:
                if not power:
                    return False 
                deq.pop()
                power -= 1 
        return True

     l, r = 0, min(m,n)
     while l <= r:
        mid = (r + l) // 2 
        if l == r:
            return l-1 if not check(l) else l 
        if check(mid):
            l = mid + 1 
        else:
            r = mid 
     return l 
