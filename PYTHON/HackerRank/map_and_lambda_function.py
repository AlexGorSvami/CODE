cube = lambda x: x ** 3

def fibonacci(n):
    res = [0,1,1]
    if n > 3:
        for _ in range(3,n):
            res.append(res[-2] + res[-1])
    else:
        return res[:n]
            
    return res

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
