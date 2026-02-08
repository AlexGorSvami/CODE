def isBalanced(root: Optional:[TreeNode]) -> bool:
    from typing import Optional 
    def dfs(root: Optional:) -> int:
        if not root:
            return 0 

        left, right = dfs(root.left), dfs(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1 

        return 1 + max(left, right)

    return dfs(root) != -1
