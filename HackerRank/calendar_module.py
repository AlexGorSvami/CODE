import calendar
month, day, year = map(int, input().split())
weekday = calendar.weekday(year, month, day)
print(calendar.day_name[weekday])

