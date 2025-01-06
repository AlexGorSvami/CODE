import numpy
num = int(input())
res = numpy.array([input().split() for _ in range(num)], float)
print(round(numpy.linalg.det(res),2))
