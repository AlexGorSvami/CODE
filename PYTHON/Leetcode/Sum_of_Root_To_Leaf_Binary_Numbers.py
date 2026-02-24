def sumRootToLeaf(root: Optional[TreeNode]) -> int:
    root_to_leaf = curr_number = 0 

    while root:
        if root.left:
            predecessor = root.left 
            step = 1 
            while predecessor.right and predecessor.right is not root:
                predecessor = predecessor.right 
                step += 1 

            if predecessor.right is None:
                curr_number = (curr_number << 1) | root.val 
                predecessor.right = root 
                root = root.left 

            else:
                if predecessor.left is None:
                    root_to_leaf += curr_number 
                for _ in range(step):
                    curr_number >>= 1 
                predecessor.right = None 
                root = root.right 

        else:
            curr_number = (curr_number << 1) | root.val 
            if root.right is None:
                root_to_leaf += curr_number 
            root = root.right 

    return root_to_leaf
