import re
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        from itertools import groupby
    
        # Разбиваем дополненную строку на длины чередующихся блоков 1 и 0
        L = [len(list(g)) for _, g in groupby('1' + s + '1')]
        
        # Если блоков меньше 5, внутри нет ни одной '1', окруженной нулями
        if len(L) < 5:
            return s.count('1')
            
        max_gain = 0
        # Собираем все блоки нулей (они всегда на нечетных индексах) по убыванию длины
        zeros = sorted([(L[j], j) for j in range(1, len(L), 2)], reverse=True)
        
        # Перебираем все внутренние блоки единиц (четные индексы от 2 до len(L)-3)
        for i in range(2, len(L) - 1, 2):
            # Вариант 1: превращаем в единицы объединенный блок нулей вокруг текущей '1'
            gain = L[i-1] + L[i+1]
            
            # Вариант 2: превращаем в единицы какой-то другой, самый длинный блок нулей
            for z, j in zeros:
                if j not in (i - 1, i + 1):
                    gain = max(gain, z - L[i])
                    break
                    
            max_gain = max(max_gain, gain)
            
        return s.count('1') + max_gain
