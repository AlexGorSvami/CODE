n = int(input())
numbers = {}
for i in input().split():
    numbers[i] = numbers.get(i,0)+1

print(min(numbers, key=lambda x: numbers[x]))
