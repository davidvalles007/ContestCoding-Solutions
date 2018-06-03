## Author : David Valles
## Date   : 03/11/2013
## Solution : ('s', 61) 'S' 61 times

import string
import operator
alpha={}
for i in string.ascii_lowercase:
    alpha[i]=0
    
input_str="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse vitae justo est, sed ultricies lacus. Praesent adipiscing adipiscing sapien, iaculis lacinia lectus suscipit eu. Nullam eget scelerisque mi. In eget fermentum nunc. Etiam eu diam a nunc auctor viverra. Nulla leo nunc, placerat in iaculis ut, convallis ac tellus. Praesent ultrices lacinia facilisis. Vivamus dolor massa, vulputate bibendum egestas sed, euismod sit amet nulla. Aliquam erat volutpat. Nunc hendrerit euismod massa ut scelerisque. Pellentesque et diam eget mi ultricies aliquam eget vitae augue. Nunc risus turpis, pellentesque nec ornare vel, posuere vitae arcu. Mauris commodo lacinia felis. Praesent feugiat condimentum velit, a euismod nisl euismod et. Suspendisse potenti. Sed eu imperdiet nibh."

for j in input_str.lower():
    for key in alpha.iterkeys():
        if key==j:
            alpha[j]+=1

print "The third most frequently used letter is ", sorted(alpha.iteritems(), key=operator.itemgetter(1))[-3]

    
