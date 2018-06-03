## Author : David Valles
## Date   : 02/11/2013
## Solution : 14725

n=[0]
solution=[]
def generate_tri_no(num):
    i=0
    while len(str(num[-1]))<4:
        n.append(num[-1]+i+1)
        
        if len(str(num[-1]))==3:
            solution.append(num[-1])
            
        i=i+1
        
    
generate_tri_no(n)
print "Sum of 3-digit Triangular numbers are ", sum(solution)

