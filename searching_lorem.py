## Author : David Valles
## Date   : 17/02/2014
## Solution : Ut

import fileinput

tmp=words=[]

for w in fileinput.input():
    tmp.append(w)

words = tmp[0].split()
print words[1864]

