def maxTargetNodes(edges1: list, edges2: list, k: int) -> list:
    n,m = len(edges1)+1, len(edges2)+1 
    a1 = {node:[] for node in range(n)}
    a2 = {node:[] for node in range(m)}

    for n1, n2 in edges1:
        a1[n1].append(n2)
        a1[n2].append(n1)
    for n1, n2 in edges2:
        a2[n1].append(n2)
        a2[n2].append(n1)

    def bfs(st, k, a):
        count = 0
        q = deque([[st,-1]])
        dist = 0
        while q and dist <= k:
            for i in range(len(q)):
                node, par = q.popleft()
                count += 1 
                for nei in a[node]:
                    if nei != par:
                        q.append([nei, node])
            dist += 1 
        return count 

    answer = [0 for i in range(n)]
    for i in range(n):
        answer[i] = bfs(i, k, a1)

    maxim = 0
    for i in range(m):
        maxim = max(maxim, bfs(i,k-1,a2))

    for i in range(n):
        answer[i] += maxim 
    return answer 
