import re
word = input()
search = input()

pattern = re.compile(search)
match = pattern.search(word)

if not match:
    print((-1, -1))
    
while match:
    print(f'({match.start()}, {match.end()-1})')
    match = pattern.search(word, match.start()+1)


