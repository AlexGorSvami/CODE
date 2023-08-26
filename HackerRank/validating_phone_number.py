for i in  range(int(input())):
    number = input()
    if len(number) == 10 and number[0] in  ('789') and number.isdigit():
        print('YES')
    else:
        print('NO')
