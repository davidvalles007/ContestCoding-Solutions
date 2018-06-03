## Author : David Valles
## Date   : 31/10/2013
## Solution : HOLMES had been seated for some hours in silence with his long, thin back curved over a chemical vessel in which he was brewing a particularly malodorous product. His head was sunk upon his breast, and he looked from my point of view like a strange, lank bird, with dull grey plumage and a black top-knot.

import string
encrypt="OVSTLZ ohk illu zlhalk mvy zvtl ovbyz pu zpslujl dpao opz svun, aopu ihjr jbyclk vcly h joltpjhs clzzls pu dopjo ol dhz iyldpun h whyapjbshysf thsvkvyvbz wyvkbja. Opz olhk dhz zbur bwvu opz iylhza, huk ol svvrlk myvt tf wvpua vm cpld sprl h zayhunl, shur ipyk, dpao kbss nylf wsbthnl huk h ishjr avw-ruva."
key=7           ## Decryption key is 7 here
decrypt=""

for i in range(len(encrypt)):

    if encrypt[i]==str(" "):
        decrypt=decrypt+' '
        continue

    if encrypt[i]==",":
        decrypt=decrypt+","
        continue

    if encrypt[i]==".":
        decrypt=decrypt+"."
        continue

    if encrypt[i]=="-":
        decrypt=decrypt+"-"
        continue
        
    else:
        if encrypt[i] in string.lowercase:
            if (ord(encrypt[i])-97)<key:
                decrypt=decrypt+(chr((ord(encrypt[i])-97)-key+123))
            else:
                decrypt=decrypt+(chr(ord(encrypt[i])-key))
        else:
            if (ord(encrypt[i])-65)<key:
                decrypt=decrypt+(chr((ord(encrypt[i])-65)-key+91))
            else:
                decrypt=decrypt+(chr(ord(encrypt[i])-key))
           
print decrypt
raw_input()
