class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
            book = dict(zip(postorder, range(len(postorder))))

            root = TreeNode(preorder[0])
            stack = [root]
            for i in range(1, len(preorder)):
                curr = preorder[i]
                n = TreeNode(curr)
                pos = book[curr]

                if pos < book[stack[-1].val]:
                    stack[-1].left = n 
                else:
                    stack.pop()
                    while stack and pos > book[stack[-1].val]:
                        stack.pop()
                    stack.pop().right = n 

                stack.append(n)


            return root     
