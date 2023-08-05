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
        dt = datetime.strptime(dt, '%Y %B %d')
        res.append(dt.date())
    return sorted(res)

# -------------------------------------------------
def get_days_in_month1(year, month):
    from datetime import datetime, date
    month = list(calendar.month_name).index(month)
    return [date(year, month, day) for day in range(1, calendar.monthrange(year, month)[1]+1)]

print(get_days_in_month(2021, 'December'))
