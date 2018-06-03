## Author : David Valles
## Date   : 16/11/2013
## Solution : Hello World199 Bottles of BeerH+9JQ29H39+Q99 Bottles of BeerHello World99 Bottles of Beer2H+9JQ29H39+Q

source="H+9JQ29H39+Q"

H="Hello World"
Q=source
nine="99 Bottles of Beer"
plus=0
instructions={'H':"Hello World",'Q':source,'9':"99 Bottles of Beer",'+':0}
output=""
for i in range(len(source)):
    if source[i] in instructions:
        if source[i]=='+':
            instructions[source[i]]+=1
            output+=str(instructions[source[i]])
        else:
            output+=instructions[source[i]]
    else:
        pass

print output
print raw_input()
