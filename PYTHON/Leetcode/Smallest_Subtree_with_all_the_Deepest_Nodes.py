from typing import Optional


def subtreeWithAllDeepest(root: Optional[TreeNode]) -> Optional[TreeNode]:
    depth = {None: -1}
    def dfs(node, parent):
        if node:
            depth[node] = depth[parent] + 1 
            dfs(node.left, node)
            dfs(node.right, node)

    dfs(root, None)
    max_depth = max(depth.values())

    def final(node):
        if not node or depth.get(node, None) == max_depth:
            return node 
        left, right = final(node.left), final(node.right)
        return node if left and right else left or right 

    return final(root)
