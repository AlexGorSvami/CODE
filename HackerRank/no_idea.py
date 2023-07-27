from collections import Counter

n, m = map(int, input().split())
data = list(map(int, input().split()))
data_counter = Counter(data)
data_set = set(data)

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

happiness = 0

for i in data_set & set_a:
    happiness += data_counter[i]
for i in data_set & set_b:
    happiness -= data_counter[i]

print(happiness)
