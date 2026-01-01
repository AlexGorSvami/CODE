def plusOne(digits: list) -> list:
    result = []
    plus = 1 
    for i in range(len(digits)-1, -1, -1):
        digit = digits[i] + plus 
        if digit > 9:
            plus = 1 
        else:
            plus = 0 
        result.append(digit % 10)
        if plus == 1:
            result.append(1)
    
    return result[::-1]
