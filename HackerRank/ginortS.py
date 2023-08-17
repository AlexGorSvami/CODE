from string import ascii_lowercase, ascii_uppercase
sortkey = ascii_lowercase + ascii_uppercase + '1357902468'
x = input()
print(*map(lambda y: y * x.count(y), sortkey), sep='')
