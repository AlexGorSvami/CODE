def findMissingAndRepeatedValues(grid: list) -> list:
    numbers = [i for i in range(1, (len(grid)**2)+1)]
    answer = [None, None]
    for row in grid:
        for i in row:
            if i in numbers:
                numbers.remove(i)
            else:
                answer[0] = i
    answer[1] = numbers[0]
    return answer 



print(findMissingAndRepeatedValues([[1,3], [2,2]]))
print(findMissingAndRepeatedValues([[9,1,7], [8,9,2], [3,4,6]]))

