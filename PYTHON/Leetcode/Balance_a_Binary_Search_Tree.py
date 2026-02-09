def balanceBST(root: Optional) -> Optional:
    def in_order(root):
        if not root:
            return [] 
        return in_order(root.left) + [root.val] + in_order(root.right)

    inorder = in_order(root)
    
    def balance(a, b):
        if a > b:
            return None 
        mid = (a + b) // 2 
        root = TreeNode(inorder[mid]) 
        root.left = balance(a, mid-1)
        root.right = balance(mid+1, b)

        return root 
    
    return balance(0, len(inorder) - 1)

    

