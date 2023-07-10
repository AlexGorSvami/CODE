from datetime import date 

print(date.today())
print(date(1991, 11, 6).weekday())
print(date(1991, 11, 6).isoweekday())


dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]
for data in dates:
    print(f'{data.year}-Q{(data.month - 1) // 3 + 1}')


def get_min_max(dates: list) -> tuple:
    if dates:
        return (min(dates), max(dates))
    return tuple()

from datetime import date
def get_date_range(start, end):
    res = []
    for i in range(start.toordinal(), end.toordinal()+1):
        res.append(i)
    res = [date.fromordinal(i) for i in res]
    return res

date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')
