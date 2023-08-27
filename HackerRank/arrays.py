import numpy

def arrays(arr):
    return numpy.array([float(i) for i in arr][::-1])

arr = input().strip().split(' ')
