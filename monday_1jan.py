## Author : David Valles
## Date   : 04/01/2014
## Solution : 282

import datetime

weekday={0:'Monday',1:'Tuesday',2:'Wednesday',
         3:'Thursday',4:'Friday',5:'Saturday',
         6:'Sunday'}

years=[]

print "The following years between 0 AD to 2014 AD have Monday on the 1st January\n"

for y in range(0001,2015):
    if 'Monday' == weekday[datetime.date(y,01,01).weekday()]:
        years.append(y)
        print str(y)+" AD"

print "\nThe number of years between 0 AD to 2014 AD that have \
began (on the 1st January)on a Monday are", len(years)

raw_input()
