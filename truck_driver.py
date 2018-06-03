## Author : David Valles
## Date   : 01/12/2013
## Solution : 14.98, That's ~15

import math
metric={
'WashingtonDC':{'Pittsburgh' : 245,
                'Richmond' : 108,
                'Philadelphia' : 142},
'Pittsburgh':{'Richmond' : 345,
             'Philadelphia' : 304,
             'WashingtonDC' : 245},
'Richmond':{'Philadelphia' : 248,
            'Pittsburgh' : 345,
            'WashingtonDC' : 108},
'Philadelphia':{'WashingtonDC' : 142,
            'Pittsburgh' : 304,
            'Richmond' : 248}
}
def path(stops,route):
    for i in stops:
        route.append(i)
    route.append("WashingtonDC")
    return route

stops=["Pittsburgh","Richmond","Philadelphia"]
combo=[]
weight={}
index=0

def calculate(route):
    add=0
    prev=""
    global index
    for count,r in enumerate(route):
        if 0<count<len(route):
            add+=metric[prev][r]
        prev=r

    weight[index]=add
    index+=1
    
for i in range(len(stops)):
    route=["WashingtonDC"]
    tmp=stops[0]
    stops=stops[1:]
    stops.append(tmp)
    combo.append(path(stops,route))

for i in range(len(combo)):
    calculate(combo[i])
    
for k,v in weight.iteritems():
    if v==min(weight.itervalues()):
        print "Optimal Route : ",v
        for n in (combo[k]):
            print n,
        print "\nTime taken : %.2f hour(s)"%(v/60.0)
