class Solution:

    def mostProfitablePath(self, edges, bob, amount):
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        x = []

        def dfs(node, path, parent):
            path.append(node)
            if node == 0:
                x.extend(path)
                return
            for neigh in graph[node]:
                if neigh == parent:
                    continue
                dfs(neigh, path, node)
                path.pop()

        dfs(bob,[],-1)

        for i in range(len(x)//2):
            amount[x[i]] = 0
        if len(x) % 2:
            amount[x[len(x)//2]] //=2 

        def mostprofit(node, parent):
            if len(graph[node]) == 1 and graph[node][0] == parent:
                return amount[node]
            mx = -inf
            for neigh in graph[node]:
                if neigh == parent:
                    continue 
                mx = max(mx, mostprofit(neigh, node))
            return mx + amount[node]

        return mostprofit(0, parent = -1)

