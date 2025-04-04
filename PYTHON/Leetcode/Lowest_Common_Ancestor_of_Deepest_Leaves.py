def lcaDeepestLeaves(root: TreeNode) -> TreeNode:
    self.lca = None
    self.deepest = 0

    def helper(node, depth):
        self.deepest = max(self.deepest, depth)
        if not node:
            return depth 

        left = helper(node.left, depth+1)
        right = helper(node.right, depth+1)

        if left == right == self.deepest:
            self.lca = node 

        return max(right, left)

    helper(root, 0)
    return self.lca 



