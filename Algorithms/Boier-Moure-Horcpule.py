t = 'данные'

 # Этап 1: формирование таблицы смещений
S = set()
M = len(t)
d = {}

for i in range(M-2, -1, -1):
    if t[i] not in S:
        d[t[i]] = M-i-1
        S.add(t[i])

if t[M-1] not in S:
    d[t[M-1]] = M

d['*'] = M

print(d)

# Этап 2: поиск образа в строке

a = 'больште метеоданные'
N = len(a)

if N >= M:
    i = M-1

    while i < N:
        k = 0
        for j in range(M-1, -1, -1):
            if a[i-k] != t[j]:
                if j == M-1:
                    off = d[a[i]] if d.get(a[i], False) else d['*']
                else:
                    off = d[t[j]]

                i += off
                break

            k += 1

        if j == 0:
            print(f"образ найден по индексу {i-k+1}")
            break
else:
    print('Образ  не найден')

