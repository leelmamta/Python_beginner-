import calendar
import datetime
import time
print(calendar.weekheader(3)) # all week days with first three words 
print() # blank line 
print(calendar.firstweekday())
print()
print(calendar.month(2019,3)) # print month like calender 
print(calendar.monthcalendar(2019,3)) # print month in array of weeks 
print(calendar.calendar(2000)) # print calender of particular year

day_of_week = calendar.weekday(2019,3,8) 
print(day_of_week)
is_leap = calendar.isleap(2019)
print(is_leap)

how_many_leap_days = calendar.leapdays(2000,2012) # 2012 is exclusive while 2000 is inclusive here 
print(how_many_leap_days)