def snakesAndLadders(board: list) -> int:
    array = [0]
    n = len(board) ** 2
    q = [1]
    seen = set()
    moves = 0 

    for i, row in enumerate(board[::-1]):
        if i % 2 != 0:
            array += row[::-1]
        else:
            array += row 

    while q:
        new = []
        for s in q:
            if s == n:
                return moves 
            for i in range(1,7):
                if s+i <= n and s+i not in seen:
                    seen.add(s+i)
                    new.append(s+i if array[s+i] == -1 else array[s+i])
        q, moves = new, moves+1 

    return -1 

