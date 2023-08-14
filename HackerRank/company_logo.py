from collections import Counter
letters = Counter(sorted(input())).most_common(3)
for i in  sorted(letters, key=lambda x: x[1], reverse=True):    
    print(i[0],i[1])


