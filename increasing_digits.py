## Author : David Valles
## Date   : 08/11/2013
## Solution : 126

print "Following are the increasing 4 digit numbers:\n"
c=0
for i in range(1000,10000):
    i=str(i)
    if (str(i[0])<str(i[1])<str(i[2])<str(i[3])):
        print i
        c+=1

print "\nThe total number of 4-digit integers such that every \
digit in that integer increases from left to right : ",c
