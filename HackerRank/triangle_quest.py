for i in range(1, int(input())):
    print(i*((10**i-1) // 9))


for j in range(1, int(input())):
    print(j * int(bin(2**j - 1)[2:]) )
