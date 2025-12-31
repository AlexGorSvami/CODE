def latestDayToCross(row: int, col: int, cells: list) -> int:
    l, h = 0, len(cells) - 1

    while h >= l:
        middle = (h + l) // 2 

        matrix = [[0] * col for i in range(row)]
        for i in range(middle):
            matrix[cells[i][0] - 1][cells[i][1] - 1] = 1 

        stack = deque()
        passed = False
        for i in range(col):
            if matrix[0][i] == 0:
                stack.append((0, i))

        while stack:
            curr_y, curr_x = stack.pop()

            if curr_y == row - 1:
                passed = True
                break 
            
            matrix[curr_y][curr_x] = 1 

             if curr_y > 0 and matrix[curr_y - 1][curr_x] == 0: 
                stack.append((curr_y - 1, curr_x))
             if curr_y < row - 1 and matrix[curr_y + 1][curr_x] == 0: 
                stack.append((curr_y + 1, curr_x))
             if curr_x > 0 and matrix[curr_y][curr_x - 1] == 0: 
                stack.append((curr_y, curr_x - 1))
             if curr_x < col - 1 and matrix[curr_y][curr_x + 1] == 0: 
                stack.append((curr_y, curr_x + 1))

        if passed: 
            l = middle + 1 
        else:
            h = middle - 1 

    return h 
