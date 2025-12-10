def countPermutations(complexity: list) -> int:
    MOD = 1000000007
    if complexity[0] >= min(complexity[1:]):
        return 0 
    return math.factorial(len(complexity)-1) % MOD 
