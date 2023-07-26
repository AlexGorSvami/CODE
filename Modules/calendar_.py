import calendar, locale

for name in calendar.day_name:
    print(name)

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
for name in calendar.day_name:
    print(name)

for name in calendar.day_abbr:
    print(name)

# -----------------month_name-------------------
russian_names = list(calendar.month_name)
locale.setlocale(locale.LC_ALL, 'en_EN.US')
english_names = list(calendar.month_name)
print(*russian_names)
print(*english_names)

