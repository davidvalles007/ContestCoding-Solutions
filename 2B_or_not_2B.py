## Author : David Valles
## Date   : 12/11/2013
## Solution : oT be or not ot be – ahtt is eht einoqstu: 
##            eehhrtW ’ist belnor in eht dimn ot effrsu 
##            ehT gilnss adn aorrsw fo aegoorstuu efnortu, 
##            Or ot aekt amrs aaginst a aes fo belorstu 
##            Adn, by ginoopps, den ehmt.

 
import string
input_string='''To be or not to be – that is the question: 
 Whether ’tis nobler in the mind to suffer 
 The slings and arrows of outrageous fortune, 
 Or to take arms against a sea of troubles 
 And, by opposing, end them.'''
output_string=""
line=[]
line.append(input_string.split(' '))
token=False
pre=False
for i in range(len(line[0])):
    tmp=''
    if line[0][i][0] in string.ascii_uppercase:
        if not line[0][i].isalpha():
            c=sorted(line[0][i][:-1].upper())
            ele=line[0][i][-1]
            token=True
        else:
            c=sorted(line[0][i].upper())
        for j in range(len(c)):
            if c[j].lower() in line[0][i]:
                tmp=tmp+(c[j].lower())
            else:
                tmp=tmp+(c[j])
        if token:
            token=False
            output_string+=tmp+ele+' '
        else:
            output_string+=tmp+' '
                       
    elif line[0][i][0] in string.ascii_lowercase:
        if not line[0][i].isalpha():
            c=sorted(line[0][i][:-1])
            ele=line[0][i][-1]
            token=True
        else:
            c=sorted(line[0][i])
        for j in range(len(c)):
            tmp=tmp+(c[j])
        if token:
            token=False
            output_string+=tmp+ele+' '
        else:
            output_string+=tmp+' '

    else:
        try:
            if line[0][i][1]==str(' '):
                tmp=line[0][i]
        except:
            tmp=line[0][i]
            output_string+=tmp+' '
        else:
            
            if not line[0][i].isalpha():
                if not line[0][i][-1].isalpha():
                    c=sorted(line[0][i][:-1])
                    ele=line[0][i][-1]
                    token=True
                else:
                    c=sorted(line[0][i][1:])
                    ele=line[0][i][0]
                    token=True
                    pre=True
            else:
                c=sorted(line[0][i])
            for j in range(len(c)):
                tmp=tmp+(c[j])
            if token:
                token=False
                if not pre:
                    output_string+=tmp+ele+' '
                else:
                    pre=False
                    output_string+=ele+tmp+' '
            else:
                output_string+=tmp+' '
            
print input_string
print
print output_string
