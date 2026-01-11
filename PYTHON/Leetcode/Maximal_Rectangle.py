def maximalRectangle(matrix: list) -> int:
    if not matrix or not matrix[0]: 
        return 0
    def call_area():
        s, result = [], 0
        for i in range(len(heights) + 1):
            while s and (i == len(heights) or heights[s[-1]] > heights[i]):
                h = heights[s.pop()]
                x = i - s[-1] - 1 if s else i 
                result = max(result, x * h)
            s.append(i)
        return result 

    n, m, result = len(matrix), len(matrix[0]), 0 
    heights = [0] * m
    for i in range(n):
        for j in range(m):
            heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0 
        result = max(result, call_area())

    return result 
