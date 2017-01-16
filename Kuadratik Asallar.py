from functions import allprimes
from functions import isprime

def quadratic(a,b):
    primecount = 0
    for n in range(100):
        if(isprime(n**2+a*n+b)==1):
            primecount += 1
        else:
            break
    return(primecount)

blist = allprimes(1000)
maxab = 1
sonuc = None

for a in range(-999,1000):
    for b in blist:
        if(quadratic(a,b)>maxab):
            maxab = quadratic(a,b)
            sonuc = a*b
print(sonuc)
