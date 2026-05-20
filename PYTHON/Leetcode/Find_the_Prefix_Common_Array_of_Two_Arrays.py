class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = [0] * (n + 1)
        common_cnt = 0 
        res = []

        for i in range(n):
            freq[A[i]] += 1 
            if freq[A[i]] == 2:
                common_cnt += 1      

            freq[B[i]] += 1 
            if freq[B[i]] == 2:
                common_cnt += 1 
            res.append(common_cnt)
        return res 

        
