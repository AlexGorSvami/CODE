n = int(input())
set1 = set([int(i) for i in input().split()])
for i in range(int(input())):
    operation, col = input().split()
    new_set = set([int(i) for i in input().split()])
    if operation == 'intersection_update':
        set1 &= new_set
    elif operation == 'update':
        set1 |= new_set
    elif operation == 'symmetric_difference_update':
        set1 ^= new_set
    elif operation == 'difference_update':
        set1 -= new_set

print(sum(set1))
