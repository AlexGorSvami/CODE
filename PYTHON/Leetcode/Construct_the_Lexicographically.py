def constructDistancedSequence(n: int) -> list:
    size = 2 * n-1
    result = [0] * size 
    used = set()

    def backtrack(ind):
        if ind == size:
            return True 
        if result[ind] != 0:
            return backtrack(ind + 1)

        for num in range(n, 0, -1):
            if num in used:
                continue 

            if num == 1:
                result[ind] = num 
                used.add(num)
                if backtrack(ind+1):
                    return True 
                result[ind] = 0
                used.remove(num)
            else:
                if ind + num < size and result[ind + num] == 0:
                    result[ind] = result[ind + num] = num 
                    used.add(num)
                    if backtrack(ind+1):
                        return True 
                    result[ind] = result[ind + num] = 0
                    used.remove(num)

        return False 

    backtrack(0)
    return result 



print(constructDistancedSequence(3))
print(constructDistancedSequence(5))

