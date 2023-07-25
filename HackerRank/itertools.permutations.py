from itertools import permutations
word, count = input().split()
for i in sorted(list(permutations(word, int(count)))):
    print(''.join(i))
