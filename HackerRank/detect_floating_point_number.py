import re
for  i in range(int(input())):
    print(re.search(r'^([-\+])?\d*\.\d+$', input()) is not None)
