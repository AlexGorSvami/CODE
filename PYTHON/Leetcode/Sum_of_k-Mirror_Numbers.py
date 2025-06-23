def kMirror(k: int, n: int) -> int:
    def fn(x):
        n = len(x) // 2
        for i in range(n, len(x)):
            if int(x[i])+1 < k:
                x[i] = x[~i] = str(int(x[i])+1)
                for j in range(n, i):
                    x[j] = x[~j] = '0'
                return x 
        return ['1'] + ['0'] * (len(x)-1) + ['1']

    x = ['0']
    answer = 0 
    for _ in range(n):
        while True:
            x = fn(x)
            value = int(''.join(x), k)
            if str(value)[::-1] == str(value):
                break
        answer += value 
    return answer 
