## Author : David Valles
## Date   : 03/03/2014
## Solution : 0   

n=[0,1]
def generate_fibonacci(num1,num2):

        if str(num1+num2)[0] == "7":
            n.append((num1+num2))
            print "The third digit of the smallest Fibonacci number which has a first digit of 7 is ", str(n[-1])[2]
            #75025
            
        else:
            n.append((num1+num2))
            generate_fibonacci(n[-1],n[-2])

generate_fibonacci(n[-1],n[-2])
raw_input()
