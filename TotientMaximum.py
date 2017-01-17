from fractions import gcd
def totient(n):
    sonuc=1
    for i in range(2,n):
        if(gcd(n,i)==1):
            sonuc += 1
    return(n/sonuc)

ebn=[]
for n in range(2,1000000,2):
    if(n%3!=0 or n%5!=0 or n%7!=0 or n%11!=0 or n%13!=0 or n%17!=0):
        ebn.append(1)
        continue
    ebn.append(totient(n))
print(2*ebn.index(max(ebn))+2)
