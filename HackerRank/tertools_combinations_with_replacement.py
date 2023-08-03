from itertools import combinations_with_replacement
word,num  = input().split()
for i in combinations_with_replacement(''.join(sorted(word)),int(num)):
    print(*i, sep='')
