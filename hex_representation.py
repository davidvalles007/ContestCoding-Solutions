## Author : David Valles
## Date   : 11/11/2013
## Solution : 4

print "The difference in size between the decimal and hexadecimal representation of \
10000000000000000000 (in decimal notation) is\n"
print (len(str(10000000000000000000))-len(hex(10000000000000000000)[2:-1]))
print "\nas 10000000000000000000 in hex is ",hex(10000000000000000000)[2:-1]
