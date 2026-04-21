from typing import List 
from collections import defaultdict, Counter 
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], alllowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        #Объеддиняем индексы в группы
        for u, v in alllowedSwaps:
            root_u, root_v = find(u), find(v)
            if root_u != root_v:
                parent[root_u] = root_v 

        #Группируем значения по компонентам 
        groups = defaultdict(lambda: Counter())
        for i in range(n):
            groups[find(i)][source[i]] += 1 

        #Считаем совпадения
        matches = 0 
        for i in range(n):
            root = find(i)
            val = target[i]
            if groups[root][val] > 0:
                matches += 1 
                groups[root][val] -= 1 

        return n - matches
