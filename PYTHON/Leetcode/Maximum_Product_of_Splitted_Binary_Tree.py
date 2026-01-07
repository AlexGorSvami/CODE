def maxProduct(root: Optional[TreeNode]) -> int:
    sums = []

    def sum_tree(subroot):
        if subroot is None: return 0 
        left_sum = sum_tree(subroot.left)
        right_sum = sum_tree(subroot.right)
        total_sum = left_sum + right_sum + subroot.val
        sums.append(total_sum)
        return total_sum

    total = sum_tree(root)
    best = 0 
    for i in sums:
        best = max(best, i * (total - i))
    return best % (10 ** 9 + 7)
