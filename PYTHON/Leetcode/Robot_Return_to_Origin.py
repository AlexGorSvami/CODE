def jubgeCircle(moves: str) -> bool:
    return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
