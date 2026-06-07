class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        
        # Шаг 1: Создание узлов и их связывание
        for parent_val, child_val, is_left in descriptions:
            # Создаем узлы, если они еще не существуют в словаре
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
                
            # Связываем потомка с родителем
            if is_left == 1:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]
                
            # Запоминаем узел, который является потомком
            children.add(child_val)
            
        # Шаг 2: Поиск и возврат корня
        for parent_val, _, _ in descriptions:
            if parent_val not in children:
                return nodes[parent_val]
