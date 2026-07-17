class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        max_val = max(nums)
        cnt = [0] * (max_val + 1)
        for x in nums: 
            cnt[x] += 1
        
        exact = [0] * (max_val + 1)
        # Идем с конца для корректного вычета кратных НОД
        for i in range(max_val, 0, -1):
            c = sum(cnt[i::i]) # Количество чисел, кратных i
            exact[i] = c * (c - 1) // 2
            # Вычитаем пары, чей НОД является кратным i (2i, 3i и т.д.)
            for j in range(2 * i, max_val + 1, i):
                exact[i] -= exact[j]
        
        # Строим массив префиксных сумм
        prefix = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix[i] = prefix[i - 1] + exact[i]
            
        # Бинарный поиск для каждого запроса
        return [bisect.bisect_right(prefix, q) for q in queries]  
