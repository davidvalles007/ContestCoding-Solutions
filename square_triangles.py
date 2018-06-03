## Author : David Valles
## Date   : 12/01/2014
## Solution : 48024900

import math
n=[0]
solution=[]
def generate_tri_no(num):
    i=0
    while len(str(num[-1]))<9:
        n.append(num[-1]+i+1)
        
        if (math.sqrt(num[-1])%1)==0:
            solution.append(num[-1])
            
        i=i+1
        
    
generate_tri_no(n)
print "Sixth Square Triangular number is", solution[-1]
raw_input()
