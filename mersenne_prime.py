## Author : David Valles
## Date   : 09/11/2013
## Solution : 2047

def isPrime(i):
    for j in xrange(2,i):
        if(i%j==0):
            break
        else:
            pass

        if(j==(i/2)):
            return True

print "The smallest Mersenne number such that the base of that Mersenne number \
is a prime number, but the Mersenne number itself is not\n"

for n in xrange(5,100):
    if isPrime(n):
        M=(2**n)-1
        if not isPrime(M):
            print M
            break
        else:
            pass
    
