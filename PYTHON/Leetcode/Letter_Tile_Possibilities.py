def numtilepossibilities(tiles: str) -> int:
    result = set()

    def backtrack(choices, path):
        if path:
            result.add(path)

        for i in range(len(choices)):
            backtrack(choices[:i] + choices[i+1:], path + choices[i])
            
    backtrack(tiles, '')

    return len(result)


print(numtilepossibilities("aab"))
print(numtilepossibilities("aaabbc"))
print(numtilepossibilities("v"))
