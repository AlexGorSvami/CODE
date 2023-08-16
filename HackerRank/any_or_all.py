n =  int(input())
array = [int(i) for i in input().split()]
print(all([i > 0 for i in array]) and any(int(str(i)[::-1]) is i for i in array))
