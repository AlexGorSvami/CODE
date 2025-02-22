from collections import deque
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        ans = TreeNode('-')
        queue = deque([ans])
        cur_depth = 0
        for c in S.split('-'):
            if c:
                for _ in range(len(queue)-1-cur_depth):
                    queue.pop()
                node = TreeNode(int(c))                    
                setattr(queue[-1], 'left' if queue[-1].left is None else 'right', node)
                queue.append(node)
                cur_depth = 1
            else:                    
                cur_depth += 1 
                
        return ans.left  
