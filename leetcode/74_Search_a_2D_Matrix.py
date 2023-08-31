class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for i in matrix:
            if target in i:
                return True
        return False
    
    def searchMatrix1(self, matrix: list[list[int]], target: int) -> bool:
        def search(mat):
            mid = len(mat)//2
            if mid == 0:
                return target in mat[0]
            elif mat[mid][0] > target:
                return search(mat[:mid])
            return search(mat[mid:])
        return search(matrix)
