n,m = map(int, input().split())
res = []
for i in range(int(n)):
    res.append([int(i) for i in input().split()])
    
sor = int(input())
for i in sorted(res, key=lambda x: x[sor]):
    print(*i)    

