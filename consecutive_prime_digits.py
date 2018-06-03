## Author : David Valles
## Date   : 09/11/2013
## Solution : 37

prime="23"

for i in range(4,101):
    for j in range(2,i):
        if(i%j==0):
            break
        else:
            pass

        if(j==(i/2)):
            prime+=(str(i))

l=0
mx=0
seq=[]
while l<(len(prime)-4):
    buf=[]
    for i in range(l,l+5,1):
        buf.append(int(prime[i]))
    if sum(buf)>mx:
        mx=sum(buf)
        seq=buf
    l+=1

print "The largest sum of 5 consecutive digits in the series is for the subset\n"
print seq, " -> ", mx
