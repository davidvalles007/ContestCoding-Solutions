## Author : David Valles
## Date   : 01/11/2013
## Solution : 75025

n=[0,1]
def generate_fibonacci(num1,num2):
    if(num1+num2)<100000:
        n.append(num1+num2)
        generate_fibonacci(n[-1],n[-2])

generate_fibonacci(n[-1],n[-2])
print "Fibonacci number closest to 100000 is ", n[-1]
raw_input()
