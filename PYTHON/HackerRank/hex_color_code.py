import re
pattern = r'#([A-Fa-f0-9]{3,6})'
res = []
for i in range(int(input())):
    s = input()
    if not s.startswith('#'):
        if re.findall(pattern, s):
            res.append((re.findall(pattern, s))[0])
            if len(re.findall(pattern, s)) > 1:
                res.append((re.findall(pattern, s))[1])
            
for i in res:
    print('#' + ''.join(i))
           

in_css = False
for _ in range(int(input())):
    s = input()
    if '{' in s:
        in_css = True
    elif '}' in s:
        in_css = False
    if in_css:
        for color in re.findall('#[0-9a-fA-F]{3,6}', s):
            print(color)

