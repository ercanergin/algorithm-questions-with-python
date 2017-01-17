from functions import allprimes
from math import sqrt

def goldbach(n):
    kontrol = allprimes(n)
    for p in kontrol:
        if(int(sqrt((n-p)/2))==sqrt((n-p)/2)):
            return(1)
            break
    else:
        return(0)

asal = allprimes(10000)

for n in range(9,10000,2):
    if(asal.count(n)==1):
        continue
    if(goldbach(n)==0):
        print(n)
        break
