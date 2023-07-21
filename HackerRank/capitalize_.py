s = input()
for i in s.split():
    s = s.replace(i, i.capitalize())
print(s)

def capit(word):
    return ' '.join([i.capitalize() for i in word.split(' ')])

print(capit(input()))
