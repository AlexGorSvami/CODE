def areAlmostEqual(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    difference = [(i1, i2) for i1, i2 in zip(s1, s2) if i1 != i2]
    return len(difference) == 2 and difference[0] == difference[1][::-1]

print(areAlmostEqual('bank', 'kanb'))
print(areAlmostEqual('attack','defend'))
print(areAlmostEqual('kelb','kelb'))
