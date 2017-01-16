from sympy import isprime

toplam=0
LIMIT = 150000000

for n in range(10,LIMIT,10):
    if(n%3==0 or n%7==0 or n%13==0):
        continue
    m = n**2+1
    if(m%6!=1 and m%6!=5):
        continue
    if(isprime(m)==1):
        if(isprime(m+2)==1):
            if(isprime(m+6)==1):
                if(isprime(m+8)==1):
                    if(isprime(m+12)==1):
                        if(isprime(m+20)!=1):
                            if(isprime(m+26)==1):
                                toplam += n
print(toplam)
