## Author : David Valles
## Date   : 03/02/2014
## Solution : ['k', 'j', 'q', 'v']

input_string='''
Of the twenty six letters in the alphabet, how many of them do no appear in
this puzzle - excluding the reminder below?
'''

import string

alpha={}
value=0
for l in string.ascii_lowercase:
    alpha[l]=value
    
tmpstr=input_string.lower()
for i in tmpstr:
    if i in string.ascii_lowercase:
        alpha[i]+=1

    else:
        pass
    
print "Following letters do not appear in the puzzle",[xx[0] for xx in alpha.items() if xx[1]==0]
raw_input()
