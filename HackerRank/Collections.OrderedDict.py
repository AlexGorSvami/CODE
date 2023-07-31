from collections import OrderedDict
goods = OrderedDict()
item = ''
number = ''
for i in range(int(input())):
    for j in input().split():
        if j.isalpha():
            item += j +  " "
        else:
            number += j
    if item not in goods:
        goods[item] = int(number)
    else:
        goods[item] += int(number)
    item = ''
    number = ''

for key, value in goods.items():
    print(key,value)


# ------------------------------------------------
products =  OrderedDict()
for i in range(int(input())):
    item = input().split()
    price = item[-1]
    good = ' '.join(item[:-1])
    if products.get(good):
        products[good] += price
    else:
        products[good] = price

for i in products.keys():
    print(i, products[i])

    

