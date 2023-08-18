from string import ascii_lowercase, ascii_uppercase
sortkey = ascii_lowercase + ascii_uppercase + '1357902468'
x = input()
print(*map(lambda y: y * x.count(y), sortkey), sep='')


print('----------------------------------------------')
s = input()
s = sorted(s, key=lambda x: (x.isdigit() and int(x)%2==0, x.isdigit(), x.isupper(),x))
print(''.join(s))
