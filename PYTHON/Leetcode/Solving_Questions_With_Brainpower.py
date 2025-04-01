def mostPoints(questions: list) -> int:
    n = len(questions)
    def go(index):
        if index >= n:
            return 0
        points, skip = questions[index]
        result = go(index + 1)
        result = max(result, points + go(index + skip + 1))
        return result 
    return go(0)



print(mostPoints([[3,2], [4,3], [4,4], [2,5]]))
print(mostPoints([[1,1], [2,2], [3,3], [4,4], [5,5]]))
