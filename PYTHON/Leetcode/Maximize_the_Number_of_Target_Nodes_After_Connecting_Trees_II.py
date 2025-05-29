def maxTargetNodes(edges1: list, edges2: list) -> list:
    def get_depths_and_parity_counts(n, edges):
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            depth = [-1] * n
            depth[0] = 0
            even, odd = 1, 0

            queue = deque([0])
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if depth[v] == -1:
                        depth[v] = depth[u] + 1
                        if depth[v] % 2 == 0:
                            even += 1
                        else:
                            odd += 1
                        queue.append(v)
            return depth, even, odd

        n = len(edges1) + 1
        m = len(edges2) + 1

        depth1, even1, odd1 = get_depths_and_parity_counts(n, edges1)
        _, even2, odd2 = get_depths_and_parity_counts(m, edges2)

        answer = []
        for i in range(n):
            if depth1[i] % 2 == 0:
                max_target = max(even1 + even2, even1 + odd2)
            else:
                max_target = max(odd1 + even2, odd1 + odd2)
            answer.append(max_target)

        return answer
