def countPalindromicSubsequence(s: str) -> int:
    result, left, right = set(), set(), Counter(s)
    for i in s:
        right[i] -= 1 
        for c in left:
            if right[c] > 0:
                result.add((i, c))
        left.add(i)
    return len(result)
