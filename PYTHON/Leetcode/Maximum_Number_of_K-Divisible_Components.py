def maxKDivisibkeComponents(self, n: int, edges: list, values: list, k: int) -> int:
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    visited = [False] * n 
    self.components = 0 

    def dfs(node: int) -> int:
        visited[node] = True 
        subtree_sum = values[node] 

        for neighbor in tree[node]:
            if not visited[neighbor]:
                child_sum = dfs(neighbor)
                if child_sum % k == 0:
                    self.components += 1 
                else:
                    subtree_sum += child_sum 
    
        return subtree_sum 

    total_sum = dfs(0)

    if total_sum % k == 0:
        self.components += 1 

    return self.components 

