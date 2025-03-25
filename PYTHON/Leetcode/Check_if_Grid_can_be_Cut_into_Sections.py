def checkValidCuts(n: int, rectangles: list) -> bool:
    x = [(r[0], r[2]) for r in rectangles]
    y = [(r[1], r[3]) for r in rectangles]
    x.sort(), y.sort()

    def count(interval):
        c = 0
        prev = -1

        for start, end in interval:
            if prev <= start:
                c += 1 
            prev = max(prev, end)
        return c 

    return max(count(x), count(y)) >= 3


print(checkValidCuts(5, [[1,0,5,2], [0,2,2,4], [3,2,5,3], [0,4,4,5]]))
print(checkValidCuts(4, [[0,0,1,1], [2,0,3,4], [0,2,2,3], [3,0,4,3]]))
