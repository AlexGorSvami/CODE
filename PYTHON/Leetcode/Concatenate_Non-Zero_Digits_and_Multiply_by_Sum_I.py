class Solution:
    def sumAndMultiply(self, n: int) -> int:
        res = str(n).replace('0', '').replace('-', '')
        return int(res) * sum(map(int, res)) if res else 0 

