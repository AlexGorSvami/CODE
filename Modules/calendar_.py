import calendar, locale

# for name in calendar.day_name:
#     print(name)
#
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# for name in calendar.day_name:
#     print(name)
#
# for name in calendar.day_abbr:
#     print(name)
#
# # -----------------month_name-------------------
# russian_names = list(calendar.month_name)
# locale.setlocale(locale.LC_ALL, 'en_EN.US')
# english_names = list(calendar.month_name)
# print(*russian_names)
# print(*english_names)

def get_days_in_month(year, month): 
    from datetime import datetime
    import calendar
    d = str(year) + " " + month
    date = datetime.strptime(d, '%Y %B')
    res = []
    for i in range(1,calendar.monthrange(date.year, date.month)[-1]+1):
        dt = str(year) + " " + month + " " + str(i)
        res.append(datetime.strptime(dt, '%Y %B %d'))
    return sorted(res)

print(get_days_in_month(2021, 'December'))
