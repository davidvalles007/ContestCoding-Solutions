## Author : David Valles
## Date   : 04/11/2013
## Solution : 100

import math
n=2
base=0
square=0
while True:
    square=pow(n,2)
    base = math.sqrt(square)
    n+=1
    if len(str(square))>4:
        break

print "Base of the first square number to exceed 5-digits ",base
