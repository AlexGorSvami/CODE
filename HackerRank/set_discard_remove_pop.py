n = int(input())
my_set = set([int(i) for i in input().split()])
for i in range(int(input())):
    command = input().split()
    if command[0] == 'pop':
        my_set.pop()
    elif command[0] == 'remove':
        my_set.remove(int(command[1]))
    else:
        my_set.discard(int(command[1]))

print(sum(my_set))

