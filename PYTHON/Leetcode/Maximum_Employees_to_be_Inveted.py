def maximumInvitations(favourite: list) -> int:
    length = len(favourite)
    visit_time = [0] * length 
    in_path = [False] * length
    cur_time = 1

    def get_max_len(cur):
        nonlocal cur_time 
        in_path[cur], visit_time[cur], nxt = True, cur_time, favourite[cur]
        cur_time += 1
        ret = 0 if not in_path[nxt] else visit_time[cur] - visit_time[nxt] + 1
        if visit_time[nxt] == 0: 
            ret = max(ret, get_max_len(nxt))
        in_path[cur] = False 
        return ret 

    ret_cycle = 0
    for i in range(length):
        if visit_time[i] == 0:
            ret_cycle = max(ret_cycle, get_max_len(i))

    ret_not_cycle = 0
    back_edge_graph = [[] for _ in range(length)]
    for i in range(length):
        back_edge_graph[favourite[i]].append(i)

    def get_max_depth(cur):
        ret = 0
        for nxt in back_edge_graph[cur]:
            if favourite[cur] != nxt:
                ret = max(ret, get_max_depth(nxt) + 1)
        return ret 

    for i in range(length):
        if favourite[favourite[i]] == i:
            ret_not_cycle += get_max_depth(i) + 1

    ret = max(ret_cycle, ret_not_cycle)

    return ret


print(maximumInvitations([2,2,1,2]))
print(maximumInvitations([1,2,0]))
print(maximumInvitations([3,0,1,4,1]))

