## Author : David Valles
## Date   : 03/11/2013
## Solution : 5291328

import math

def IsPrime(num):
    flag=False
    
    for j in range(2,num):
        if(num%j==0):
            break
        else:
            pass

        if(j==(num-1)):
            flag=True
            return flag
n=0
perfect=[]
while len(perfect)<4:
    n=n+1

    if n==2:
        perfect.append(pow(2,n-1)*(pow(2,n)-1))
        
    if IsPrime(n):
        perfect.append(pow(2,n-1)*(pow(2,n)-1))

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def multi_lcm(*args):
    return reduce(lcm,args)

print "LCM of the first 4 perfect numbers "+str(perfect)+" is ", multi_lcm(*perfect)
    



