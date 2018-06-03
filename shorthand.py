## Author : David Valles
## Date   : 01/12/2013
## Solution :   Frnds, Rmns, cntrymn, lnd m yr ers! 
##              I cm t bry Csr, nt t prs hm. 
##              Th evl tht mn d lvs aftr thm, 
##              Th gd is oft intrèd wth thr bns: 
##              S lt it b wth Csr. Th nbl Brts 
##              Hth tld y Csr ws ambts; 
##              If it wr s, it ws a grvs flt, 
##              And grvsly hth Csr answrd it. 
##              Hr, undr lv of Brts and th rst - 
##              Fr Brts is an hnrbl mn, 
##              S ar thy al, al hnrbl mn - 
##              Cm I t spk in Csr’s fnrl.

inp='''Friends, Romans, countrymen, lend me your ears!
I come to bury Caesar, not to praise him.
The evil that men do lives after them,
The good is oft interrèd with their bones:
So let it be with Caesar. The noble Brutus
Hath told you Caesar was ambitious;
If it were so, it was a grievous fault,
And grievously hath Caesar answered it.
Here, under leave of Brutus and the rest -
For Brutus is an honourable man,
So are they all, all honourable men -
Come I to speak in Caesar’s funeral.'''

out=""
vowels=['a','e','i','o','u','A','E','I','O','U']

buf=[]

lines=[l for l in inp.split('\n')]
for line in lines:
    prev=""
    for i in line.split():
        for j in i:
            
            if i.index(j)!=0:
                    if j not in vowels and j.lower()!=prev.lower():
                           buf.append(j)
                    
            else:
                    buf.append(j)

            prev=j
        buf.append(" ")
    buf.append("\n")

out=''.join(buf)
print 
print out

