def findEvenNumbers(digits: list) -> list:
    distinct = [0] * 10
    for i in digits:
        distinct[i] += 1 
        res = []
    for j in range(100, 1000, 2):
        k = 0
        while k < 10:
            if str(j).count(str(k)) > distinct[k]:
                break
            k += 1 
        if k == 10:
            res.append(j)
    return res


print(findEvenNumbers([2,1,3,0]))
print(findEvenNumbers([2,2,8,8,2]))
