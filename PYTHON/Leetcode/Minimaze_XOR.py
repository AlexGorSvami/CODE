def minimazeXor(num1: int, num2: int) -> int:
    num1_cnt1, num2_cnt1 = bin(num1).count('1'), bin(num2).count('1')
    result = num1
    for i in range(32):
        if num1_cnt1 > num2_cnt1 and (1 << i) & num1 > 0:
            result ^= 1 << i 
            num1_cnt1 -= 1 
        if num1_cnt1 < num2_cnt1 and (1 << i) & num1 == 0:
            result ^= 1 << i 
            num1_cnt1 += 1 

    return result 


print(minimazeXor(3, 5))
print(minimazeXor(1, 12))
