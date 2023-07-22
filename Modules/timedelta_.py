from datetime import timedelta, date, datetime

delta = timedelta(days=7, hours=20, minutes=7, seconds=17)
print(delta)
print(type(delta))

delta1 = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)
delta2 = timedelta(weeks=1, hours=23, minutes=61)
delta3 = timedelta(hours=25)
print(delta1, delta2, delta3, sep='\n')
# Обрати внимание на то, что если во временном интервале (timedelta) значение days=0, то 
# оно не выводится. Временной интервал timedelta может быть отрицательным

delta5 = timedelta(hours=-25)
print(delta5)

# Метод total_seconds() возвращает общее количество секунд в интервале timedelta
# Обратите внимание на то, что у типа timedelta нет атрибутов hours и minutes, позволяющих получить количество часов и минут соответственно. Достать часы и минуты можно так:

def hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60

delta6 = timedelta(days=7, seconds=125, minutes=10, hours=8, weeks=2)

hours, minutes = hours_minutes(delta)
print(delta6.total_seconds())


my_life = date(1991, 11, 6)
today = date.today()
print(my_life - today)


dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)

print(dt.strftime('%d.%m.%Y %H:%M:%S'))


today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = today - birthday

print(abs(days.days)) 

