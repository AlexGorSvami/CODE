from itertools import groupby
string = input()
array = [list(v) for k, v in  groupby(string)]
res = []
for i in array:
    res.append(tuple((len(i), int(i[0]))))

print(*res)
