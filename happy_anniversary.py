## Author : David Valles
## Date   : 10/03/2014
## Solution : 2025

import datetime

weekday={0:'Monday',1:'Tuesday',2:'Wednesday',
         3:'Thursday',4:'Friday',5:'Saturday',
         6:'Sunday'}

year=[]

y=2015

while 1:
    
    if 'Saturday' == weekday[datetime.date(y,03,8).weekday()]:
        year.append(y)
        break

    y+=1

print "\nThe next time the anniversary of contestcoding will on a\
 Saturday in", year[0]

raw_input()
