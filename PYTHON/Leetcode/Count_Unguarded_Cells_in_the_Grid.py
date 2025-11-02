def countUnguarded(m: int, n: int, guards: list, walls: list) -> int:
    cnt = m * n - len(walls)
    guards = set([tuple(g) for g in guards])
    walls = set([tuple(w) for w in walls])
    visited = set()

    for row, col in guards:
        cnt -= 1 
        if (row, col) in visited:
            continue 
        visited.add((row, col))

        for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            i, j = row, col 
            while (0 <= (ni := i + di) < m and 
                   0 <= (nj := j + dj) < n and
                   (ni, nj) not in guards):

                    i, j = ni, nj 

                    if (i, j) in walls:
                        break 
                    if (i, j) in visited:
                        continue 
                    cnt -= 1 
                    visited.add((i, j))

    return cnt 
