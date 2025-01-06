from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    answer1 = input()
    d[answer1].append(i+1)
for j in range(m):
    answer2 = input()
    if answer2 in d:
        print(*d[answer2])
    else:
        print(-1)

