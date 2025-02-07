def queryResults(limit: int, queries: list) -> list:
    from collections import defaultdict
    colors = defaultdict(lambda: 0)
    balls = {}
    answer = []

    for (i, color) in queries:
        if i in balls:
            old_color = balls[i]
            
            colors[old_color] -= 1
            if colors[old_color] == 0:
                colors.pop(old_color)

        balls[i] = color 
        colors[color] += 1
        answer.append(len(colors))

    return answer 


print(queryResults(4, [[1,4], [2,5], [1,3], [3,4]]))
print(queryResults(4, [[0,1], [1,2], [2,2], [3,4], [4,5]]))
