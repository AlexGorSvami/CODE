col, row = map(int, input().split())
res = []
for i in range(row):
    i = [float(i) for i in input().split()]
    res.append(i)
print(*[sum(i) / len(i) for i in zip(*res)],sep='\n')
