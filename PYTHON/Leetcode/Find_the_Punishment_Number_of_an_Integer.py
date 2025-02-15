def punishmentNumber(n: int) -> int:
    def checkVailid(str_num, target):
        if not str_num and target == 0:
            return True
        for i in range(len(str_num)):
            left = str_num[:i +1]
            right = str_num[i +1:]
            leftNum = int(left)
            if checkVailid(right, target - leftNum):
                return True 
        return False 

    result = 0
    for i in range(1, n+1):
        sqr_num = i**2
        if checkVailid(str(sqr_num), i):
            result += sqr_num 
    return result


print(punishmentNumber(10))
print(punishmentNumber(37))

