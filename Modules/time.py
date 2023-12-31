# Начало эпохи - это  полночь 1 января 1970 года (00:00:00 UTC), когда  счётчик секунд имел  полностью нулевое значение.
# Модуль time предостовляет только функции, позволяющие работать со временем. С его помощью
# можно получать информацию о текущих дате и времени, выводить эти сведения в необходимом формате, а также 
# управлять ходом выполнения программы, добовляя задержки по таймеру.
# При помощи time можно:
#     - отображать инфориацию о времени, прошедшем с начала эпохи;
#     - преобразовывать значение системного времени к удобному виду;
#     - перрывать выполнение программы на заданное количество секунд;
#     - измерять время выполнения программ целиком или её отдельныъ частей;

import time 

seconds = time.time()
print('Количество секунд с начала эпохи:', seconds)

# # ------------------ctime-----------------
# Для того чтобы получить текущую дату и  время в более удобном для человека виде,
# нужно использовать функцию ctime(). Функция  time.ctime() принимает в качестве аргумента количество секунд, прошедших с начала эпохи
# и  возвращает строку представляющую собой местное(локальное) время.

local_time = time.ctime(seconds)
print('Местное время: ', local_time)

# Вызывать функцию ctime() можно без аргументов, в этом случае в качестве аргумента подставится
# значение вызова функции time().

print('local time', time.ctime())

# --------------sleep-----------------------
print('Before')
print(time.sleep(3))
print('After')

start_time = time.time()
for i in range(5):
    print(i)
    time.sleep(1)

end_time = time.time()

elapsed_time = end_time - start_time
print(f'The program worked = {elapsed_time}')


# --------------------monotonic---------------------
# Для измерения времени выполнения программы идеально подходит функция monotonic(), доступная на всех ОС (начиная с Python 3.5), так как ее результат не зависит от корректировки системных часов.
start = time.monotonic()

for i in range(5):
    print(i)
    time.sleep(0.5)

end =  time.monotonic()

elapsed = end - start
print(f'Time worked programm = {elapsed}')

# -------------------------perf_counter---------------
# Для самого точного измерения времени выполнения программы следует использовать функцию perf_counter(). Данная функция использует таймер с наибольшим доступным разрешением, что делает эту функцию отличным инструментом для измерения времени выполнения кода на коротких интервалах.

start_ = time.perf_counter()
for i in range(5):
    print(i)
    time.sleep(1)

end_ = time.perf_counter()

elapsed_ = end_ - start_
print(f'The program worked:  {elapsed}')

# ----------------examples---------------------
def calculate_it(func, *args):
    import time
    start = time.perf_counter()
    val = func(*args)
    end = time.perf_counter()
    time = end - start
    return val,time
print('----------------------------------------------')



