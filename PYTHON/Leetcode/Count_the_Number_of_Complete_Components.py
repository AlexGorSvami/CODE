def countCompleteComponents(n: int, edges: list) -> int:
    from collections import defaultdict 
    answer = 0
    graph = defaultdict(list)

    for edg1, edg2 in edges:
        graph[edg1].append(edg2)
        graph[edg2].append(edg1)

    seen = set()
    for start in range(n):
        cnt = 0

        if start in seen:
            continue 

        query = [start]
        seen.add(start)
        for edge_from in query:
            for edge_to in graph[edge_from]:
                if edge_to  not in seen:
                    cnt += 1 
                    query.append(edge_to)
                    seen.add(edge_to)

        if all(len(graph[edge_from]) == cnt for edge_from in query):
            answer += 1 
    return answer 



print(countCompleteComponents(6, [[0,1], [0,2], [1,2], [3,4]]))
print(countCompleteComponents(6, [[0,1], [0,2], [1,2], [3,4], [3,5]]))

