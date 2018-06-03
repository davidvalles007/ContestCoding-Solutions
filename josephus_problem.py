## Author : David Valles
## Date   : 09/12/2013
## Solution : 24

def onemore(pos):
    p=pos-len(l)
    if p<len(l):
        return p
    else:
        return onemore(p)
    

l=[i for i in range(40)]
pos=6

while len(l)!=1:

    if len(l)>pos:
        del l[pos]
       
    else:
        
        pos=onemore(pos)  
        del l[pos]
                     
    pos=pos+6

print "The position at which Josephus sat was ", l[0]+1
