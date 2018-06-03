## Author : David Valles
## Date   : 31/10/2013
## Solution : It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way. In short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.

import string
encrypt="Yj mqi jxu ruij ev jycui, yj mqi jxu mehij ev jycui, yj mqi jxu qwu ev myitec, yj mqi jxu qwu ev veebyixduii, yj mqi jxu ufesx ev rubyuv, yj mqi jxu ufesx ev ydshutkbyjo, yj mqi jxu iuqied ev Bywxj, yj mqi jxu iuqied ev Tqhaduii, yj mqi jxu ifhydw ev xefu, yj mqi jxu mydjuh ev tuifqyh, mu xqt uluhojxydw ruvehu ki, mu xqt dejxydw ruvehu ki, mu muhu qbb weydw tyhusj je Xuqlud, mu muhu qbb weydw tyhusj jxu ejxuh mqo. Yd ixehj, jxu fuhyet mqi ie vqh byau jxu fhuiudj fuhyet, jxqj iecu ev yji deyiyuij qkjxehyjyui ydiyijut ed yji ruydw husuylut, veh weet eh veh ulyb, yd jxu ikfuhbqjylu tuwhuu ev secfqhyied edbo."
key=16
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
        
    else:
        if encrypt[i] in string.lowercase:
            if (ord(encrypt[i])-97)<16:
                decrypt=decrypt+(chr((ord(encrypt[i])-97)-16+123))
            else:
                decrypt=decrypt+(chr(ord(encrypt[i])-16))
        else:
            if (ord(encrypt[i])-65)<16:
                decrypt=decrypt+(chr((ord(encrypt[i])-65)-16+91))
            else:
                decrypt=decrypt+(chr(ord(encrypt[i])-16))
           
print decrypt
