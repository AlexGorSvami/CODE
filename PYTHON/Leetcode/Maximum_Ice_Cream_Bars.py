from typing import List 
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq = [0] * (max(costs) + 1)
        for c in costs:
            freq[c] += 1 

        total = 0 
        for price in range(1, len(freq)):
            if coins < price:
                break 
            if freq[price]:
                cnt = min(freq[price], coins // price)
                total += cnt 
                coins -= price * cnt 

        return total 
