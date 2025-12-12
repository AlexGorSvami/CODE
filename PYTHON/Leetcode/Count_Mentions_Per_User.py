def countMentions(numberOfUsers: int, events: list) -> list:
    events.sort(key=lambda x: (int(x[1]), x[0] == 'MESSAGE'))
    cnt = [0] * numberOfUsers 
    next_time = [0] * numberOfUsers 
    for event in events:
        curr_time = int(event[1])
        if event[0] == 'MESSAGE':
            if event[2] == 'ALL':
                for i in range(numberOfUsers):
                    cnt[i] += 1 
            elif event[2] == 'HERE':
                for i, t in enumerate(next_time):
                    if t <= curr_time:
                        cnt[i] += 1 
            else:
                for ind in event[2].split():
                    cnt[int(ind[2:])] += 1 
        else:
            next_time[int(event[2])] = curr_time + 60 
    return cnt 
