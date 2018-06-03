## Author : David Valles
## Date   : 20/11/2013

for i in range(1,101):
    out=""
    flag=False
    if i%3==0:
        out+="Fizz"
        flag=True
    if i%5==0:
        out+="Buzz"
        flag=True
    if '3' in str(i):
        out+="Bizz"
        flag=True
    if '5' in str(i):
        out+="Fuzz"
        flag=True

    if not flag:
        out=i
    print out

raw_input()
