superset = set(map(int, input().split()))
sett = set()
for i in range(int(input())):
    s = set(map(int, input().split()))
    sett = sett.union(s)
    
print(superset == sett)
    
