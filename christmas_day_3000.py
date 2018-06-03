## Author : David Valles
## Date   : 09/11/2013
## Solution : Thursday

import datetime

weekday={0:'Monday',1:'Tuesday',2:'Wednesday',
         3:'Thursday',4:'Friday',5:'Saturday',
         6:'Sunday'}

print "The day of the week that 25th December 3000 A.D. will fall on is\n"
print weekday[datetime.date(3000,12,25).weekday()]
