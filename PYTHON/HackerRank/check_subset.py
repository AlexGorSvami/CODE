for i in range(int(input())):
    n1 = int(input())
    set1 = set([int(i) for i in input().split()])
    n2 = int(input())
    set2 = set([int(i) for i in input().split()])
    print(set2 > set1)

