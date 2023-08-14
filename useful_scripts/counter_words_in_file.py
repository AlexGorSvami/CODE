from collections import Counter
from re import findall

with open('file_name') as fp:
    words = findall(r'\w+', fp.read().lower())

cnt = Counter(words).most_common(10)
print(cnt)
