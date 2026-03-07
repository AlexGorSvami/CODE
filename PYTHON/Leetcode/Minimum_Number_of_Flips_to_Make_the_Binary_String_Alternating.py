def minFlips(s: str) -> int:
    result = float('inf')
    for wanted in '01':
        missmatch = 0 
        flip_missmatch = 0 
        for bit in s:
            if wanted != bit:
                missmatch += 1 
            elif len(s) % 2:
                flip_missmatch = min(flip_missmatch + 1, missmatch)
            wanted = '1' if wanted == '0' else '0'
        result = min(result, missmatch, flip_missmatch if len(s) % 2 else float('inf'))
    return result
