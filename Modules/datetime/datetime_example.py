from datetime import datetime, date, time

my_datetime = datetime(1991, 11, 6, 9, 40, 23, 51204)
only_date = datetime(2021, 12, 31)

print(my_datetime)
print(only_date)
print(type(my_datetime))

print('Year = ', my_datetime.year)
print('Month = ', my_datetime.month)
print('Day = ', my_datetime.day)
print('Hour = ', my_datetime.hour)

my_date = date(1991, 11, 6)
my_time = time(8, 30, 12)
my_combine_datetime = datetime.combine(my_date, my_time)
print(my_combine_datetime)

print(my_datetime.date())
print(my_datetime.time())

print(datetime.now())
print(datetime.utcnow())

# ---------------------Метод timestamp()---------------
# Метод timestamp() позволяет преобразовать объект типа datetime в количество секунд, прошедших с момента начала эпохи.
# Данный метод возвращает значение типа float.

print(my_datetime.timestamp())

print(datetime.fromtimestamp(689413223.051204))

from datetime import datetime

times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26), 
                      datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59), 
                      datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53), 
                      datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3), 
                      datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5), 
                      datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54), 
                      datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45), 
                      datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57), 
                      datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42), 
                      datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12), 
                      datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27), 
                      datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41), 
                      datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44), 
                      datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]
 

for i in times_of_purchases:
    if i.hour > 11:
        print(i)


data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'), 
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'), 
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'), 
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'), 
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'), 
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'), 
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'), 
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'), 
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'), 
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'), 
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
res = {}
for key,values in data.items():
    res[key] = values[1].split()[1] - values[0].split()[1]
    print(res)
