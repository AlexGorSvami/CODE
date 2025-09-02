def numberOfPairs(points: list) -> int:
    answer = 0
    points.sort(key=lambda x: (x[0], -x[1]))
    for i in range(len(points)):
        _, y1 = points[i]
        y_max = float('-inf')
        for j in range(i+1, len(points)):
            _, y2 = points[j]
            if y1 >= y2 and y2 > y_max:
                answer += 1 
                y_max = y2
    return answer 
