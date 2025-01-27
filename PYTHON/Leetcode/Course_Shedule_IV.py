def checkifPerequisite(numCourses: int, perequisites: list, queries: list) -> list:
    req = [set() for _ in range(numCourses)]
    for prerequis in perequisites:
        req[prerequis[1]].add(prerequis[0])

    def find_prerequis(node):
        if visit[node]:
            return req[node]
        req_list = list(req[node])
        for cur in req_list:
            req[node].update(find_prerequis(cur))
        visit[node] = True
        return req[node]

    visit = [False] * numCourses 
    for node in range(numCourses):
        if not visit[node]:
            req[node].update(find_prerequis(node))

    result = []
    for querie in queries:
        if querie[0] in req[querie[1]]:
            result.append(True)
        else:
            result.append(False)
    return result 




print(checkifPerequisite(2, [[1,0]], [[0,1], [1,0]]))
print(checkifPerequisite(2, [], [[1,0], [0,1]]))
print(checkifPerequisite(3, [[1,2],[1,0], [2,0]], [[1,0],[1,2]]))
