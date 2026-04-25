from typing import List
import bisect

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # Преобразуем точки и удаляем дубликаты
        positions = set()
        for x, y in points:
            if y == 0:
                pos = x
            elif x == side:
                pos = side + y
            elif y == side:
                pos = 2 * side + (side - x)
            else:
                pos = 3 * side + (side - y)
            positions.add(pos)
        
        positions = sorted(positions)
        n = len(positions)
        
        if n < k:
            return 0
        
        perimeter = 4 * side
        
        # Разворачиваем массив для избежания modulo
        extended = positions + [p + perimeter for p in positions]
        
        def can_place(dist: int) -> bool:
            # Быстрые проверки
            if dist > 2 * side:  # Максимальное манхэттенское расстояние на периметре
                return False
            
            full_circle_dist = perimeter - dist
            
            for start in range(n):
                curr = start
                count = 1
                
                for _ in range(k - 1):
                    target = extended[curr] + dist
                    next_idx = bisect.bisect_left(extended, target, lo=curr + 1)
                    
                    if next_idx >= start + n:
                        break
                    
                    count += 1
                    curr = next_idx
                    
                    # Оптимизация: если расстояние между текущей и начальной точкой
                    # уже слишком большое, продолжаем
                    if extended[curr] - extended[start] > full_circle_dist:
                        break
                
                if count >= k and extended[curr] - extended[start] <= full_circle_dist:
                    return True
            
            return False
        
        # Бинарный поиск с уточнёнными границами
        left, right = 1, 2 * side
        
        while left <= right:
            mid = (left + right) // 2
            if can_place(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right
