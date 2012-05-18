#Project Euler problem #19

import datetime, calendar

count = 0
d=datetime.date(1901,1,1)

while d<=datetime.date(2000,12,31):
    if d.day == 1 and d.weekday() == calendar.SUNDAY:
        count +=1
    d += datetime.timedelta(days=1)

print count
