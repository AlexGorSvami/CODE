def minDominoRotations(tops: list, bottoms: list) -> int:
    candidates = list(set([tops[0], bottoms[0]]))
    for i in range(len(tops)):
        for candidate in candidates:
            if candidate != tops[i] and candidate != bottoms[i]:
                candidates.remove(candidate)
        if not candidates:
            return -1 
    value = len(tops)
    for candidate in candidates:
        tops_count = len([i for i in tops if i != candidate])
        bottoms_count = len([i for i in bottoms if i != candidate])
        value = min(value, tops_count, bottoms_count)
    return value



