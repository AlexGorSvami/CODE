def eventualSafeNodes(graph: list) -> list:
    states = dict()
    def safe(value):
        if value in states:
            return states[value]
        states[value] = False
        for i in graph[value]:
            if not safe(i):
                return states[value]
        states[value] = True
        return states[value]
    nodes = []
    for i in range(len(graph)):
        if safe(i):
            nodes.append(i)
    return nodes 




print(eventualSafeNodes([[1,2], [2,3], [5], [0], [5], [], []]))
print(eventualSafeNodes([[1,2,3,4], [1,2], [3,4], [0,4], []]))
