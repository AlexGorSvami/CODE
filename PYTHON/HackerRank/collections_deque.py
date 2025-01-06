from collections import deque
array = deque()

for i in range(int(input())):
    command  = input().split()
    if command[0] == 'pop':
        array.pop()
    elif command[0] == 'append':
        array.append(command[1])
    elif command[0] == 'appendleft':
        array.appendleft(command[1])
    elif command[0] == 'popleft':
        array.popleft()

print(*array)

