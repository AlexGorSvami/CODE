def solution(array_a, array_b):
    res = []
    for i in range(len(array_a)):
        res.append(abs(array_a[i] - array_b[i])**2)
    return sum(res) / len(res)
       
def solution1(a, b):
    return sum((x - y)**2 for x, y in zip(a, b)) / len(a)
