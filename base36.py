## Author : David Valles
## Date   : 18/12/2013
## Solution : 60106575588567168940

import string

index=0
base36={}

for i in string.digits:
    base36[i]=str(index)
    index+=1

for i in string.ascii_uppercase:
    base36[i]=str(index)
    index+=1


input_string="CONTESTCODING"
#input_string="CON"

MSB=len(input_string)-1
base10=0

for i in input_string:
    base10+=int(base36[i])*(pow(36,MSB))
    MSB-=1

print "The decimal(base 10) equivalent of the base 36 number \"CONTESTCODING\" is",base10
raw_input()


