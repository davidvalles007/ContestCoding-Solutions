## Author : David Valles
## Date   : 08/11/2013
## Solution : 

import sys
print 
print "The largest prime number that remains a prime number when the right most\ndigit is removed until only one digit remains:"
print

flag=False

def isPrime(n):
       for j in xrange(2,n):
        if(n%j==0):
            break
        else:
            pass

        if(j==(n/2)):
            return True
        
for j in xrange(sys.maxint,sys.maxint/2,-1):
#for j in xrange(10000,700,-1):
    
    if flag:
        break
    if isPrime(j):
        prime_number=j
        for k in range(len(str(prime_number))):
            if j!=0:
                j=j/10
                if isPrime(j):
                    if len(str(j))==1:
                        print prime_number
                        flag=True
                        break
                else:
                    break


        
