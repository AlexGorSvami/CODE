class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1 
        n = len(words)
        ind = [i for i in range(n) if target == words[i]]
        res = 1000 
        start_index_n = startIndex + n 
        start_index_n_neg = startIndex - n 
        for i in ind:
            res = min(res, abs(startIndex - i))
            res = min(res, abs(start_index_n - i))
            res = min(res, abs(start_index_n_neg - i))
        return res
            
