from typing import List
from collections import defaultdict 
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        array = [0] * n 
        # Группируем индексы для каждого числа
        groups = defaultdict(list)
        for i, j in enumerate(nums):
            groups[j].append(i)

        for k in groups:
            indices = groups[k]
            m = len(indices)

            #Считаем общую сумму индексов
            total_sum = sum(indices)
            prefix = 0 

            for i, ind in enumerate(indices):
                left = i * ind - prefix 
                right = (total_sum - prefix - ind) - (m - 1 - i) * ind

                array[ind] = left + right 
                prefix += ind 

        return array
