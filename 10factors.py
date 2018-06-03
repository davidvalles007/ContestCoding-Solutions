## Author : David Valles
## Date   : 09/12/2013
## Solution : 48

for i in xrange(2,100):
    count=2
    
    for j in xrange(2,i+1):
        if(i%j==0) and j<=i/2:
            count+=1
            
        else:
            pass

    if count==10:
        print "The first number to have 10 or more factors is ",i
        break

