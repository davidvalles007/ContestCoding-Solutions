## Author : David Valles
## Date   : 30/10/2013
## Solution : 98689

print 
print "Following is the largest 5-digit Palindromic Prime Number:"
print

flag=False
##Set the 5-digit range of numbers
for i in range(99999,10000,-1):
    digits=[]
    if flag:
        break
    
    for j in range(2,i):
        if(i%j==0):
            break
        else:
            pass

        if(j==(i/2)):
            prime_number=i
            
            for k in range(5):
                digits.append(i%10)
                i=i/10

            if(digits[0]==digits[-1] and digits[1]==digits[-2]):
                flag=True
                print prime_number
                print
                break
            



        
