def findRedundantConnection(edges: list) -> list:
    # Parent of each node 
    parent = {node: node for node in range(1, len(edges) + 1)}
    # Tree depth
    rank = {node: 1 for node in range(1, len(edges) + 1)}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node]) # Сжатие пути
        return parent[node]


    def union(node1, node2):
        #Union of a set of two nodes
        root1 = find(node1)
        root2 = find(node2)

        if root1 == root2:
            return True

        if rank[root1] > rank[root2]:
            parent[root2] = root1 

        elif rank[root1] < rank[root2]:
            parent[root1] = root2 

        else:
            parent[root2] = root1 
            rank[root1] += 1 
        
        return False

    for node1, node2 in edges:
        if union(node1, node2):
            return [node1, node2]





print(findRedundantConnection([[1,2], [1,3], [2,3]]))
print(findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
