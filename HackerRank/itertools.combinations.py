from itertools import combinations
word, count = input().split()
count = int(count)
for i in range(1, count+1):
    for j in combinations(sorted(word), i):
        print(''.join(j))

