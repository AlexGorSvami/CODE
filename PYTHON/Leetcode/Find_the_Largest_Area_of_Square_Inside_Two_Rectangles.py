def largestSquareArea(bottomLeft: list, topRight: list) -> int:
    answer = 0
    n = len(bottomLeft)
    for i in range(n - 1):
        for j in range(i + 1, n):
            max_x_left_bottom = max(bottomLeft[i][0], bottomLeft[j][0])
            min_x_top_right = min(topRight[i][0], topRight[j][0])

            max_y_bottom_left = max(bottomLeft[i][1], bottomLeft[j][1])
            min_y_top_right = min(topRight[i][1], topRight[j][1])

            if max_x_left_bottom < min_x_top_right and max_y_bottom_left < min_y_top_right:
                side = min(min_x_top_right - max_x_left_bottom, min_y_top_right - max_y_bottom_left)
                answer = max(answer, side ** 2)

    return answer
