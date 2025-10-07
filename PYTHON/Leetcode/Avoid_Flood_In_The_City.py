class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        from collections import defaultdict
        lastRain = {}
        dryDays = SortedList()
        res = [-1]*len(rains)

        for i, lake in enumerate(rains):
            if lake == 0:
                dryDays.add(i)
                res[i] = 1  # по умолчанию осушаем любое озеро
            else:
                if lake in lastRain:
                    idx = dryDays.bisect_right(lastRain[lake])
                    if idx == len(dryDays):
                        return []  # нет сухого дня → наводнение
                    dry_idx = dryDays[idx]
                    res[dry_idx] = lake  # осушаем именно это озеро
                    dryDays.pop(idx)
                lastRain[lake] = i
                res[i] = -1  # дождь над озером
        return res    
