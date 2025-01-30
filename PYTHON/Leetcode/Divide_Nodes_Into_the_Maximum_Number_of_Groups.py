def magnificentSets(n: int, edges: list) -> int:
    from collections import deque, defaultdict

    def make_graph(edges):
        graph = defaultdict(list)
        for node_a, node_b in edges:
            node_a -= 1
            node_b -= 1
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)
        return graph 

    def get_connected_components(graph):
        visited = [False] * n 
        components = []
        def dfs(node, parent, collector):
            if visited[node]:
                return collector 
            collector.add(node)
            visited[node] = True
            for neighbor in graph[node]:
                dfs(neighbor, node, collector)
            return collector

        for node in range(n):
            if not visited[node]:
                components.append(dfs(node, -1, set()))
        return components

    def bfs(start):
        result = 0
        visited = set()
        queue = {start}
        while queue:
            result += 1
            next_queue = set()
            for cur_code in queue:
                visited.add(cur_code)
                for next_node in graph[cur_code]:
                    if next_node in queue:
                        return -1 
                    if next_node in visited:
                        continue 
                    next_queue.add(next_node)
            queue = next_queue 
        return result 

    graph = make_graph(edges)
    components = get_connected_components(graph)
    result = 0
    for component in components:
        best_component = -1
        for start in component:
            best_component = max(best_component, bfs(start))
            if best_component == -1:
                return -1
        result += best_component 
    return result




print(magnificentSets(6, [[1,2], [1,4], [1,5], [2,6], [2,3], [4,6]]))
print(magnificentSets(3, [[1,2], [2,3], [3,1]]))
