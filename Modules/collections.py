from collections import OrderedDict, ChainMap, Counter, defaultdict, deque, namedtuple
import csv 



# OrderedDict нужен для действий со словарём где необходим порядок элементовб например сравнение с учётом порядка
# перестановки элементов с сохранением порядка. Платим памятью!
first = {1:1, 2:2}
second =  {2:2, 1:1}

order1 = OrderedDict(first)
order2 = OrderedDict(second)

print(order1 == order2)
order2.popitem(last=False)
order1.move_to_end(1)
print(order1)


#ChainMap нужен для логического объудинения словарей для поиска информацииб но при изменениях меняется первый словарь
chain = ChainMap(first, second)
print(chain)
chain[5]=200
print(chain)


#Counter - нужен для подсчёта элементов последовательностейб работает только с hashable
counter = Counter('hello')
print(counter)
counter.update('world')
print(counter)
print(counter.most_common(3))


#defaultdict - нужен для создания словаря со значением по умлочаниюю Значение подставляется при оюращении к несужществующему ключу
a_dict = defaultdict(int)
print(int())
for char in 'hello':
    a_dict[char] +=1

print(sorted(a_dict))


# deque птокобезопасна, быстро оперирует с обоими сторонами
a_deque = deque()
a_deque.append(1)
print(a_deque)
a_deque.appendleft(2)
print(a_deque)
a_deque.popleft()
print(a_deque)
b_deque =deque([1,2,3,4], maxlen=3)
print(b_deque)

with open('points.csv') as file:
    c_deque = deque(file, maxlen=2)

for line in c_deque:
    print(line.rstrip())


# namedtuple - нужен для создания структуры, нечто среднее между стандартными типами и самописным классом
# Неизменяемый, поддерживает обращение по индексуеизменяемый, поддерживает обращение по индексуеизменяемый, поддерживает обращение по индексу
Cat = namedtuple('Cat', 'name age color')
tom = Cat('Tom', 5, 'grey')
print(tom)
print(tom[0])
print(tom.age)

Point = namedtuple('Point', ('x y'))
with open('points.csv') as file:
    for line in csv.reader(file):
        point = Point._make(line)
        print(point)
         
