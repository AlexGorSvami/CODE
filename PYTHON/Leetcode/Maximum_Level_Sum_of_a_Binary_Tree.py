class TreeNode:
    def  __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 

class Solution:
    def maxLevelSum(root: Optional[TreeNode]) -> int:
        max_total = -float('inf')
        level = 1 
        queue = deque([root])

        while queue:
            total = 0 
            for i in range(len(queue)):
                node = queue.popleft()
                total += node.val 
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if total > max_total:
                max_total, answer = total, level 
            level += 1 
        
        return answer
