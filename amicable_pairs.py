## Author : David Valles
## Date   : 09/11/2013
## Solution : 5544

list_of_amicables=[]
first_divisors=[]
second_divisors=[]

def test_divisibility(i):
    buf=[]
    for j in range(1,(i/2)+1):
        if(i%j==0):
            buf.append(j)
        else:
            pass
    return buf

for i in xrange(30,10000):
    first_divisors=test_divisibility(i)
    first_sum=sum(first_divisors)
    second_divisors=test_divisibility(first_sum)
    flag=True
    if i==sum(second_divisors) and i!=first_sum:
        if len(list_of_amicables)==0:
            list_of_amicables.append((i,first_sum))
        for l in range(len(list_of_amicables)):
            if i in list_of_amicables[l]:
                flag=False
        if flag:
            list_of_amicables.append((i,first_sum))
    if len(list_of_amicables)==3:
        break

print "Sum of third amicable pair (%i,%i) is %i"%(list_of_amicables[-1][0],list_of_amicables[-1][1],sum(list_of_amicables[-1]))
