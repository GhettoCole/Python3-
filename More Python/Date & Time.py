# Date & Time with python

import time 

ticks = time.time()

print('The number of ticks since 21:18PM, Novemeber 24, 2016: ', ticks,"\n")

localtime = time.localtime(time.time())
print("Local current time: ",localtime,"\n")

# Formatting time to be more readable
localtime = time.asctime(time.localtime(time.time()))
print("Formatted Local Current Time: ",localtime,"\n")

# Getting a calendar for a month
import calendar

cal = calendar.month(2016, 11)
print("Calender for November 2016")
print(cal)
