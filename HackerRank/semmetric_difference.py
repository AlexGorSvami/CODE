n = int(input())
set1 = set(map(int, input().split()))
n1 = int(input())
set2 = set(map(int, input().split()))
for i in sorted(set1 ^ set2):
    print(i)



