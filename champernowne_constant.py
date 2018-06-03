## Author : David Valles
## Date   : 20/11/2013
## Solution : 123456789101112138268390208509359795778623524870438036195186556218753188450158147127844097541067238.0/1000000000000000055511151231257827021181583404541015625000000000000000000000000000000000000000000000

from decimal import *
getcontext().prec = 100

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

print "Following is the fraction when champernowne constant \
is rounded to 100 decimal place\n"
c=0
n=1
for i in range(2,60):
    if len(str(n))<100:
        n=str(n)+str(i)

n=n[:100]

gcf=round(gcd(Decimal(pow(10,100.0)),Decimal(n)))
num=Decimal(Decimal(n)*Decimal(gcf)*Decimal(0.1))
den=Decimal(pow(10,100)*Decimal(gcf)*Decimal(0.1))
print '%s / %s'%(num,den)
 

print "\nChampernowne constant upto 100 digits after decimal point on performing division of above fraction\n",Decimal(num/den)

