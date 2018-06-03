## Author : David Valles
## Date   : 12/01/2014
## Solution : 13211321322113

def gen(n=1):
    num=n
    snum=str(num)
    count=1
    index=0
    out=[]
    cin=0

    while index<len(snum):
        l=snum[index]
        
        while cin<len(snum)-1:
            #To count if successive digit(s) are same
            if l==snum[cin+1]:
                count+=1
                cin+=1
                index+=1
            
            else:
                out.append(str(count)+""+l)
                count=1
                
                break

        #To append if the successive digits were same with their relevant counts
        else:
            out.append(str(count)+""+l)
       
        index+=1
        cin+=1
        
    
    fin.append(int(''.join(out)))
    if len(fin)<8:
        gen(fin[-1])
        
fin=[3]
gen(fin[-1])
#print fin
print "The 8th term of the look and say sequence beginning with 3 is", fin[-1]
raw_input()
