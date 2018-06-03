## Author : David Valles
## Date   : 08/11/2013
## Solution : 81

import random
import sys

pars=[3,4,5]
course=[]
combo=[]
n=0

def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
    
print "Following are the par combinations that meets the sum criteria of 72 \n"

#Using the 18P3/6 Permutation formula, a total of 816 possible combination where possible.
for i in xrange((factorial(18)/(factorial(3)*factorial(18-3)))):
    
    
    for i in range(18):
        course.append(random.choice(pars))

    if sum(course)==72:
        print course
        combo.append(course)
        
    else:
        course=[]
        
    n+=1
                    
print " The total number of possible 18 golf courses is ",len(combo)
