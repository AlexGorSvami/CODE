from collections import namedtuple

n = int(input())
name = input().split()
lis = []
summ = 0
for i in range(n):
    lis.append(input().split())

marks = name.index('MARKS')

for i in range(n):
    summ += int(lis[i][marks])
print(summ/n)

    

