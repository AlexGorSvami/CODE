from typing import List 
import bisect
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        if maxDiff < 0:
            return [0 if u == v else -1 for u, v in queries]

        vals = sorted(list(set(nums)))
        m = len(vals)

        # up[i][j] хранит индекс, в который мы попадаем из i за 2^j шагов 
        up = [[0] * 20 for _ in range(m)]
        comp = [0] * m 

        # Инициализация базовых прыжков (2^0 = 1 step) и компонент связности
        for i in range(m):
            up[i][0] = bisect.bisect_right(vals, vals[i] + maxDiff) - 1 
            if i > 0:
                comp[i] = comp[i-1] if vals[i] - vals[i-1] <= maxDiff else i 

        # Заполнение таблицы двоичного подъёма
        for j in range(1, 20):
            for i in range(m):
                up[i][j] = up[up[i][j-1]][j-1]

        answer = []
        for u, v in queries:
            if u == v:
                answer.append(0)
                continue 

            val_u, val_v = nums[u], nums[v]
            if val_u == val_v:
                answer.append(1)
                continue 

            # Направление обхода не важно, всегда идём от меньшего к большему
            if val_u > val_v:
                val_u, val_v = val_v, val_u 

            start = bisect.bisect_left(vals, val_u)
            target = bisect.bisect_left(vals, val_v)

            # Если значения в разных компонентах связности, пути нет 
            if comp[start] != comp[target]:
                answer.append(-1)
                continue 

            curr = start 
            steps = 0 

            #Жадный поиск с помощью двоичного подъёма 
            for j in range(19, -1, -1):
                if up[curr][j] < target:
                    curr = up[curr][j]
                    steps += 1 << j 

            answer.append(steps + 1)

        return answer 

    
