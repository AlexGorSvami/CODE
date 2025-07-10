def maxFreeTime(eventTime: int, startTime: list, endTime: list) -> int:
        n = len(startTime)
        free_time = []
        for i in range(n-1):
            if i == 0:
                free_time.append(startTime[i] - 0)
            free_time.append(startTime[i+1] - endTime[i])
        free_time.append(eventTime - endTime[-1])

        largetst_left, largetst_right = [0]*n, [0] * n
        for i in range(1, n):
            largetst_left[i] = max(largetst_left[i-1], free_time[i-1])
        for i in range(n-2, -1, -1):
            largetst_right[i] = max(largetst_right[i+1], free_time[i+2])

        result = 0
        for i in range(n):
            result = max(result, free_time[i] + free_time[i+1])
            interval = endTime[i] - startTime[i]
            if interval <= largetst_left[i] or interval <= largetst_right[i]:
                result = max(result, free_time[i] + free_time[i+1] + interval)
        return result
