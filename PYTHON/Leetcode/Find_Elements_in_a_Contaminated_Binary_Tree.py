class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.aim = aim = set()
        def recover(n,x):
            if n:
                aim.add(x)
                recover(n.left, 2*x + 1)
                recover(n.right, 2*x + 2)
        
        recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.aim 


