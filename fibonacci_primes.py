## Author : David Valles
## Date   : 19/02/2014
## Solution : 10

import math
from decimal import *
getcontext().prec=15
n=[0,1]
fp=[]

def isPrime(i):
    if i==1: return False
    j=2
    while j<Decimal(math.sqrt(i)):
        if((i%j)==0):
            return False
        
        j=j+1

    
    return True

        
def generate_fibonacci(num1,num2):
    if(len(fp))<11:
        if isPrime(num1+num2):
            fp.append(num1+num2)

        n.append(num1+num2)
        generate_fibonacci(n[-1],n[-2])
    

generate_fibonacci(n[-1],n[-2])
print "Fibonacci Primes"
print fp
print "\nNumber of digits in 11th Fibonacci Prime is ", len(str(fp[-1]))
raw_input()
