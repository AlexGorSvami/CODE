from datetime import date, time
import locale

my_date = date(2021, 2, 10)
my_time = time(4,12,43)

print(my_date)
print(my_time)

print(my_date.strftime('%d/%m/%y'))
print(my_date.strftime('%A %d, %B %Y'))
print(my_time.strftime('%H.%M.%S'))

print(my_date.strftime('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S %f %z %Z %j %U %W %c %x %X'))
print(my_time.strftime('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S %f %z %Z %j %U %W %c %x %X'))

given_date = date(2021, 7, 17)

print(given_date.strftime('%A %d %B %Y'))
print(given_date.strftime('%Y/%m/%d'))
print(given_date.strftime('%d.%m.%Y (%A, %B)'))
print(given_date.strftime('Day of year: %j, week number: %U'))

given_time = time(14, 4, 29)

print(given_time.strftime('Hours: %H, minutes: %M, seconds: %S.'))
print(given_time.strftime('%H:%M:%S'))
print(given_time.strftime('%I:%M:%S %p'))


locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

my_rudate = date(1991, 11,6)
print(my_rudate.strftime('%A %d, %B %Y'))

# Для того, чтобы получить строковое представление объектов типа date и time в ISO формате, 
# можно воспользоваться методом isoformat()

print('Date: ' + my_date.isoformat())
print('Time: ' + my_time.isoformat())

print('Date: ' + str(my_date))
print('Time: ' + str(my_time))


#----------- Преобразование строки в дату и время -----------
while True:
    try:
        day, month, year = input('Введите дату и время в формате ДД.ММ.ГГГГ').split('.')
        hour, minute, second = input('Введите время в формате ЧЧ:ММ:СС').split(':')
        my_input_date = date(int(year), int(month), int(day))
        my_input_time = time(int(hour), int(minute), int(second))
        print(my_input_date)
        print(my_input_time)
        break
    except :
        print('Ошибка ввода.Введите корректные данные!!!')

# ---------------------Преобразование строки в дату с помощью метода fromisoformat()-------------

my_iso_date = date.fromisoformat('1991-11-06')
print(my_iso_date)
print(type(my_iso_date))


